import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS for Auth
css_auth = """
    .auth-wrapper { position: fixed; inset: 0; z-index: 100; display: flex; align-items: center; justify-content: center; background: var(--green-dark); }
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
    .app.authenticated { display: block; }
"""
content = content.replace(".app { min-height: 100vh; }", css_auth)

# 2. Add Login HTML
login_html = """  <div class="auth-wrapper" id="auth-screen">
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
  </div>
  <div class="app" id="app-main">"""
content = content.replace('<div class="app">', login_html)

# 3. Update Sidebar Profile
sidebar_profile_old = '<div class="profile"><div class="avatar">MA</div><div><div class="profile-name">Minh Anh</div><div class="profile-level">Thành viên học tập</div></div></div>'
sidebar_profile_new = '<div class="profile"><div class="avatar" id="sidebar-avatar">MA</div><div><div class="profile-name" id="sidebar-name">Minh Anh</div><div class="profile-level">Thành viên học tập</div></div><button class="logout-btn" id="logout-btn" aria-label="Đăng xuất">Thoát</button></div>'
content = content.replace(sidebar_profile_old, sidebar_profile_new)

# 4. Update Topbar Avatar
topbar_old = '<div class="top-actions"><span class="today" id="today-label"></span><button class="notify" aria-label="Thông báo">♧</button><div class="avatar" aria-label="Minh Anh">MA</div></div>'
topbar_new = '<div class="top-actions"><span class="today" id="today-label"></span><button class="notify" aria-label="Thông báo">♧</button><div class="avatar" id="topbar-avatar" aria-label="Tài khoản">MA</div></div>'
content = content.replace(topbar_old, topbar_new)

# 5. Update Welcome Name
welcome_old = '<h1>Chào buổi sáng, Minh Anh</h1>'
welcome_new = '<h1 id="welcome-name">Chào buổi sáng, Minh Anh</h1>'
content = content.replace(welcome_old, welcome_new)

# 6. Add JS Logic
js_auth = """
    function initAuth() {
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
    });
"""
content = content.replace("renderCourses();", js_auth + "\n    initAuth();\n    renderCourses();")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Auth update complete")
