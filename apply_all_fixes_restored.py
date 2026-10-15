import sys
import io

# sys.stdout reconfigure
pass

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Sidebar Nav HTML
old_nav = '''      <nav class="nav" aria-label="Điều hướng chính">
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

new_nav = '''      <nav class="nav" aria-label="Điều hướng chính">
        <p class="nav-label">TRANG CHỦ DỰ ÁN</p>
        <button class="active" data-view="overview" onclick="showView('overview')" title="Trang chủ Lingua English Hub">
          <span class="nav-glyph">🏠</span>Trang chủ Dự án
        </button>

        <p class="nav-label" style="margin-top:12px;">KHÔNG GIAN HỌC TẬP</p>
        <button data-view="practice" onclick="showView('practice')">
          <span class="nav-glyph">▤</span>1. Luyện đề 4 kỹ năng
        </button>
        <button data-view="analyzer" onclick="showView('analyzer')">
          <span class="nav-glyph">🤖</span>2. AI Phân tích tài liệu
        </button>
        <button data-view="profile" onclick="showView('profile')">
          <span class="nav-glyph">👤</span>3. Hồ sơ & Lộ trình AI
        </button>
        <button data-view="vocabulary" onclick="showView('vocabulary')">
          <span class="nav-glyph">📖</span>4. Sổ tay từ vựng (Phân trang)
        </button>

        <p class="nav-label" style="margin-top:12px;">KHÔNG GIAN QUẢN TRỊ</p>
        <button data-view="admin" id="nav-btn-admin" onclick="showView('admin')" style="color:#fde047;">
          <span class="nav-glyph" style="background:rgba(253,224,71,0.18); color:#fde047;">⚡</span>Admin Dashboard
        </button>
      </nav>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print("✓ Updated sidebar navigation successfully")
else:
    print("✗ Warning: old_nav not found exactly")

# 2. Update Overview top hero cards - replace Aa Từ vựng with Hồ sơ & Lộ trình AI
old_hero_grid = '''             <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; min-width:260px;">
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

new_hero_grid = '''             <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; min-width:260px;">
                <div onclick="showView('practice')" style="background:rgba(255,255,255,0.08); padding:12px 14px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để mở Luyện đề 4 kỹ năng">
                   <strong style="display:block; font-size:18px; color:#c9ef75;">▤ 4 Kỹ năng</strong>
                   <small style="font-size:11px; color:#b8c8bf;">ETS & Cambridge ➜</small>
                </div>
                <div onclick="showView('profile')" style="background:rgba(255,255,255,0.08); padding:12px 14px; border-radius:10px; border:1px solid rgba(255,255,255,0.12); text-align:center; cursor:pointer; transition:all .2s;" onmouseover="this.style.background='rgba(255,255,255,0.18)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'" title="Bấm để xem Hồ sơ & Lộ trình AI">
                   <strong style="display:block; font-size:18px; color:#c9ef75;">👤 Hồ sơ AI</strong>
                   <small style="font-size:11px; color:#b8c8bf;">Mục tiêu cá nhân ➜</small>
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

if old_hero_grid in content:
    content = content.replace(old_hero_grid, new_hero_grid)
    print("✓ Updated hero cards without vocabulary clutter")
else:
    print("✗ Warning: old_hero_grid not found")

# 3. Update Overview right-column panel
old_right_col = '''              <section class="panel" style="background:#fff; border:1px solid #d8e5db; border-radius:12px; padding:18px;">
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

new_right_col = '''              <section class="panel" style="background:#fff; border:1px solid #d8e5db; border-radius:12px; padding:18px;">
                <h3 style="font-size:13px; font-weight:700; color:var(--green-dark); margin-bottom:12px; display:flex; align-items:center; justify-content:space-between;">
                   <span>⚡ Không gian Học tập & Quản trị</span>
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
                   <button type="button" onclick="showView('analyzer')" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">🤖</span>
                      <div style="flex:1;">
                        <div>2. AI Phân tích tài liệu</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">Kéo thả PDF, Word, Excel hoặc paste</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('profile')" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">👤</span>
                      <div style="flex:1;">
                        <div>3. Hồ sơ & Lộ trình AI</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">Mục tiêu cá nhân hóa & 4 kỹ năng</small>
                      </div>
                      <span style="color:var(--green); font-size:11px;">➜</span>
                   </button>
                   <button type="button" onclick="showView('vocabulary')" style="display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid var(--line); border-radius:8px; background:#fbfdfa; cursor:pointer; text-align:left; font-size:12px; font-weight:600; color:var(--green-dark); transition:all .15s;" onmouseover="this.style.background='#eaf3e8'; this.style.borderColor='var(--green)';" onmouseout="this.style.background='#fbfdfa'; this.style.borderColor='var(--line)';">
                      <span style="font-size:15px;">📖</span>
                      <div style="flex:1;">
                        <div>4. Sổ tay từ vựng (Phân trang)</div>
                        <small style="color:var(--muted); font-size:10px; font-weight:400;">B1 - C2, Flashcard & Phân trang 8 từ</small>
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

if old_right_col in content:
    content = content.replace(old_right_col, new_right_col)
    print("✓ Updated right-column panel")
else:
    print("✗ Warning: old_right_col not found")

# 4. Update vocab pagination markup in view-vocabulary
old_vocab_list_wrap = '''            <div>
              <div class="section-head">
                 <h2>Danh sách từ (<span id="filtered-vocab-count">0</span>)</h2>
                 <span style="font-size:12px; color:var(--muted);">Bấm 🔊 để nghe giọng đọc bản ngữ</span>
              </div>
              <div class="vocab-list" id="vocab-list" style="max-height: 480px; overflow-y: auto; padding-right:6px;"></div>
            </div>'''

new_vocab_list_wrap = '''            <div>
              <div class="section-head" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                 <div>
                   <h2 style="margin:0;">Danh sách từ vựng (<span id="filtered-vocab-count">0</span>)</h2>
                   <span style="font-size:12px; color:var(--muted);">Bấm 🔊 nghe phát âm · Phân trang chuẩn 8 từ/trang</span>
                 </div>
                 <div id="vocab-page-badge" style="font-size:11.5px; font-weight:700; background:#f0fdf4; color:var(--green-dark); padding:4px 10px; border-radius:6px; border:1px solid #bbf7d0;">Trang 1</div>
              </div>
              <div class="vocab-list" id="vocab-list" style="min-height: 360px; padding-right:4px;"></div>
              
              <!-- THANH PHÂN TRANG TỪ VỰNG CHUẨN MỰC -->
              <div class="vocab-pagination-bar" id="vocab-pagination-bar" style="display:flex; justify-content:space-between; align-items:center; margin-top:14px; padding-top:12px; border-top:1px solid var(--line); flex-wrap:wrap; gap:10px;">
                 <span id="vocab-page-info" style="font-size:12px; color:var(--muted); font-weight:600;">Hiển thị 1 - 8 trong 126 từ</span>
                 <div id="vocab-pagination-btns" style="display:flex; gap:5px; align-items:center; flex-wrap:wrap;"></div>
              </div>
            </div>'''

if old_vocab_list_wrap in content:
    content = content.replace(old_vocab_list_wrap, new_vocab_list_wrap)
    print("✓ Updated vocab-list pagination markup")
else:
    print("✗ Warning: old_vocab_list_wrap not found")

# 5. Update renderVocabList and add pagination JavaScript
old_render_vocab = '''    function renderVocabList() {
        const listEl = $('#vocab-list');
        const countEl = $('#filtered-vocab-count');
        if (countEl) countEl.textContent = currentFilteredVocab.length;
        if (!listEl) return;

        if (currentFilteredVocab.length === 0) {
            listEl.innerHTML = '<div class="empty-state" style="padding:20px; font-size:13px;">Chưa tìm thấy từ vựng nào khớp bộ lọc. Bạn hãy thử chọn chủ đề khác nhé.</div>';
            return;
        }

        listEl.innerHTML = currentFilteredVocab.map((item, idx) => `
            <div class="vocab-item" style="display:flex; justify-content:space-between; align-items:center; padding:10px 12px; margin-bottom:8px; background:#fff; border:1px solid var(--line); border-radius:8px; cursor:pointer;" onclick="selectVocabItem(${idx})">
               <div>
                  <div style="display:flex; align-items:center; gap:8px;">
                     <strong style="font-size:14.5px; color:var(--ink);">${item.word}</strong>
                     <span class="level-badge ${item.level.toLowerCase()}">${item.level}</span>
                     <span style="font-size:11.5px; color:var(--muted);">${item.phonetic}</span>
                     <button class="speak-btn" onclick="event.stopPropagation(); speakWord('${item.word}')">🔊</button>
                  </div>
                  <div style="font-size:12.5px; color:#334155; margin-top:2px;">${item.meaning}</div>
                  <div style="font-size:11.5px; color:var(--muted); font-style:italic;">"${item.example}"</div>
               </div>
               <span class="topic-pill" style="font-size:10.5px;">${item.topicLabel}</span>
            </div>
        `).join('');
    }

    function selectVocabItem(idx) {
        currentVocabIndex = idx;
        flashRevealed = true;
        renderFlashcard();
        window.scrollTo({ top: $('#flashcard').offsetTop - 80, behavior: 'smooth' });
    }'''

new_render_vocab = '''    let vocabCurrentPage = 1;
    const VOCAB_PAGE_SIZE = 8;

    function renderVocabList() {
        const listEl = $('#vocab-list');
        const countEl = $('#filtered-vocab-count');
        const pageInfo = $('#vocab-page-info');
        const pageBtns = $('#vocab-pagination-btns');
        const pageBadge = $('#vocab-page-badge');

        const totalItems = currentFilteredVocab.length;
        if (countEl) countEl.textContent = totalItems;
        if (!listEl) return;

        if (totalItems === 0) {
            listEl.innerHTML = '<div class="empty-state" style="padding:28px 16px; font-size:13.5px; text-align:center; color:var(--muted); background:#fff; border-radius:10px; border:1px dashed var(--line);">Chưa tìm thấy từ vựng nào khớp bộ lọc. Bạn hãy thử chọn chủ đề hoặc cấp độ khác nhé.</div>';
            if (pageInfo) pageInfo.textContent = '0 từ vựng';
            if (pageBtns) pageBtns.innerHTML = '';
            if (pageBadge) pageBadge.textContent = 'Trang 0';
            return;
        }

        const totalPages = Math.ceil(totalItems / VOCAB_PAGE_SIZE) || 1;
        if (vocabCurrentPage > totalPages) vocabCurrentPage = totalPages;
        if (vocabCurrentPage < 1) vocabCurrentPage = 1;

        if (pageBadge) pageBadge.textContent = `Trang ${vocabCurrentPage} / ${totalPages}`;

        const startIdx = (vocabCurrentPage - 1) * VOCAB_PAGE_SIZE;
        const endIdx = Math.min(startIdx + VOCAB_PAGE_SIZE, totalItems);
        const pagedItems = currentFilteredVocab.slice(startIdx, endIdx);

        if (pageInfo) {
            pageInfo.textContent = `Hiển thị ${startIdx + 1} - ${endIdx} trong số ${totalItems} từ (Trang ${vocabCurrentPage}/${totalPages})`;
        }

        listEl.innerHTML = pagedItems.map((item, localIdx) => {
            const globalIdx = startIdx + localIdx;
            const isSelected = globalIdx === currentVocabIndex;
            return `
            <div class="vocab-item" style="display:flex; justify-content:space-between; align-items:center; padding:11px 14px; margin-bottom:8px; background:${isSelected ? '#f0fdf4' : '#fff'}; border:1px solid ${isSelected ? '#86efac' : 'var(--line)'}; border-radius:10px; cursor:pointer; transition:all .18s; box-shadow:0 1px 3px rgba(0,0,0,0.02);" onmouseover="this.style.borderColor='var(--green)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.05)';" onmouseout="this.style.borderColor='${isSelected ? '#86efac' : 'var(--line)'}'; this.style.boxShadow='0 1px 3px rgba(0,0,0,0.02)';" onclick="selectVocabItem(${globalIdx})">
               <div style="flex:1; min-width:0; padding-right:12px;">
                  <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                     <strong style="font-size:15px; color:${isSelected ? 'var(--green-dark)' : 'var(--ink)'};">${item.word}</strong>
                     <span class="level-badge ${item.level.toLowerCase()}" style="font-size:10.5px; padding:2px 7px; border-radius:5px; font-weight:700;">${item.level}</span>
                     <span style="font-size:12px; color:var(--muted);">${item.phonetic}</span>
                     <button class="speak-btn" style="border:none; background:none; cursor:pointer; font-size:13px;" onclick="event.stopPropagation(); speakWord('${item.word}')" title="Nghe phát âm">🔊</button>
                  </div>
                  <div style="font-size:13px; color:#1e293b; margin-top:3px; font-weight:500;">${item.meaning}</div>
                  <div style="font-size:11.5px; color:var(--muted); font-style:italic; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">"${item.example}"</div>
               </div>
               <span class="topic-pill" style="font-size:11px; padding:3px 9px; border-radius:999px; background:#f1f5f9; color:#475569; font-weight:600; white-space:nowrap;">${item.topicLabel}</span>
            </div>`;
        }).join('');

        // Thanh phân trang với nút Trước/Sau và số trang
        if (pageBtns) {
            let html = '';
            // Nút Trang trước
            const prevDisabled = vocabCurrentPage <= 1;
            html += `<button type="button" onclick="goToVocabPage(${vocabCurrentPage - 1})" ${prevDisabled ? 'disabled' : ''} style="padding:6px 12px; font-size:12px; border:1px solid var(--line); border-radius:6px; background:${prevDisabled ? '#f8fafc' : '#fff'}; color:${prevDisabled ? '#cbd5e1' : 'var(--ink)'}; cursor:${prevDisabled ? 'not-allowed' : 'pointer'}; font-weight:600;">‹ Trước</button>`;

            // Danh sách số trang
            const maxVisible = 5;
            let startP = Math.max(1, vocabCurrentPage - 2);
            let endP = Math.min(totalPages, startP + maxVisible - 1);
            if (endP - startP < maxVisible - 1) {
                startP = Math.max(1, endP - maxVisible + 1);
            }

            if (startP > 1) {
                html += `<button type="button" onclick="goToVocabPage(1)" style="padding:6px 10px; font-size:12px; border:1px solid var(--line); border-radius:6px; background:#fff; cursor:pointer; font-weight:600;">1</button>`;
                if (startP > 2) html += `<span style="font-size:11px; color:var(--muted); padding:0 2px;">...</span>`;
            }

            for (let p = startP; p <= endP; p++) {
                const isActive = p === vocabCurrentPage;
                html += `<button type="button" onclick="goToVocabPage(${p})" style="padding:6px 11px; font-size:12px; border:1px solid ${isActive ? 'var(--green-dark)' : 'var(--line)'}; border-radius:6px; background:${isActive ? 'var(--green-dark)' : '#fff'}; color:${isActive ? '#fff' : 'var(--ink)'}; font-weight:${isActive ? '700' : '500'}; cursor:pointer; transition:all .15s;">${p}</button>`;
            }

            if (endP < totalPages) {
                if (endP < totalPages - 1) html += `<span style="font-size:11px; color:var(--muted); padding:0 2px;">...</span>`;
                html += `<button type="button" onclick="goToVocabPage(${totalPages})" style="padding:6px 10px; font-size:12px; border:1px solid var(--line); border-radius:6px; background:#fff; cursor:pointer; font-weight:600;">${totalPages}</button>`;
            }

            // Nút Trang sau
            const nextDisabled = vocabCurrentPage >= totalPages;
            html += `<button type="button" onclick="goToVocabPage(${vocabCurrentPage + 1})" ${nextDisabled ? 'disabled' : ''} style="padding:6px 12px; font-size:12px; border:1px solid var(--line); border-radius:6px; background:${nextDisabled ? '#f8fafc' : '#fff'}; color:${nextDisabled ? '#cbd5e1' : 'var(--ink)'}; cursor:${nextDisabled ? 'not-allowed' : 'pointer'}; font-weight:600;">Tiếp ›</button>`;

            pageBtns.innerHTML = html;
        }
    }

    function goToVocabPage(p) {
        const totalPages = Math.ceil(currentFilteredVocab.length / VOCAB_PAGE_SIZE) || 1;
        if (p < 1 || p > totalPages) return;
        vocabCurrentPage = p;
        renderVocabList();
        const flashEl = $('#flashcard');
        if (flashEl) {
            flashEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    }

    function selectVocabItem(idx) {
        currentVocabIndex = idx;
        flashRevealed = true;
        renderFlashcard();
        renderVocabList();
        const flashcardEl = $('#flashcard');
        if (flashcardEl) {
            flashcardEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }'''

if old_render_vocab in content:
    content = content.replace(old_render_vocab, new_render_vocab)
    print("✓ Replaced renderVocabList with full pagination logic")
else:
    print("✗ Warning: old_render_vocab not found")

# 6. Reset vocabCurrentPage to 1 in applyVocabFilters
old_apply_filters = '''        currentVocabIndex = 0;
        flashRevealed = false;
        wordRevealed = false;
        renderFlashcard();
        renderVocabList();'''

new_apply_filters = '''        currentVocabIndex = 0;
        vocabCurrentPage = 1;
        flashRevealed = false;
        wordRevealed = false;
        renderFlashcard();
        renderVocabList();'''

if old_apply_filters in content:
    content = content.replace(old_apply_filters, new_apply_filters)
    print("✓ Added vocabCurrentPage = 1 reset on filter change")
else:
    print("✗ Warning: old_apply_filters not found")

# 7. Remove duplicate event listener on .nav button
old_dup_listener = "$$('.nav button').forEach(button => button.addEventListener('click', () => showView(button.dataset.view)));"
new_dup_listener = "// Navigation click is handled directly via onclick='showView(...)' to prevent double-execution."

if old_dup_listener in content:
    content = content.replace(old_dup_listener, new_dup_listener)
    print("✓ Removed duplicate .nav button addEventListener")
else:
    print("✗ Warning: old_dup_listener not found")

# 8. Update breadcrumbs in showView
old_crumbs = '''      const breadcrumbNames = {
          overview: 'Trang chủ Dự án Lingua Hub',
          practice: '1. Luyện đề 4 kỹ năng (ETS & Cambridge)',
          vocabulary: '2. Sổ tay từ vựng CEFR B1 - C2',
          analyzer: '3. AI Phân tích tài liệu (PDF, Word, Excel)',
          profile: '4. Hồ sơ & Lộ trình AI cá nhân hóa',
          progress: 'Tiến độ & Lịch sử điểm số',
          bookmarks: 'Đã lưu & Báo cáo câu hỏi',
          admin: '⚡ Admin Dashboard - Quản trị & Upload Đề thi'
      };'''

new_crumbs = '''      const breadcrumbNames = {
          overview: 'Trang chủ Dự án Lingua Hub',
          practice: '1. Luyện đề 4 kỹ năng (ETS & Cambridge)',
          analyzer: '2. AI Phân tích tài liệu (PDF, Word, Excel)',
          profile: '3. Hồ sơ & Lộ trình AI cá nhân hóa',
          vocabulary: '4. Sổ tay từ vựng CEFR (Có phân trang)',
          progress: 'Tiến độ & Lịch sử điểm số',
          bookmarks: 'Đã lưu & Báo cáo câu hỏi',
          admin: '⚡ Admin Dashboard - Quản trị & Upload Đề thi'
      };'''

if old_crumbs in content:
    content = content.replace(old_crumbs, new_crumbs)
    print("✓ Updated breadcrumb names")
else:
    print("✗ Warning: old_crumbs not found")

# 9. Clean up AI Roadmap text in generateStudyRoadmap
old_roadmap_text = "${phase1Focus}. Học mỗi ngày ${dailyTime} phút trong Sổ tay từ vựng & AI Doc."
new_roadmap_text = "${phase1Focus}. Luyện tập đều đặn mỗi ngày ${dailyTime} phút theo kế hoạch trọng tâm."

if old_roadmap_text in content:
    content = content.replace(old_roadmap_text, new_roadmap_text)
    print("✓ Updated AI roadmap text")
else:
    print("✗ Warning: old_roadmap_text not found")

# 10. Improve sidebar CSS to prevent awkward detachment/scrolling
old_sidebar_css = ".sidebar { width: 256px; min-width: 256px; max-width: 256px; height: 100vh; position: sticky; top: 0; z-index: 50; display: flex; flex-direction: column; padding: 22px 14px 18px; background: #0c1f18; color: #eaf1e9; border-right: 1px solid rgba(255,255,255,0.06); box-shadow: 4px 0 24px rgba(0,0,0,0.05); overflow-y: auto; box-sizing: border-box; }"
new_sidebar_css = ".sidebar { width: 256px; min-width: 256px; max-width: 256px; height: 100vh; position: sticky; top: 0; z-index: 50; display: flex; flex-direction: column; padding: 18px 14px 14px; background: #0c1f18; color: #eaf1e9; border-right: 1px solid rgba(255,255,255,0.06); box-shadow: 4px 0 24px rgba(0,0,0,0.05); overflow-y: auto; overflow-x: hidden; box-sizing: border-box; flex-shrink: 0; scrollbar-width: thin; }"

if old_sidebar_css in content:
    content = content.replace(old_sidebar_css, new_sidebar_css)
    print("✓ Updated sidebar CSS for solid positioning")
else:
    print("✗ Warning: old_sidebar_css not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("--- ALL MODIFICATIONS COMPLETED SUCCESSFULLY ---")
