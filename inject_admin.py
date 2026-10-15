with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('admin_view_snippet.html', 'r', encoding='utf-8') as f:
    admin_view_html = f.read()

with open('admin_js_snippet.js', 'r', encoding='utf-8') as f:
    admin_js_code = f.read()

# 1. Insert admin_view_html right before `</div> <!-- end .page -->`
marker_page_end = '</div> <!-- end .page -->'
if 'id="view-admin"' not in html and marker_page_end in html:
    html = html.replace(marker_page_end, admin_view_html + '\n      ' + marker_page_end)
    print("SUCCESS: admin view HTML inserted before page end")
else:
    print("Check admin view insertion:", 'id="view-admin"' in html)

# 2. Update showView function to handle 'admin'
# Let's inspect showView definition in html
old_breadcrumb = '''      const breadcrumbNames = {
          overview: 'Trang chủ',
          practice: 'Luyện đề 4 kỹ năng',
          vocabulary: 'Sổ tay từ vựng theo chủ đề & CEFR',
          progress: 'Tiến độ & Lịch sử',
          bookmarks: 'Đã lưu & Báo cáo',
          profile: 'Hồ sơ mục tiêu',
          analyzer: 'AI Phân tích tài liệu (PDF, Excel, Word)'
      };'''

new_breadcrumb = '''      const breadcrumbNames = {
          overview: 'Trang chủ Dự án Lingua Hub',
          practice: '1. Luyện đề 4 kỹ năng (ETS & Cambridge)',
          vocabulary: '2. Sổ tay từ vựng CEFR B1 - C2',
          analyzer: '3. AI Phân tích tài liệu (PDF, Word, Excel)',
          profile: '4. Hồ sơ & Lộ trình AI cá nhân hóa',
          progress: 'Tiến độ & Lịch sử điểm số',
          bookmarks: 'Đã lưu & Báo cáo câu hỏi',
          admin: '⚡ Admin Dashboard - Quản trị & Upload Đề thi'
      };'''

if old_breadcrumb in html:
    html = html.replace(old_breadcrumb, new_breadcrumb)
    print("SUCCESS: breadcrumbNames updated")

# Also add if (name === 'admin') renderAdminDashboard();
old_showview_calls = '''      if (name === 'bookmarks') renderBookmarksView();
      if (name === 'profile') renderProfileView();
      if (name === 'progress') updateScores();'''

new_showview_calls = '''      if (name === 'bookmarks') renderBookmarksView();
      if (name === 'profile') renderProfileView();
      if (name === 'progress') updateScores();
      if (name === 'admin') renderAdminDashboard();'''

if old_showview_calls in html:
    html = html.replace(old_showview_calls, new_showview_calls)
    print("SUCCESS: showView calls updated")

# 3. Insert admin_js_code before `// KHỞI CHẠY TẤT CẢ`
marker_init = '// KHỞI CHẠY TẤT CẢ'
if 'function handleAdminSubmitExam' not in html and marker_init in html:
    html = html.replace(marker_init, admin_js_code + '\n\n    ' + marker_init)
    print("SUCCESS: admin JS code inserted")

# 4. In KHỞI CHẠY TẤT CẢ, call syncAdminExamsToSystem()
old_init_block = '''    // KHỞI CHẠY TẤT CẢ
    loadSavedCustomVocab();
    renderCourses();'''

new_init_block = '''    // KHỞI CHẠY TẤT CẢ
    syncAdminExamsToSystem();
    loadSavedCustomVocab();
    renderCourses();'''

if old_init_block in html:
    html = html.replace(old_init_block, new_init_block)
    print("SUCCESS: init block updated with syncAdminExamsToSystem")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with Admin module")
