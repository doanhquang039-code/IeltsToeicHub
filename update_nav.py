import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar Nav to have the clean 4 student menus + 1 Admin menu
old_sidebar_nav = '''      <nav class="nav" aria-label="Điều hướng chính">
        <p class="nav-label">HỌC TẬP & ĐỀ THI</p>
        <button class="active" data-view="overview" onclick="showView('overview')" title="Trang chủ Lingua English Hub">
          <span class="nav-glyph">🏠</span>Trang chủ
        </button>
        <button data-view="practice" onclick="showView('practice')">
          <span class="nav-glyph">▤</span>Luyện đề 4 kỹ năng
        </button>
        <button data-view="vocabulary" onclick="showView('vocabulary')">
          <span class="nav-glyph">Aa</span>Sổ tay từ vựng
        </button>

        <p class="nav-label" style="margin-top:12px;">THEO DÕI NĂNG LỰC</p>
        <button data-view="progress" onclick="showView('progress')">
          <span class="nav-glyph">↗</span>Tiến độ & Lịch sử
        </button>
        <button data-view="bookmarks" onclick="showView('bookmarks')">
          <span class="nav-glyph">★</span>Đã lưu & Báo cáo
        </button>
        <button data-view="profile" onclick="showView('profile')">
          <span class="nav-glyph">👤</span>Hồ sơ mục tiêu
        </button>

        <p class="nav-label" style="margin-top:12px;">TRÍ TUỆ NHÂN TẠO</p>
        <button data-view="analyzer" onclick="showView('analyzer')">
          <span class="nav-glyph">🤖</span>AI Phân tích tài liệu
        </button>
      </nav>'''

new_sidebar_nav = '''      <nav class="nav" aria-label="Điều hướng chính">
        <p class="nav-label">TRANG CHỦ DỰ ÁN</p>
        <button class="active" data-view="overview" onclick="showView('overview')" title="Trang chủ Lingua English Hub">
          <span class="nav-glyph">🏠</span>Trang chủ Dự án
        </button>

        <p class="nav-label" style="margin-top:14px;">4 KHÔNG GIAN HỌC TẬP</p>
        <button data-view="practice" onclick="showView('practice')">
          <span class="nav-glyph">▤</span>1. Luyện đề 4 kỹ năng
        </button>
        <button data-view="vocabulary" onclick="showView('vocabulary')">
          <span class="nav-glyph">Aa</span>2. Sổ tay từ vựng CEFR
        </button>
        <button data-view="analyzer" onclick="showView('analyzer')">
          <span class="nav-glyph">🤖</span>3. AI Phân tích tài liệu
        </button>
        <button data-view="profile" onclick="showView('profile')">
          <span class="nav-glyph">👤</span>4. Hồ sơ & Lộ trình AI
        </button>

        <p class="nav-label" style="margin-top:14px;">KHÔNG GIAN QUẢN TRỊ</p>
        <button data-view="admin" id="nav-btn-admin" onclick="showView('admin')" style="color:#fde047;">
          <span class="nav-glyph" style="background:rgba(253,224,71,0.18); color:#fde047;">⚡</span>Admin Dashboard
        </button>
      </nav>'''

if old_sidebar_nav in html:
    html = html.replace(old_sidebar_nav, new_sidebar_nav)
    print("SUCCESS: Sidebar Nav Updated")
else:
    print("WARNING: Sidebar Nav exact match not found, looking for alternative match")
    nav_match = re.search(r'<nav class="nav" aria-label="Điều hướng chính">.*?</nav>', html, re.DOTALL)
    if nav_match:
        html = html[:nav_match.start()] + new_sidebar_nav + html[nav_match.end():]
        print("SUCCESS: Sidebar Nav Updated via regex")

# 2. Add Admin Switcher & Status to Topbar & Sidebar profile
old_profile_side = '''      <div class="profile">
        <div class="avatar" id="sidebar-avatar">MA</div>
        <div style="flex:1; min-width:0;">
          <div class="profile-name" id="sidebar-name" style="white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Minh Anh</div>
          <div class="profile-level">Học viên chính thức</div>
        </div>
        <button class="logout-btn" id="logout-btn" aria-label="Đăng xuất">Thoát</button>
      </div>'''

new_profile_side = '''      <div class="profile">
        <div class="avatar" id="sidebar-avatar">MA</div>
        <div style="flex:1; min-width:0;">
          <div class="profile-name" id="sidebar-name" style="white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">Minh Anh</div>
          <div class="profile-level" id="sidebar-role" style="display:flex; align-items:center; gap:4px;">
            <span>Học viên chính thức</span>
          </div>
        </div>
        <button class="logout-btn" id="logout-btn" aria-label="Đăng xuất">Thoát</button>
      </div>'''

if old_profile_side in html:
    html = html.replace(old_profile_side, new_profile_side)
    print("SUCCESS: Sidebar Profile Updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved partial update 1")
