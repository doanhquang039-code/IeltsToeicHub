# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r"e:\EngLish-IE-Toeic\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update .app.authenticated, .sidebar, .main, .view in CSS
old_css_part = """    .app { min-height: 100vh; display: none; }
    .app.authenticated { display: flex !important; width: 100%; min-height: 100vh; background: #f8fafc; }

    /* SIDEBAR: STICKY FLEX SIBLING - NEVER OVERLAPS CONTENT */
    .sidebar { width: 256px; min-width: 256px; max-width: 256px; height: 100vh; position: sticky; top: 0; z-index: 50; display: flex; flex-direction: column; padding: 18px 14px 14px; background: #0c1f18; color: #eaf1e9; border-right: 1px solid rgba(255,255,255,0.06); box-shadow: 4px 0 24px rgba(0,0,0,0.05); overflow-y: auto; overflow-x: hidden; box-sizing: border-box; flex-shrink: 0; scrollbar-width: thin; }"""

new_css_part = """    .app { min-height: 100vh; display: none; }
    .app.authenticated {
      display: flex !important;
      flex-direction: row !important;
      flex-wrap: nowrap !important;
      width: 100% !important;
      min-height: 100vh;
      background: #f8fafc;
    }

    /* SIDEBAR: STICKY FLEX SIBLING - NEVER OVERLAPS CONTENT */
    .sidebar {
      width: 256px !important;
      min-width: 256px !important;
      max-width: 256px !important;
      height: 100vh;
      position: sticky !important;
      top: 0 !important;
      z-index: 50;
      display: flex;
      flex-direction: column;
      padding: 18px 14px 14px;
      background: #0c1f18;
      color: #eaf1e9;
      border-right: 1px solid rgba(255,255,255,0.06);
      box-shadow: 4px 0 24px rgba(0,0,0,0.05);
      overflow-y: auto;
      overflow-x: hidden;
      box-sizing: border-box;
      flex-shrink: 0 !important;
      scrollbar-width: thin;
    }"""

if old_css_part in content:
    content = content.replace(old_css_part, new_css_part, 1)
    print("SUCCESS: Updated .app.authenticated and .sidebar in CSS")
else:
    print("WARNING: old_css_part not found")

# 2. Update .main and .view in CSS
old_main_css = """    /* MAIN AREA: FLEX: 1, ZERO MARGIN-LEFT - IMPOSSIBLE TO SLIDE UNDER SIDEBAR */
    .main { flex: 1; min-width: 0; margin-left: 0 !important; padding: 0 36px 48px; background: #f8fafc; overflow-x: hidden; box-sizing: border-box; }
    .topbar { display: flex; height: 72px; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 40; background: rgba(248, 250, 252, 0.94); backdrop-filter: blur(12px); margin-bottom: 8px; }
    .crumb { color: var(--muted); font-size: 13px; font-weight: 500; display: flex; align-items: center; }
    .crumb b { color: var(--ink); font-weight: 700; }
    .top-actions { display: flex; align-items: center; gap: 14px; }
    .today { color: var(--muted); font-size: 12.5px; font-weight: 500; }
    .notify { position: relative; display: grid; width: 36px; height: 36px; place-items: center; border: 1px solid var(--line); border-radius: 50%; background: #fff; cursor: pointer; transition: all .15s; }
    .notify:hover { background: #f1f5f9; transform: scale(1.05); }
    .notify::after { position: absolute; top: 8px; right: 8px; width: 6px; height: 6px; border: 1px solid #fff; border-radius: 50%; background: var(--coral); content: ''; }
    .page { max-width: 1240px; margin: 0 auto; width: 100%; box-sizing: border-box; }
    .view { display: none; padding-top: 18px; animation: enter .24s ease both; }
    .view.active { display: block; }"""

new_main_css = """    /* MAIN AREA: FLEX: 1, ZERO MARGIN-LEFT - IMPOSSIBLE TO SLIDE UNDER SIDEBAR */
    .main {
      flex: 1 1 0% !important;
      min-width: 0 !important;
      margin-left: 0 !important;
      padding: 0 36px 48px !important;
      background: #f8fafc;
      overflow-x: hidden;
      box-sizing: border-box;
    }
    .topbar { display: flex; height: 72px; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 40; background: rgba(248, 250, 252, 0.94); backdrop-filter: blur(12px); margin-bottom: 8px; }
    .crumb { color: var(--muted); font-size: 13px; font-weight: 500; display: flex; align-items: center; }
    .crumb b { color: var(--ink); font-weight: 700; }
    .top-actions { display: flex; align-items: center; gap: 14px; }
    .today { color: var(--muted); font-size: 12.5px; font-weight: 500; }
    .notify { position: relative; display: grid; width: 36px; height: 36px; place-items: center; border: 1px solid var(--line); border-radius: 50%; background: #fff; cursor: pointer; transition: all .15s; }
    .notify:hover { background: #f1f5f9; transform: scale(1.05); }
    .notify::after { position: absolute; top: 8px; right: 8px; width: 6px; height: 6px; border: 1px solid #fff; border-radius: 50%; background: var(--coral); content: ''; }
    .page { max-width: 1240px; margin: 0 auto; width: 100%; box-sizing: border-box; }
    .view { display: none !important; }
    .view.active { display: block !important; padding-top: 18px; animation: enter .24s ease both; }"""

if old_main_css in content:
    content = content.replace(old_main_css, new_main_css, 1)
    print("SUCCESS: Updated .main and .view in CSS")
else:
    print("WARNING: old_main_css not found")

# 3. Fix showApp display: block -> display: flex
old_show_app = """        const appEl = $('#app-main');
        if (appEl) {
            appEl.classList.add('authenticated');
            appEl.style.display = 'block';
        }"""

new_show_app = """        const appEl = $('#app-main');
        if (appEl) {
            appEl.classList.add('authenticated');
            appEl.style.display = 'flex';
        }"""

if old_show_app in content:
    content = content.replace(old_show_app, new_show_app, 1)
    print("SUCCESS: Updated showApp appEl.style.display to 'flex'")
else:
    print("WARNING: old_show_app not found")

# 4. Update analyzeTextWithAI to take optional shouldScroll parameter
old_analyze_fn_header = "function analyzeTextWithAI(title, text, forcedType = null) {"
new_analyze_fn_header = "function analyzeTextWithAI(title, text, forcedType = null, shouldScroll = true) {"
if old_analyze_fn_header in content:
    content = content.replace(old_analyze_fn_header, new_analyze_fn_header, 1)
    print("SUCCESS: Updated analyzeTextWithAI header")

old_analyze_scroll = "window.scrollTo({ top: $('#analyzer-results').offsetTop - 70, behavior: 'smooth' });"
new_analyze_scroll = "if (shouldScroll) { window.scrollTo({ top: $('#analyzer-results').offsetTop - 70, behavior: 'smooth' }); }"
if old_analyze_scroll in content:
    content = content.replace(old_analyze_scroll, new_analyze_scroll, 1)
    print("SUCCESS: Updated analyzeTextWithAI scroll condition")

# 5. Update showView to strictly isolate views with setProperty('display', '...', 'important')
old_show_view = """    function showView(name) {
      const allViews = $$('.view');
      allViews.forEach(view => {
          const isTarget = view.id === `view-${name}`;
          view.classList.toggle('active', isTarget);
          view.style.display = isTarget ? 'block' : 'none';
      });

      $$('.nav button').forEach(button => {
          button.classList.toggle('active', button.dataset.view === name);
      });
      
      const breadcrumbNames = {
          overview: 'Trang chủ Dự án Lingua Hub',
          practice: '1. Luyện đề 4 kỹ năng (ETS & Cambridge)',
          analyzer: '2. AI Phân tích tài liệu (PDF, Word, Excel)',
          profile: '3. Hồ sơ & Lộ trình AI cá nhân hóa',
          vocabulary: '4. Sổ tay từ vựng CEFR (Có phân trang)',
          progress: 'Tiến độ & Lịch sử điểm số',
          bookmarks: 'Đã lưu & Báo cáo câu hỏi',
          admin: '⚡ Admin Dashboard - Quản trị & Upload Đề thi'
      };
      if ($('#crumb-current')) $('#crumb-current').textContent = breadcrumbNames[name] || 'Không gian học';
      
      if (name === 'practice') renderCourses();
      if (name === 'vocabulary') { applyVocabFilters(); }
      if (name === 'analyzer') { 
          setupDropzone(); 
          const results = $('#analyzer-results');
          if (results && (results.style.display === 'none' || !$('#res-doc-summary')?.innerHTML.trim())) {
              const s = sampleDocuments.ielts;
              analyzeTextWithAI(s.title, s.text, s.type);
          }
      }
      if (name === 'bookmarks') renderBookmarksView();
      if (name === 'profile') renderProfileView();
      if (name === 'progress') updateScores();
      if (name === 'admin') renderAdminDashboard();
      
      window.scrollTo({ top: 0, behavior: 'instant' });
      const mainEl = document.querySelector('.main');
      if (mainEl) mainEl.scrollTop = 0;
      const sidebarEl = document.querySelector('.sidebar');
      if (sidebarEl) sidebarEl.scrollTop = 0;
    }"""

new_show_view = """    function showView(name) {
      // 1. Cưỡng chế ẩn toàn bộ tất cả các view với !important
      document.querySelectorAll('.view').forEach(view => {
          view.classList.remove('active');
          view.style.setProperty('display', 'none', 'important');
      });

      // 2. Chỉ kích hoạt duy nhất view được chọn
      const targetView = document.getElementById(`view-${name}`);
      if (targetView) {
          targetView.classList.add('active');
          targetView.style.setProperty('display', 'block', 'important');
      }

      // 3. Cập nhật nút active trên thanh sidebar
      document.querySelectorAll('.nav button').forEach(button => {
          button.classList.toggle('active', button.dataset.view === name);
      });
      
      const breadcrumbNames = {
          overview: 'Trang chủ Dự án Lingua Hub',
          practice: '1. Luyện đề 4 kỹ năng (ETS & Cambridge)',
          analyzer: '2. AI Phân tích tài liệu (PDF, Word, Excel)',
          profile: '3. Hồ sơ & Lộ trình AI cá nhân hóa',
          vocabulary: '4. Sổ tay từ vựng CEFR (Có phân trang)',
          progress: 'Tiến độ & Lịch sử điểm số',
          bookmarks: 'Đã lưu & Báo cáo câu hỏi',
          admin: '⚡ Admin Dashboard - Quản trị & Upload Đề thi'
      };
      if ($('#crumb-current')) $('#crumb-current').textContent = breadcrumbNames[name] || 'Không gian học';
      
      if (name === 'practice') renderCourses();
      if (name === 'vocabulary') { applyVocabFilters(); }
      if (name === 'analyzer') { 
          setupDropzone(); 
          const results = $('#analyzer-results');
          if (results && (results.style.display === 'none' || !$('#res-doc-summary')?.innerHTML.trim())) {
              const s = sampleDocuments.ielts;
              analyzeTextWithAI(s.title, s.text, s.type, false);
          }
      }
      if (name === 'bookmarks') renderBookmarksView();
      if (name === 'profile') renderProfileView();
      if (name === 'progress') updateScores();
      if (name === 'admin') renderAdminDashboard();
      
      // 4. Luôn luôn cuộn ngay về đỉnh trang khi chuyển menu
      window.scrollTo({ top: 0, behavior: 'instant' });
      document.documentElement.scrollTop = 0;
      document.body.scrollTop = 0;
      const mainEl = document.querySelector('.main');
      if (mainEl) mainEl.scrollTop = 0;
      const sidebarEl = document.querySelector('.sidebar');
      if (sidebarEl) sidebarEl.scrollTop = 0;
    }"""

if old_show_view in content:
    content = content.replace(old_show_view, new_show_view, 1)
    print("SUCCESS: Updated showView function with strict view isolation")
else:
    print("WARNING: old_show_view not found")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("FILE SAVED!")
