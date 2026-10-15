# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

html_path = r"e:\EngLish-IE-Toeic\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------------
# 1. THÊM CDN LIBRARIES TRONG <head>: PDF.js & Mammoth.js
# -------------------------------------------------------------------
cdn_libs = """  <!-- PDF.js & Mammoth.js for client-side Document Parsing (PDF & Word) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js"></script>
  <script>
    if (window.pdfjsLib) {
      window.pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    }
  </script>
"""
if "pdf.min.js" not in html:
    html = html.replace("</head>", cdn_libs + "\n</head>")
    print("Injected PDF.js and Mammoth.js CDN libraries.")

# -------------------------------------------------------------------
# 2. THÊM CSS MỚI CHO VOCAB HUB, ANALYZER, SCORING SCALE
# -------------------------------------------------------------------
advanced_css = """
    /* --- ADVANCED SUITE: VOCABULARY, ANALYZER, SCORING --- */
    /* Badges & Tags */
    .test-badge { display: inline-flex; align-items: center; gap: 4px; padding: 2px 7px; border-radius: 4px; font-size: 10px; font-weight: 700; text-transform: uppercase; }
    .test-badge.actual { background: #fee2e2; color: #b91c1c; border: 1px solid #fca5a5; }
    .test-badge.cambridge { background: #ede9fe; color: #6d28d9; border: 1px solid #ddd6fe; }
    .test-badge.ets { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
    .test-badge.mock { background: #fef9c3; color: #854d0e; border: 1px solid #fef08a; }

    /* Level Pills B1 - C2 */
    .level-badge { display: inline-flex; align-items: center; justify-content: center; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 800; }
    .level-badge.b1 { background: #e0f2fe; color: #0284c7; }
    .level-badge.b2 { background: #dcfce7; color: #16a34a; }
    .level-badge.c1 { background: #fef3c7; color: #d97706; }
    .level-badge.c2 { background: #f3e8ff; color: #9333ea; }

    /* Topic Pills */
    .topic-pill { display: inline-flex; align-items: center; gap: 4px; padding: 3px 8px; border-radius: 999px; font-size: 11px; background: #f1f5f9; color: #475569; }

    /* Vocab Hub Controls */
    .vocab-hub-header { display: flex; flex-direction: column; gap: 14px; margin-bottom: 22px; }
    .filter-pills-row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
    .filter-pill-btn { background: #fff; border: 1px solid var(--line); padding: 6px 13px; border-radius: 999px; font-size: 12.5px; font-weight: 600; color: var(--muted); cursor: pointer; transition: all .15s; display: inline-flex; align-items: center; gap: 6px; }
    .filter-pill-btn:hover { border-color: var(--green); color: var(--green-dark); background: #f8fafc; }
    .filter-pill-btn.active { background: var(--green-dark); color: #fff; border-color: var(--green-dark); }
    .speak-btn { background: transparent; border: none; font-size: 14px; cursor: pointer; opacity: 0.7; transition: opacity .15s, transform .15s; padding: 2px 4px; border-radius: 4px; }
    .speak-btn:hover { opacity: 1; transform: scale(1.15); background: #f1f5f9; }

    /* Vocab Quiz Box */
    .vocab-quiz-box { background: #fdfbf7; border: 1px solid #fed7aa; border-radius: 12px; padding: 18px 22px; margin-top: 20px; }
    .vocab-quiz-q { font-size: 15px; font-weight: 700; color: var(--ink); margin-bottom: 12px; }
    .vocab-quiz-opts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
    @media (max-width: 600px) { .vocab-quiz-opts { grid-template-columns: 1fr; } }
    .vocab-opt-btn { background: #fff; border: 1px solid var(--line); border-radius: 8px; padding: 10px 14px; text-align: left; font-size: 13px; cursor: pointer; transition: all .15s; }
    .vocab-opt-btn:hover { border-color: var(--green); background: #f8fafc; }
    .vocab-opt-btn.correct { background: #dcfce7 !important; border-color: #22c55e !important; color: #15803d !important; font-weight: 700; }
    .vocab-opt-btn.wrong { background: #fee2e2 !important; border-color: #ef4444 !important; color: #b91c1c !important; text-decoration: line-through; }

    /* AI Document Analyzer Layout */
    .analyzer-dropzone { border: 2px dashed #94a3b8; border-radius: 16px; background: #f8fafc; padding: 35px 20px; text-align: center; cursor: pointer; transition: all .2s; }
    .analyzer-dropzone:hover, .analyzer-dropzone.dragover { border-color: var(--green); background: #f0fdf4; }
    .dropzone-icon { font-size: 44px; margin-bottom: 10px; color: var(--green); }
    .sample-doc-chips { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-top: 15px; }
    .sample-doc-btn { background: #fff; border: 1px solid var(--line); padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer; color: var(--muted); transition: all .15s; display: inline-flex; align-items: center; gap: 5px; }
    .sample-doc-btn:hover { border-color: var(--green); color: var(--green-dark); background: #f0fdf4; }

    .analysis-results-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; margin-top: 22px; }
    .analysis-card { background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); }
    .analysis-card-title { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: .5px; color: var(--muted); margin-bottom: 12px; display: flex; align-items: center; gap: 6px; }

    /* Scoring Modal Table */
    .scoring-table { width: 100%; border-collapse: collapse; font-size: 13px; text-align: left; }
    .scoring-table th, .scoring-table td { padding: 9px 12px; border-bottom: 1px solid var(--line); }
    .scoring-table th { background: #f8fafc; font-weight: 700; color: var(--muted); font-size: 11px; text-transform: uppercase; }
    .scoring-table tr:hover { background: #fcfcfc; }
"""

if ".test-badge" not in html:
    html = html.replace("</style>", advanced_css + "\n  </style>")
    print("Injected advanced suite CSS styles.")

# -------------------------------------------------------------------
# 3. CẬP NHẬT SIDEBAR NAV: THÊM NÚT "AI PHÂN TÍCH TÀI LIỆU"
# -------------------------------------------------------------------
old_nav_code = """        <button data-view="bookmarks"><span class="nav-glyph">★</span>Đã lưu & Báo cáo</button>
        <button data-view="profile"><span class="nav-glyph">👤</span>Hồ sơ mục tiêu</button>"""

new_nav_code = """        <button data-view="bookmarks"><span class="nav-glyph">★</span>Đã lưu & Báo cáo</button>
        <button data-view="profile"><span class="nav-glyph">👤</span>Hồ sơ mục tiêu</button>
        <button data-view="analyzer"><span class="nav-glyph">🤖</span>AI Phân tích tài liệu</button>"""

if 'data-view="analyzer"' not in html:
    html = html.replace(old_nav_code, new_nav_code)
    print("Added 'AI Phân tích tài liệu' to sidebar navigation.")

# -------------------------------------------------------------------
# 4. NÂNG CẤP VIEW: #view-practice (THÊM BỘ LỌC ĐỀ THI THẬT & NÚT KHUNG ĐIỂM)
# -------------------------------------------------------------------
old_practice_header = """        <section class="view" id="view-practice">
          <div class="page-title-row"><div><p class="eyebrow">Thư viện bài tập</p><h1>Luyện đề theo mục tiêu</h1><p>Chọn kỹ năng muốn cải thiện và bắt đầu ngay.</p></div><label class="search"><span>⌕</span><input id="course-search" type="search" placeholder="Tìm bài luyện tập..." aria-label="Tìm bài luyện tập"></label></div>
          <div class="filters" role="group" aria-label="Lọc đề thi"><button class="filter active" data-practice-filter="Tất cả">Tất cả</button><button class="filter" data-practice-filter="TOEIC">TOEIC</button><button class="filter" data-practice-filter="IELTS">IELTS</button></div>
          <div class="all-courses" id="all-courses"></div>
        </section>"""

new_practice_header = """        <section class="view" id="view-practice">
          <div class="page-title-row">
            <div>
              <p class="eyebrow">Thư viện bài tập 4 kỹ năng</p>
              <h1>Đề thi TOEIC & IELTS chuẩn khảo thí</h1>
              <p>Bao gồm đề thi thật ETS, đề thi Cambridge IELTS chính thức và các đề luyện chuyên sâu.</p>
            </div>
            <div style="display:flex; gap:10px; align-items:center;">
              <button class="text-button" style="border:1px solid var(--green); color:var(--green-dark); padding:8px 14px; border-radius:8px; font-weight:600; font-size:12.5px; display:inline-flex; align-items:center; gap:6px;" onclick="openScoringModal()">
                <span>📊</span> Khung quy đổi điểm chuẩn
              </button>
              <label class="search"><span>⌕</span><input id="course-search" type="search" placeholder="Tìm đề thi..." aria-label="Tìm bài luyện tập"></label>
            </div>
          </div>

          <!-- Bộ lọc đa tầng: Kỳ thi & Phân loại đề -->
          <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:18px;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
               <div class="filters" role="group" aria-label="Lọc kỳ thi">
                  <button class="filter active" data-practice-filter="Tất cả">Tất cả kỳ thi</button>
                  <button class="filter" data-practice-filter="TOEIC">TOEIC</button>
                  <button class="filter" data-practice-filter="IELTS">IELTS</button>
               </div>

               <div class="filters" role="group" aria-label="Lọc kỹ năng" id="skill-filter-group">
                  <button class="filter active" data-skill-filter="Tất cả">Mọi kỹ năng</button>
                  <button class="filter" data-skill-filter="Listening">🎧 Listening</button>
                  <button class="filter" data-skill-filter="Reading">📖 Reading</button>
                  <button class="filter" data-skill-filter="Writing">✍️ Writing</button>
                  <button class="filter" data-skill-filter="Speaking">🎙️ Speaking</button>
               </div>
            </div>

            <div class="filter-pills-row">
               <span style="font-size:11.5px; font-weight:700; color:var(--muted); text-transform:uppercase; margin-right:4px;">Nguồn đề:</span>
               <button class="filter-pill-btn active" data-source-filter="all" onclick="setSourceFilter('all')">Tất cả nguồn</button>
               <button class="filter-pill-btn" data-source-filter="actual" onclick="setSourceFilter('actual')">🔥 Đề thi thật (Actual Test)</button>
               <button class="filter-pill-btn" data-source-filter="cambridge" onclick="setSourceFilter('cambridge')">🏛️ Cambridge Official</button>
               <button class="filter-pill-btn" data-source-filter="ets" onclick="setSourceFilter('ets')">🏢 ETS Official</button>
            </div>
          </div>

          <div class="all-courses" id="all-courses"></div>
        </section>"""

if "Khung quy đổi điểm chuẩn" not in html:
    html = html.replace(old_practice_header, new_practice_header)
    print("Upgraded #view-practice with multi-dimensional filters and scoring scale button.")

# -------------------------------------------------------------------
# 5. NÂNG CẤP VIEW: #view-vocabulary (THÊM BỘ LỌC CHỦ ĐỀ & CẤP ĐỘ B1-C2 & QUIZ)
# -------------------------------------------------------------------
old_vocab_view = """        <section class="view" id="view-vocabulary">
          <div class="page-title-row"><div><p class="eyebrow">Học chắc, nhớ lâu</p><h1>Sổ tay từ vựng</h1><p>Ôn các từ thường gặp trong bài thi TOEIC và IELTS.</p></div><div class="date-pill">Bộ từ vựng học thuật</div></div>
          <div class="vocab-layout"><button class="flashcard" id="flashcard" aria-label="Lật thẻ từ vựng"><div class="flashcard-inner"><small id="flashcard-label">Từ 1 trong 8 · Nhấn để lật thẻ</small><h2 id="flashcard-word">allocate</h2><p id="flashcard-detail">/ˈæləkeɪt/ · động từ</p><p class="reveal-hint" id="flashcard-hint">Chạm để xem nghĩa và ví dụ</p></div></button><div><div class="section-head"><h2>Danh sách từ</h2></div><div class="vocab-list" id="vocab-list"></div></div></div>
        </section>"""

new_vocab_view = """        <section class="view" id="view-vocabulary">
          <div class="page-title-row">
            <div>
              <p class="eyebrow">Trau dồi vốn từ chuyên sâu</p>
              <h1>Sổ tay từ vựng theo chủ đề & Khung CEFR</h1>
              <p>Lựa chọn chủ đề cuộc sống hoặc lọc theo chuẩn năng lực B1, B2, C1, C2 để học có trọng tâm.</p>
            </div>
            <div style="display:flex; gap:8px;">
               <button class="primary" style="padding:8px 14px; font-size:13px;" onclick="startVocabQuickQuiz()">⚡ Kiểm tra nhanh từ vựng</button>
            </div>
          </div>

          <!-- Bộ lọc Cấp độ & Chủ đề -->
          <div class="vocab-hub-header">
            <!-- Hàng 1: Cấp độ CEFR -->
            <div class="filter-pills-row">
               <span style="font-size:11.5px; font-weight:700; color:var(--muted); text-transform:uppercase; margin-right:4px;">Cấp độ CEFR:</span>
               <button class="filter-pill-btn active" data-vlevel="all" onclick="filterVocabByLevel('all')">Tất cả</button>
               <button class="filter-pill-btn" data-vlevel="B1" onclick="filterVocabByLevel('B1')"><span class="level-badge b1">B1</span> Trung cấp</button>
               <button class="filter-pill-btn" data-vlevel="B2" onclick="filterVocabByLevel('B2')"><span class="level-badge b2">B2</span> Trung cao cấp</button>
               <button class="filter-pill-btn" data-vlevel="C1" onclick="filterVocabByLevel('C1')"><span class="level-badge c1">C1</span> Cao cấp</button>
               <button class="filter-pill-btn" data-vlevel="C2" onclick="filterVocabByLevel('C2')"><span class="level-badge c2">C2</span> Tinh hoa (Mastery)</button>
            </div>

            <!-- Hàng 2: Chủ đề cuộc sống & công sở -->
            <div class="filter-pills-row">
               <span style="font-size:11.5px; font-weight:700; color:var(--muted); text-transform:uppercase; margin-right:4px;">Chủ đề đời sống:</span>
               <button class="filter-pill-btn active" data-vtopic="all" onclick="filterVocabByTopic('all')">🌐 Mọi chủ đề</button>
               <button class="filter-pill-btn" data-vtopic="business" onclick="filterVocabByTopic('business')">🏢 Công sở & Kinh doanh</button>
               <button class="filter-pill-btn" data-vtopic="travel" onclick="filterVocabByTopic('travel')">✈️ Du lịch & Dịch vụ</button>
               <button class="filter-pill-btn" data-vtopic="daily" onclick="filterVocabByTopic('daily')">☕ Đời sống thường nhật</button>
               <button class="filter-pill-btn" data-vtopic="tech" onclick="filterVocabByTopic('tech')">💻 Công nghệ & Trí tuệ AI</button>
               <button class="filter-pill-btn" data-vtopic="environment" onclick="filterVocabByTopic('environment')">🌿 Môi trường & Khí hậu</button>
               <button class="filter-pill-btn" data-vtopic="health" onclick="filterVocabByTopic('health')">🏥 Sức khỏe & Y tế</button>
               <button class="filter-pill-btn" data-vtopic="academic" onclick="filterVocabByTopic('academic')">🎓 Học thuật & Giáo dục</button>
            </div>
          </div>

          <div class="vocab-layout">
            <div>
               <!-- Flashcard tương tác -->
               <button class="flashcard" id="flashcard" aria-label="Lật thẻ từ vựng">
                 <div class="flashcard-inner">
                   <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:8px;">
                      <small id="flashcard-label">Từ 1 trong 5 · Nhấn để lật thẻ</small>
                      <div id="flashcard-badges" style="display:flex; gap:6px;"></div>
                   </div>
                   <div style="display:flex; align-items:center; justify-content:center; gap:8px;">
                      <h2 id="flashcard-word" style="margin:0;">allocate</h2>
                      <button class="speak-btn" id="btn-speak-flashcard" title="Nghe phát âm">🔊</button>
                   </div>
                   <p id="flashcard-detail">/ˈæləkeɪt/ · động từ</p>
                   <p class="reveal-hint" id="flashcard-hint">Chạm để xem nghĩa và ví dụ</p>
                 </div>
               </button>
               
               <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px;">
                  <button class="text-button" id="prev-word-btn" onclick="prevVocabWord()">← Từ trước</button>
                  <button class="primary" style="padding:8px 16px; font-size:13px;" id="next-word-btn" onclick="nextVocabWord()">Từ tiếp theo →</button>
               </div>

               <!-- Khung Vocab Quiz -->
               <div class="vocab-quiz-box" id="vocab-quiz-section" style="display:none;">
                  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                     <strong style="color:#c2410c; font-size:13px;">⚡ THỬ THÁCH TRẮC NGHIỆM TỪ VỰNG</strong>
                     <span id="quiz-progress-label" style="font-size:12px; color:var(--muted);">Câu 1 / 5</span>
                  </div>
                  <div class="vocab-quiz-q" id="vocab-quiz-question"></div>
                  <div class="vocab-quiz-opts" id="vocab-quiz-options"></div>
                  <div id="vocab-quiz-feedback" style="margin-top:10px; font-size:13px; font-weight:600; display:none;"></div>
               </div>
            </div>

            <div>
              <div class="section-head">
                 <h2>Danh sách từ (<span id="filtered-vocab-count">0</span>)</h2>
                 <span style="font-size:12px; color:var(--muted);">Bấm 🔊 để nghe giọng đọc bản ngữ</span>
              </div>
              <div class="vocab-list" id="vocab-list" style="max-height: 480px; overflow-y: auto; padding-right:6px;"></div>
            </div>
          </div>
        </section>"""

if "Khung CEFR" not in html:
    html = html.replace(old_vocab_view, new_vocab_view)
    print("Upgraded #view-vocabulary with Topics, CEFR B1-C2 levels, speech button, and quiz.")

# -------------------------------------------------------------------
# 6. THÊM VIEW MỚI: #view-analyzer (AI DOCUMENT ANALYZER) TRƯỚC </main>
# -------------------------------------------------------------------
analyzer_view = """
        <!-- VIEW: AI PHÂN TÍCH TÀI LIỆU (PDF & WORD) -->
        <section class="view" id="view-analyzer">
          <div class="page-title-row">
            <div>
              <p class="eyebrow">Trợ lý học thuật AI</p>
              <h1>Phân tích tài liệu học tập (PDF & Word)</h1>
              <p>Tải lên đề thi, bài luận hoặc tài liệu PDF/Word. AI sẽ phân loại tài liệu, đo cấp độ CEFR, trích xuất từ vựng và tự động sinh câu hỏi kiểm tra độ hiểu.</p>
            </div>
          </div>

          <!-- Dropzone Upload File -->
          <div class="analyzer-dropzone" id="doc-dropzone">
             <div class="dropzone-icon">📄</div>
             <h3 style="margin:0 0 6px; font-size:17px;">Kéo & Thả file PDF hoặc Word (.docx) vào đây</h3>
             <p style="margin:0 0 15px; font-size:13px; color:var(--muted);">Hỗ trợ định dạng: <strong>.pdf, .docx, .doc, .txt</strong> (Tối đa 15MB)</p>
             
             <input type="file" id="doc-file-input" accept=".pdf,.docx,.doc,.txt" style="display:none;" onchange="handleFileSelected(event)">
             <button type="button" class="primary" style="padding:10px 22px;" onclick="$('#doc-file-input').click()">Chọn file từ thiết bị</button>

             <div style="margin-top:20px; border-top:1px dashed var(--line); padding-top:15px;">
                <span style="font-size:12px; color:var(--muted); font-weight:600;">HOẶC TRẢI NGHIỆM NGAY VỚI TÀI LIỆU MẪU:</span>
                <div class="sample-doc-chips">
                   <button type="button" class="sample-doc-btn" onclick="loadSampleDocument('ielts')">
                      <span>📖</span> Mẫu IELTS Reading: Renewable Energy & Carbon Policy
                   </button>
                   <button type="button" class="sample-doc-btn" onclick="loadSampleDocument('toeic')">
                      <span>🏢</span> Mẫu TOEIC Business: Tech Corp Quarterly Strategy
                   </button>
                   <button type="button" class="sample-doc-btn" onclick="loadSampleDocument('academic')">
                      <span>🎓</span> Mẫu Học thuật: Cognitive Effects of Language Learning
                   </button>
                </div>
             </div>
          </div>

          <!-- Trạng thái đang phân tích -->
          <div id="analyzer-loading" style="display:none; text-align:center; padding:35px 20px; background:#fff; border-radius:12px; border:1px solid var(--line); margin-top:20px;">
             <div style="font-size:32px; animation: pulse 1s infinite;">⚡</div>
             <h3 style="margin:10px 0 4px; font-size:16px;" id="analyzer-status-text">AI đang đọc và trích xuất dữ liệu tài liệu...</h3>
             <p style="margin:0; font-size:13px; color:var(--muted);">Phân tích từ vựng, đo lường độ phức tạp ngữ pháp và cấu trúc...</p>
          </div>

          <!-- Kết quả phân tích từ AI -->
          <div id="analyzer-results" style="display:none; margin-top:24px;">
             <!-- Header kết quả -->
             <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:12px; padding:18px 22px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
                <div>
                   <span class="skill-pill reading" id="res-doc-type">Học thuật / IELTS Reading</span>
                   <h2 id="res-doc-title" style="margin:6px 0 2px; font-size:18px; color:var(--green-dark);">Tiêu đề tài liệu</h2>
                   <p id="res-doc-meta" style="margin:0; font-size:12.5px; color:var(--muted);">785 từ · Ước tính 5 phút đọc hiểu</p>
                </div>
                <div style="display:flex; gap:12px; align-items:center;">
                   <div style="text-align:right;">
                      <div style="font-size:11px; text-transform:uppercase; font-weight:700; color:var(--muted);">Độ khó CEFR</div>
                      <div id="res-doc-cefr" style="font-size:24px; font-family:var(--display); font-weight:800; color:var(--green-dark);">C1</div>
                   </div>
                   <div style="text-align:right; border-left:1px solid #bbf7d0; padding-left:12px;">
                      <div style="font-size:11px; text-transform:uppercase; font-weight:700; color:var(--muted);">Mức điểm đề xuất</div>
                      <div id="res-doc-target" style="font-size:18px; font-weight:700; color:#15803d;">IELTS 7.0+ / TOEIC 850+</div>
                   </div>
                </div>
             </div>

             <!-- Grid 3 phần phân tích -->
             <div class="analysis-results-grid">
                <!-- Cột 1: Tóm tắt ý chính -->
                <div class="analysis-card">
                   <div class="analysis-card-title"><span>📌</span> Tóm tắt nội dung chính (Key Takeaways)</div>
                   <ul id="res-doc-summary" style="margin:0; padding-left:20px; font-size:13px; line-height:1.7; color:#334155;"></ul>
                </div>

                <!-- Cột 2: Từ vựng học thuật trích xuất -->
                <div class="analysis-card">
                   <div class="analysis-card-title"><span>💎</span> Từ vựng học thuật & Collocations nổi bật</div>
                   <div id="res-doc-vocab" style="display:flex; flex-direction:column; gap:8px;"></div>
                </div>

                <!-- Cột 3: Đánh giá văn phong & ngữ pháp -->
                <div class="analysis-card">
                   <div class="analysis-card-title"><span>📊</span> Phân tích ngữ pháp & Văn phong</div>
                   <div id="res-doc-style" style="font-size:13px; line-height:1.6; color:#334155;"></div>
                </div>
             </div>

             <!-- Phần bài kiểm tra trắc nghiệm độ hiểu do AI sinh ra -->
             <div style="background:#fff; border:1px solid var(--line); border-radius:14px; padding:24px; margin-top:20px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
                   <div>
                      <h3 style="margin:0 0 4px; font-size:16px;">🎯 Bài kiểm tra độ hiểu do AI tự sinh từ tài liệu</h3>
                      <p style="margin:0; font-size:12.5px; color:var(--muted);">Trả lời các câu hỏi bên dưới để kiểm tra mức độ nắm bắt nội dung tài liệu vừa tải lên.</p>
                   </div>
                   <button class="primary" style="padding:8px 18px;" onclick="gradeDocumentQuiz()">Chấm điểm bài test</button>
                </div>
                
                <div id="res-doc-quiz" style="display:flex; flex-direction:column; gap:16px;"></div>
                <div id="res-quiz-result-box" style="display:none; margin-top:15px; padding:14px 18px; border-radius:10px; font-size:14px; font-weight:700;"></div>
             </div>
          </div>
        </section>
"""

if "id=\"view-analyzer\"" not in html:
    html = html.replace("</main>", analyzer_view + "\n    </main>")
    print("Added #view-analyzer before </main>.")

# -------------------------------------------------------------------
# 7. THÊM MODAL KHUNG ĐIỂM CHUẨN (#scoring-modal) TRƯỚC </body>
# -------------------------------------------------------------------
scoring_modal_html = """
  <!-- MODAL: KHUNG QUY ĐỔI ĐIỂM CHUẨN TOEIC & IELTS -->
  <div class="modal-backdrop" id="scoring-modal" role="presentation">
    <section class="exam-modal" style="width:min(860px, 95%); height:88vh; max-height:88vh; padding:24px; display:flex; flex-direction:column;" role="dialog">
      <div class="modal-top">
         <div>
            <div class="modal-label" style="color:var(--green-dark);">Khảo thí quốc tế</div>
            <h2 style="margin:0; font-size:18px;">Khung quy đổi điểm chuẩn TOEIC & IELTS</h2>
         </div>
         <button class="close-modal" onclick="closeScoringModal()">×</button>
      </div>

      <div class="tabs-nav" style="margin-top:15px;">
         <button class="tab-btn active" id="tab-btn-ets" onclick="switchScoringTab('ets')">🏢 Bảng điểm TOEIC chuẩn ETS (10 - 990)</button>
         <button class="tab-btn" id="tab-btn-idp" onclick="switchScoringTab('idp')">🏛️ Thang điểm IELTS IDP / British Council (1.0 - 9.0)</button>
      </div>

      <div style="flex:1; overflow-y:auto; padding-right:8px;" id="scoring-content-area">
         <!-- Bảng TOEIC -->
         <div id="tab-content-ets">
            <p style="font-size:13px; color:var(--muted); margin-bottom:12px;">Thang điểm quy đổi TOEIC 2 kỹ năng (Listening & Reading: mỗi kỹ năng tối đa 495 điểm) và 4 kỹ năng theo chuẩn Khảo thí Quốc tế ETS:</p>
            <table class="scoring-table">
               <thead>
                  <tr>
                     <th>Số câu đúng (trên 100)</th>
                     <th>Điểm Listening</th>
                     <th>Điểm Reading</th>
                     <th>Tổng điểm</th>
                     <th>Trình độ tương đương CEFR</th>
                  </tr>
               </thead>
               <tbody>
                  <tr><td><strong>96 – 100 câu</strong></td><td>495 pts</td><td>495 pts</td><td><strong>950 – 990 pts</strong></td><td><span class="level-badge c1">C1</span> Thành thạo chuyên nghiệp</td></tr>
                  <tr><td><strong>90 – 95 câu</strong></td><td>465 – 490 pts</td><td>455 – 485 pts</td><td><strong>905 – 945 pts</strong></td><td><span class="level-badge c1">C1</span> Cao cấp (Advanced)</td></tr>
                  <tr><td><strong>80 – 89 câu</strong></td><td>410 – 455 pts</td><td>395 – 445 pts</td><td><strong>785 – 900 pts</strong></td><td><span class="level-badge b2">B2</span> Làm việc công sở quốc tế</td></tr>
                  <tr><td><strong>65 – 79 câu</strong></td><td>335 – 400 pts</td><td>310 – 385 pts</td><td><strong>605 – 780 pts</strong></td><td><span class="level-badge b1">B1</span> Giao tiếp độc lập</td></tr>
                  <tr><td><strong>45 – 64 câu</strong></td><td>235 – 325 pts</td><td>205 – 300 pts</td><td><strong>405 – 600 pts</strong></td><td><span class="level-badge b1">B1</span> Cơ bản đủ tốt nghiệp</td></tr>
                  <tr><td><strong>25 – 44 câu</strong></td><td>135 – 225 pts</td><td>115 – 195 pts</td><td><strong>255 – 400 pts</strong></td><td><span class="level-badge b1">A2</span> Sơ cấp</td></tr>
                  <tr><td><strong>0 – 24 câu</strong></td><td>5 – 125 pts</td><td>5 – 105 pts</td><td><strong>10 – 250 pts</strong></td><td><span class="level-badge b1">A1</span> Mới bắt đầu</td></tr>
               </tbody>
            </table>

            <div style="margin-top:16px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:12px; font-size:12.5px; color:#475569;">
               <strong>TOEIC Speaking & Writing:</strong> Mỗi kỹ năng được chấm trên thang từ <strong>0 – 200 điểm</strong>. Tổng 2 kỹ năng là 400 điểm. Đạt từ 310+ được xếp vào cấp độ B2 / C1.
            </div>
         </div>

         <!-- Bảng IELTS -->
         <div id="tab-content-idp" style="display:none;">
            <p style="font-size:13px; color:var(--muted); margin-bottom:12px;">Quy tắc quy đổi số câu đúng sang IELTS Band Score (theo thang điểm chính thức Cambridge & IDP):</p>
            <table class="scoring-table">
               <thead>
                  <tr>
                     <th>Số câu đúng (trên 40)</th>
                     <th>IELTS Listening</th>
                     <th>Academic Reading</th>
                     <th>General Reading</th>
                     <th>Đánh giá năng lực</th>
                  </tr>
               </thead>
               <tbody>
                  <tr><td><strong>39 – 40 câu</strong></td><td><strong>Band 9.0</strong></td><td><strong>Band 9.0</strong></td><td>Band 9.0</td><td><span class="level-badge c2">C2</span> Expert User (Bản ngữ)</td></tr>
                  <tr><td><strong>37 – 38 câu</strong></td><td><strong>Band 8.5</strong></td><td><strong>Band 8.5</strong></td><td>Band 8.5</td><td><span class="level-badge c2">C2</span> Very Good User</td></tr>
                  <tr><td><strong>35 – 36 câu</strong></td><td><strong>Band 8.0</strong></td><td><strong>Band 8.0</strong></td><td>Band 8.0</td><td><span class="level-badge c1">C1</span> Very Good User</td></tr>
                  <tr><td><strong>32 – 34 câu</strong></td><td><strong>Band 7.5</strong></td><td><strong>Band 7.5</strong></td><td>Band 7.5</td><td><span class="level-badge c1">C1</span> Good User (Đạt chuẩn định cư/du học)</td></tr>
                  <tr><td><strong>30 – 31 câu</strong></td><td><strong>Band 7.0</strong></td><td><strong>Band 7.0</strong></td><td>Band 7.0</td><td><span class="level-badge c1">C1</span> Good User</td></tr>
                  <tr><td><strong>26 – 29 câu</strong></td><td><strong>Band 6.5</strong></td><td><strong>Band 6.5</strong></td><td>Band 6.5</td><td><span class="level-badge b2">B2</span> Competent User (Đại học quốc tế)</td></tr>
                  <tr><td><strong>23 – 25 câu</strong></td><td><strong>Band 6.0</strong></td><td><strong>Band 6.0</strong></td><td>Band 6.0</td><td><span class="level-badge b2">B2</span> Competent User</td></tr>
                  <tr><td><strong>19 – 22 câu</strong></td><td><strong>Band 5.5</strong></td><td><strong>Band 5.5</strong></td><td>Band 5.5</td><td><span class="level-badge b1">B1</span> Modest User</td></tr>
                  <tr><td><strong>15 – 18 câu</strong></td><td><strong>Band 5.0</strong></td><td><strong>Band 5.0</strong></td><td>Band 5.0</td><td><span class="level-badge b1">B1</span> Modest User</td></tr>
               </tbody>
            </table>

            <div style="margin-top:16px; background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:12px; font-size:12.5px; color:#166534;">
               <strong>Quy tắc làm tròn Overall Band:</strong> Điểm tổng là trung bình cộng 4 kỹ năng. Nếu số lẻ là <strong>.25</strong> sẽ làm tròn lên <strong>.5</strong>; nếu số lẻ là <strong>.75</strong> sẽ làm tròn lên <strong>1.0</strong> (Ví dụ: 6.25 ➔ 6.5; 6.75 ➔ 7.0).
            </div>
         </div>
      </div>

      <div style="padding-top:14px; border-top:1px solid var(--line); display:flex; justify-content:flex-end;">
         <button class="primary" onclick="closeScoringModal()">Đã hiểu</button>
      </div>
    </section>
  </div>
"""

if "id=\"scoring-modal\"" not in html:
    html = html.replace("""<div class="toast" id="toast" role="status"></div>""", """<div class="toast" id="toast" role="status"></div>\n""" + scoring_modal_html)
    print("Added #scoring-modal markup before closing.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML template structure upgrade completed.")
