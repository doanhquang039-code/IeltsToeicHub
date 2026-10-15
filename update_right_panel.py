with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_right_panel = '''              <section class="panel" style="background:#fff; border:1px solid #d8e5db; border-radius:12px; padding:16px;">
                <h3 style="font-size:13px; font-weight:700; color:var(--green-dark); margin-bottom:12px; display:flex; align-items:center; justify-content:space-between;">
                   <span>⚡ Khám phá nhanh 4 Khu vực</span>
                </h3>
                <div style="display:flex; flex-direction:column; gap:8px;">
                   <button type="button" onclick="showView('progress')" style="display:flex; align-items:center; gap:10px; padding:9px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">↗</span>
                      <div style="flex:1;">
                        <div>Tiến độ & Lịch sử</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">Bảng điểm, biểu đồ & bài thi gần đây</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('bookmarks')" style="display:flex; align-items:center; gap:10px; padding:9px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">★</span>
                      <div style="flex:1;">
                        <div>Đã lưu & Báo cáo</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">Sổ tay câu hỏi khó & câu đã gửi báo cáo</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('profile')" style="display:flex; align-items:center; gap:10px; padding:9px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">👤</span>
                      <div style="flex:1;">
                        <div>Hồ sơ mục tiêu</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">Khảo sát band điểm & lộ trình AI</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('analyzer')" style="display:flex; align-items:center; gap:10px; padding:9px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">🤖</span>
                      <div style="flex:1;">
                        <div>AI Phân tích tài liệu</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">Kéo thả PDF, Word, Excel hoặc paste</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                </div>
              </section>'''

new_right_panel = '''              <section class="panel" style="background:#fff; border:1px solid #d8e5db; border-radius:12px; padding:18px;">
                <h3 style="font-size:13px; font-weight:700; color:var(--green-dark); margin-bottom:12px; display:flex; align-items:center; justify-content:space-between;">
                   <span>⚡ 4 Không gian Học tập</span>
                </h3>
                <div style="display:flex; flex-direction:column; gap:8px;">
                   <button type="button" onclick="showView('practice')" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">▤</span>
                      <div style="flex:1;">
                        <div>1. Luyện đề 4 kỹ năng</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">ETS TOEIC & Cambridge IELTS</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('vocabulary')" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">Aa</span>
                      <div style="flex:1;">
                        <div>2. Sổ tay từ vựng CEFR</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">B1 - C2, Flashcard & Custom Vocab</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('analyzer')" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">🤖</span>
                      <div style="flex:1;">
                        <div>3. AI Phân tích tài liệu</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">Kéo thả PDF, Word, Excel hoặc paste</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('profile')" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">👤</span>
                      <div style="flex:1;">
                        <div>4. Hồ sơ & Lộ trình AI</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">Mục tiêu cá nhân hóa & 4 kỹ năng</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('admin')" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid #fef08a; border-radius:8px; background:#fefce8; cursor:pointer; text-align:left; font-size:12px; font-weight:700; color:#854d0e; transition:all .15s; margin-top:4px;" onmouseover="this.style.background='#fef9c3';" onmouseout="this.style.background='#fefce8';">
                      <span style="font-size:15px;">⚡</span>
                      <div style="flex:1;">
                        <div>Admin Dashboard</div>
                        <small style="color:#a16207; font-size:10px; font-weight:400;">Upload & Quản lý đề thi</small>
                      </div>
                      <span style="color:#ca8a04; font-size:11px;">➜</span>
                   </button>
                </div>
              </section>'''

if old_right_panel in html:
    html = html.replace(old_right_panel, new_right_panel)
    print("SUCCESS: Overview right panel updated")
else:
    print("Warning: right panel exact string not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
