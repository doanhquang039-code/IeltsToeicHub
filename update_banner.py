import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's clean up the 4 quick action boxes in view-overview banner
# Notice lines 627-644:
# <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; min-width:240px;">
#   ... 4 boxes ...
# </div>

target_box_old = '''             <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; min-width:240px;">
                <div onclick="showView('practice')" style="background:rgba(255,255,255,0.08); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để đến Thư viện luyện đề 4 kỹ năng">
                   <strong style="display:block; font-size:20px; color:#c9ef75;">4 Kỹ năng</strong>
                   <small style="font-size:11px; color:#b8c8bf;">TOEIC & IELTS ➜</small>
                </div>
                <div onclick="showView('vocabulary')" style="background:rgba(255,255,255,0.08); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để xem Sổ tay từ vựng">
                   <strong style="display:block; font-size:20px; color:#c9ef75;">126+ Từ vựng</strong>
                   <small style="font-size:11px; color:#b8c8bf;">Chuẩn B1 - C2 ➜</small>
                </div>
                <div onclick="showView('analyzer')" style="background:rgba(255,255,255,0.08); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để mở AI Phân tích tài liệu">
                   <strong style="display:block; font-size:20px; color:#c9ef75;">🤖 AI Doc</strong>
                   <small style="font-size:11px; color:#b8c8bf;">PDF / Excel / Word ➜</small>
                </div>
                <div onclick="showView('progress')" style="background:rgba(255,255,255,0.08); padding:12px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để xem Tiến độ & Lịch sử điểm">
                   <strong style="display:block; font-size:20px; color:#c9ef75;">📈 Real-Time</strong>
                   <small style="font-size:11px; color:#b8c8bf;">Chấm điểm & Lịch sử ➜</small>
                </div>
             </div>'''

# Replace with clean, elegant status cards highlighting 4 official learning areas + Admin shortcut
target_box_new = '''             <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; min-width:260px;">
                <div onclick="showView('practice')" style="background:rgba(255,255,255,0.08); padding:12px 14px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để mở Luyện đề 4 kỹ năng">
                   <strong style="display:block; font-size:18px; color:#c9ef75;">▤ 4 Kỹ năng</strong>
                   <small style="font-size:11px; color:#b8c8bf;">ETS & Cambridge ➜</small>
                </div>
                <div onclick="showView('vocabulary')" style="background:rgba(255,255,255,0.08); padding:12px 14px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để mở Sổ tay từ vựng">
                   <strong style="display:block; font-size:18px; color:#c9ef75;">Aa Từ vựng</strong>
                   <small style="font-size:11px; color:#b8c8bf;">B1 - C2 Flashcard ➜</small>
                </div>
                <div onclick="showView('analyzer')" style="background:rgba(255,255,255,0.08); padding:12px 14px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để mở Trợ lý AI tài liệu">
                   <strong style="display:block; font-size:18px; color:#c9ef75;">🤖 AI Analyzer</strong>
                   <small style="font-size:11px; color:#b8c8bf;">PDF, Word, Excel ➜</small>
                </div>
                <div onclick="showView('admin')" style="background:rgba(253,224,71,0.15); padding:12px 14px; border-radius:10px; border:1px solid rgba(253,224,71,0.3); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(253,224,71,0.25)'" onmouseout="this.style.background='rgba(253,224,71,0.15)'" title="Bấm để vào Dashboard Quản trị viên">
                   <strong style="display:block; font-size:18px; color:#fde047;">⚡ Admin Hub</strong>
                   <small style="font-size:11px; color:#fef08a;">Upload & Quản lý đề ➜</small>
                </div>
             </div>'''

if target_box_old in html:
    html = html.replace(target_box_old, target_box_new)
    print("SUCCESS: Overview top banner cards updated cleanly")
else:
    print("Searching for grid banner via regex...")
    pattern = r'<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; min-width:240px;">.*?</div>\s*</div>'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        html = html[:match.start()] + target_box_new + html[match.end()-6:]
        print("SUCCESS: Banner cards updated via regex")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
