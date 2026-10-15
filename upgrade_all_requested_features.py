import re

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# -----------------------------------------------------------------
# 1. ADD SHEETJS CDN (for Excel .xlsx and .xls file parsing)
# -----------------------------------------------------------------
sheetjs_tag = '<script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>'
if 'xlsx.full.min.js' not in content:
    content = content.replace(
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js"></script>',
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js"></script>\n  ' + sheetjs_tag
    )
    print("SUCCESS: Added SheetJS CDN script")

# -----------------------------------------------------------------
# 2. TOPBAR & AUTH MODAL ENHANCEMENT:
#    - Show Login/Register button on topbar
#    - Add close button (X) to #auth-screen so users can explore landing page freely
# -----------------------------------------------------------------
old_topbar_actions = """        <div class="top-actions"><span class="today" id="today-label"></span><button class="notify" aria-label="Thông báo">♧</button><div class="avatar" id="topbar-avatar" style="cursor:pointer;" title="Xem hồ sơ cá nhân" onclick="showView('profile')">MA</div></div>"""

new_topbar_actions = """        <div class="top-actions" style="display:flex; align-items:center; gap:10px;">
           <span class="today" id="today-label"></span>
           <button type="button" class="tool-btn" id="topbar-login-btn" onclick="showLogin()" style="background:var(--lime); color:var(--green-dark); font-weight:700; border:none; padding:7px 14px; border-radius:8px; cursor:pointer; display:flex; align-items:center; gap:6px; font-size:12.5px; transition:transform .15s;" onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='none'">
              <span>🔑</span> <span id="topbar-login-text">Đăng nhập / Đăng ký</span>
           </button>
           <button class="notify" aria-label="Thông báo">♧</button>
           <div class="avatar" id="topbar-avatar" style="cursor:pointer;" title="Xem hồ sơ cá nhân" onclick="showView('profile')">MA</div>
        </div>"""

if old_topbar_actions in content:
    content = content.replace(old_topbar_actions, new_topbar_actions, 1)
    print("SUCCESS: Updated topbar with login button")

# Add Close 'X' button to #auth-screen card
old_auth_card_start = '<div class="auth-card">'
new_auth_card_start = """<div class="auth-card" style="position:relative;">
      <button type="button" class="close-modal" onclick="closeLoginModal()" title="Đóng và khám phá trang chủ" style="position:absolute; top:16px; right:16px; cursor:pointer; width:32px; height:32px; border-radius:50%; border:1px solid var(--line); background:#f8fafc; font-size:16px; display:flex; align-items:center; justify-content:center;">✕</button>"""

if old_auth_card_start in content and 'closeLoginModal' not in content:
    content = content.replace(old_auth_card_start, new_auth_card_start, 1)
    print("SUCCESS: Added close X button to auth card")

# -----------------------------------------------------------------
# 3. ENHANCE VIEW-OVERVIEW (HOMEPAGE LANDING BANNER SHOWCASING ALL FEATURES)
# -----------------------------------------------------------------
old_welcome = """          <div class="welcome"><div><p class="eyebrow">Bắt đầu ngày mới</p><h1 id="welcome-name">Chào buổi sáng, Minh Anh</h1><p>Hôm nay mình học thêm một chút nhé.</p></div><div class="date-pill" id="date-pill"></div></div>"""

new_welcome = """          <!-- Banner Chào Mừng & Giới thiệu Nền tảng Lingua -->
          <div style="background:linear-gradient(135deg, #173d32 0%, #235b48 100%); color:#fff; border-radius:16px; padding:24px 28px; margin-bottom:24px; box-shadow:0 10px 25px rgba(23,61,50,0.15); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:18px;">
             <div style="max-width:620px;">
                <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(201,239,117,0.2); color:#c9ef75; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:700; margin-bottom:10px; letter-spacing:.5px;">
                   <span>✨</span> NỀN TẢNG LUYỆN THI THÔNG MINH TOEIC & IELTS 4 KỸ NĂNG
                </div>
                <h1 id="welcome-name" style="margin:0 0 8px; font-size:24px; font-family:var(--display); color:#fff;">Chào bạn đến với Lingua English Hub</h1>
                <p style="margin:0 0 16px; font-size:13.5px; color:#d1e2d9; line-height:1.6;">
                   Khám phá trọn bộ đề thi thật ETS & Cambridge 4 kỹ năng (Nghe, Đọc, Viết, Nói), sổ tay từ vựng chuẩn CEFR B1 - C2, công cụ AI phân tích tài liệu (PDF, Excel, Word), và lộ trình học tập cá nhân hóa theo mục tiêu điểm số.
                </p>
                <div style="display:flex; gap:10px; flex-wrap:wrap;">
                   <button type="button" class="primary" onclick="showView('practice')" style="background:#c9ef75; color:#173d32; font-weight:700; padding:10px 18px; border:none; border-radius:8px; cursor:pointer;">
                      🚀 Luyện đề thi ngay (Miễn phí)
                   </button>
                   <button type="button" class="text-button" onclick="showView('analyzer')" style="background:rgba(255,255,255,0.12); color:#fff; border:1px solid rgba(255,255,255,0.25); padding:10px 18px; border-radius:8px; cursor:pointer; font-weight:600;">
                      🤖 Dùng thử AI Phân tích tài liệu
                   </button>
                   <button type="button" class="text-button" onclick="showLogin()" style="background:transparent; color:#c9ef75; border:1px dashed #c9ef75; padding:10px 18px; border-radius:8px; cursor:pointer; font-weight:700;">
                      🔑 Đăng nhập để lưu tiến độ
                   </button>
                </div>
             </div>
             <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; min-width:240px;">
                <div style="background:rgba(255,255,255,0.08); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center;">
                   <strong style="display:block; font-size:20px; color:#c9ef75;">4 Kỹ năng</strong>
                   <small style="font-size:11px; color:#b8c8bf;">TOEIC & IELTS</small>
                </div>
                <div style="background:rgba(255,255,255,0.08); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center;">
                   <strong style="display:block; font-size:20px; color:#c9ef75;">126+ Từ vựng</strong>
                   <small style="font-size:11px; color:#b8c8bf;">Chuẩn B1 - C2</small>
                </div>
                <div style="background:rgba(255,255,255,0.08); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center;">
                   <strong style="display:block; font-size:20px; color:#c9ef75;">AI Doc</strong>
                   <small style="font-size:11px; color:#b8c8bf;">PDF / Excel / Word</small>
                </div>
                <div style="background:rgba(255,255,255,0.08); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center;">
                   <strong style="display:block; font-size:20px; color:#c9ef75;">Real-Time</strong>
                   <small style="font-size:11px; color:#b8c8bf;">Chấm điểm & Lịch sử</small>
                </div>
             </div>
          </div>"""

if old_welcome in content:
    content = content.replace(old_welcome, new_welcome, 1)
    print("SUCCESS: Replaced overview banner with feature showcase")

# -----------------------------------------------------------------
# 4. ENHANCE VOCABULARY VIEW (view-vocabulary):
#    - Add interactive "Add Custom Word" form
#    - Add filter for "My Custom Words"
# -----------------------------------------------------------------
old_vocab_header = """          <!-- Bộ lọc Cấp độ & Chủ đề -->
          <div class="vocab-hub-header">"""

new_vocab_header = """          <!-- Khung Người dùng tự nhập từ vựng cá nhân từ bàn phím -->
          <div style="background:#fff; border:1px solid var(--line); border-radius:14px; padding:18px 22px; margin-bottom:20px; box-shadow:0 2px 6px rgba(0,0,0,0.03);">
             <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                <div style="display:flex; align-items:center; gap:8px;">
                   <span style="font-size:18px;">✍️</span>
                   <strong style="font-size:14px; color:var(--green-dark);">Tự thêm từ vựng theo nhu cầu công việc & cuộc sống của bạn</strong>
                </div>
                <span style="font-size:12px; color:var(--muted);">Từ bạn nhập sẽ tự động lưu vào Flashcard & Quiz</span>
             </div>
             
             <form id="add-custom-vocab-form" onsubmit="handleAddNewWord(event)" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)) 120px; gap:10px; align-items:end;">
                <div>
                   <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">TỪ TIẾNG ANH (*)</label>
                   <input type="text" id="inp-custom-word" class="auth-input" placeholder="VD: Overtime, Synergy..." required style="padding:9px 12px; font-size:13px;">
                </div>
                <div>
                   <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">NGHĨA TIẾNG VIỆT (*)</label>
                   <input type="text" id="inp-custom-meaning" class="auth-input" placeholder="VD: Làm thêm giờ, Sự phối hợp..." required style="padding:9px 12px; font-size:13px;">
                </div>
                <div>
                   <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">CHỦ ĐỀ</label>
                   <select id="inp-custom-topic" class="auth-input" style="padding:9px 12px; font-size:13px;">
                      <option value="business">🏢 Công sở & Kinh doanh</option>
                      <option value="daily">☕ Đời sống thường nhật</option>
                      <option value="tech">💻 Công nghệ & Trí tuệ AI</option>
                      <option value="travel">✈️ Du lịch & Dịch vụ</option>
                      <option value="health">🏥 Sức khỏe & Y tế</option>
                      <option value="environment">🌿 Môi trường & Khí hậu</option>
                      <option value="academic">🎓 Học thuật & Giáo dục</option>
                   </select>
                </div>
                <div>
                   <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">CẤP ĐỘ CEFR</label>
                   <select id="inp-custom-level" class="auth-input" style="padding:9px 12px; font-size:13px;">
                      <option value="B1">B1 (Trung cấp)</option>
                      <option value="B2" selected>B2 (Trung cao cấp)</option>
                      <option value="C1">C1 (Cao cấp)</option>
                      <option value="C2">C2 (Thành thạo)</option>
                   </select>
                </div>
                <div style="grid-column: span 2;">
                   <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">CÂU VÍ DỤ ỨNG DỤNG (TÙY CHỌN)</label>
                   <input type="text" id="inp-custom-example" class="auth-input" placeholder="VD: The team collaborated to achieve cross-functional synergy." style="padding:9px 12px; font-size:13px;">
                </div>
                <div>
                   <button type="submit" class="primary" style="width:100%; padding:10px 14px; font-size:13px; font-weight:700;">➕ Thêm từ</button>
                </div>
             </form>
          </div>

          <!-- Bộ lọc Cấp độ & Chủ đề -->
          <div class="vocab-hub-header">"""

if old_vocab_header in content:
    content = content.replace(old_vocab_header, new_vocab_header, 1)
    print("SUCCESS: Added custom vocabulary keyboard input form")

# Add "⭐ Từ tự thêm" filter pill in Level row
content = content.replace(
    """<button class="filter-pill-btn" data-vlevel="C2" onclick="filterVocabByLevel('C2')"><span class="level-badge c2">C2</span> Tinh hoa (Mastery)</button>""",
    """<button class="filter-pill-btn" data-vlevel="C2" onclick="filterVocabByLevel('C2')"><span class="level-badge c2">C2</span> Tinh hoa (Mastery)</button>
               <button class="filter-pill-btn" data-vlevel="custom" onclick="filterVocabByLevel('custom')" style="border-color:#f59e0b; color:#b45309;">⭐ Từ tôi tự thêm (<span id="custom-vocab-count-badge">0</span>)</button>"""
)

# -----------------------------------------------------------------
# 5. ENHANCE AI DOCUMENT ANALYZER (view-analyzer):
#    - Add Excel (.xlsx, .xls) support in dropzone and input
#    - Add sample Excel document chip
#    - Ensure dropzone has clear drag-and-drop visuals
# -----------------------------------------------------------------
content = content.replace(
    'accept=".pdf,.docx,.doc,.txt"',
    'accept=".pdf,.docx,.doc,.xlsx,.xls,.txt"'
)

content = content.replace(
    'Bấm vào đây hoặc Kéo & Thả file PDF / Word (.docx) vào đây',
    'Bấm vào đây hoặc Kéo & Thả file PDF, Excel (.xlsx/.xls), Word (.docx) vào đây'
)

content = content.replace(
    'Hỗ trợ định dạng: <strong>.pdf, .docx, .doc, .txt</strong> (Tối đa 15MB)',
    'Hỗ trợ định dạng: <strong>.pdf, .xlsx, .xls, .docx, .doc, .txt</strong> (Tối đa 25MB)'
)

# Add Excel sample document chip
old_sample_chips = """                     <button type="button" class="sample-doc-btn" onclick="loadSampleDocument('toeic')">
                        <span>🏢</span> Mẫu TOEIC Business: Tech Corp Quarterly Strategy
                     </button>"""

new_sample_chips = """                     <button type="button" class="sample-doc-btn" onclick="loadSampleDocument('toeic')">
                        <span>🏢</span> Mẫu TOEIC Business: Tech Corp Quarterly Strategy (.docx)
                     </button>
                     <button type="button" class="sample-doc-btn" onclick="loadSampleDocument('excel')">
                        <span>📊</span> Mẫu Excel: Báo cáo Doanh thu & Chi phí Vận hành Q3 (.xlsx)
                     </button>"""

if old_sample_chips in content:
    content = content.replace(old_sample_chips, new_sample_chips, 1)
    print("SUCCESS: Added Excel sample document chip")

# -----------------------------------------------------------------
# 6. ENHANCE PROFILE VIEW (view-profile):
#    - Add Interactive Target Assessment (Options for target, current level, weak skill, study time, goal)
#    - Add Personalized AI Study Strategy Generator
# -----------------------------------------------------------------
old_profile_card = """                 <div class="target-gauge">
                    <div style="font-size:12px; color:#15803d; font-weight:700; margin-bottom:4px;">🎯 MỤC TIÊU HIỆN TẠI</div>
                    <div style="display:flex; justify-content:space-between; align-items:baseline;">
                       <strong id="profile-target-title" style="font-size:20px; font-family:var(--display); color:var(--green-dark);">TOEIC 750+</strong>
                       <span id="profile-countdown" style="font-size:12px; color:var(--muted);">Còn 45 ngày</span>
                    </div>
                 </div>"""

new_profile_card = """                 <div class="target-gauge">
                    <div style="font-size:12px; color:#15803d; font-weight:700; margin-bottom:4px;">🎯 MỤC TIÊU HIỆN TẠI</div>
                    <div style="display:flex; justify-content:space-between; align-items:baseline;">
                       <strong id="profile-target-title" style="font-size:20px; font-family:var(--display); color:var(--green-dark);">TOEIC 750+</strong>
                       <span id="profile-countdown" style="font-size:12px; color:var(--muted);">Còn 45 ngày</span>
                    </div>
                 </div>

                 <!-- Khảo sát mục tiêu cá nhân hóa & Gợi ý lộ trình AI -->
                 <div style="margin-top:20px; border-top:1px solid var(--line); padding-top:18px;">
                    <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
                       <span style="font-size:16px;">🤖</span>
                       <h4 style="margin:0; font-size:14px; color:var(--green-dark);">Khảo sát thiết lập lộ trình học tối ưu</h4>
                    </div>

                    <form id="ai-study-plan-form" onsubmit="generateStudyRoadmap(event)" style="display:flex; flex-direction:column; gap:12px;">
                       <div>
                          <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">1. KỲ THI & BAND ĐIỂM MỤC TIÊU</label>
                          <select id="survey-target-score" class="auth-input" style="padding:8px 12px; font-size:12.5px;">
                             <option value="TOEIC 550+">TOEIC 550+ (Cơ bản / Đầu ra Đại học)</option>
                             <option value="TOEIC 750+" selected>TOEIC 750+ (Tiêu chuẩn Doanh nghiệp đa quốc gia)</option>
                             <option value="TOEIC 850+">TOEIC 850+ (Quản lý / Giao tiếp chuyên nghiệp)</option>
                             <option value="TOEIC 950+">TOEIC 950+ (Chuyên gia ngôn ngữ)</option>
                             <option value="IELTS 5.5">IELTS 5.5 (Cơ bản / Xét tuyển)</option>
                             <option value="IELTS 6.5">IELTS 6.5 (Chuẩn Du học / Thạc sĩ)</option>
                             <option value="IELTS 7.5">IELTS 7.5 (Học thuật nâng cao / Định cư)</option>
                             <option value="IELTS 8.0+">IELTS 8.0+ (Xuất sắc / Định cư diện chuyên gia)</option>
                          </select>
                       </div>

                       <div>
                          <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">2. TRÌNH ĐỘ HIỆN TẠI CỦA BẠN</label>
                          <select id="survey-current-level" class="auth-input" style="padding:8px 12px; font-size:12.5px;">
                             <option value="A2">Mất gốc / Cơ bản (A1 - A2: 300 TOEIC / 4.0 IELTS)</option>
                             <option value="B1" selected>Trung cấp (B1: 500 TOEIC / 5.0 IELTS)</option>
                             <option value="B2">Khá / Tự tin giao tiếp (B2: 650 TOEIC / 6.0 IELTS)</option>
                             <option value="C1">Nâng cao (C1: 800+ TOEIC / 7.0+ IELTS)</option>
                          </select>
                       </div>

                       <div>
                          <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">3. KỸ NĂNG CẦN TẬP TRUNG KHẮC PHỤC</label>
                          <select id="survey-weak-skill" class="auth-input" style="padding:8px 12px; font-size:12.5px;">
                             <option value="Listening" selected>🎧 Listening (Nghe hiểu & Phản xạ âm)</option>
                             <option value="Reading">📖 Reading (Đọc hiểu & Từ vựng)</option>
                             <option value="Writing">✍️ Writing (Viết luận & Email thương mại)</option>
                             <option value="Speaking">🎙️ Speaking (Nói lưu loát & Phát âm)</option>
                          </select>
                       </div>

                       <div>
                          <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">4. THỜI GIAN HỌC MỖI NGÀY</label>
                          <select id="survey-daily-time" class="auth-input" style="padding:8px 12px; font-size:12.5px;">
                             <option value="20">20 phút/ngày (Học nhanh duy trì thói quen)</option>
                             <option value="45" selected>45 phút/ngày (Cân bằng & Tiến bộ đều)</option>
                             <option value="90">90 phút/ngày (Luyện thi tăng tốc)</option>
                             <option value="120">120 phút/ngày (Cấp tốc trong 30 ngày)</option>
                          </select>
                       </div>

                       <button type="submit" class="primary" style="padding:10px; margin-top:4px; font-weight:700; font-size:13px; display:flex; align-items:center; justify-content:center; gap:6px;">
                          <span>✨</span> AI Phân tích & Gợi ý lộ trình
                       </button>
                    </form>
                 </div>"""

if old_profile_card in content:
    content = content.replace(old_profile_card, new_profile_card, 1)
    print("SUCCESS: Added interactive target survey to profile view")

# Add AI Study Roadmap display container right below skills breakdown in profile view
old_profile_skills = """                    <h3 style="margin:0 0 16px; font-size:16px;">Phân tích năng lực 4 kỹ năng</h3>"""
new_profile_skills = """                    <h3 style="margin:0 0 16px; font-size:16px;">Phân tích năng lực 4 kỹ năng</h3>
                    <div id="ai-roadmap-box" style="margin-bottom:20px; background:#f0fdf4; border:1px solid #bbf7d0; border-radius:12px; padding:16px; display:none;">
                       <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                          <strong style="color:var(--green-dark); font-size:14px; display:flex; align-items:center; gap:6px;">
                             <span>🎯</span> Lộ trình học AI đề xuất riêng cho bạn
                          </strong>
                          <span class="skill-pill" id="roadmap-badge" style="background:#dcfce7; color:#15803d; font-weight:700;">TOEIC 750+</span>
                       </div>
                       <p id="roadmap-summary" style="font-size:12.5px; color:#1e293b; margin:0 0 12px; line-height:1.5;"></p>
                       <div id="roadmap-phases" style="display:grid; gap:8px;"></div>
                       <div style="margin-top:12px; display:flex; gap:8px;">
                          <button type="button" class="primary" style="padding:7px 14px; font-size:12px;" onclick="showView('practice')">Luyện đề theo lộ trình này →</button>
                          <button type="button" class="text-button" style="border:1px solid #bbf7d0; padding:7px 14px; font-size:12px;" onclick="showView('vocabulary')">Học từ vựng đề xuất</button>
                       </div>
                    </div>"""

if old_profile_skills in content:
    content = content.replace(old_profile_skills, new_profile_skills, 1)
    print("SUCCESS: Added AI roadmap display container to profile view")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("PART 1 UPDATES WRITTEN TO FILE!")
