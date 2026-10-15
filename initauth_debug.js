function initAuth() {
        // Bước 1: Xử lý redirect OAuth2 nếu vừa đăng nhập qua Google/GitHub/Microsoft
        const isOAuth = await handleOAuthRedirectParams();
        if (isOAuth) return;

        // Bước 2: Kiểm tra phiên đăng nhập đã lưu trong LocalStorage (lingua-user)
        const savedUser = localStorage.getItem('lingua-user');
        if (savedUser) {
            showApp(savedUser);
            return;
        }

        // Bước 3: Kiểm tra phiên lưu trữ từ Supabase SDK trong LocalStorage
        const sbSavedName = getSupabaseStoredUser();
        if (sbSavedName) {
            localStorage.setItem('lingua-user', sbSavedName);
            showApp(sbSavedName);
            return;
        }

        // Bước 4: Kiểm tra session trực tiếp từ Supabase
        if (sbClient) {
            try {
                const { data: { session } } = await sbClient.auth.getSession();
                if (session && session.user) {
                    const u = session.user;
                    const name = u.user_metadata?.full_name || u.user_metadata?.name || (u.email ? u.email.split('@')[0] : 'Học viên');
                    localStorage.setItem('lingua-user', name);
                    showApp(name);
                    return;
                }
            } catch(e) {
                console.warn('Lỗi getSession:', e);
            }
        }

        // Mặc định cho phép người dùng vào xem và khám phá toàn bộ trang chủ Lingua với tư cách Khách
        showApp('Khách Trải Nghiệm');
    }

    // 1. Social Login (Google, GitHub, Microsoft)
    window.handleSocialLogin = async function(provider) {
        const providerName = provider === 'azure' ? 'Microsoft' : (provider.charAt(0).toUpperCase() + provider.slice(1));
        
        // Ghi nhận trước để khi redirect về biết chắc chắn provider nào vừa được kích hoạt
        sessionStorage.setItem('oauth_in_progress', providerName);
        sessionStorage.setItem('oauth_time', Date.now().toString());

        const msgEl = document.getElementById('auth-message');
        if (msgEl) {
            msgEl.textContent = `Đang kết nối xác thực ${providerName}...`;
            msgEl.style.color = '#2563eb';
        }
        
        const btnId = `btn-${provider === 'azure' ? 'microsoft' : provider}`;
        const btn = document.getElementById(btnId);
        if (btn) {
            btn.disabled = true;
            btn.style.opacity = '0.7';
        }
        
        const redirectUri = window.location.origin 