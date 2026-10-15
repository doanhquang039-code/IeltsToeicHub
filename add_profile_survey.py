with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

target_str = '<div class="target-gauge">'
idx = content.find(target_str, 50000)
end_div = content.find('</div>\n\n                <div style="margin-top:20px;', idx)

survey_html = """

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

if idx != -1 and end_div != -1:
    content = content[:end_div+6] + survey_html + content[end_div+6:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Inserted survey form into profile view")
else:
    print(f"FAILED to find target: idx={idx}, end_div={end_div}")
