# -*- coding: utf-8 -*-
import sys
import re

html_path = r"e:\EngLish-IE-Toeic\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Block to insert before window.handleSocialLogin
auth_and_core_js = """
    // ==========================================
    // 0. CORE HELPERS & STATE
    // ==========================================
    const $ = (selector, root = document) => root.querySelector(selector);
    const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];

    let activeFilter = 'Tất cả';
    let practiceFilter = 'Tất cả';
    let wordIndex = 0;
    let wordRevealed = false;
    let flashRevealed = false;

    const words = [
      { word: 'Pragmatic', phonetic: '/præɡˈmætɪk/', pos: 'adj', meaning: 'Thực tế, coi trọng hiệu quả hơn lý thuyết suông', example: 'We need a pragmatic solution to increase workplace productivity.' },
      { word: 'Feasible', phonetic: '/ˈfiːzəbl/', pos: 'adj', meaning: 'Khả thi, có thể thực hiện được thuận lợi', example: 'It is simply not feasible to finish the entire project in two days.' },
      { word: 'Mitigate', phonetic: '/ˈmɪtɪɡeɪt/', pos: 'v', meaning: 'Giảm nhẹ, làm bớt tính nghiêm trọng của rủi ro', example: 'Steps have been taken to mitigate future economic damage.' },
      { word: 'Substantial', phonetic: '/səbˈstænʃl/', pos: 'adj', meaning: 'Đáng kể, có giá trị lớn hoặc số lượng lớn', example: 'A substantial number of candidates passed the IELTS examination.' },
      { word: 'Cohesive', phonetic: '/kəʊˈhiːsɪv/', pos: 'adj', meaning: 'Gắn kết chặt chẽ, mạch lạc và thống nhất', example: 'A cohesive essay always uses clear linking words and smooth transitions.' }
    ];

    function notify(message) {
      const toast = $('#toast');
      if (!toast) return;
      toast.textContent = message;
      toast.classList.add('show');
      window.setTimeout(() => toast.classList.remove('show'), 2200);
    }

    function courseCard(course) {
      return `
        <article class="course" data-kind="${course.kind}">
          <div class="course-mark">${course.mark}</div>
          <div>
            <div class="course-type">${course.kind} · ${course.skill || course.detail}</div>
            <h3>${course.title}</h3>
            <div class="course-meta">${course.questions} câu hỏi <span>·</span> ${course.time}</div>
          </div>
          <button class="course-action" data-start="${course.title}">Luyện ngay</button>
        </article>
      `;
    }

    function renderCourses() {
      const shown = courses.filter(course => activeFilter === 'Tất cả' || course.kind === activeFilter).slice(0, 4);
      if ($('#featured-courses')) $('#featured-courses').innerHTML = shown.map(courseCard).join('');
      const search = ($('#course-search')?.value || '').trim().toLocaleLowerCase('vi');
      const allShown = courses.filter(course => (practiceFilter === 'Tất cả' || course.kind === practiceFilter) && `${course.kind} ${course.title} ${course.detail}`.toLocaleLowerCase('vi').includes(search));
      if ($('#all-courses')) $('#all-courses').innerHTML = allShown.length ? allShown.map(courseCard).join('') : '<div class="empty-state">Chưa tìm thấy bài tập phù hợp. Thử từ khóa khác nhé.</div>';
    }

    function showWord(index) {
      const word = words[index];
      if (!word) return;
      if ($('#daily-word')) $('#daily-word').textContent = word.word;
      if ($('#daily-pronounce')) $('#daily-pronounce').textContent = `${word.phonetic} · ${word.pos}`;
      if ($('#daily-definition')) $('#daily-definition').textContent = wordRevealed ? word.example : word.meaning;
      if ($('#word-count')) $('#word-count').textContent = `${String(index + 1).padStart(2, '0')} / ${String(words.length).padStart(2, '0')}`;
      if ($('#reveal-word')) $('#reveal-word').textContent = wordRevealed ? 'Xem nghĩa' : 'Hiện ví dụ';
      if ($('#flashcard-label')) $('#flashcard-label').textContent = `Từ ${index + 1} trong ${words.length} · Nhấn để lật thẻ`;
      if ($('#flashcard-word')) $('#flashcard-word').textContent = word.word;
      if ($('#flashcard-detail')) $('#flashcard-detail').textContent = `${word.phonetic} · ${word.pos}`;
      if ($('#flashcard-hint')) $('#flashcard-hint').textContent = flashRevealed ? `${word.meaning} · ${word.example}` : 'Chạm để xem nghĩa và ví dụ';
      if ($('#vocab-list')) $('#vocab-list').innerHTML = words.map(item => `<div class="vocab-item"><strong>${item.word}</strong><span>${item.phonetic} · ${item.pos}</span></div>`).join('');
    }

    // ==========================================
    // 0.1 SUPABASE CLIENT & AUTH MANAGEMENT
    // ==========================================
    const SUPABASE_URL = 'https://tgcgdgmgxjuvwedwcvlf.supabase.co';
    const SUPABASE_ANON_KEY = 'sb_publishable_t_n3odLV8Icio8GY1DqSsg_3-KLku0E';
    var sbClient = null;
    try {
        if (window.supabase && typeof window.supabase.createClient === 'function') {
            sbClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
                auth: {
                    autoRefreshToken: true,
                    persistSession: true,
                    detectSessionInUrl: true
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
        $('#auth-screen')?.classList.add('hidden');
        $('#app-main')?.classList.add('authenticated');
        
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
        $('#app-main')?.classList.remove('authenticated');
        $('#auth-screen')?.classList.remove('hidden');
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
    function handleOAuthRedirectParams() {
        const hash = window.location.hash || '';
        const search = window.location.search || '';

        // 1. Kiểm tra lỗi nếu user bấm Hủy
        if (hash.includes('error=') || search.includes('error=')) {
            const params = new URLSearchParams(hash.startsWith('#') ? hash.substring(1) : search);
            const errorDesc = params.get('error_description') || params.get('error') || 'Đăng nhập không thành công';
            setAuthMessage(decodeURIComponent(errorDesc).replace(/\\+/g, ' '));
            window.history.replaceState(null, null, window.location.pathname);
            return false;
        }

        // 2. Kiểm tra access_token trong Hash Fragment (#access_token=...)
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

                    // Lưu trạng thái đăng nhập
                    localStorage.setItem('lingua-user', userName);

                    try {
                        const prof = JSON.parse(localStorage.getItem('lingua-profile') || '{}');
                        prof.name = userName;
                        if (userEmail) prof.email = userEmail;
                        localStorage.setItem('lingua-profile', JSON.stringify(prof));
                    } catch(e) {}

                    // Gán session cho Supabase client nếu có
                    if (sbClient && refreshToken) {
                        sbClient.auth.setSession({ access_token: accessToken, refresh_token: refreshToken }).catch(e => console.warn(e));
                    }

                    // Dọn dẹp URL hash sạch sẽ
                    window.history.replaceState(null, null, window.location.pathname + window.location.search);

                    // CHUYỂN NGAY VÀO TRANG CHỦ!
                    showApp(userName);
                    notify(`Chào mừng ${userName} đã đăng nhập thành công! 🎉`);
                    return true;
                }
            } catch (err) {
                console.error('Lỗi phân tích OAuth Token:', err);
            }
        }
        return false;
    }

    function initAuth() {
        // Bước 1: Xử lý redirect OAuth2 nếu vừa đăng nhập qua Google/GitHub/Microsoft
        const isOAuth = handleOAuthRedirectParams();
        if (isOAuth) return;

        // Bước 2: Kiểm tra phiên đăng nhập đã lưu trong LocalStorage
        const savedUser = localStorage.getItem('lingua-user');
        if (savedUser) {
            showApp(savedUser);
            return;
        }

        // Bước 3: Kiểm tra session từ Supabase
        if (sbClient) {
            sbClient.auth.getSession().then(({ data: { session } }) => {
                if (session && session.user) {
                    const u = session.user;
                    const name = u.user_metadata?.full_name || u.user_metadata?.name || u.email?.split('@')[0] || 'Học viên';
                    localStorage.setItem('lingua-user', name);
                    showApp(name);
                } else {
                    showLogin();
                }
            }).catch(() => {
                showLogin();
            });

            // Lắng nghe sự kiện đăng nhập thay đổi
            sbClient.auth.onAuthStateChange((event, session) => {
                if (session && session.user) {
                    const u = session.user;
                    const name = u.user_metadata?.full_name || u.user_metadata?.name || u.email?.split('@')[0] || 'Học viên';
                    localStorage.setItem('lingua-user', name);
                    showApp(name);
                }
            });
        } else {
            showLogin();
        }
    }
"""

# Insert auth_and_core_js before window.handleSocialLogin
marker_social = "// 1. Social Login (Google, GitHub, Microsoft) trực tiếp qua Supabase Auth Gateway"
if marker_social in content:
    content = content.replace(marker_social, auth_and_core_js + "\n    " + marker_social)
    print("Injected core helpers and auth engine before handleSocialLogin.")
else:
    print("Error: marker_social not found!")
    sys.exit(1)

# Now attach listeners and initAuth at the end of the script before </script>
footer_listeners = """
    // ==========================================
    // 10. AUTH & INTERFACE EVENT LISTENERS
    // ==========================================
    // Chuyển tab Đăng nhập / Đăng ký
    $$('.auth-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            $$('.auth-tab').forEach(t => t.classList.remove('active'));
            $$('.auth-form').forEach(f => f.classList.remove('active'));
            tab.classList.add('active');
            $(`#${tab.dataset.tab}-form`)?.classList.add('active');
            setAuthMessage('');
        });
    });

    // Chuyển đổi giữa Mật khẩu và OTP
    $('#toggle-otp-login')?.addEventListener('click', () => {
        const isOtp = $('#login-otp-section').style.display !== 'none';
        if (isOtp) {
            $('#login-otp-section').style.display = 'none';
            $('#login-password-section').style.display = 'block';
            $('#toggle-otp-login').textContent = 'Đăng nhập qua mã OTP';
        } else {
            $('#login-otp-section').style.display = 'block';
            $('#login-password-section').style.display = 'none';
            $('#toggle-otp-login').textContent = 'Đăng nhập qua Mật khẩu';
        }
        setAuthMessage('');
    });

    // Gửi mã OTP
    $('#btn-send-otp')?.addEventListener('click', async () => {
        const email = $('#login-email')?.value.trim();
        if (!email) return setAuthMessage('Vui lòng nhập Email để nhận mã OTP.');
        
        $('#btn-send-otp').textContent = 'Đang gửi mã...';
        $('#btn-send-otp').disabled = true;

        if (sbClient) {
            const { error } = await sbClient.auth.signInWithOtp({ email });
            if (error) {
                setAuthMessage('Lỗi gửi OTP: ' + error.message);
                $('#btn-send-otp').disabled = false;
                $('#btn-send-otp').textContent = 'Gửi mã OTP qua Email';
                return;
            }
        }
        
        $('#otp-inputs-wrapper').style.display = 'block';
        $('#btn-send-otp').style.display = 'none';
        setAuthMessage('Mã OTP đã được gửi đến hộp thư email của bạn!', false);
    });

    // Xác nhận mã OTP
    $('#btn-verify-otp')?.addEventListener('click', async () => {
        const email = $('#login-email')?.value.trim();
        const otp = $('#login-otp')?.value.trim();
        if (!otp) return setAuthMessage('Vui lòng nhập mã OTP 6 chữ số.');

        setAuthMessage('Đang xác thực...', false);
        if (sbClient) {
            const { data, error } = await sbClient.auth.verifyOtp({ email, token: otp, type: 'email' });
            if (error) return setAuthMessage('Mã OTP không hợp lệ hoặc đã hết hạn.');
            const name = data.user?.user_metadata?.full_name || email.split('@')[0];
            localStorage.setItem('lingua-user', name);
            showApp(name);
            notify(`Chào mừng ${name}!`);
        } else {
            const name = email.split('@')[0];
            localStorage.setItem('lingua-user', name);
            showApp(name);
        }
    });

    // Đăng nhập bằng Mật khẩu (Form Submit)
    $('#login-form')?.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = $('#login-email')?.value.trim();
        const password = $('#login-password')?.value;
        if (!email) return setAuthMessage('Vui lòng nhập Email.');

        setAuthMessage('Đang kiểm tra...', false);
        if (sbClient && password) {
            const { data, error } = await sbClient.auth.signInWithPassword({ email, password });
            if (error) {
                setAuthMessage('Thông tin đăng nhập chưa chính xác. Bạn có thể bấm "Dùng thử ngay (Khách)" hoặc Đăng ký tài khoản mới.');
                return;
            }
            const name = data.user?.user_metadata?.full_name || email.split('@')[0];
            localStorage.setItem('lingua-user', name);
            showApp(name);
            notify(`Đăng nhập thành công! Chào ${name}`);
        } else {
            const name = email.split('@')[0];
            localStorage.setItem('lingua-user', name);
            showApp(name);
        }
    });

    // Đăng ký tài khoản mới
    $('#register-form')?.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = $('#reg-name')?.value.trim();
        const email = $('#reg-email')?.value.trim();
        const password = $('#reg-password')?.value;
        if (!email || !password) return setAuthMessage('Vui lòng điền đầy đủ email và mật khẩu.');

        setAuthMessage('Đang tạo tài khoản...', false);
        if (sbClient) {
            const { data, error } = await sbClient.auth.signUp({
                email,
                password,
                options: { data: { full_name: name } }
            });
            if (error) return setAuthMessage('Lỗi đăng ký: ' + error.message);
        }
        localStorage.setItem('lingua-user', name || email.split('@')[0]);
        showApp(name || email.split('@')[0]);
        notify('Đăng ký tài khoản thành công!');
    });

    // Dùng thử ngay với tư cách Khách
    $('#btn-guest-login')?.addEventListener('click', () => {
        const guest = 'Khách Trải Nghiệm';
        localStorage.setItem('lingua-user', guest);
        showApp(guest);
        notify('Đang dùng thử với tư cách Khách.');
    });
    $('#btn-guest-register')?.addEventListener('click', () => {
        const guest = 'Khách Trải Nghiệm';
        localStorage.setItem('lingua-user', guest);
        showApp(guest);
        notify('Đang dùng thử với tư cách Khách.');
    });

    // Đăng xuất
    $('#logout-btn')?.addEventListener('click', async () => {
        if (sbClient) {
            try { await sbClient.auth.signOut(); } catch(e) {}
        }
        localStorage.removeItem('lingua-user');
        showLogin();
        notify('Đã đăng xuất tài khoản.');
    });

    // UI Click Listeners
    $$('.nav button').forEach(button => button.addEventListener('click', () => showView(button.dataset.view)));
    $$('[data-go]').forEach(button => button.addEventListener('click', () => showView(button.dataset.go)));
    
    $$('[data-filter]').forEach(button => button.addEventListener('click', () => {
      activeFilter = button.dataset.filter;
      $$('[data-filter]').forEach(item => item.classList.toggle('active', item === button));
      renderCourses();
    }));

    $$('[data-practice-filter]').forEach(button => button.addEventListener('click', () => {
      practiceFilter = button.dataset.practiceFilter;
      $$('[data-practice-filter]').forEach(item => item.classList.toggle('active', item === button));
      renderCourses();
    }));

    $('#course-search')?.addEventListener('input', renderCourses);

    document.addEventListener('click', event => {
      const startButton = event.target.closest('[data-start]');
      if (startButton) openExam(startButton.dataset.start);
    });

    $('#close-modal')?.addEventListener('click', closeExam);
    $('#exam-backdrop')?.addEventListener('click', event => { if (event.target === $('#exam-backdrop')) closeExam(); });

    $('#reveal-word')?.addEventListener('click', () => { wordRevealed = !wordRevealed; showWord(wordIndex); });
    $('#next-word')?.addEventListener('click', () => { wordIndex = (wordIndex + 1) % words.length; wordRevealed = false; flashRevealed = false; showWord(wordIndex); });
    $('#flashcard')?.addEventListener('click', () => { flashRevealed = !flashRevealed; wordRevealed = flashRevealed; showWord(wordIndex); });
    $('.notify')?.addEventListener('click', () => notify('Bạn đã hoàn thành 5 ngày học liên tiếp!'));

    const now = new Date();
    if ($('#today-label')) $('#today-label').textContent = new Intl.DateTimeFormat('vi-VN', { weekday: 'long', day: 'numeric', month: 'long' }).format(now);
    if ($('#date-pill')) $('#date-pill').textContent = new Intl.DateTimeFormat('vi-VN', { day: 'numeric', month: 'long', year: 'numeric' }).format(now);

    // KHỞI CHẠY TẤT CẢ
    renderCourses();
    showWord(0);
    updateScores();
    renderBookmarksView();
    renderProfileView();
    initAuth();
  </script>
"""

# Replace old ending
old_ending = """    renderCourses();
    showWord(0);
    updateScores();
    renderBookmarksView();
    renderProfileView();
    renderBookmarksView();
    renderProfileView();
  </script>"""

if old_ending in content:
    content = content.replace(old_ending, footer_listeners)
    print("Replaced footer initialization with complete listeners and initAuth.")
else:
    print("Warning: old_ending exact match failed, searching near </script>")
    end_script_idx = content.rfind("</script>")
    start_replace = content.rfind("renderCourses();", 0, end_script_idx)
    content = content[:start_replace] + footer_listeners + content[end_script_idx+9:]
    print("Replaced footer dynamically.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Patch applied successfully!")
