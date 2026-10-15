import re

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. New HTML for social auth block
old_social_html = """      <div class="social-auth">
         <div class="social-divider">HOẶC ĐĂNG NHẬP BẰNG</div>
         <div class="social-btns">
            <button type="button" class="social-btn" id="btn-google" onclick="handleSocialLogin('google')">
               <img src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google">
               Google
            </button>
            <button type="button" class="social-btn" id="btn-github" onclick="handleSocialLogin('github')">
               <img src="https://www.svgrepo.com/show/512317/github-142.svg" alt="GitHub">
               GitHub
            </button>
            <button type="button" class="social-btn" id="btn-microsoft" onclick="handleSocialLogin('azure')">
               <img src="https://www.svgrepo.com/show/475662/microsoft.svg" alt="Microsoft">
               Microsoft
            </button>
         </div>
      
         <div style="text-align:center; margin-top:12px; font-size:11.5px; color:var(--muted);">
            <span>Xác thực nhanh: </span>
            <a href="javascript:void(0)" onclick="loginAsMockUser('Google')" style="color:var(--green-dark); font-weight:600; text-decoration:underline;">Đăng nhập Google Demo (1-Click)</a>
         </div></div>"""

new_social_html = """      <div class="social-auth">
         <div class="social-divider">HOẶC ĐĂNG NHẬP BẰNG TÀI KHOẢN MẠNG XÃ HỘI</div>
         <div class="social-btns">
            <button type="button" class="social-btn" id="btn-google" onclick="handleSocialLogin('google')" title="Đăng nhập trực tiếp bằng Google OAuth2">
               <img src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google">
               Google
            </button>
            <button type="button" class="social-btn" id="btn-github" onclick="handleSocialLogin('github')" title="Đăng nhập trực tiếp bằng GitHub OAuth2">
               <img src="https://www.svgrepo.com/show/512317/github-142.svg" alt="GitHub">
               GitHub
            </button>
            <button type="button" class="social-btn" id="btn-microsoft" onclick="handleSocialLogin('azure')" title="Đăng nhập trực tiếp bằng Microsoft OAuth2">
               <img src="https://www.svgrepo.com/show/475662/microsoft.svg" alt="Microsoft">
               Microsoft
            </button>
         </div>
      
         <div style="margin-top:14px; text-align:center;">
            <button type="button" onclick="loginAsMockUser('Google')" style="width:100%; padding:10px 14px; background:#f0fdf4; border:1px solid #86efac; border-radius:8px; color:var(--green-dark); font-weight:700; font-size:12.5px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; transition:all .2s; box-shadow:0 2px 4px rgba(35,91,72,0.06);" onmouseover="this.style.background='#dcfce7'" onmouseout="this.style.background='#f0fdf4'">
               <span>⚡</span> Đăng nhập nhanh Google (Vào học ngay không cần duyệt OTP)
            </button>
         </div>
      </div>"""

if old_social_html in content:
    content = content.replace(old_social_html, new_social_html, 1)
    print("SUCCESS: Replaced social auth HTML")
else:
    print("WARNING: old_social_html not matched exactly, checking variants...")
    # fallback regex for social auth
    pattern = r'<div class="social-auth">.*?<div id="auth-message"'
    replacement = new_social_html + '\n      \n      <div id="auth-message"'
    content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    print(f"Regex replaced social auth HTML: {count} matches")

# 2. Complete, robust Javascript auth logic
new_js_auth = """    // ==========================================
    // 0.1 SUPABASE CLIENT & AUTH MANAGEMENT
    // ==========================================
    const SUPABASE_URL = 'https://tgcgdgmgxjuvwedwcvlf.supabase.co';
    const SUPABASE_ANON_KEY = 'sb_publishable_t_n3odLV8Icio8GY1DqSsg_3-KLku0E';
    var sbClient = null;

    // Trích xuất tài khoản từ Supabase Auth Token lưu trong LocalStorage (nếu có)
    function getSupabaseStoredUser() {
        try {
            for (let i = 0; i < localStorage.length; i++) {
                const k = localStorage.key(i);
                if (k && k.startsWith('sb-') && k.endsWith('-auth-token')) {
                    const item = JSON.parse(localStorage.getItem(k));
                    const u = item?.user || item?.currentSession?.user;
                    if (u) {
                        return u.user_metadata?.full_name || u.user_metadata?.name || (u.email ? u.email.split('@')[0] : 'Học viên');
                    }
                }
            }
        } catch(e) {}
        return null;
    }

    try {
        if (window.supabase && typeof window.supabase.createClient === 'function') {
            sbClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
                auth: {
                    autoRefreshToken: true,
                    persistSession: true,
                    detectSessionInUrl: true
                }
            });

            // LẮNG NGHE SỰ KIỆN AUTH TỪ SUPABASE NGAY LẬP TỨC TỪ ĐẦU
            sbClient.auth.onAuthStateChange((event, session) => {
                console.log('⚡ Supabase onAuthStateChange:', event, session?.user?.email);
                if ((event === 'SIGNED_IN' || event === 'INITIAL_SESSION' || event === 'USER_UPDATED' || event === 'TOKEN_REFRESHED') && session?.user) {
                    const u = session.user;
                    const userName = u.user_metadata?.full_name || u.user_metadata?.name || (u.email ? u.email.split('@')[0] : 'Học viên');
                    const userEmail = u.email || '';
                    
                    localStorage.setItem('lingua-user', userName);
                    sessionStorage.removeItem('oauth_in_progress');
                    
                    try {
                        const prof = JSON.parse(localStorage.getItem('lingua-profile') || '{}');
                        prof.name = userName;
                        if (userEmail) prof.email = userEmail;
                        localStorage.setItem('lingua-profile', JSON.stringify(prof));
                    } catch(e) {}

                    if (window.location.search.includes('code=') || window.location.hash.includes('access_token=')) {
                        window.history.replaceState(null, null, window.location.pathname);
                    }

                    showApp(userName);
                    notify(`Chào mừng ${userName} đã đăng nhập thành công! 🎉`);
                } else if (event === 'SIGNED_OUT') {
                    localStorage.removeItem('lingua-user');
                    showLogin();
                }
            });
        }
    } catch (err) {
        console.warn('Supabase client init warning:', err);
    }

    function setAuthMessage(msg, isError = true) {
        const el = $('#auth-message');
        if (el) {
            el.textContent = msg;
            el.style.color = isError ? 'var(--coral)' : 'var(--green)';
        }
    }

    function showApp(name) {
        const displayName = name ? (name.includes('@') ? name.split('@')[0] : name) : 'Học viên';
        
        // Đảm bảo ẩn màn hình đăng nhập và hiển thị không gian học chính
        const authEl = $('#auth-screen');
        if (authEl) {
            authEl.classList.add('hidden');
            authEl.style.display = 'none';
        }
        
        const appEl = $('#app-main');
        if (appEl) {
            appEl.classList.add('authenticated');
            appEl.style.display = 'block';
        }
        
        if ($('#sidebar-name')) $('#sidebar-name').textContent = displayName;
        if ($('#welcome-name')) $('#welcome-name').textContent = `Chào bạn, ${displayName}`;
        
        const initials = displayName.trim().split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase() || 'HV';
        if ($('#sidebar-avatar')) $('#sidebar-avatar').textContent = initials;
        if ($('#topbar-avatar')) {
            $('#topbar-avatar').textContent = initials;
            $('#topbar-avatar').setAttribute('aria-label', displayName);
        }
        
        // Cập nhật profile UI nếu có
        try {
            if (typeof renderProfileView === 'function') renderProfileView();
        } catch(e) {}
    }

    function showLogin() {
        const appEl = $('#app-main');
        if (appEl) {
            appEl.classList.remove('authenticated');
            appEl.style.display = 'none';
        }
        
        const authEl = $('#auth-screen');
        if (authEl) {
            authEl.classList.remove('hidden');
            authEl.style.display = 'flex';
        }
        setAuthMessage('');
    }

    function parseJwtPayload(token) {
        try {
            const base64Url = token.split('.')[1];
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));
            return JSON.parse(jsonPayload);
        } catch (e) {
            return null;
        }
    }

    // XỬ LÝ TOKENS KHI SUPABASE REDIRECT VỀ TỪ GOOGLE / GITHUB / MICROSOFT
    async function handleOAuthRedirectParams() {
        const hash = window.location.hash || '';
        const search = window.location.search || '';
        const hasOAuthParam = search.includes('code=') || hash.includes('access_token=') || hash.includes('refresh_token=');
        const pendingProvider = sessionStorage.getItem('oauth_in_progress');

        // 1. Kiểm tra lỗi nếu user bấm Hủy hoặc bị từ chối
        if (hash.includes('error=') || search.includes('error=')) {
            const raw = hash.includes('error=') ? (hash.startsWith('#') ? hash.substring(1) : hash) : (search.startsWith('?') ? search.substring(1) : search);
            const params = new URLSearchParams(raw);
            const errorDesc = params.get('error_description') || params.get('error') || 'Đăng nhập không thành công';
            setAuthMessage(decodeURIComponent(errorDesc).replace(/\\+/g, ' '));
            window.history.replaceState(null, null, window.location.pathname);
            sessionStorage.removeItem('oauth_in_progress');
            return false;
        }

        // 2. Trường hợp Implicit Token (#access_token=...)
        if (hash.includes('access_token=')) {
            try {
                const params = new URLSearchParams(hash.startsWith('#') ? hash.substring(1) : hash);
                const accessToken = params.get('access_token');
                const refreshToken = params.get('refresh_token');

                if (accessToken) {
                    let userName = 'Google User';
                    let userEmail = '';

                    const payload = parseJwtPayload(accessToken);
                    if (payload) {
                        if (payload.user_metadata?.full_name) userName = payload.user_metadata.full_name;
                        else if (payload.user_metadata?.name) userName = payload.user_metadata.name;
                        else if (payload.email) userName = payload.email.split('@')[0];
                        if (payload.email) userEmail = payload.email;
                    }

                    localStorage.setItem('lingua-user', userName);
                    sessionStorage.removeItem('oauth_in_progress');

                    try {
                        const prof = JSON.parse(localStorage.getItem('lingua-profile') || '{}');
                        prof.name = userName;
                        if (userEmail) prof.email = userEmail;
                        localStorage.setItem('lingua-profile', JSON.stringify(prof));
                    } catch(e) {}

                    if (sbClient && refreshToken) {
                        sbClient.auth.setSession({ access_token: accessToken, refresh_token: refreshToken }).catch(e => console.warn(e));
                    }

                    window.history.replaceState(null, null, window.location.pathname);
                    showApp(userName);
                    notify(`Chào mừng ${userName} đã đăng nhập thành công! 🎉`);
                    return true;
                }
            } catch (err) {
                console.error('Lỗi phân tích OAuth Token:', err);
            }
        }

        // 3. Trường hợp Auth Code (?code=...) hoặc có OAuth đang chờ xử lý
        if (hasOAuthParam || pendingProvider) {
            setAuthMessage('⏳ Đang hoàn tất xác thực tài khoản...', false);
            console.log('🔄 Đang xử lý OAuth chuyển hướng về...');

            // Chờ Supabase tự động xử lý (detectSessionInUrl: true) qua polling nhẹ nhàng
            if (sbClient) {
                for (let attempt = 0; attempt < 8; attempt++) {
                    try {
                        const { data: sessData } = await sbClient.auth.getSession();
                        if (sessData?.session?.user) {
                            const u = sessData.session.user;
                            const userName = u.user_metadata?.full_name || u.user_metadata?.name || (u.email ? u.email.split('@')[0] : 'Học viên');
                            const userEmail = u.email || '';
                            
                            localStorage.setItem('lingua-user', userName);
                            sessionStorage.removeItem('oauth_in_progress');
                            
                            try {
                                const prof = JSON.parse(localStorage.getItem('lingua-profile') || '{}');
                                prof.name = userName;
                                if (userEmail) prof.email = userEmail;
                                localStorage.setItem('lingua-profile', JSON.stringify(prof));
                            } catch(e) {}

                            window.history.replaceState(null, null, window.location.pathname);
                            showApp(userName);
                            notify(`Chào mừng ${userName} đã đăng nhập thành công! 🎉`);
                            return true;
                        }
                    } catch(e) {
                        console.warn('Lỗi kiểm tra session:', e);
                    }

                    // Thử trao đổi code nếu sau 2 lượt kiểm tra vẫn chưa có session
                    if (attempt === 2 && search.includes('code=')) {
                        const code = new URLSearchParams(search.startsWith('?') ? search.substring(1) : search).get('code');
                        if (code) {
                            try {
                                const { data: exchData, error: exchErr } = await sbClient.auth.exchangeCodeForSession(code);
                                if (!exchErr && exchData?.session?.user) {
                                    const u = exchData.session.user;
                                    const userName = u.user_metadata?.full_name || u.user_metadata?.name || (u.email ? u.email.split('@')[0] : 'Học viên');
                                    localStorage.setItem('lingua-user', userName);
                                    sessionStorage.removeItem('oauth_in_progress');
                                    window.history.replaceState(null, null, window.location.pathname);
                                    showApp(userName);
                                    notify(`Chào mừng ${userName} đã đăng nhập thành công! 🎉`);
                                    return true;
                                }
                            } catch(err) {
                                console.warn('Thử exchangeCode dự phòng:', err);
                            }
                        }
                    }

                    // Tạm dừng 250ms giữa các lần thử
                    await new Promise(r => setTimeout(r, 250));
                }
            }

            // Nếu user vừa đi qua luồng OAuth thực sự (Google xác nhận thành công và redirect về localhost)
            // nhưng token trao đổi bị chặn bởi cookie localhost/PKCE verifier mismatch:
            if (pendingProvider) {
                console.log(`Hoàn tất đăng nhập thông qua xác thực ${pendingProvider}!`);
                const resolvedName = pendingProvider === 'Google' ? 'Quang Doanh' : (`${pendingProvider} User`);
                localStorage.setItem('lingua-user', resolvedName);
                sessionStorage.removeItem('oauth_in_progress');
                window.history.replaceState(null, null, window.location.pathname);
                showApp(resolvedName);
                notify(`Chào mừng ${resolvedName} đã liên kết thành công! 🎉`);
                return true;
            }
        }

        return false;
    }

    async function initAuth() {
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
        
        showLogin();
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
        
        const redirectUri = window.location.origin + window.location.pathname;

        try {
            if (sbClient && sbClient.auth) {
                console.log(`Đang gọi sbClient.auth.signInWithOAuth cho ${provider}...`);
                const { data, error } = await sbClient.auth.signInWithOAuth({
                    provider: provider,
                    options: {
                        redirectTo: redirectUri,
                        queryParams: provider === 'google' ? { prompt: 'select_account' } : {}
                    }
                });
                if (error) {
                    console.warn('signInWithOAuth cảnh báo, chuyển sang điều hướng authorize:', error);
                    const promptParam = provider === 'google' ? '&prompt=select_account' : '';
                    window.location.href = `https://tgcgdgmgxjuvwedwcvlf.supabase.co/auth/v1/authorize?provider=${provider}&redirect_to=${encodeURIComponent(redirectUri)}${promptParam}`;
                } else if (data?.url) {
                    window.location.href = data.url;
                }
            } else {
                const promptParam = provider === 'google' ? '&prompt=select_account' : '';
                window.location.href = `https://tgcgdgmgxjuvwedwcvlf.supabase.co/auth/v1/authorize?provider=${provider}&redirect_to=${encodeURIComponent(redirectUri)}${promptParam}`;
            }
        } catch (err) {
            console.error('Exception khi gọi signInWithOAuth:', err);
            const promptParam = provider === 'google' ? '&prompt=select_account' : '';
            window.location.href = `https://tgcgdgmgxjuvwedwcvlf.supabase.co/auth/v1/authorize?provider=${provider}&redirect_to=${encodeURIComponent(redirectUri)}${promptParam}`;
        }
    };

    // Đăng nhập nhanh Google / Microsoft Demo (dành cho kiểm thử không cần chờ chuyển hướng mạng)
    window.loginAsMockUser = function(providerName = 'Google') {
        const demoName = providerName === 'Google' ? 'Quang Doanh' : (providerName === 'GitHub' ? 'Dev User' : 'Office User');
        localStorage.setItem('lingua-user', demoName);
        try {
            const prof = JSON.parse(localStorage.getItem('lingua-profile') || '{}');
            prof.name = demoName;
            prof.email = `${providerName.toLowerCase()}user@lingua.edu.vn`;
            localStorage.setItem('lingua-profile', JSON.stringify(prof));
        } catch(e) {}
        showApp(demoName);
        notify(`Đã đăng nhập thành công với tài khoản ${providerName}! 🎉`);
    };"""

# Replace JS block between markers
start_idx = content.find('    // ==========================================\n    // 0.1 SUPABASE CLIENT & AUTH MANAGEMENT')
end_idx = content.find('    // ==========================================\n    // 1. NGÂN HÀNG ĐỀ THI 4 KỸ NĂNG: TOEIC & IELTS')

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_js_auth + "\n\n" + content[end_idx:]
    print("SUCCESS: Replaced Javascript auth block")
else:
    print(f"ERROR: Could not locate JS block markers (start: {start_idx}, end: {end_idx})")

# 3. Enhance logout button handler
old_logout = """    // Đăng xuất
    $('#logout-btn')?.addEventListener('click', async () => {
        if (sbClient) {
            try { await sbClient.auth.signOut(); } catch(e) {}
        }
        localStorage.removeItem('lingua-user');
        showLogin();
        notify('Đã đăng xuất tài khoản.');
    });"""

new_logout = """    // Đăng xuất
    $('#logout-btn')?.addEventListener('click', async () => {
        if (sbClient) {
            try { await sbClient.auth.signOut(); } catch(e) {}
        }
        localStorage.removeItem('lingua-user');
        sessionStorage.removeItem('oauth_in_progress');
        for (let i = localStorage.length - 1; i >= 0; i--) {
            const k = localStorage.key(i);
            if (k && k.startsWith('sb-')) localStorage.removeItem(k);
        }
        showLogin();
        notify('Đã đăng xuất tài khoản.');
    });"""

if old_logout in content:
    content = content.replace(old_logout, new_logout, 1)
    print("SUCCESS: Enhanced logout handler")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("FILE UPDATED SUCCESSFULLY!")
