# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
html_path = r"e:\EngLish-IE-Toeic\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------------
# 1. FIX DOM: CHUYỂN TẤT CẢ CÁC VIEW VÀO BÊN TRONG <div class="page">
# -------------------------------------------------------------------
# Tìm thẻ </div> kết thúc <div class="page"> ở dòng 710 (ngay sau </section> của view-progress)
progress_close = "</section>\n      </div>\n    \n        <!-- VIEW: CÂU HỎI ĐÃ LƯU & BÁO CÁO -->"
progress_close_clean = "</section>\n    \n        <!-- VIEW: CÂU HỎI ĐÃ LƯU & BÁO CÁO -->"

if progress_close in html:
    html = html.replace(progress_close, progress_close_clean)
    print("Removed premature </div> closing for .page after view-progress.")
else:
    # Pattern search
    pattern = r'(id="view-progress"[^>]*>.*?</section>)\s*</div>\s*(<!-- VIEW: CÂU HỎI)'
    html = re.sub(pattern, r'\1\n        \2', html, flags=re.DOTALL)
    print("Cleaned page closing div via regex.")

# Đảm bảo đóng </div> cho .page ngay trước </main>
main_close_pattern = "</section>\n\n    </main>"
main_close_correct = "</section>\n      </div> <!-- end .page -->\n    </main>"
if main_close_pattern in html:
    html = html.replace(main_close_pattern, main_close_correct)
    print("Closed .page properly right before </main>.")

# -------------------------------------------------------------------
# 2. GẮN TRỰC TIẾP ONCLICK CHO TẤT CẢ CÁC NÚT SIDEBAR NAV
# -------------------------------------------------------------------
old_nav_markup = """      <nav class="nav" aria-label="Điều hướng chính">
        <button class="active" data-view="overview"><span class="nav-glyph">⌂</span>Tổng quan</button>
        <button data-view="practice"><span class="nav-glyph">▤</span>Luyện đề 4 kỹ năng</button>
        <button data-view="vocabulary"><span class="nav-glyph">Aa</span>Từ vựng</button>
        <button data-view="progress"><span class="nav-glyph">↗</span>Tiến độ & Lịch sử</button>
        <button data-view="bookmarks"><span class="nav-glyph">★</span>Đã lưu & Báo cáo</button>
        <button data-view="profile"><span class="nav-glyph">👤</span>Hồ sơ mục tiêu</button>
        <button data-view="analyzer"><span class="nav-glyph">🤖</span>AI Phân tích tài liệu</button>
      </nav>"""

new_nav_markup = """      <nav class="nav" aria-label="Điều hướng chính">
        <button class="active" data-view="overview" onclick="showView('overview')"><span class="nav-glyph">⌂</span>Tổng quan</button>
        <button data-view="practice" onclick="showView('practice')"><span class="nav-glyph">▤</span>Luyện đề 4 kỹ năng</button>
        <button data-view="vocabulary" onclick="showView('vocabulary')"><span class="nav-glyph">Aa</span>Từ vựng</button>
        <button data-view="progress" onclick="showView('progress')"><span class="nav-glyph">↗</span>Tiến độ & Lịch sử</button>
        <button data-view="bookmarks" onclick="showView('bookmarks')"><span class="nav-glyph">★</span>Đã lưu & Báo cáo</button>
        <button data-view="profile" onclick="showView('profile')"><span class="nav-glyph">👤</span>Hồ sơ mục tiêu</button>
        <button data-view="analyzer" onclick="showView('analyzer')"><span class="nav-glyph">🤖</span>AI Phân tích tài liệu</button>
      </nav>"""

if old_nav_markup in html:
    html = html.replace(old_nav_markup, new_nav_markup)
    print("Added explicit inline onclick to all sidebar buttons.")

# -------------------------------------------------------------------
# 3. THAY THẾ RENDER QUESTION: TÍCH HỢP TỐC ĐỘ NGHE 0.75x/1.0x/1.25x & THU ÂM THỰC
# -------------------------------------------------------------------
# Tìm đoạn audio player trong renderQuestion
old_audio_box = """        // Audio Player (cho Listening)
        let mediaHtml = '';
        if (currentExamData && currentExamData.audioTitle) {
            mediaHtml = `
              <div class="audio-box">
                 <button class="audio-play-btn" id="audio-play-toggle" onclick="toggleSimulatedAudio()">▶</button>
                 <div class="audio-track">
                    <div class="audio-title">
                       <span>${currentExamData.audioTitle}</span>
                       <span id="audio-time-label">0:00 / 1:30</span>
                    </div>
                    <div class="audio-wave"><div class="audio-progress" id="audio-progress-bar"></div></div>
                 </div>
                 <button class="text-button" style="font-size:11px; padding:4px 8px; border:1px solid #bbf7d0; border-radius:4px;" onclick="$('#audio-transcript').classList.toggle('show')">Lời thoại (Transcript)</button>
              </div>
              <div class="transcript-box" id="audio-transcript">${currentExamData.audioScript || ''}</div>
            `;
        }"""

new_audio_box = """        // Audio Player (cho Listening có chỉnh tốc độ thời gian thực 0.75x, 1.0x, 1.25x)
        let mediaHtml = '';
        if (currentExamData && currentExamData.audioTitle) {
            mediaHtml = `
              <div class="audio-box" style="flex-wrap: wrap;">
                 <button class="audio-play-btn" id="audio-play-toggle" onclick="toggleSimulatedAudio()">▶</button>
                 <div class="audio-track" style="min-width: 220px;">
                    <div class="audio-title">
                       <span>${currentExamData.audioTitle}</span>
                       <span id="audio-time-label">0:00 / 1:30 (1.0x)</span>
                    </div>
                    <div class="audio-wave"><div class="audio-progress" id="audio-progress-bar"></div></div>
                 </div>
                 <div style="display:flex; align-items:center; gap:4px; background:#fff; border:1px solid #bbf7d0; border-radius:6px; padding:4px 8px;">
                    <span style="font-size:11px; font-weight:700; color:var(--muted);">Tốc độ:</span>
                    <button type="button" class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75)" style="padding:2px 6px; font-size:11.5px; border:1px solid #bbf7d0; background:none; cursor:pointer; font-weight:600; border-radius:4px;">0.75x</button>
                    <button type="button" class="speed-btn active" data-speed="1.0" onclick="setAudioSpeed(1.0)" style="padding:2px 6px; font-size:11.5px; border:1px solid var(--green); background:var(--green); color:#fff; cursor:pointer; font-weight:600; border-radius:4px;">1.0x</button>
                    <button type="button" class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25)" style="padding:2px 6px; font-size:11.5px; border:1px solid #bbf7d0; background:none; cursor:pointer; font-weight:600; border-radius:4px;">1.25x</button>
                 </div>
                 <button type="button" class="text-button" style="font-size:11.5px; padding:5px 9px; border:1px solid #bbf7d0; border-radius:6px;" onclick="$('#audio-transcript').classList.toggle('show')">Lời thoại (Transcript)</button>
              </div>
              <div class="transcript-box" id="audio-transcript">${currentExamData.audioScript || ''}</div>
            `;
        }"""

if old_audio_box in html:
    html = html.replace(old_audio_box, new_audio_box)
    print("Replaced audio box with real-time speed selector controls.")

# Cập nhật writing box với progress bar số từ trực quan theo thời gian thực
old_writing_box = """              <div class="writing-box">
                 <textarea class="writing-textarea" id="writing-input" placeholder="Nhập bài viết của bạn tại đây bằng tiếng Anh..." oninput="updateWritingWordCount()">${uAns || ''}</textarea>
                 <div class="writing-stats">
                    <span>Số từ hiện tại: <strong id="word-count-num">0</strong> từ ${item.minWords ? `(Yêu cầu tối thiểu: ${item.minWords} từ)` : ''}</span>
                    <button class="primary" style="padding:8px 16px; font-size:13px;" onclick="saveWritingAnswer()">Lưu bài viết</button>
                 </div>
              </div>"""

new_writing_box = """              <div class="writing-box">
                 <textarea class="writing-textarea" id="writing-input" placeholder="Nhập bài viết của bạn tại đây bằng tiếng Anh..." oninput="updateWritingWordCount()">${uAns || ''}</textarea>
                 <div class="writing-stats" style="flex-wrap: wrap; gap: 8px;">
                    <div style="flex: 1; min-width: 200px;">
                       <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                          <span>Số từ: <strong id="word-count-num">0</strong> từ ${item.minWords ? `(Mục tiêu: ${item.minWords} từ)` : ''}</span>
                          <span id="writing-req-status" style="font-size:11.5px;"></span>
                       </div>
                       <div style="height:6px; background:#e2e8f0; border-radius:3px; overflow:hidden;">
                          <div id="writing-word-progress" style="height:100%; width:0%; background:#f59e0b; border-radius:3px; transition:width .2s;"></div>
                       </div>
                    </div>
                    <button class="primary" style="padding:8px 16px; font-size:13px;" onclick="saveWritingAnswer()">Lưu bài viết</button>
                 </div>
              </div>"""

if old_writing_box in html:
    html = html.replace(old_writing_box, new_writing_box)
    print("Upgraded Writing live word counter with real-time progress bar.")

# Cập nhật nút thoát về trang chủ trong modal kết quả
old_result_buttons = """              <div style="display:flex; justify-content:center; gap:12px;">
                 <button class="primary" onclick="openReviewModalFromLatest()">Xem lại chi tiết bài làm 🔍</button>
                 <button class="text-button" style="border:1px solid var(--line); border-radius:8px; padding:10px 16px;" onclick="closeExam()">Quay lại danh sách đề</button>
              </div>"""

new_result_buttons = """              <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
                 <button class="primary" onclick="openReviewModalFromLatest()">Xem lại chi tiết bài làm 🔍</button>
                 <button class="text-button" style="border:1px solid var(--line); border-radius:8px; padding:10px 16px;" onclick="closeExam()">Quay lại danh sách đề</button>
                 <button class="text-button" style="border:1px solid var(--green); color:var(--green-dark); border-radius:8px; padding:10px 16px; font-weight:700;" onclick="closeExamAndGoHome()">🏠 Về trang chủ</button>
              </div>"""

if old_result_buttons in html:
    html = html.replace(old_result_buttons, new_result_buttons)
    print("Added 'Về trang chủ' button to exam completion modal.")

# Thêm nút 'Về trang chủ' trong review modal
old_review_close = """      <div style="padding-top:14px; border-top:1px solid var(--line); display:flex; justify-content:flex-end;">
         <button class="primary" onclick="closeReviewModal()">Đóng xem lại</button>
      </div>"""

new_review_close = """      <div style="padding-top:14px; border-top:1px solid var(--line); display:flex; justify-content:flex-end; gap:10px;">
         <button class="text-button" style="border:1px solid var(--green); color:var(--green-dark); padding:8px 16px; border-radius:8px; font-weight:600;" onclick="closeReviewModalAndGoHome()">🏠 Về trang chủ</button>
         <button class="primary" onclick="closeReviewModal()">Đóng xem lại</button>
      </div>"""

if old_review_close in html:
    html = html.replace(old_review_close, new_review_close)
    print("Added 'Về trang chủ' button to review modal.")

# -------------------------------------------------------------------
# 4. THAY THẾ TOÀN BỘ LOGIC AUDIO (SPEECH SYNTHESIS REAL-TIME + TỐC ĐỘ 1.25x)
#    VÀ REAL-TIME MICROPHONE RECORDER CHO PHẦN THI NÓI
# -------------------------------------------------------------------
old_audio_logic_start = "    let currentExamData = null;"
old_audio_logic_end = "    function closeExam() {"

idx_a1 = html.find(old_audio_logic_start)
idx_a2 = html.find(old_audio_logic_end)

if idx_a1 == -1 or idx_a2 == -1:
    print(f"Error finding audio logic indices: idx_a1={idx_a1}, idx_a2={idx_a2}")
    sys.exit(1)

# Find the end of closeExam
end_close_exam = html.find("    // ==========================================\n    // 7. REVIEW MODAL", idx_a2)

new_audio_and_exam_runtime = r'''    let currentExamData = null;
    let currentExamTitle = '';
    let currentQuestions = [];
    let isReviewMode = false;
    let simulatedAudioPlaying = false;
    let audioTimer = null;
    let audioProgressVal = 0;
    let currentAudioSpeed = 1.0;
    let activeUtterance = null;
    
    // Live Microphone Recording State
    let isSpeakingRecording = false;
    let mediaRecorderInstance = null;
    let audioChunks = [];
    let recordingTimerInterval = null;
    let recordingSeconds = 0;

    function setAudioSpeed(spd) {
        currentAudioSpeed = spd;
        $$('.speed-btn').forEach(btn => {
            const isMatch = parseFloat(btn.dataset.speed) === spd;
            btn.style.background = isMatch ? 'var(--green)' : 'none';
            btn.style.color = isMatch ? '#fff' : 'inherit';
            btn.style.borderColor = isMatch ? 'var(--green)' : '#bbf7d0';
        });
        
        const lbl = $('#audio-time-label');
        if (lbl) {
            const curSec = Math.floor((audioProgressVal / 100) * 90);
            lbl.textContent = `0:${String(curSec).padStart(2,'0')} / 1:30 (${spd}x)`;
        }

        // Nếu đang phát âm thanh, đồng bộ tốc độ ngay lập tức theo thời gian thực
        if (simulatedAudioPlaying) {
            stopAudioPlayback();
            startAudioPlayback();
        }
    }

    function toggleSimulatedAudio() {
        if (simulatedAudioPlaying) {
            stopAudioPlayback();
        } else {
            startAudioPlayback();
        }
    }

    function startAudioPlayback() {
        simulatedAudioPlaying = true;
        const btn = $('#audio-play-toggle');
        if (btn) btn.textContent = '⏸';

        const scriptText = (currentExamData?.audioScript || currentQuestions[questionIndex]?.text || 'Audio listening test track').replace(/\\n/g, ' ');

        // Phát âm thanh giọng bản ngữ thực qua Web Speech API
        if (window.speechSynthesis) {
            window.speechSynthesis.cancel();
            activeUtterance = new SpeechSynthesisUtterance(scriptText);
            activeUtterance.lang = 'en-US';
            activeUtterance.rate = currentAudioSpeed;
            activeUtterance.onend = () => {
                stopAudioPlayback();
            };
            activeUtterance.onerror = () => {
                stopAudioPlayback();
            };
            window.speechSynthesis.speak(activeUtterance);
        }

        const bar = $('#audio-progress-bar');
        const lbl = $('#audio-time-label');
        clearInterval(audioTimer);
        
        audioTimer = setInterval(() => {
            audioProgressVal += (1.6 * currentAudioSpeed);
            if (audioProgressVal > 100) {
                audioProgressVal = 0;
                stopAudioPlayback();
            }
            if (bar) bar.style.width = audioProgressVal + '%';
            const curSec = Math.floor((audioProgressVal / 100) * 90);
            if (lbl) lbl.textContent = `0:${String(curSec).padStart(2,'0')} / 1:30 (${currentAudioSpeed}x)`;
        }, 250);
    }

    function stopAudioPlayback() {
        simulatedAudioPlaying = false;
        if (window.speechSynthesis) window.speechSynthesis.cancel();
        clearInterval(audioTimer);
        const btn = $('#audio-play-toggle');
        if (btn) btn.textContent = '▶';
    }

    // Thu âm giọng nói trực tiếp qua MediaRecorder API (Real-time Microphone)
    async function toggleSpeakingRecord() {
        const btn = $('#record-btn');
        const st = $('#record-status');
        const pb = $('#speech-playback-wrap');
        const audioEl = $('#speech-playback');

        if (!isSpeakingRecording) {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                mediaRecorderInstance = new MediaRecorder(stream);
                audioChunks = [];
                mediaRecorderInstance.ondataavailable = e => { if (e.data.size > 0) audioChunks.push(e.data); };
                mediaRecorderInstance.onstop = () => {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
                    const audioUrl = URL.createObjectURL(audioBlob);
                    if (audioEl) audioEl.src = audioUrl;
                    stream.getTracks().forEach(t => t.stop());
                };
                mediaRecorderInstance.start();
            } catch(e) {
                console.warn('Microphone permission or support notice:', e);
            }

            isSpeakingRecording = true;
            recordingSeconds = 0;
            btn.classList.add('recording');
            st.textContent = '🔴 Đang ghi âm thời gian thực: 00:00 (Bấm nút mic để dừng)';
            st.style.color = '#ef4444';
            if (pb) pb.style.display = 'none';

            clearInterval(recordingTimerInterval);
            recordingTimerInterval = setInterval(() => {
                recordingSeconds++;
                const m = String(Math.floor(recordingSeconds / 60)).padStart(2, '0');
                const s = String(recordingSeconds % 60).padStart(2, '0');
                st.textContent = `🔴 Đang ghi âm thời gian thực: ${m}:${s} (Bấm nút mic để dừng)`;
            }, 1000);

        } else {
            isSpeakingRecording = false;
            clearInterval(recordingTimerInterval);
            btn.classList.remove('recording');
            st.textContent = `✓ Đã hoàn thành ghi âm bài nói (${recordingSeconds} giây)! Bấm play bên dưới để nghe lại:`;
            st.style.color = 'var(--green)';
            if (pb) pb.style.display = 'block';

            if (mediaRecorderInstance && mediaRecorderInstance.state !== 'inactive') {
                mediaRecorderInstance.stop();
            }

            userAnswers[questionIndex] = `recorded_voice_${recordingSeconds}s`;
            correctAnswers++;
            renderQuestionGrid();
        }
    }

    // Đếm số từ bài viết theo thời gian thực (Real-time Word Count)
    function updateWritingWordCount() {
        const text = $('#writing-input')?.value || '';
        const words = text.trim() ? text.trim().split(/\s+/).length : 0;
        const numEl = $('#word-count-num');
        const item = currentQuestions[questionIndex] || {};
        const minWords = item.minWords || 150;
        
        if (numEl) numEl.textContent = words;
        
        const progEl = $('#writing-word-progress');
        if (progEl) {
            const pct = Math.min(100, Math.round((words / minWords) * 100));
            progEl.style.width = pct + '%';
            progEl.style.background = words >= minWords ? 'var(--green)' : '#f59e0b';
        }

        const reqStatusEl = $('#writing-req-status');
        if (reqStatusEl) {
            if (words >= minWords) {
                reqStatusEl.innerHTML = `<span style="color:#15803d; font-weight:700;">✓ Đạt tiêu chuẩn (${words}/${minWords} từ)</span>`;
            } else {
                reqStatusEl.innerHTML = `<span style="color:#b45309;">Cần thêm ${minWords - words} từ nữa</span>`;
            }
        }
    }

    function saveWritingAnswer() {
        const text = $('#writing-input')?.value || '';
        userAnswers[questionIndex] = text;
        correctAnswers++;
        notify('Đã lưu bài viết của bạn.');
        renderQuestion();
        renderQuestionGrid();
    }

    function openExam(title) {
        currentExamTitle = title;
        isReviewMode = false;
        
        const courseConfig = courses.find(c => c.title === title) || { kind: 'TOEIC', skill: 'Reading', time: '15 phút' };
        currentExamData = examDatabase[title] || { questions: questions };
        currentQuestions = currentExamData.questions || questions;

        questionIndex = 0;
        correctAnswers = 0;
        userAnswers = new Array(currentQuestions.length).fill(null);
        audioProgressVal = 0;
        currentAudioSpeed = 1.0;
        
        $('#exam-label').textContent = title;
        $('#exam-backdrop').classList.add('open');
        document.body.style.overflow = 'hidden';

        const parseMinutes = parseInt(courseConfig.time) || 15;
        
        $('#exam-content').innerHTML = `
          <div class="exam-layout">
             <div class="exam-main" id="exam-main-area"></div>
             <div class="exam-sidebar">
                <div class="exam-timer">
                   <div class="timer-clock" id="timer-clock">${String(parseMinutes).padStart(2,'0')}:00</div>
                   <div class="timer-label">Thời gian còn lại</div>
                </div>
                <div style="margin-top: 10px;">
                   <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                      <span style="font-size:11px; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.5px;">Danh sách câu</span>
                      <span class="skill-pill ${courseConfig.skill.toLowerCase()}">${courseConfig.skill}</span>
                   </div>
                   <div class="question-grid" id="question-grid"></div>
                </div>
                <div style="margin-top: auto; display:flex; flex-direction:column; gap:8px;">
                   <button class="primary" style="padding: 12px; text-align: center; justify-content: center; width: 100%; display: flex;" id="submit-exam-btn">Nộp bài sớm</button>
                   <button type="button" class="text-button" style="font-size:12px; color:var(--muted); text-align:center; padding:6px;" onclick="closeExamAndGoHome()">Thoát về trang chủ</button>
                </div>
             </div>
          </div>
        `;
        
        renderQuestionGrid();
        renderQuestion();
        startTimer(parseMinutes);
        
        $('#submit-exam-btn').addEventListener('click', finishExam);
        $('#close-modal').focus();
    }

    function renderQuestionGrid() {
        const grid = $('#question-grid');
        if (!grid) return;
        grid.innerHTML = currentQuestions.map((_, i) => `
            <button class="q-btn ${i === questionIndex ? 'active' : ''} ${userAnswers[i] !== null ? 'answered' : ''}" data-qindex="${i}">
               ${i + 1}
            </button>
        `).join('');
        $$('.q-btn').forEach(btn => btn.addEventListener('click', () => {
            stopAudioPlayback();
            questionIndex = Number(btn.dataset.qindex);
            renderQuestion();
            renderQuestionGrid();
        }));
    }

    function renderQuestion() {
        const item = currentQuestions[questionIndex];
        const hasAnswered = userAnswers[questionIndex] !== null;
        const uAns = userAnswers[questionIndex];
        const isBookmarked = isQuestionBookmarked(currentExamTitle, questionIndex);
        
        let headerHtml = `
          <div class="q-action-bar">
             <div class="q-action-btns">
                <button class="q-tool-btn ${isBookmarked ? 'bookmarked' : ''}" onclick="toggleBookmark('${currentExamTitle.replace(/'/g, "\\'")}', ${questionIndex})">
                   <span>${isBookmarked ? '★' : '☆'}</span> ${isBookmarked ? 'Đã lưu' : 'Lưu câu'}
                </button>
                <button class="q-tool-btn" onclick="openReportModal('${currentExamTitle.replace(/'/g, "\\'")}', ${questionIndex})">
                   <span>🚩</span> Báo cáo
                </button>
             </div>
             <div class="q-action-btns">
                <button class="tool-btn" id="btn-translate"><span>文A</span> Dịch câu</button>
                <button class="tool-btn" id="btn-ai-explain" ${!hasAnswered ? 'disabled style="opacity:0.6;cursor:not-allowed;" title="Trả lời câu hỏi để xem giải thích"' : ''}><span>✨</span> Giải thích AI</button>
             </div>
          </div>
        `;

        // Audio Player (cho Listening có chỉnh tốc độ)
        let mediaHtml = '';
        if (currentExamData && currentExamData.audioTitle) {
            mediaHtml = `
              <div class="audio-box" style="flex-wrap: wrap;">
                 <button class="audio-play-btn" id="audio-play-toggle" onclick="toggleSimulatedAudio()">▶</button>
                 <div class="audio-track" style="min-width: 220px;">
                    <div class="audio-title">
                       <span>${currentExamData.audioTitle}</span>
                       <span id="audio-time-label">0:00 / 1:30 (${currentAudioSpeed}x)</span>
                    </div>
                    <div class="audio-wave"><div class="audio-progress" id="audio-progress-bar"></div></div>
                 </div>
                 <div style="display:flex; align-items:center; gap:4px; background:#fff; border:1px solid #bbf7d0; border-radius:6px; padding:4px 8px;">
                    <span style="font-size:11px; font-weight:700; color:var(--muted);">Tốc độ:</span>
                    <button type="button" class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75)" style="padding:2px 6px; font-size:11.5px; border:1px solid ${currentAudioSpeed === 0.75 ? 'var(--green)' : '#bbf7d0'}; background:${currentAudioSpeed === 0.75 ? 'var(--green)' : 'none'}; color:${currentAudioSpeed === 0.75 ? '#fff' : 'inherit'}; cursor:pointer; font-weight:600; border-radius:4px;">0.75x</button>
                    <button type="button" class="speed-btn" data-speed="1.0" onclick="setAudioSpeed(1.0)" style="padding:2px 6px; font-size:11.5px; border:1px solid ${currentAudioSpeed === 1.0 ? 'var(--green)' : '#bbf7d0'}; background:${currentAudioSpeed === 1.0 ? 'var(--green)' : 'none'}; color:${currentAudioSpeed === 1.0 ? '#fff' : 'inherit'}; cursor:pointer; font-weight:600; border-radius:4px;">1.0x</button>
                    <button type="button" class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25)" style="padding:2px 6px; font-size:11.5px; border:1px solid ${currentAudioSpeed === 1.25 ? 'var(--green)' : '#bbf7d0'}; background:${currentAudioSpeed === 1.25 ? 'var(--green)' : 'none'}; color:${currentAudioSpeed === 1.25 ? '#fff' : 'inherit'}; cursor:pointer; font-weight:600; border-radius:4px;">1.25x</button>
                 </div>
                 <button type="button" class="text-button" style="font-size:11.5px; padding:5px 9px; border:1px solid #bbf7d0; border-radius:6px;" onclick="$('#audio-transcript').classList.toggle('show')">Lời thoại (Transcript)</button>
              </div>
              <div class="transcript-box" id="audio-transcript">${currentExamData.audioScript || ''}</div>
            `;
        }

        // Reading Passage
        if (currentExamData && currentExamData.passageText) {
            mediaHtml = `
              <div class="passage-card">
                 <h4>📖 ${currentExamData.passageTitle || 'Reading Comprehension Passage'}</h4>
                 <p style="white-space: pre-line; margin:0;">${currentExamData.passageText}</p>
              </div>
            `;
        }

        // Body Content based on question type
        let bodyHtml = '';
        if (item.choices && item.choices.length > 0) {
            bodyHtml = `
              <div class="question-count">Câu ${questionIndex + 1} / ${currentQuestions.length}</div>
              <div class="question-text">${item.text}</div>
              <div class="translated-text" id="translated-text">${item.translated || ''}</div>
              <div class="options">
                ${item.choices.map((choice, index) => {
                   let cls = 'option';
                   if (hasAnswered) {
                      if (index === item.answer) cls += ' correct';
                      else if (index === uAns) cls += ' wrong';
                   }
                   return `<button class="${cls}" data-choice="${index}" ${hasAnswered ? 'disabled' : ''}>
                      <span class="letter">${String.fromCharCode(65 + index)}</span>
                      <span>${choice}</span>
                   </button>`;
                }).join('')}
              </div>
            `;
        } else if (currentExamData && currentExamData.type === 'writing') {
            bodyHtml = `
              <div class="question-count">Bài viết ${questionIndex + 1} / ${currentQuestions.length}</div>
              <div class="question-text" style="white-space:pre-line;">${item.text}</div>
              <div class="translated-text" id="translated-text">${item.translated || ''}</div>
              
              <div class="writing-box">
                 <textarea class="writing-textarea" id="writing-input" placeholder="Nhập bài viết của bạn tại đây bằng tiếng Anh..." oninput="updateWritingWordCount()">${uAns || ''}</textarea>
                 <div class="writing-stats" style="flex-wrap: wrap; gap: 8px;">
                    <div style="flex: 1; min-width: 200px;">
                       <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                          <span>Số từ: <strong id="word-count-num">0</strong> từ ${item.minWords ? `(Mục tiêu: ${item.minWords} từ)` : ''}</span>
                          <span id="writing-req-status" style="font-size:11.5px;"></span>
                       </div>
                       <div style="height:6px; background:#e2e8f0; border-radius:3px; overflow:hidden;">
                          <div id="writing-word-progress" style="height:100%; width:0%; background:#f59e0b; border-radius:3px; transition:width .2s;"></div>
                       </div>
                    </div>
                    <button class="primary" style="padding:8px 16px; font-size:13px;" onclick="saveWritingAnswer()">Lưu bài viết</button>
                 </div>
              </div>
            `;
        } else if (currentExamData && currentExamData.type === 'speaking') {
            bodyHtml = `
              <div class="question-count">Phần thi nói ${questionIndex + 1} / ${currentQuestions.length}</div>
              <div class="question-text" style="white-space:pre-line;">${item.text}</div>
              <div class="translated-text" id="translated-text">${item.translated || ''}</div>

              <div class="speaking-box">
                 <p style="font-size:13px; color:#6b21a8; margin:0 0 10px;">Chuẩn bị: <strong>${item.prepTime || 30}s</strong> · Thời gian nói: <strong>${item.speakTime || 60}s</strong></p>
                 <button class="record-btn" id="record-btn" onclick="toggleSpeakingRecord()">🎙️</button>
                 <div id="record-status" style="font-size:13px; font-weight:700; color:#7e22ce;">Nhấn mic để bắt đầu thu âm thời gian thực</div>
                 <div id="speech-playback-wrap" style="display:none; margin-top:15px;">
                    <audio id="speech-playback" controls style="width:100%; max-width:360px; margin:auto;"></audio>
                    <p style="font-size:12px; color:var(--green); font-weight:600; margin-top:6px;">✓ Đã thu âm giọng nói thực tế! Bấm play để nghe lại.</p>
                 </div>
              </div>
            `;
        }

        let explainHtml = `
          <div class="ai-explain-box" id="ai-explain-box">
             <h4><span class="ai-icon">✨</span> Phân tích & Hướng dẫn từ AI</h4>
             <p style="white-space:pre-line; margin-bottom:8px;">${item.ai_explain || ''}</p>
             ${item.sampleAnswer ? `<div style="background:#fff; border:1px solid #bbf7d0; padding:10px; border-radius:6px; font-size:12px; color:#14532d;"><strong>Bài mẫu tham khảo:</strong><br>${item.sampleAnswer}</div>` : ''}
          </div>
        `;

        let footerHtml = `
          <div class="modal-footer" style="margin-top: 30px; border-top: 1px solid var(--line); padding-top: 20px;">
             <button class="text-button" id="prev-question" ${questionIndex === 0 ? 'style="opacity:0; pointer-events:none;"' : ''}>← Câu trước</button>
             <button class="primary" id="next-question">${questionIndex === currentQuestions.length - 1 ? (hasAnswered ? 'Xem kết quả' : 'Nộp bài') : 'Câu tiếp theo →'}</button>
          </div>
        `;

        $('#exam-main-area').innerHTML = headerHtml + mediaHtml + bodyHtml + explainHtml + footerHtml;

        // Listeners
        $$('.option:not([disabled])').forEach(button => button.addEventListener('click', () => chooseAnswer(Number(button.dataset.choice))));
        
        $('#btn-translate')?.addEventListener('click', function() {
            this.classList.toggle('active');
            $('#translated-text').classList.toggle('show');
        });
        
        $('#btn-ai-explain')?.addEventListener('click', function() {
            if (!hasAnswered) return;
            this.classList.toggle('active');
            $('#ai-explain-box').classList.toggle('show');
        });

        $('#prev-question')?.addEventListener('click', () => {
            if (questionIndex > 0) { 
                stopAudioPlayback();
                questionIndex--; 
                renderQuestion(); 
                renderQuestionGrid(); 
            }
        });
        
        $('#next-question')?.addEventListener('click', () => {
            if (questionIndex < currentQuestions.length - 1) {
                stopAudioPlayback();
                questionIndex++;
                renderQuestion();
                renderQuestionGrid();
            } else {
                finishExam();
            }
        });
        
        if (currentExamData && currentExamData.type === 'writing') {
            updateWritingWordCount();
        }
    }

    function chooseAnswer(choice) {
        if (userAnswers[questionIndex] !== null) return;
        userAnswers[questionIndex] = choice;
        if (choice === currentQuestions[questionIndex].answer) correctAnswers++;
        renderQuestion();
        renderQuestionGrid();
    }

    function finishExam() {
        clearInterval(examTimer);
        stopAudioPlayback();

        const courseConfig = courses.find(c => c.title === currentExamTitle) || { kind: 'TOEIC', skill: 'Reading' };
        const total = currentQuestions.length;
        const percentage = Math.round((correctAnswers / total) * 100);

        let scoreSummary = null;
        if (courseConfig.kind === 'TOEIC') {
            scoreSummary = calculateToeicScore(correctAnswers, total, courseConfig.skill);
        } else {
            scoreSummary = calculateIeltsBand(correctAnswers, total, courseConfig.skill);
        }

        const history = JSON.parse(localStorage.getItem('lingua-history') || '[]');
        const examRecord = {
            id: 'exam_' + Date.now(),
            title: currentExamTitle,
            kind: courseConfig.kind,
            skill: courseConfig.skill,
            date: new Date().toISOString(),
            score: percentage,
            scoreSummary: scoreSummary,
            correct: correctAnswers,
            total: total,
            timeSpent: (15 * 60) - timeLeft,
            questions: currentQuestions,
            userAnswers: [...userAnswers]
        };
        history.unshift(examRecord);
        localStorage.setItem('lingua-history', JSON.stringify(history.slice(0, 50)));

        $('#exam-content').innerHTML = `
          <div class="result" style="margin-top: 20px;">
             <div class="result-score" style="width:110px; height:110px; font-size:32px;">${percentage}%</div>
             <h2>${percentage >= 70 ? 'Xuất sắc! Kết quả rất ấn tượng 🌟' : 'Đã hoàn thành bài thi! Cố gắng luyện thêm nhé 💪'}</h2>
             
             <div class="result-score-card">
                <div class="result-score-box">
                   <small>QUY ĐỔI ${courseConfig.kind}</small>
                   <strong>${courseConfig.kind === 'TOEIC' ? scoreSummary.display : scoreSummary.display}</strong>
                </div>
                <div class="result-score-box">
                   <small>SỐ CÂU ĐÚNG</small>
                   <strong>${correctAnswers} / ${total}</strong>
                </div>
                <div class="result-score-box">
                   <small>THỜI GIAN LÀM</small>
                   <strong>${Math.floor(((15*60)-timeLeft)/60)}p ${((15*60)-timeLeft)%60}s</strong>
                </div>
             </div>

             <p style="color:var(--muted); font-size:13px; max-width:550px; margin:0 auto 20px;">
                Kết quả bài thi đã được lưu vào lịch sử học tập cá nhân theo thời gian thực. Bạn có thể xem lại chi tiết từng câu làm đúng / sai để rút kinh nghiệm.
             </p>

             <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
                <button class="primary" onclick="openReviewModalFromLatest()">Xem lại chi tiết bài làm 🔍</button>
                <button class="text-button" style="border:1px solid var(--line); border-radius:8px; padding:10px 16px;" onclick="closeExam()">Quay lại danh sách đề</button>
                <button class="text-button" style="border:1px solid var(--green); color:var(--green-dark); border-radius:8px; padding:10px 16px; font-weight:700;" onclick="closeExamAndGoHome()">🏠 Về trang chủ</button>
             </div>
          </div>
        `;

        updateScores();
        renderProfileView();
    }

    function closeExam() {
        clearInterval(examTimer);
        stopAudioPlayback();
        $('#exam-backdrop').classList.remove('open');
        document.body.style.overflow = '';
    }

    function closeExamAndGoHome() {
        closeExam();
        showView('overview');
    }

    function closeReviewModalAndGoHome() {
        closeReviewModal();
        showView('overview');
    }
'''

html = html[:idx_a1] + new_audio_and_exam_runtime + html[end_close_exam:]
print("Integrated Live Speech Synthesis, real-time speed selector, MediaRecorder mic, and go home handlers.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully.")
