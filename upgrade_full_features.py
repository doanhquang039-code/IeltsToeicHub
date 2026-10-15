# -*- coding: utf-8 -*-
import sys
import re

html_path = r"e:\EngLish-IE-Toeic\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. ADD CSS STYLES
new_css = """
    /* --- NEW FEATURES: 4 SKILLS, PROFILE, REPORTS, REVIEW --- */
    .skill-pill { display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; border-radius: 999px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .skill-pill.listening { background: #e0f2fe; color: #0369a1; }
    .skill-pill.reading { background: #dcfce7; color: #15803d; }
    .skill-pill.writing { background: #fef3c7; color: #b45309; }
    .skill-pill.speaking { background: #f3e8ff; color: #7e22ce; }
    
    .score-chip { font-family: var(--display); font-weight: 700; padding: 3px 8px; border-radius: 6px; font-size: 13px; }
    .score-chip.high { background: #dcfce7; color: #15803d; }
    .score-chip.mid { background: #fef9c3; color: #a16207; }
    .score-chip.low { background: #fee2e2; color: #b91c1c; }

    /* Audio Player */
    .audio-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; padding: 14px 18px; margin-bottom: 20px; display: flex; align-items: center; gap: 15px; }
    .audio-play-btn { width: 44px; height: 44px; border-radius: 50%; background: var(--green); color: #fff; border: none; cursor: pointer; display: grid; place-items: center; font-size: 18px; flex-shrink: 0; transition: transform .15s; }
    .audio-play-btn:hover { transform: scale(1.06); }
    .audio-track { flex: 1; }
    .audio-title { font-weight: 700; font-size: 13px; color: var(--green-dark); margin-bottom: 4px; display: flex; justify-content: space-between; }
    .audio-wave { height: 8px; background: #dcfce7; border-radius: 4px; position: relative; overflow: hidden; cursor: pointer; }
    .audio-progress { height: 100%; width: 0%; background: var(--green); border-radius: 4px; transition: width .2s linear; }
    .transcript-box { background: #fff; border: 1px dashed #cbd5e1; border-radius: 8px; padding: 12px 14px; margin-top: 10px; font-size: 13px; color: #475569; display: none; line-height: 1.6; }
    .transcript-box.show { display: block; }

    /* Reading Passage */
    .passage-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin-bottom: 20px; max-height: 260px; overflow-y: auto; font-size: 13px; line-height: 1.7; color: #334155; }
    .passage-card h4 { margin: 0 0 8px; font-size: 15px; color: var(--ink); }

    /* Writing Editor */
    .writing-box { display: flex; flex-direction: column; gap: 12px; margin-top: 15px; }
    .writing-prompt { background: #fdfbf7; border-left: 4px solid var(--lime); padding: 12px 16px; border-radius: 0 8px 8px 0; font-size: 13.5px; line-height: 1.6; }
    .writing-textarea { width: 100%; min-height: 220px; padding: 14px; border: 1px solid var(--line); border-radius: 10px; font-family: var(--sans); font-size: 14px; line-height: 1.6; resize: vertical; outline: none; }
    .writing-textarea:focus { border-color: var(--green); box-shadow: 0 0 0 3px rgba(35,91,72,.1); }
    .writing-stats { display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: var(--muted); }

    /* Speaking Recorder */
    .speaking-box { text-align: center; padding: 25px 15px; background: #faf5ff; border: 1px dashed #d8b4fe; border-radius: 12px; margin-top: 15px; }
    .record-btn { width: 68px; height: 68px; border-radius: 50%; background: #9333ea; color: #fff; border: none; font-size: 26px; cursor: pointer; margin: 15px auto; display: grid; place-items: center; transition: all .2s; }
    .record-btn:hover { transform: scale(1.08); background: #7e22ce; }
    .record-btn.recording { background: #ef4444; animation: pulse 1.2s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(239,68,68,0.5); } 70% { box-shadow: 0 0 0 16px rgba(239,68,68,0); } 100% { box-shadow: 0 0 0 0 rgba(239,68,68,0); } }

    /* Question tools: Bookmark & Report */
    .q-action-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid var(--line); }
    .q-action-btns { display: flex; gap: 8px; }
    .q-tool-btn { display: inline-flex; align-items: center; gap: 5px; background: #fff; border: 1px solid var(--line); padding: 5px 11px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer; color: var(--muted); transition: all .15s; }
    .q-tool-btn:hover { background: #f8fafc; color: var(--ink); border-color: #cbd5e1; }
    .q-tool-btn.bookmarked { color: #eab308; border-color: #fde047; background: #fefce8; }
    .q-tool-btn.reported { color: #ef4444; border-color: #fca5a5; background: #fef2f2; }

    /* Result Modal Upgrades */
    .result-score-card { display: flex; gap: 15px; justify-content: center; margin: 20px 0; }
    .result-score-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 15px 22px; text-align: center; }
    .result-score-box small { font-size: 11px; text-transform: uppercase; font-weight: 700; color: var(--muted); display: block; margin-bottom: 4px; }
    .result-score-box strong { font-family: var(--display); font-size: 28px; color: var(--green-dark); }

    /* Profile Layout */
    .profile-container { display: grid; grid-template-columns: 320px 1fr; gap: 24px; }
    .profile-card { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 24px; }
    .profile-header-avatar { width: 74px; height: 74px; border-radius: 20px; background: var(--lime); color: var(--green-dark); font-family: var(--display); font-size: 30px; display: grid; place-items: center; margin-bottom: 14px; font-weight: 700; }
    .target-gauge { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 14px; margin: 15px 0; }
    .skill-bar-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; font-size: 13px; }
    .skill-bar-track { width: 140px; height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; }
    .skill-bar-fill { height: 100%; border-radius: 4px; }

    /* Bookmarks & Reports Layout */
    .tabs-nav { display: flex; gap: 10px; border-bottom: 1px solid var(--line); margin-bottom: 20px; }
    .tab-btn { background: none; border: none; padding: 10px 16px; font-weight: 600; font-size: 14px; color: var(--muted); cursor: pointer; border-bottom: 2px solid transparent; }
    .tab-btn.active { color: var(--green); border-bottom-color: var(--green); }
    .bookmark-card { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 18px; margin-bottom: 12px; transition: transform .15s; }
    .bookmark-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }

    /* Review Modal */
    .review-item { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 18px; margin-bottom: 15px; }
    .review-item.is-correct { border-left: 5px solid #22c55e; }
    .review-item.is-wrong { border-left: 5px solid #ef4444; }
    .review-item.is-skipped { border-left: 5px solid #94a3b8; }
    
    @media (max-width: 900px) {
        .profile-container { grid-template-columns: 1fr; }
    }
"""

# Insert new CSS before </style>
html = html.replace("</style>", new_css + "\n  </style>")

# 2. ADD SIDEBAR NAV BUTTONS FOR BOOKMARKS & PROFILE
old_nav = """        <button class="active" data-view="overview"><span class="nav-glyph">⌂</span>Tổng quan</button>
        <button data-view="practice"><span class="nav-glyph">▤</span>Luyện đề</button>
        <button data-view="vocabulary"><span class="nav-glyph">Aa</span>Từ vựng</button>
        <button data-view="progress"><span class="nav-glyph">↗</span>Tiến độ</button>
      </nav>"""

new_nav = """        <button class="active" data-view="overview"><span class="nav-glyph">⌂</span>Tổng quan</button>
        <button data-view="practice"><span class="nav-glyph">▤</span>Luyện đề 4 kỹ năng</button>
        <button data-view="vocabulary"><span class="nav-glyph">Aa</span>Từ vựng</button>
        <button data-view="progress"><span class="nav-glyph">↗</span>Tiến độ & Lịch sử</button>
        <button data-view="bookmarks"><span class="nav-glyph">★</span>Đã lưu & Báo cáo</button>
        <button data-view="profile"><span class="nav-glyph">👤</span>Hồ sơ mục tiêu</button>
      </nav>"""

html = html.replace(old_nav, new_nav)

# 3. ADD PROFILE BUTTON ON TOPBAR AVATAR
html = html.replace(
    """<div class="avatar" id="topbar-avatar" aria-label="Tài khoản">MA</div>""",
    """<div class="avatar" id="topbar-avatar" style="cursor:pointer;" title="Xem hồ sơ cá nhân" onclick="showView('profile')">MA</div>"""
)

# 4. ADD NEW VIEWS: #view-bookmarks AND #view-profile
new_views_html = """
        <!-- VIEW: CÂU HỎI ĐÃ LƯU & BÁO CÁO -->
        <section class="view" id="view-bookmarks">
          <div class="page-title-row">
            <div>
              <p class="eyebrow">Sổ tay ghi nhớ</p>
              <h1>Câu hỏi đã lưu & Đã báo cáo</h1>
              <p>Ôn lại những câu khó và theo dõi phản hồi các câu bạn đã gửi báo cáo.</p>
            </div>
          </div>
          
          <div class="tabs-nav">
             <button class="tab-btn active" id="tab-btn-bookmarks" onclick="switchBookmarkTab('bookmarks')">⭐ Câu hỏi đã lưu (<span id="count-bookmarks">0</span>)</button>
             <button class="tab-btn" id="tab-btn-reports" onclick="switchBookmarkTab('reports')">🚩 Câu hỏi đã báo cáo (<span id="count-reports">0</span>)</button>
          </div>

          <div id="tab-content-bookmarks">
             <div id="bookmarks-list" style="display:flex; flex-direction:column; gap:12px;"></div>
          </div>

          <div id="tab-content-reports" style="display:none;">
             <div id="reports-list" style="display:flex; flex-direction:column; gap:12px;"></div>
          </div>
        </section>

        <!-- VIEW: HỒ SƠ NGƯỜI DÙNG & MỤC TIÊU -->
        <section class="view" id="view-profile">
          <div class="page-title-row">
            <div>
              <p class="eyebrow">Thông tin học viên</p>
              <h1>Hồ sơ & Mục tiêu điểm số</h1>
              <p>Tùy chỉnh mục tiêu chứng chỉ TOEIC / IELTS và xem thống kê toàn diện 4 kỹ năng.</p>
            </div>
          </div>

          <div class="profile-container">
             <!-- Cột trái: Thông tin cá nhân -->
             <div class="profile-card">
                <div class="profile-header-avatar" id="profile-big-avatar">MA</div>
                <h2 id="profile-display-name" style="margin:0 0 4px; font-size:20px;">Học viên</h2>
                <p id="profile-email" style="margin:0 0 15px; color:var(--muted); font-size:13px;">user@example.com</p>

                <div class="target-gauge">
                   <div style="font-size:12px; color:#15803d; font-weight:700; margin-bottom:4px;">🎯 MỤC TIÊU HIỆN TẠI</div>
                   <div style="display:flex; justify-content:space-between; align-items:baseline;">
                      <strong id="profile-target-title" style="font-size:20px; font-family:var(--display); color:var(--green-dark);">TOEIC 750+</strong>
                      <span id="profile-countdown" style="font-size:12px; color:var(--muted);">Còn 45 ngày</span>
                   </div>
                </div>

                <div style="margin-top:20px; border-top:1px solid var(--line); padding-top:18px;">
                   <h4 style="margin:0 0 12px; font-size:14px;">Cập nhật mục tiêu & Hồ sơ</h4>
                   <form id="profile-edit-form" style="display:flex; flex-direction:column; gap:10px;">
                      <div>
                         <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">TÊN HIỂN THỊ</label>
                         <input type="text" id="edit-profile-name" class="auth-input" style="padding:8px 12px;" required>
                      </div>
                      <div>
                         <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">KỲ THI MỤC TIÊU</label>
                         <select id="edit-profile-exam" class="auth-input" style="padding:8px 12px;">
                            <option value="TOEIC 550+">TOEIC 550+ (Cơ bản)</option>
                            <option value="TOEIC 750+" selected>TOEIC 750+ (Doanh nghiệp)</option>
                            <option value="TOEIC 850+">TOEIC 850+ (Thành thạo)</option>
                            <option value="TOEIC 950+">TOEIC 950+ (Xuất sắc)</option>
                            <option value="IELTS 6.0">IELTS 6.0 (Competent)</option>
                            <option value="IELTS 6.5">IELTS 6.5 (Standard)</option>
                            <option value="IELTS 7.0">IELTS 7.0 (Good User)</option>
                            <option value="IELTS 7.5">IELTS 7.5 (Very Good)</option>
                            <option value="IELTS 8.0+">IELTS 8.0+ (Expert)</option>
                         </select>
                      </div>
                      <div>
                         <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">NGÀY DỰ THI DỰ KIẾN</label>
                         <input type="date" id="edit-profile-date" class="auth-input" style="padding:8px 12px;">
                      </div>
                      <button type="submit" class="auth-btn" style="padding:10px; margin-top:5px; background:var(--green-dark); color:#fff;">Lưu thay đổi</button>
                   </form>
                </div>
             </div>

             <!-- Cột phải: Thống kê 4 kỹ năng & Dữ liệu -->
             <div style="display:flex; flex-direction:column; gap:20px;">
                <div class="profile-card">
                   <h3 style="margin:0 0 16px; font-size:16px;">Phân tích năng lực 4 kỹ năng</h3>
                   <div id="skills-breakdown">
                      <div class="skill-bar-row">
                         <span>🎧 Listening (Nghe hiểu)</span>
                         <div style="display:flex; align-items:center; gap:10px;">
                            <div class="skill-bar-track"><div class="skill-bar-fill" id="bar-listening" style="width:78%; background:#0284c7;"></div></div>
                            <strong id="val-listening" style="font-size:12px; width:45px; text-align:right;">78%</strong>
                         </div>
                      </div>
                      <div class="skill-bar-row">
                         <span>📖 Reading (Đọc hiểu)</span>
                         <div style="display:flex; align-items:center; gap:10px;">
                            <div class="skill-bar-track"><div class="skill-bar-fill" id="bar-reading" style="width:72%; background:#16a34a;"></div></div>
                            <strong id="val-reading" style="font-size:12px; width:45px; text-align:right;">72%</strong>
                         </div>
                      </div>
                      <div class="skill-bar-row">
                         <span>✍️ Writing (Viết luận)</span>
                         <div style="display:flex; align-items:center; gap:10px;">
                            <div class="skill-bar-track"><div class="skill-bar-fill" id="bar-writing" style="width:65%; background:#d97706;"></div></div>
                            <strong id="val-writing" style="font-size:12px; width:45px; text-align:right;">65%</strong>
                         </div>
                      </div>
                      <div class="skill-bar-row">
                         <span>🎙️ Speaking (Nói & Phát âm)</span>
                         <div style="display:flex; align-items:center; gap:10px;">
                            <div class="skill-bar-track"><div class="skill-bar-fill" id="bar-speaking" style="width:70%; background:#9333ea;"></div></div>
                            <strong id="val-speaking" style="font-size:12px; width:45px; text-align:right;">70%</strong>
                         </div>
                      </div>
                   </div>
                </div>

                <div class="profile-card">
                   <h3 style="margin:0 0 16px; font-size:16px;">Huy hiệu & Thành tích đạt được</h3>
                   <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:12px;">
                      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px; text-align:center;">
                         <div style="font-size:24px; margin-bottom:4px;">🔥</div>
                         <div style="font-weight:700; font-size:12px;">Streak 5 ngày</div>
                         <small style="color:var(--muted); font-size:10px;">Chăm chỉ mỗi ngày</small>
                      </div>
                      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px; text-align:center;">
                         <div style="font-size:24px; margin-bottom:4px;">🎯</div>
                         <div style="font-weight:700; font-size:12px;">Part 5 Master</div>
                         <small style="color:var(--muted); font-size:10px;">Đạt &gt;80% ngữ pháp</small>
                      </div>
                      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px; text-align:center;">
                         <div style="font-size:24px; margin-bottom:4px;">🏆</div>
                         <div style="font-weight:700; font-size:12px;">IELTS Fighter</div>
                         <small style="color:var(--muted); font-size:10px;">Hoàn thành đề thi viết</small>
                      </div>
                      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px; text-align:center;">
                         <div style="font-size:24px; margin-bottom:4px;">⚡</div>
                         <div style="font-weight:700; font-size:12px;">Speed Runner</div>
                         <small style="color:var(--muted); font-size:10px;">Làm bài dưới 10 phút</small>
                      </div>
                   </div>
                </div>

                <div class="profile-card" style="display:flex; justify-content:space-between; align-items:center;">
                   <div>
                      <h4 style="margin:0 0 4px; font-size:14px; color:#ef4444;">Xóa dữ liệu học tập cục bộ</h4>
                      <p style="margin:0; font-size:12px; color:var(--muted);">Xóa toàn bộ lịch sử thi, câu đã lưu và đặt lại từ đầu.</p>
                   </div>
                   <button type="button" class="text-button" style="color:#ef4444; border:1px solid #fca5a5; padding:6px 14px; border-radius:6px;" onclick="resetUserData()">Xóa dữ liệu</button>
                </div>
             </div>
          </div>
        </section>
"""

# Insert new views right before </main>
html = html.replace("</main>", new_views_html + "\n    </main>")

# 5. ADD REPORT MODAL AND REVIEW MODAL MARKUP (before </body>)
modals_html = """
  <!-- MODAL: BÁO CÁO CÂU HỎI -->
  <div class="modal-backdrop" id="report-modal" role="presentation">
    <section class="exam-modal" style="width:min(500px, 95%); height:auto; max-height:90vh; padding:25px;" role="dialog">
      <div class="modal-top">
         <div><div class="modal-label" style="color:#ef4444;">🚩 Báo cáo lỗi câu hỏi</div></div>
         <button class="close-modal" onclick="closeReportModal()">×</button>
      </div>
      <p style="font-size:13px; color:var(--muted); margin:10px 0 15px;">Chúng tôi trân trọng đóng góp của bạn để nội dung câu hỏi ngày càng chính xác hơn.</p>
      
      <form id="report-form" onsubmit="submitReport(event)">
         <input type="hidden" id="report-q-index">
         <div style="display:flex; flex-direction:column; gap:8px; margin-bottom:15px; font-size:13px;">
            <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
               <input type="radio" name="report_reason" value="Sai đáp án chính xác" checked> Đáp án chấm chưa chính xác
            </label>
            <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
               <input type="radio" name="report_reason" value="Lỗi ngữ pháp hoặc chính tả"> Lỗi ngữ pháp hoặc từ ngữ (typo)
            </label>
            <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
               <input type="radio" name="report_reason" value="Bản dịch tiếng Việt chưa chuẩn"> Bản dịch tiếng Việt chưa tự nhiên / chưa sát nghĩa
            </label>
            <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
               <input type="radio" name="report_reason" value="Lỗi file audio hoặc hình ảnh"> Lỗi phát âm audio / hình ảnh minh họa
            </label>
            <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
               <input type="radio" name="report_reason" value="Khác"> Lý do khác
            </label>
         </div>
         <textarea id="report-note" class="auth-input" style="height:90px; padding:10px; resize:none; font-size:13px;" placeholder="Mô tả cụ thể vấn đề hoặc đề xuất đáp án đúng..."></textarea>
         
         <div style="display:flex; justify-content:flex-end; gap:10px; margin-top:15px;">
            <button type="button" class="text-button" onclick="closeReportModal()">Hủy</button>
            <button type="submit" class="primary" style="background:#ef4444; border-color:#ef4444;">Gửi báo cáo</button>
         </div>
      </form>
    </section>
  </div>

  <!-- MODAL: XEM LẠI CHI TIẾT BÀI LÀM (REVIEW EXAM) -->
  <div class="modal-backdrop" id="review-modal" role="presentation">
    <section class="exam-modal" style="width:min(900px, 95%); height:92vh; max-height:92vh; padding:22px; display:flex; flex-direction:column;" role="dialog">
      <div class="modal-top">
         <div>
            <div class="modal-label" id="review-exam-label">Chi tiết bài thi</div>
            <div id="review-exam-meta" style="font-size:12px; color:var(--muted); margin-top:2px;"></div>
         </div>
         <button class="close-modal" onclick="closeReviewModal()">×</button>
      </div>
      <div id="review-content" style="flex:1; overflow-y:auto; margin-top:15px; padding-right:8px;"></div>
      <div style="padding-top:14px; border-top:1px solid var(--line); display:flex; justify-content:flex-end;">
         <button class="primary" onclick="closeReviewModal()">Đóng xem lại</button>
      </div>
    </section>
  </div>
"""

html = html.replace("""<div class="toast" id="toast" role="status"></div>""", """<div class="toast" id="toast" role="status"></div>\n""" + modals_html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("CSS, Nav, Views & Modals markup injected successfully!")
