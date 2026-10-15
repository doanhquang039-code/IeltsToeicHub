import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the Auth CSS
css_old = """    .auth-wrapper { position: fixed; inset: 0; z-index: 100; display: flex; align-items: center; justify-content: center; background: var(--green-dark); }
    .auth-wrapper.hidden { display: none; }
    .auth-card { width: min(400px, 90%); background: #fff; border-radius: 16px; padding: 40px; box-shadow: 0 20px 40px rgba(0,0,0,.2); animation: enter .4s ease both; }
    .auth-brand { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 30px; font-size: 24px; font-weight: 700; color: var(--green-dark); letter-spacing: .5px; }
    .auth-brand .brand-mark { width: 38px; height: 38px; font-size: 24px; border-radius: 12px 12px 12px 4px; }
    .auth-form { display: flex; flex-direction: column; gap: 15px; }
    .auth-input { width: 100%; padding: 14px 16px; border: 1px solid var(--line); border-radius: 8px; font-size: 14px; outline: none; transition: border-color .2s, box-shadow .2s; }
    .auth-input:focus { border-color: var(--green); box-shadow: 0 0 0 3px rgba(35,91,72,.1); }
    .auth-btn { padding: 14px; background: var(--lime); color: var(--green-dark); border: none; border-radius: 8px; font-weight: 700; font-size: 15px; cursor: pointer; transition: transform .15s; margin-top: 5px; }
    .auth-btn:hover { transform: translateY(-2px); background: #b8e064; }
    .logout-btn { background: transparent; border: 1px solid #355547; color: #a9bbb0; padding: 4px 8px; border-radius: 4px; font-size: 10px; cursor: pointer; margin-left: auto; transition: background .15s; }
    .logout-btn:hover { background: #355547; color: #fff; }
    .app { min-height: 100vh; display: none; }
    .app.authenticated { display: block; }"""

css_new = """    .auth-wrapper { position: fixed; inset: 0; z-index: 100; display: flex; align-items: center; justify-content: center; background: var(--green-dark); overflow-y: auto; padding: 20px; }
    .auth-wrapper.hidden { display: none; }
    .auth-card { width: min(420px, 100%); background: #fff; border-radius: 16px; padding: 35px; box-shadow: 0 20px 40px rgba(0,0,0,.2); animation: enter .4s ease both; margin: auto; }
    .auth-brand { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 25px; font-size: 24px; font-weight: 700; color: var(--green-dark); letter-spacing: .5px; }
    .auth-brand .brand-mark { width: 38px; height: 38px; font-size: 24px; border-radius: 12px 12px 12px 4px; }
    
    .auth-tabs { display: flex; border-bottom: 1px solid var(--line); margin-bottom: 20px; }
    .auth-tab { flex: 1; padding: 10px 0; text-align: center; cursor: pointer; font-weight: 600; color: var(--muted); border-bottom: 2px solid transparent; transition: all .2s; }
    .auth-tab.active { color: var(--green); border-bottom-color: var(--green); }
    
    .auth-form { display: none; flex-direction: column; gap: 12px; }
    .auth-form.active { display: flex; }
    .auth-input { width: 100%; padding: 12px 16px; border: 1px solid var(--line); border-radius: 8px; font-size: 14px; outline: none; transition: border-color .2s, box-shadow .2s; }
    .auth-input:focus { border-color: var(--green); box-shadow: 0 0 0 3px rgba(35,91,72,.1); }
    .auth-btn { padding: 14px; background: var(--lime); color: var(--green-dark); border: none; border-radius: 8px; font-weight: 700; font-size: 14px; cursor: pointer; transition: transform .15s; margin-top: 5px; }
    .auth-btn:hover { transform: translateY(-2px); background: #b8e064; }
    .auth-btn:disabled { opacity: 0.7; cursor: not-allowed; transform: none; }
    
    .social-auth { margin-top: 20px; }
    .social-divider { display: flex; align-items: center; text-align: center; color: var(--muted); font-size: 11px; margin-bottom: 15px; }
    .social-divider::before, .social-divider::after { content: ''; flex: 1; border-bottom: 1px solid var(--line); }
    .social-divider:not(:empty)::before { margin-right: 10px; }
    .social-divider:not(:empty)::after { margin-left: 10px; }
    .social-btns { display: grid; grid-template-columns: 1fr; gap: 10px; }
    .social-btn { display: flex; align-items: center; justify-content: center; gap: 10px; padding: 10px; border: 1px solid var(--line); border-radius: 8px; background: #fff; color: var(--ink); font-weight: 600; font-size: 13px; cursor: pointer; transition: background .15s; }
    .social-btn:hover { background: #f5f8f3; }
    .social-btn img { width: 18px; height: 18px; }
    
    .otp-section { display: none; flex-direction: column; gap: 12px; padding: 15px; background: #f8fbf7; border-radius: 8px; border: 1px solid #d9e5da; margin-top: 5px; }
    .otp-section.active { display: flex; }
    
    .logout-btn { background: transparent; border: 1px solid #355547; color: #a9bbb0; padding: 4px 8px; border-radius: 4px; font-size: 10px; cursor: pointer; margin-left: auto; transition: background .15s; }
    .logout-btn:hover { background: #355547; color: #fff; }
    .app { min-height: 100vh; display: none; }
    .app.authenticated { display: block; }"""

content = content.replace(css_old, css_new)

# Replace the HTML for Login Modal
html_old = """  <div class="auth-wrapper" id="auth-screen">
    <div class="auth-card">
      <div class="auth-brand"><span class="brand-mark">L</span> lingua<span style="color:var(--green)">.</span></div>
      <form class="auth-form" id="login-form">
         <h2 style="margin: 0 0 5px; text-align: center; font-size: 22px; color: var(--ink);">Đăng nhập</h2>
         <p style="text-align: center; color: var(--muted); font-size: 13px; margin: 0 0 25px;">Chào mừng trở lại! Hãy tiếp tục hành trình.</p>
         <input type="text" class="auth-input" id="auth-name" placeholder="Tên của bạn (VD: Minh Anh)" required>
         <input type="email" class="auth-input" id="auth-email" placeholder="Địa chỉ Email" required>
         <input type="password" class="auth-input" id="auth-password" placeholder="Mật khẩu" required>
         <button type="submit" class="auth-btn">Vào Không Gian Học</button>
      </form>
    </div>
  </div>"""

html_new = """  <div class="auth-wrapper" id="auth-screen">
    <div class="auth-card">
      <div class="auth-brand"><span class="brand-mark">L</span> lingua<span style="color:var(--green)">.</span></div>
      
      <div class="auth-tabs">
         <div class="auth-tab active" data-tab="login">Đăng nhập</div>
         <div class="auth-tab" data-tab="register">Đăng ký</div>
      </div>

      <!-- Login Form -->
      <form class="auth-form active" id="login-form">
         <p style="text-align: center; color: var(--muted); font-size: 12px; margin: 0 0 10px;">Đăng nhập bằng Email và mã OTP</p>
         <input type="email" class="auth-input" id="login-email" placeholder="Địa chỉ Email" required>
         <button type="button" class="auth-btn" id="btn-send-otp" style="background: var(--green-dark); color: #fff;">Gửi mã OTP</button>
         
         <div class="otp-section" id="login-otp-section">
             <p style="margin:0; font-size:11px; color:var(--muted); text-align:center;">Mã gồm 6 chữ số đã được gửi đến email.</p>
             <input type="text" class="auth-input" id="login-otp" placeholder="Nhập mã OTP (6 số)" maxlength="6">
             <button type="submit" class="auth-btn">Xác nhận & Đăng nhập</button>
         </div>
      </form>

      <!-- Register Form -->
      <form class="auth-form" id="register-form">
         <input type="text" class="auth-input" id="reg-name" placeholder="Tên hiển thị (Username)" required>
         <input type="email" class="auth-input" id="reg-email" placeholder="Địa chỉ Email" required>
         <input type="password" class="auth-input" id="reg-password" placeholder="Mật khẩu" required>
         <button type="submit" class="auth-btn">Đăng ký tài khoản</button>
      </form>

      <div class="social-auth">
         <div class="social-divider">HOẶC ĐĂNG NHẬP BẰNG</div>
         <div class="social-btns">
            <button class="social-btn" id="btn-google">
               <img src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google">
               Google
            </button>
            <button class="social-btn" id="btn-github">
               <img src="https://www.svgrepo.com/show/512317/github-142.svg" alt="GitHub">
               GitHub
            </button>
            <button class="social-btn" id="btn-microsoft">
               <img src="https://www.svgrepo.com/show/475662/microsoft.svg" alt="Microsoft">
               Microsoft
            </button>
         </div>
      </div>
      
      <div id="auth-message" style="margin-top: 15px; font-size: 12px; text-align: center; color: var(--coral);"></div>
    </div>
  </div>"""
content = content.replace(html_old, html_new)

# Add Supabase CDN just before closing body
supabase_script = """  <!-- Supabase CDN -->
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
"""
content = content.replace("  <script>", supabase_script + "  <script>")

# Replace JS logic
js_auth_old = """    function initAuth() {
        const user = localStorage.getItem('lingua-user');
        if (user) {
            showApp(user);
        } else {
            $('#auth-screen').classList.remove('hidden');
            $('#app-main').classList.remove('authenticated');
        }
    }

    function showApp(name) {
        $('#auth-screen').classList.add('hidden');
        $('#app-main').classList.add('authenticated');
        
        $('#sidebar-name').textContent = name;
        $('#welcome-name').textContent = `Chào bạn, ${name}`;
        
        const parts = name.trim().split(' ');
        const initials = parts.length > 1 ? parts[0][0] + parts[parts.length-1][0] : name.slice(0, 2);
        const uppercaseInitials = initials.toUpperCase();
        $('#sidebar-avatar').textContent = uppercaseInitials;
        $('#topbar-avatar').textContent = uppercaseInitials;
        $('#topbar-avatar').setAttribute('aria-label', name);
    }

    $('#login-form')?.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = $('#auth-name').value.trim();
        if (name) {
            localStorage.setItem('lingua-user', name);
            showApp(name);
        }
    });

    $('#logout-btn')?.addEventListener('click', () => {
        localStorage.removeItem('lingua-user');
        $('#app-main').classList.remove('authenticated');
        $('#auth-screen').classList.remove('hidden');
        $('#auth-name').value = '';
        $('#auth-password').value = '';
    });"""

js_auth_new = """    // Thay thế bằng Credentials thật của dự án Supabase
    const SUPABASE_URL = 'https://YOUR_PROJECT_ID.supabase.co';
    const SUPABASE_KEY = 'YOUR_ANON_KEY';
    
    // Khởi tạo Supabase client (hiện tại dùng URL giả nên sẽ catch error để demo UI)
    let supabase = null;
    try {
        supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
    } catch (e) {
        console.warn("Supabase chưa được cấu hình đúng. Dùng dữ liệu mô phỏng.");
    }

    function initAuth() {
        const user = localStorage.getItem('lingua-user');
        if (user) {
            showApp(user);
        } else {
            $('#auth-screen').classList.remove('hidden');
            $('#app-main').classList.remove('authenticated');
        }
        
        // Kiểm tra session thực tế từ Supabase nếu có
        /*
        supabase?.auth.getSession().then(({ data: { session } }) => {
            if (session) {
                const name = session.user.user_metadata.full_name || session.user.email;
                localStorage.setItem('lingua-user', name);
                showApp(name);
            }
        });
        */
    }

    function showApp(name) {
        $('#auth-screen').classList.add('hidden');
        $('#app-main').classList.add('authenticated');
        
        const displayName = name.split('@')[0]; // fallback nếu là email
        
        $('#sidebar-name').textContent = displayName;
        $('#welcome-name').textContent = `Chào bạn, ${displayName}`;
        
        const parts = displayName.trim().split(' ');
        const initials = parts.length > 1 ? parts[0][0] + parts[parts.length-1][0] : displayName.slice(0, 2);
        const uppercaseInitials = initials.toUpperCase();
        $('#sidebar-avatar').textContent = uppercaseInitials;
        $('#topbar-avatar').textContent = uppercaseInitials;
        $('#topbar-avatar').setAttribute('aria-label', displayName);
    }

    function setAuthMessage(msg, isError = true) {
        const el = $('#auth-message');
        el.textContent = msg;
        el.style.color = isError ? 'var(--coral)' : 'var(--green)';
    }

    // Tabs logic
    $$('.auth-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            $$('.auth-tab').forEach(t => t.classList.remove('active'));
            $$('.auth-form').forEach(f => f.classList.remove('active'));
            tab.classList.add('active');
            $(`#${tab.dataset.tab}-form`).classList.add('active');
            setAuthMessage('');
        });
    });

    // 1. Login with OTP
    $('#btn-send-otp')?.addEventListener('click', async () => {
        const email = $('#login-email').value.trim();
        if (!email) return setAuthMessage('Vui lòng nhập email');
        
        $('#btn-send-otp').textContent = 'Đang gửi...';
        $('#btn-send-otp').disabled = true;
        
        // Đoạn code thực tế gọi Supabase
        /*
        const { error } = await supabase.auth.signInWithOtp({ email });
        if (error) {
            setAuthMessage(error.message);
            $('#btn-send-otp').disabled = false;
            return;
        }
        */
        
        // Mô phỏng thành công
        setTimeout(() => {
            $('#login-otp-section').classList.add('active');
            $('#btn-send-otp').style.display = 'none';
            setAuthMessage('Đã gửi mã OTP!', false);
        }, 1000);
    });

    $('#login-form')?.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = $('#login-email').value.trim();
        const otp = $('#login-otp').value.trim();
        
        if (!otp) return setAuthMessage('Vui lòng nhập mã OTP');
        
        // Đoạn code thực tế gọi Supabase
        /*
        const { data, error } = await supabase.auth.verifyOtp({ email, token: otp, type: 'email' });
        if (error) return setAuthMessage('Mã OTP không hợp lệ');
        const user = data.user;
        */
        
        // Mô phỏng
        localStorage.setItem('lingua-user', email);
        showApp(email);
    });

    // 2. Sign Up
    $('#register-form')?.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = $('#reg-name').value.trim();
        const email = $('#reg-email').value.trim();
        const password = $('#reg-password').value;
        
        // Đoạn code thực tế gọi Supabase
        /*
        const { data, error } = await supabase.auth.signUp({ 
            email, password, options: { data: { full_name: name } } 
        });
        if (error) return setAuthMessage(error.message);
        */
        
        // Mô phỏng
        setAuthMessage('Đăng ký thành công! Đang đăng nhập...', false);
        setTimeout(() => {
            localStorage.setItem('lingua-user', name);
            showApp(name);
        }, 1000);
    });

    // 3. Social Login
    const socialProviders = ['google', 'github', 'azure']; // Azure = Microsoft trong Supabase
    socialProviders.forEach(provider => {
        $(`#btn-${provider === 'azure' ? 'microsoft' : provider}`)?.addEventListener('click', async () => {
            // Đoạn code thực tế gọi Supabase
            /*
            await supabase.auth.signInWithOAuth({ provider });
            */
            
            // Mô phỏng
            const mockName = `${provider.charAt(0).toUpperCase() + provider.slice(1)} User`;
            localStorage.setItem('lingua-user', mockName);
            showApp(mockName);
        });
    });

    $('#logout-btn')?.addEventListener('click', async () => {
        // Đoạn code thực tế
        // await supabase?.auth.signOut();
        
        localStorage.removeItem('lingua-user');
        $('#app-main').classList.remove('authenticated');
        $('#auth-screen').classList.remove('hidden');
        $('#login-email').value = '';
        $('#login-otp').value = '';
        $('#login-otp-section').classList.remove('active');
        $('#btn-send-otp').style.display = 'block';
        $('#btn-send-otp').disabled = false;
        $('#btn-send-otp').textContent = 'Gửi mã OTP';
        setAuthMessage('');
    });"""

content = content.replace(js_auth_old, js_auth_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Backend Auth update complete")
