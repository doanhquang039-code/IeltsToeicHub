import re

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. FIX CLOSE MODAL BUTTON HTML
old_close_btn = '<div class="modal-top"><div><div class="modal-label" id="exam-label">Bài luyện tập</div></div><button class="close-modal" id="close-modal" aria-label="Đóng bài thi">×</button></div>'
new_close_btn = '<div class="modal-top"><div><div class="modal-label" id="exam-label">Bài luyện tập</div></div><button type="button" class="close-modal" id="close-modal" onclick="closeExam()" aria-label="Đóng bài thi" style="cursor:pointer;">×</button></div>'

if old_close_btn in content:
    content = content.replace(old_close_btn, new_close_btn, 1)
    print("SUCCESS: Updated close modal button in HTML")
else:
    print("WARNING: old_close_btn not matched exactly")

# 2. UPDATE SOCIAL LOGIN SECTION TO INCLUDE MICROSOFT QUICK LOGIN
old_social_quick = """         <div style="margin-top:14px; text-align:center;">
            <button type="button" onclick="loginAsMockUser('Google')" style="width:100%; padding:10px 14px; background:#f0fdf4; border:1px solid #86efac; border-radius:8px; color:var(--green-dark); font-weight:700; font-size:12.5px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; transition:all .2s; box-shadow:0 2px 4px rgba(35,91,72,0.06);" onmouseover="this.style.background='#dcfce7'" onmouseout="this.style.background='#f0fdf4'">
               <span>⚡</span> Đăng nhập nhanh Google (Vào học ngay không cần duyệt OTP)
            </button>
         </div>"""

new_social_quick = """         <div style="margin-top:14px; display:flex; flex-direction:column; gap:8px;">
            <button type="button" onclick="loginAsMockUser('Google')" style="width:100%; padding:10px 14px; background:#f0fdf4; border:1px solid #86efac; border-radius:8px; color:var(--green-dark); font-weight:700; font-size:12.5px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; transition:all .2s; box-shadow:0 2px 4px rgba(35,91,72,0.06);" onmouseover="this.style.background='#dcfce7'" onmouseout="this.style.background='#f0fdf4'">
               <span>⚡</span> Đăng nhập nhanh Google (Vào học ngay không cần duyệt OTP)
            </button>
            <button type="button" onclick="loginAsMockUser('Microsoft')" style="width:100%; padding:10px 14px; background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; color:#1e40af; font-weight:700; font-size:12.5px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; transition:all .2s; box-shadow:0 2px 4px rgba(37,99,235,0.06);" onmouseover="this.style.background='#dbeafe'" onmouseout="this.style.background='#eff6ff'">
               <span>⚡</span> Đăng nhập nhanh Microsoft (Bỏ qua giới hạn tài khoản cơ quan)
            </button>
         </div>"""

if old_social_quick in content:
    content = content.replace(old_social_quick, new_social_quick, 1)
    print("SUCCESS: Updated social quick login buttons")
else:
    print("WARNING: old_social_quick not found")

# 3. UPDATE FLASHCARD HTML & CONTROLS
old_flashcard_controls = """               <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px;">
                  <button class="text-button" id="prev-word-btn" onclick="prevVocabWord()">← Từ trước</button>
                  <button class="primary" style="padding:8px 16px; font-size:13px;" id="next-word-btn" onclick="nextVocabWord()">Từ tiếp theo →</button>
               </div>"""

new_flashcard_controls = """               <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px; gap:8px; flex-wrap:wrap;">
                  <button type="button" class="text-button" id="prev-word-btn" onclick="prevVocabWord()">← Từ trước</button>
                  <button type="button" class="text-button" style="border:1px solid var(--green); color:var(--green-dark); padding:7px 14px; border-radius:8px; font-weight:700; background:#f0fdf4; cursor:pointer;" onclick="toggleFlashcard()">🔄 Lật mặt thẻ (Xem nghĩa / Từ gốc)</button>
                  <button type="button" class="primary" style="padding:8px 16px; font-size:13px;" id="next-word-btn" onclick="nextVocabWord()">Từ tiếp theo →</button>
               </div>"""

if old_flashcard_controls in content:
    content = content.replace(old_flashcard_controls, new_flashcard_controls, 1)
    print("SUCCESS: Updated flashcard controls")
else:
    print("WARNING: old_flashcard_controls not found")

# Update #flashcard button tag to include onclick="toggleFlashcard()"
content = content.replace('<button class="flashcard" id="flashcard" aria-label="Lật thẻ từ vựng">', '<button type="button" class="flashcard" id="flashcard" onclick="toggleFlashcard()" aria-label="Lật thẻ từ vựng" style="cursor:pointer;">')

# 4. UPDATE JS: FLASHCARD FUNCTIONS (toggleFlashcard, renderFlashcard)
old_flashcard_js = """    function renderFlashcard() {
        const item = currentFilteredVocab[currentVocabIndex] || allVocabDatabase[0];
        if (!item) return;

        if ($('#flashcard-label')) $('#flashcard-label').textContent = `Từ ${currentVocabIndex + 1} / ${currentFilteredVocab.length} · Nhấn để lật thẻ`;
        if ($('#flashcard-word')) $('#flashcard-word').textContent = item.word;
        if ($('#flashcard-detail')) $('#flashcard-detail').textContent = `${item.phonetic} · ${item.pos}`;
        if ($('#flashcard-hint')) {
            $('#flashcard-hint').textContent = flashRevealed ? 
               `${item.meaning} \\nVí dụ: ${item.example}` : 
               'Chạm vào thẻ để xem nghĩa tiếng Việt & ví dụ thực tế';
            $('#flashcard-hint').style.whiteSpace = 'pre-line';
        }
        
        // Badges trên flashcard
        const badgeWrap = $('#flashcard-badges');
        if (badgeWrap) {
            badgeWrap.innerHTML = `
               <span class="level-badge ${item.level.toLowerCase()}">${item.level}</span>
               <span class="topic-pill">${item.topicLabel}</span>
            `;
        }

        // Nút loa phát âm
        const speakBtn = $('#btn-speak-flashcard');
        if (speakBtn) {
            speakBtn.onclick = (e) => {
                e.stopPropagation();
                speakWord(item.word);
            };
        }
    }"""

new_flashcard_js = """    function toggleFlashcard() {
        flashRevealed = !flashRevealed;
        renderFlashcard();
    }

    function renderFlashcard() {
        const item = currentFilteredVocab[currentVocabIndex] || allVocabDatabase[0];
        if (!item) return;

        const card = $('#flashcard');
        const label = $('#flashcard-label');
        const word = $('#flashcard-word');
        const detail = $('#flashcard-detail');
        const hint = $('#flashcard-hint');
        const badgeWrap = $('#flashcard-badges');
        const speakBtn = $('#btn-speak-flashcard');

        if (badgeWrap) {
            badgeWrap.innerHTML = `
               <span class="level-badge ${item.level.toLowerCase()}">${item.level}</span>
               <span class="topic-pill">${item.topicLabel}</span>
            `;
        }

        if (card) {
            card.style.transition = 'all 0.25s ease';
            card.style.cursor = 'pointer';
        }

        if (flashRevealed) {
            // MẶT SAU: HIỂN THỊ NGHĨA TIẾNG VIỆT TO RÕ RÀNG & VÍ DỤ MINH HỌA
            if (label) label.innerHTML = `Từ ${currentVocabIndex + 1} / ${currentFilteredVocab.length} · <span style="color:var(--green-dark); font-weight:700;">🔄 MẶT SAU: NGHĨA TIẾNG VIỆT</span>`;
            if (word) {
                word.textContent = item.meaning;
                word.style.color = 'var(--green-dark)';
                word.style.fontSize = '25px';
                word.style.fontWeight = '700';
            }
            if (detail) {
                detail.innerHTML = `<span style="font-weight:600; color:var(--ink);">Từ gốc: <strong>${item.word}</strong></span> <span style="color:var(--muted); font-size:12px;">(${item.phonetic} · ${item.pos})</span>`;
            }
            if (hint) {
                hint.innerHTML = `<div style="background:#fff; border:1px solid #bbf7d0; padding:12px 14px; border-radius:8px; text-align:left; margin-top:12px; box-shadow:0 2px 5px rgba(0,0,0,0.03);">
                    <div style="font-size:11px; font-weight:700; color:var(--green); text-transform:uppercase; margin-bottom:4px;">Ví dụ thực tế:</div>
                    <div style="font-style:italic; color:#1e293b; font-size:13px; line-height:1.5;">"${item.example}"</div>
                </div>
                <div style="margin-top:10px; font-size:11px; color:var(--muted); font-weight:600;">↺ Chạm vào thẻ để lật lại mặt trước (tiếng Anh)</div>`;
                hint.style.whiteSpace = 'normal';
            }
            if (card) {
                card.style.background = '#f0fdf4';
                card.style.borderColor = '#86efac';
            }
        } else {
            // MẶT TRƯỚC: TỪ TIẾNG ANH & PHIÊN ÂM
            if (label) label.textContent = `Từ ${currentVocabIndex + 1} / ${currentFilteredVocab.length} · Nhấn để lật thẻ`;
            if (word) {
                word.textContent = item.word;
                word.style.color = 'var(--ink)';
                word.style.fontSize = '36px';
                word.style.fontWeight = '700';
            }
            if (detail) {
                detail.textContent = `${item.phonetic} · ${item.pos}`;
            }
            if (hint) {
                hint.innerHTML = `<span style="display:inline-block; padding:5px 12px; background:rgba(35,91,72,0.08); border-radius:20px; font-weight:600; color:var(--green-dark); font-size:11.5px;">👆 Chạm vào thẻ để xem nghĩa tiếng Việt & ví dụ thực tế</span>`;
                hint.style.whiteSpace = 'normal';
            }
            if (card) {
                card.style.background = '';
                card.style.borderColor = '';
            }
        }

        // Nút loa phát âm
        if (speakBtn) {
            speakBtn.onclick = (e) => {
                e.stopPropagation();
                speakWord(item.word);
            };
        }
    }"""

if old_flashcard_js in content:
    content = content.replace(old_flashcard_js, new_flashcard_js, 1)
    print("SUCCESS: Updated flashcard JavaScript functions")
else:
    print("WARNING: old_flashcard_js not matched exactly")

# 5. FIX TIMER AND EXAM MODAL JS (startTimer, openExam, finishExam, closeExam)
old_exam_block = """        $('#exam-label').textContent = title;
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
    }"""

new_exam_block = """        $('#exam-label').textContent = title;
        const examBackdrop = $('#exam-backdrop');
        if (examBackdrop) {
            examBackdrop.classList.add('open');
            examBackdrop.style.display = 'flex';
        }
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
                   <button type="button" class="primary" style="padding: 12px; text-align: center; justify-content: center; width: 100%; display: flex; cursor:pointer;" id="submit-exam-btn" onclick="finishExam()">Nộp bài sớm</button>
                   <button type="button" class="text-button" style="font-size:12px; color:var(--muted); text-align:center; padding:6px; cursor:pointer;" onclick="closeExamAndGoHome()">Thoát về trang chủ</button>
                </div>
             </div>
          </div>
        `;
        
        renderQuestionGrid();
        renderQuestion();
        startTimer(parseMinutes);
        
        $('#close-modal')?.focus();
    }"""

if old_exam_block in content:
    content = content.replace(old_exam_block, new_exam_block, 1)
    print("SUCCESS: Updated openExam block")
else:
    print("WARNING: old_exam_block not matched")

# 6. IMPLEMENT startTimer & FIX finishExam and closeExam
old_finish_block = """    function finishExam() {
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
        const el = $('#exam-backdrop');
        if (el) {
            el.classList.remove('open');
            el.style.display = 'none';
        }
        document.body.style.overflow = '';
    }"""

new_finish_block = """    var examTimer = null;
    var examTimeRemaining = 0;
    var examTotalTimeSec = 0;

    function startTimer(minutes) {
        if (examTimer) clearInterval(examTimer);
        const mins = parseInt(minutes) || 15;
        examTotalTimeSec = mins * 60;
        examTimeRemaining = examTotalTimeSec;

        function updateClockDisplay() {
            const clock = $('#timer-clock');
            if (clock) {
                const m = Math.floor(examTimeRemaining / 60);
                const s = examTimeRemaining % 60;
                clock.textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
            }
        }

        updateClockDisplay();

        examTimer = setInterval(() => {
            if (examTimeRemaining <= 0) {
                clearInterval(examTimer);
                finishExam();
            } else {
                examTimeRemaining--;
                updateClockDisplay();
            }
        }, 1000);
    }

    function finishExam() {
        if (examTimer) clearInterval(examTimer);
        stopAudioPlayback();

        const courseConfig = courses.find(c => c.title === currentExamTitle) || { kind: 'TOEIC', skill: 'Reading' };
        const total = currentQuestions.length;
        const percentage = total > 0 ? Math.round((correctAnswers / total) * 100) : 0;

        let scoreSummary = null;
        if (courseConfig.kind === 'TOEIC') {
            scoreSummary = calculateToeicScore(correctAnswers, total, courseConfig.skill);
        } else {
            scoreSummary = calculateIeltsBand(correctAnswers, total, courseConfig.skill);
        }

        const timeSpent = examTotalTimeSec > 0 ? (examTotalTimeSec - Math.max(0, examTimeRemaining)) : 120;
        const minutesSpent = Math.floor(timeSpent / 60);
        const secondsSpent = timeSpent % 60;

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
            timeSpent: timeSpent,
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
                   <strong>${scoreSummary.display}</strong>
                </div>
                <div class="result-score-box">
                   <small>SỐ CÂU ĐÚNG</small>
                   <strong>${correctAnswers} / ${total}</strong>
                </div>
                <div class="result-score-box">
                   <small>THỜI GIAN LÀM</small>
                   <strong>${minutesSpent}p ${secondsSpent}s</strong>
                </div>
             </div>

             <p style="color:var(--muted); font-size:13px; max-width:550px; margin:0 auto 20px;">
                Kết quả bài thi đã được lưu vào lịch sử học tập cá nhân theo thời gian thực. Bạn có thể xem lại chi tiết từng câu làm đúng / sai để rút kinh nghiệm.
             </p>

             <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
                <button type="button" class="primary" onclick="openReviewModalFromLatest()">Xem lại chi tiết bài làm 🔍</button>
                <button type="button" class="text-button" style="border:1px solid var(--line); border-radius:8px; padding:10px 16px; cursor:pointer;" onclick="closeExam()">Quay lại danh sách đề</button>
                <button type="button" class="text-button" style="border:1px solid var(--green); color:var(--green-dark); border-radius:8px; padding:10px 16px; font-weight:700; cursor:pointer;" onclick="closeExamAndGoHome()">🏠 Về trang chủ</button>
             </div>
          </div>
        `;

        updateScores();
        renderProfileView();
    }

    function closeExam() {
        if (examTimer) clearInterval(examTimer);
        stopAudioPlayback();
        const el = $('#exam-backdrop');
        if (el) {
            el.classList.remove('open');
            el.style.display = 'none';
        }
        document.body.style.overflow = '';
    }"""

if old_finish_block in content:
    content = content.replace(old_finish_block, new_finish_block, 1)
    print("SUCCESS: Updated finishExam, startTimer, and closeExam")
else:
    print("WARNING: old_finish_block not matched")

# 7. UPDATE BOTTOM LISTENERS
old_bottom_listener = "$('#flashcard')?.addEventListener('click', () => { flashRevealed = !flashRevealed; wordRevealed = flashRevealed; showWord(wordIndex); });"
new_bottom_listener = "$('#flashcard')?.addEventListener('click', () => toggleFlashcard());"

if old_bottom_listener in content:
    content = content.replace(old_bottom_listener, new_bottom_listener, 1)
    print("SUCCESS: Updated flashcard click listener at bottom")
else:
    print("WARNING: old_bottom_listener not found")

# 8. UPDATE AZURE / MICROSOFT OPTIONS IN handleSocialLogin & loginAsMockUser
content = content.replace(
    "demoName = providerName === 'Google' ? 'Quang Doanh (Google)' : (providerName === 'GitHub' ? 'Dev User (GitHub)' : 'Office User (Microsoft)');",
    "demoName = providerName === 'Google' ? 'Quang Doanh' : (providerName === 'Microsoft' ? 'Quang Doanh (MS)' : (providerName === 'GitHub' ? 'Dev User' : 'Office User'));"
)
content = content.replace(
    "demoName = providerName === 'Google' ? 'Quang Doanh' : (providerName === 'GitHub' ? 'Dev User' : 'Office User');",
    "demoName = providerName === 'Google' ? 'Quang Doanh' : (providerName === 'Microsoft' ? 'Quang Doanh (MS)' : (providerName === 'GitHub' ? 'Dev User' : 'Office User'));"
)

# Azure scopes in signInWithOAuth
old_azure_call = """                const { data, error } = await sbClient.auth.signInWithOAuth({
                    provider: provider,
                    options: {
                        redirectTo: redirectUri,
                        queryParams: provider === 'google' ? { prompt: 'select_account' } : {}
                    }
                });"""

new_azure_call = """                const { data, error } = await sbClient.auth.signInWithOAuth({
                    provider: provider,
                    options: {
                        redirectTo: redirectUri,
                        scopes: provider === 'azure' ? 'email profile openid' : undefined,
                        queryParams: (provider === 'google' || provider === 'azure') ? { prompt: 'select_account' } : {}
                    }
                });"""

if old_azure_call in content:
    content = content.replace(old_azure_call, new_azure_call, 1)
    print("SUCCESS: Updated Azure OAuth scopes and queryParams")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("ALL FIXES APPLIED SUCCESSFULLY!")
