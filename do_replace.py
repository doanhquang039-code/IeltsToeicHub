import sys
import io
import re

# sys.stdout reconfigure
pass

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace analyzer card 2
old_card2_re = r'<div class="analysis-card">\s*<div class="analysis-card-title"><span>💎</span>\s*Từ vựng học thuật & Collocations nổi bật</div>\s*<div id="res-doc-vocab"[^>]*></div>\s*</div>'
new_card2 = '''<div class="analysis-card">
                   <div class="analysis-card-title"><span>💡</span> Cấu trúc câu & Mẫu câu học thuật (Sentence Patterns)</div>
                   <div id="res-doc-patterns" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>'''

text, count = re.subn(old_card2_re, new_card2, text)
print(f"✓ Replaced analyzer card 2 (matches: {count})")

# 2. Replace view-profile section cleanly
p_start = text.find('<section class="view" id="view-profile">')
p_end = text.find('<!-- VIEW: AI PHÂN TÍCH TÀI LIỆU', p_start)

new_profile_content = '''<section class="view" id="view-profile">
          <div class="page-title-row">
            <div>
              <p class="eyebrow">Thông tin học viên</p>
              <h1>Hồ sơ & Mục tiêu điểm số</h1>
              <p>Tùy chỉnh mục tiêu chứng chỉ TOEIC / IELTS và xem lộ trình cá nhân hóa cùng phân tích 4 kỹ năng.</p>
            </div>
          </div>

          <!-- BANNER HỒ SƠ HỌC VIÊN CÙNG CỘT VỚI NỘI DUNG (FULL WIDTH CONTENT COLUMN) -->
          <div class="profile-card" style="margin-bottom:24px; background:linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); border:1px solid var(--line); border-radius:16px; padding:22px 26px;">
             <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px;">
                <div style="display:flex; align-items:center; gap:18px;">
                   <div class="profile-header-avatar" id="profile-big-avatar" style="margin-bottom:0; width:68px; height:68px; font-size:26px;">MA</div>
                   <div>
                      <div style="display:flex; align-items:center; gap:8px;">
                         <h2 id="profile-display-name" style="margin:0; font-size:21px; font-weight:800; color:var(--ink);">Học viên</h2>
                         <span style="background:#e0f2fe; color:#0369a1; padding:2px 10px; border-radius:999px; font-size:11px; font-weight:700;">PRO MEMBER</span>
                      </div>
                      <p id="profile-email" style="margin:3px 0 0; color:var(--muted); font-size:13.5px;">user@example.com</p>
                   </div>
                </div>

                <div style="display:flex; align-items:center; gap:16px; flex-wrap:wrap;">
                   <div class="target-gauge" style="min-width:220px; padding:12px 16px; border-radius:12px; background:#f0fdf4; border:1px solid #bbf7d0;">
                      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                         <span style="font-size:11px; color:#15803d; font-weight:800; letter-spacing:0.5px; text-transform:uppercase;">🎯 Mục tiêu hiện tại</span>
                         <span id="profile-countdown" style="font-size:11px; color:var(--muted); background:#fff; padding:2px 8px; border-radius:999px; border:1px solid #bbf7d0; font-weight:600;">Còn 45 ngày</span>
                      </div>
                      <strong id="profile-target-title" style="font-size:22px; font-family:var(--display); color:var(--green-dark); display:block;">TOEIC 750+</strong>
                   </div>

                   <!-- Accordion Cập nhật thông tin nhanh -->
                   <details style="font-size:12.5px;">
                      <summary style="cursor:pointer; color:var(--green); font-weight:700; user-select:none; display:flex; align-items:center; gap:6px; padding:10px 14px; border:1px solid var(--line); border-radius:10px; background:#fff;">
                         <span>✏️ Đổi tên & Ngày dự thi</span>
                      </summary>
                      <form id="profile-edit-form" style="position:absolute; right:36px; z-index:30; width:300px; display:flex; flex-direction:column; gap:10px; margin-top:8px; padding:16px; background:#fff; border:1px solid var(--line); border-radius:12px; box-shadow:0 12px 30px rgba(0,0,0,0.12);">
                         <div>
                            <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">TÊN HIỂN THỊ</label>
                            <input type="text" id="edit-profile-name" class="auth-input" style="padding:8px 12px; font-size:12.5px;" required>
                         </div>
                         <div>
                            <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">KỲ THI MỤC TIÊU</label>
                            <select id="edit-profile-exam" class="auth-input" style="padding:8px 12px; font-size:12.5px;">
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
                            <input type="date" id="edit-profile-date" class="auth-input" style="padding:8px 12px; font-size:12.5px;">
                         </div>
                         <button type="submit" class="auth-btn" style="padding:9px; margin-top:3px; background:var(--green-dark); color:#fff; font-size:12.5px;">Lưu thay đổi</button>
                      </form>
                   </details>
                </div>
             </div>
          </div>

          <!-- NỘI DUNG CHÍNH: KHẢO SÁT & LỘ TRÌNH ĐƯỢC ĐẶT CÙNG CỘT VỚI DÒNG CHẢY NỘI DUNG (GRID 2 CỘT CÂN ĐỐI) -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(360px, 1fr)); gap:22px; margin-bottom:24px; align-items:start;">
             <!-- Cột 1: Khảo sát mục tiêu cá nhân hóa & Gợi ý lộ trình AI -->
             <div class="profile-card">
                <div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">
                   <span style="font-size:22px;">🤖</span>
                   <div>
                      <h4 style="margin:0; font-size:15px; font-weight:800; color:var(--green-dark);">Khảo sát Lộ trình Tối ưu AI</h4>
                      <small style="color:var(--muted); font-size:11px;">Tùy biến kế hoạch học dựa trên thời gian & năng lực</small>
                   </div>
                </div>

                <form id="ai-study-plan-form" onsubmit="generateStudyRoadmap(event)" style="display:flex; flex-direction:column; gap:12px;">
                   <div>
                      <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">1. KỲ THI & BAND ĐIỂM MỤC TIÊU</label>
                      <select id="survey-target-score" class="auth-input" style="padding:9px 12px; font-size:13px;">
                         <option value="TOEIC 550+">TOEIC 550+ (Cơ bản / Đầu ra Đại học)</option>
                         <option value="TOEIC 750+" selected>TOEIC 750+ (Chuẩn Doanh nghiệp đa quốc gia)</option>
                         <option value="TOEIC 850+">TOEIC 850+ (Quản lý / Giao tiếp chuyên nghiệp)</option>
                         <option value="TOEIC 950+">TOEIC 950+ (Chuyên gia ngôn ngữ)</option>
                         <option value="IELTS 5.5">IELTS 5.5 (Cơ bản / Xét tuyển)</option>
                         <option value="IELTS 6.5">IELTS 6.5 (Chuẩn Du học / Thạc sĩ)</option>
                         <option value="IELTS 7.5">IELTS 7.5 (Học thuật nâng cao / Định cư)</option>
                         <option value="IELTS 8.0+">IELTS 8.0+ (Xuất sắc / Định cư chuyên gia)</option>
                      </select>
                   </div>

                   <div>
                      <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">2. TRÌNH ĐỘ HIỆN TẠI CỦA BẠN</label>
                      <select id="survey-current-level" class="auth-input" style="padding:9px 12px; font-size:13px;">
                         <option value="A2">Mất gốc / Cơ bản (A1 - A2: 300 TOEIC / 4.0 IELTS)</option>
                         <option value="B1" selected>Trung cấp (B1: 500 TOEIC / 5.0 IELTS)</option>
                         <option value="B2">Khá / Tự tin giao tiếp (B2: 650 TOEIC / 6.0 IELTS)</option>
                         <option value="C1">Nâng cao (C1: 800+ TOEIC / 7.0+ IELTS)</option>
                      </select>
                   </div>

                   <div>
                      <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">3. KỸ NĂNG CẦN CẢI THIỆN NHẤT</label>
                      <select id="survey-weak-skill" class="auth-input" style="padding:9px 12px; font-size:13px;">
                         <option value="Listening" selected>Listening (Nghe hiểu & Bắt key)</option>
                         <option value="Reading">Reading (Đọc hiểu & Ngữ pháp)</option>
                         <option value="Speaking">Speaking (Phát âm & Trôi chảy)</option>
                         <option value="Writing">Writing (Cấu trúc câu & Luận điểm bài luận)</option>
                      </select>
                   </div>

                   <div>
                      <label style="font-size:11px; font-weight:700; color:var(--muted); display:block; margin-bottom:4px;">4. THỜI GIAN HỌC MỖI NGÀY</label>
                      <select id="survey-daily-time" class="auth-input" style="padding:9px 12px; font-size:13px;">
                         <option value="30">30 phút / ngày (Duy trì nhẹ nhàng)</option>
                         <option value="45" selected>45 phút / ngày (Chuẩn khuyến nghị)</option>
                         <option value="60">60 phút / ngày (Cường độ cao)</option>
                         <option value="90">90+ phút / ngày (Cấp tốc bứt phá)</option>
                      </select>
                   </div>

                   <button type="submit" class="primary" style="margin-top:6px; padding:11px 18px; font-size:13px; font-weight:700; display:flex; align-items:center; justify-content:center; gap:8px; background:linear-gradient(135deg, #10b981 0%, #059669 100%); box-shadow:0 4px 12px rgba(16,185,129,0.25);">
                      <span>✨</span> AI Phân tích & Gợi ý lộ trình
                   </button>
                </form>
             </div>

             <!-- Cột 2: Khung lộ trình học tập do AI đề xuất -->
             <div class="profile-card" id="ai-roadmap-box" style="background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%); border: 1px solid #86efac; box-shadow: 0 4px 20px rgba(16,185,129,0.08);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
                   <div style="display:flex; align-items:center; gap:10px;">
                      <span style="font-size:24px; display:grid; width:38px; height:38px; place-items:center; background:#dcfce7; border-radius:10px;">🤖</span>
                      <div>
                         <h3 style="margin:0; font-size:16px; font-weight:800; color:var(--green-dark);">Lộ trình Cá nhân hóa do AI Thiết lập</h3>
                         <small style="color:var(--muted); font-size:11px;">Phân bổ mục tiêu theo thời gian thực</small>
                      </div>
                   </div>
                   <span class="skill-pill" id="roadmap-badge" style="background:var(--green-dark); color:#c9ef75; font-weight:800; padding:4px 12px; font-size:11.5px; border-radius:999px;">TOEIC 750+</span>
                </div>
                <p id="roadmap-summary" style="margin:0 0 16px; font-size:13.5px; color:#334155; line-height:1.65; background:#fff; padding:12px 16px; border-radius:10px; border:1px solid #dcfce7;">
                   Dựa trên trình độ hiện tại <strong>Trung cấp (B1)</strong>, mục tiêu <strong>TOEIC 750+</strong> với thời gian học <strong>45 phút/ngày</strong>, AI tính toán bạn cần khoảng <strong>8 tuần</strong> để đạt điểm số mong muốn. Trọng tâm đào sâu: <strong>Listening</strong>.
                </p>
                <div id="roadmap-phases" style="display:flex; flex-direction:column; gap:11px; margin-bottom:16px;"></div>
                <div style="display:flex; gap:10px; justify-content:flex-end; border-top:1px dashed #bbf7d0; padding-top:14px;">
                   <button type="button" class="primary" style="padding:10px 22px; font-size:13px; font-weight:700; background:linear-gradient(135deg, #10b981 0%, #059669 100%); box-shadow:0 4px 12px rgba(16,185,129,0.25);" onclick="showView('practice')">🎯 Bắt đầu luyện đề ngay ➜</button>
                </div>
             </div>
          </div>

          <!-- PHẦN DƯỚI: NĂNG LỰC 4 KỸ NĂNG, THÀNH TÍCH & QUẢN LÝ DỮ LIỆU CÙNG CỘT VỚI NỘI DUNG -->
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
        </section>

        '''

if p_start != -1 and p_end != -1:
    text = text[:p_start] + new_profile_content + text[p_end:]
    print("✓ Successfully replaced view-profile with full-width content column layout!")
else:
    print("✗ Failed to locate view-profile bounds")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("--- EXECUTED ALL REPLACEMENTS ---")
