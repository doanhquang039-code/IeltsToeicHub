import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

css_old = """.exam-modal { width: min(620px, 100%); max-height: min(740px, 94vh); overflow: auto; border-radius: 10px; padding: 24px; background: #fff; box-shadow: 0 24px 80px rgba(0,0,0,.2); animation: enter .2s ease both; }
    .modal-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; }"""

css_new = """.exam-modal { width: min(1000px, 95%); max-height: min(800px, 94vh); height: 94vh; display: flex; flex-direction: column; overflow: hidden; border-radius: 12px; padding: 24px; background: #fff; box-shadow: 0 24px 80px rgba(0,0,0,.2); animation: enter .2s ease both; }
    .modal-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 5px; }
    .exam-layout { display: flex; gap: 30px; flex: 1; min-height: 0; margin-top: 15px; }
    .exam-main { flex: 1; overflow-y: auto; padding-right: 10px; }
    .exam-sidebar { width: 280px; flex-shrink: 0; display: flex; flex-direction: column; gap: 20px; border-left: 1px solid var(--line); padding-left: 20px; }
    .question-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; }
    .q-btn { width: 100%; aspect-ratio: 1; display: grid; place-items: center; border-radius: 6px; border: 1px solid var(--line); background: #fff; font-size: 13px; font-weight: 600; color: var(--muted); cursor: pointer; transition: all .15s ease; }
    .q-btn:hover { border-color: var(--green); color: var(--green); }
    .q-btn.active { border-color: var(--green); background: #eaf2e4; color: var(--green); }
    .q-btn.answered { background: var(--green); border-color: var(--green); color: #fff; }
    .exam-timer { text-align: center; padding: 18px; background: #f8fbf7; border-radius: 10px; border: 1px solid var(--line); }
    .timer-clock { font-family: var(--display); font-size: 38px; font-weight: 700; color: var(--green); line-height: 1; margin-bottom: 8px; }
    .timer-label { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; font-weight: 700; }
    .tool-bar { display: flex; gap: 10px; margin-bottom: 20px; }
    .tool-btn { padding: 8px 14px; border-radius: 6px; border: 1px solid var(--line); background: #fff; font-size: 12px; font-weight: 600; cursor: pointer; color: var(--muted); transition: all .15s ease; display: flex; align-items: center; gap: 6px; }
    .tool-btn:hover { background: #f8fbf7; color: var(--green); border-color: #c8d8cc; }
    .tool-btn.active { background: #eaf2e4; color: var(--green); border-color: var(--green); }
    .translated-text { margin-bottom: 20px; font-size: 14px; color: #5c7063; background: #f5f8f3; padding: 14px 18px; border-radius: 8px; border-left: 3px solid var(--green); display: none; }
    .translated-text.show { display: block; }
    .ai-explain-box { margin-top: 20px; padding: 20px; background: #f4f7fe; border-radius: 10px; border: 1px solid #dce4f5; display: none; }
    .ai-explain-box.show { display: block; }
    .ai-explain-box h4 { margin: 0 0 12px; color: #3b5b9e; font-size: 14px; display: flex; align-items: center; gap: 8px; }
    .ai-explain-box p { margin: 0; color: #4a638c; font-size: 13.5px; line-height: 1.6; }
    .ai-icon { display: grid; width: 24px; height: 24px; place-items: center; background: #3b5b9e; color: #fff; border-radius: 50%; font-size: 12px; font-weight: 700; }
    .history-list { display: grid; gap: 10px; margin-top: 20px; }
    .history-item { display: flex; align-items: center; justify-content: space-between; padding: 15px; border: 1px solid var(--line); border-radius: 8px; background: #fff; }
    .history-info h4 { margin: 0 0 4px; font-size: 13px; }
    .history-info p { margin: 0; font-size: 11px; color: var(--muted); }
    .history-score { font-family: var(--display); font-size: 22px; font-weight: 700; color: var(--green); }"""
content = content.replace(css_old, css_new)

prog_old = """<section class="chart-panel"><h2>Thời gian học mỗi ngày</h2><div class="chart" aria-label="Biểu đồ thời gian học trong tuần"><div class="bar-wrap"><div class="bar" style="height:38%"></div><span>T2</span></div><div class="bar-wrap"><div class="bar" style="height:58%"></div><span>T3</span></div><div class="bar-wrap"><div class="bar" style="height:44%"></div><span>T4</span></div><div class="bar-wrap"><div class="bar" style="height:81%"></div><span>T5</span></div><div class="bar-wrap"><div class="bar" style="height:66%"></div><span>T6</span></div><div class="bar-wrap"><div class="bar" style="height:25%"></div><span>T7</span></div><div class="bar-wrap"><div class="bar" style="height:10%"></div><span>CN</span></div></div></section>
        </section>"""
prog_new = """<div class="content-grid" style="grid-template-columns: 1fr 1fr; gap: 20px;">
             <section class="chart-panel"><h2>Lịch sử điểm số</h2><div class="chart" id="score-chart" aria-label="Biểu đồ điểm số"></div></section>
             <section class="panel"><h2>Các bài thi gần đây</h2><div class="history-list" id="history-list"></div></section>
          </div>
        </section>"""
content = content.replace(prog_old, prog_new)

prog_stats_old = """<div class="progress-overview"><div class="big-stat"><span>Tổng thời gian học</span><strong>4 giờ 30 phút</strong></div><div class="big-stat"><span>Câu hỏi đã hoàn thành</span><strong id="progress-questions">128</strong></div><div class="big-stat"><span>Điểm trung bình</span><strong id="progress-average">76%</strong></div></div>"""
prog_stats_new = """<div class="progress-overview"><div class="big-stat"><span>Tổng bài đã làm</span><strong id="progress-exams">0</strong></div><div class="big-stat"><span>Câu hỏi đã hoàn thành</span><strong id="progress-questions">0</strong></div><div class="big-stat"><span>Điểm trung bình</span><strong id="progress-average">0%</strong></div></div>"""
content = content.replace(prog_stats_old, prog_stats_new)

modal_old = """<div class="modal-top"><div><div class="modal-label" id="exam-label">Bài luyện tập</div><div class="question-count" id="question-count"></div></div><button class="close-modal" id="close-modal" aria-label="Đóng bài thi">×</button></div>
      <div id="exam-content"></div>"""
modal_new = """<div class="modal-top"><div><div class="modal-label" id="exam-label">Bài luyện tập</div></div><button class="close-modal" id="close-modal" aria-label="Đóng bài thi">×</button></div>
      <div id="exam-content"></div>"""
content = content.replace(modal_old, modal_new)

questions_old = """const questions = [
      { text: 'The shipment is scheduled to arrive by Friday afternoon. What does “scheduled” mean?', choices: ['Expected or planned to happen at a particular time', 'Delayed until further notice', 'Already completed ahead of time', 'Cancelled by the recipient'], answer: 0, note: '“Scheduled” nghĩa là đã được lên lịch hoặc dự kiến vào một thời điểm.' },
      { text: 'Choose the best word: Please submit your expense report _____ the end of the month.', choices: ['by', 'during', 'while', 'between'], answer: 0, note: '“By the end of the month” nghĩa là trước hoặc không muộn hơn cuối tháng.' },
      { text: 'The new policy will take effect next quarter. What can be inferred?', choices: ['The policy starts next quarter.', 'The policy ended last quarter.', 'The policy is optional this week.', 'The policy has been cancelled.'], answer: 0, note: '“Take effect” nghĩa là bắt đầu có hiệu lực.' }
    ];"""
questions_new = """const questions = [
      { 
        text: 'The shipment is scheduled to arrive by Friday afternoon. What does “scheduled” mean?', 
        translated: 'Chuyến hàng được lên lịch sẽ đến vào chiều thứ Sáu. Từ "scheduled" có nghĩa là gì?',
        choices: ['Expected or planned to happen at a particular time', 'Delayed until further notice', 'Already completed ahead of time', 'Cancelled by the recipient'], 
        answer: 0, 
        ai_explain: 'Theo ngữ cảnh câu, "scheduled" (được lên lịch) chỉ một sự kiện đã được dự kiến hoặc lập kế hoạch sẽ xảy ra vào một thời điểm cụ thể (chiều thứ Sáu). Vì vậy, đáp án A là chính xác nhất. Các đáp án khác mang nghĩa trì hoãn, hoàn thành sớm, hoặc hủy bỏ đều không phù hợp.' 
      },
      { 
        text: 'Choose the best word: Please submit your expense report _____ the end of the month.', 
        translated: 'Chọn từ đúng nhất: Vui lòng nộp báo cáo chi phí của bạn _____ cuối tháng.',
        choices: ['by', 'during', 'while', 'between'], 
        answer: 0, 
        ai_explain: 'Giới từ "by" + mốc thời gian có nghĩa là "trước hoặc vào lúc" (không muộn hơn). "By the end of the month" nghĩa là trước hoặc đúng vào cuối tháng. "During" và "while" dùng cho khoảng thời gian, "between" cần hai mốc thời gian.' 
      },
      { 
        text: 'The new policy will take effect next quarter. What can be inferred?', 
        translated: 'Chính sách mới sẽ có hiệu lực vào quý tới. Có thể suy luận điều gì?',
        choices: ['The policy starts next quarter.', 'The policy ended last quarter.', 'The policy is optional this week.', 'The policy has been cancelled.'], 
        answer: 0, 
        ai_explain: 'Cụm từ "take effect" có nghĩa là "bắt đầu có hiệu lực" hoặc "bắt đầu được áp dụng". Do đó, câu này báo hiệu rằng chính sách sẽ bắt đầu (starts) vào quý tiếp theo (next quarter).' 
      },
      { 
        text: 'All employees are required to attend the safety workshop _____ they have already completed it this year.', 
        translated: 'Tất cả nhân viên được yêu cầu tham dự hội thảo an toàn _____ họ đã hoàn thành nó trong năm nay.',
        choices: ['unless', 'if', 'because', 'so that'], 
        answer: 0, 
        ai_explain: '"Unless" mang nghĩa "trừ khi". Câu này dịch là: Tất cả nhân viên phải tham dự, TRỪ KHI họ đã hoàn thành nó trong năm nay. Phù hợp nhất về mặt ngữ nghĩa.' 
      },
      { 
        text: 'The CEO expressed her _____ for the team\\'s hard work on the successful project.', 
        translated: 'CEO bày tỏ sự _____ của cô ấy đối với sự làm việc chăm chỉ của đội ngũ trong dự án thành công.',
        choices: ['appreciation', 'appreciate', 'appreciative', 'appreciatively'], 
        answer: 0, 
        ai_explain: 'Sau tính từ sở hữu "her" cần một danh từ. "Appreciation" (sự trân trọng/biết ơn) là danh từ duy nhất trong các lựa chọn. "Appreciate" là động từ, "appreciative" là tính từ.' 
      }
    ];"""
content = content.replace(questions_old, questions_new)

js_old = """    let questionIndex = 0;
    let correctAnswers = 0;
    let answered = false;"""
js_new = """    let questionIndex = 0;
    let correctAnswers = 0;
    let userAnswers = [];
    let examTimer = null;
    let timeLeft = 0;"""
content = content.replace(js_old, js_new)

js_logic_old = """    function openExam(title) {
      questionIndex = 0;
      correctAnswers = 0;
      answered = false;
      $('#exam-label').textContent = title;
      $('#exam-backdrop').classList.add('open');
      document.body.style.overflow = 'hidden';
      renderQuestion();
      $('#close-modal').focus();
    }
    function renderQuestion() {
      const item = questions[questionIndex];
      $('#question-count').textContent = `Câu ${questionIndex + 1} / ${questions.length}`;
      $('#exam-content').innerHTML = `<div class="question-text" id="exam-title">${item.text}</div><div class="options">${item.choices.map((choice, index) => `<button class="option" data-choice="${index}"><span class="letter">${String.fromCharCode(65 + index)}</span><span>${choice}</span></button>`).join('')}</div><div class="feedback" id="feedback" aria-live="polite"></div><div class="modal-footer"><span>Chọn một đáp án</span><button class="primary" id="next-question" disabled>${questionIndex === questions.length - 1 ? 'Xem kết quả' : 'Câu tiếp theo →'}</button></div>`;
      $$('.option').forEach(button => button.addEventListener('click', () => chooseAnswer(Number(button.dataset.choice))));
      $('#next-question').addEventListener('click', advanceQuestion);
    }
    function chooseAnswer(choice) {
      if (answered) return;
      answered = true;
      const item = questions[questionIndex];
      $$('.option').forEach((button, index) => {
        button.disabled = true;
        if (index === item.answer) button.classList.add('correct');
        else if (index === choice) button.classList.add('wrong');
      });
      if (choice === item.answer) correctAnswers++;
      $('#feedback').textContent = `${choice === item.answer ? 'Chính xác!' : 'Chưa đúng.'} ${item.note}`;
      $('#next-question').disabled = false;
      $('#next-question').focus();
    }
    function advanceQuestion() {
      if (!answered) return;
      questionIndex++;
      answered = false;
      if (questionIndex < questions.length) return renderQuestion();
      const percentage = Math.round(correctAnswers / questions.length * 100);
      $('#question-count').textContent = 'Hoàn thành bài luyện';
      $('#exam-content').innerHTML = `<div class="result"><div class="result-score">${percentage}%</div><h2>${percentage >= 67 ? 'Làm tốt lắm!' : 'Cứ luyện thêm nhé!'}</h2><p>Bạn trả lời đúng ${correctAnswers}/${questions.length} câu. Kết quả đã được lưu vào tiến độ học.</p><button class="primary" id="finish-exam">Quay lại học</button></div>`;
      const previous = Number(localStorage.getItem('lingua-questions') || 128);
      const scores = JSON.parse(localStorage.getItem('lingua-scores') || '[76]');
      scores.push(percentage);
      localStorage.setItem('lingua-questions', String(previous + questions.length));
      localStorage.setItem('lingua-scores', JSON.stringify(scores.slice(-10)));
      updateScores();
      $('#finish-exam').addEventListener('click', closeExam);
    }
    function closeExam() {
      $('#exam-backdrop').classList.remove('open');
      document.body.style.overflow = '';
    }
    function updateScores() {
      const total = Number(localStorage.getItem('lingua-questions') || 128);
      const scores = JSON.parse(localStorage.getItem('lingua-scores') || '[76]');
      const average = Math.round(scores.reduce((sum, value) => sum + value, 0) / scores.length);
      $('#question-total').innerHTML = `${total} <small>câu</small>`;
      $('#average-score').innerHTML = `${average}<small>%</small>`;
      $('#progress-questions').textContent = total;
      $('#progress-average').textContent = `${average}%`;
    }"""
js_logic_new = """    function startTimer(minutes) {
        timeLeft = minutes * 60;
        clearInterval(examTimer);
        updateTimerDisplay();
        examTimer = setInterval(() => {
            timeLeft--;
            updateTimerDisplay();
            if (timeLeft <= 0) {
                clearInterval(examTimer);
                finishExam();
            }
        }, 1000);
    }
    function updateTimerDisplay() {
        const m = Math.floor(timeLeft / 60);
        const s = timeLeft % 60;
        const clock = $('#timer-clock');
        if (clock) clock.textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }
    function openExam(title) {
      questionIndex = 0;
      correctAnswers = 0;
      userAnswers = new Array(questions.length).fill(null);
      $('#exam-label').textContent = title;
      $('#exam-backdrop').classList.add('open');
      document.body.style.overflow = 'hidden';
      
      $('#exam-content').innerHTML = `
        <div class="exam-layout">
           <div class="exam-main" id="exam-main-area"></div>
           <div class="exam-sidebar">
              <div class="exam-timer">
                 <div class="timer-clock" id="timer-clock">15:00</div>
                 <div class="timer-label">Thời gian còn lại</div>
              </div>
              <div style="margin-top: 10px;">
                 <div style="font-size: 11px; font-weight: 700; color: var(--muted); margin-bottom: 12px; text-transform: uppercase; letter-spacing: .5px;">Danh sách câu hỏi</div>
                 <div class="question-grid" id="question-grid"></div>
              </div>
              <button class="primary" style="margin-top: auto; padding: 12px; text-align: center; justify-content: center; width: 100%; display: flex;" id="submit-exam-btn">Nộp bài sớm</button>
           </div>
        </div>
      `;
      
      renderQuestionGrid();
      renderQuestion();
      startTimer(15);
      
      $('#submit-exam-btn').addEventListener('click', finishExam);
      $('#close-modal').focus();
    }
    
    function renderQuestionGrid() {
        const grid = $('#question-grid');
        grid.innerHTML = questions.map((_, i) => `<button class="q-btn ${i === questionIndex ? 'active' : ''} ${userAnswers[i] !== null ? 'answered' : ''}" data-qindex="${i}">${i + 1}</button>`).join('');
        $$('.q-btn').forEach(btn => btn.addEventListener('click', () => {
            questionIndex = Number(btn.dataset.qindex);
            renderQuestion();
            renderQuestionGrid();
        }));
    }

    function renderQuestion() {
      const item = questions[questionIndex];
      const hasAnswered = userAnswers[questionIndex] !== null;
      const uAns = userAnswers[questionIndex];
      
      let html = `
        <div class="tool-bar">
           <button class="tool-btn" id="btn-translate"><span>文A</span> Dịch câu hỏi</button>
           <button class="tool-btn" id="btn-ai-explain" ${!hasAnswered ? 'disabled style="opacity:0.6;cursor:not-allowed;" title="Trả lời câu hỏi để xem giải thích"' : ''}><span>✨</span> Giải thích AI</button>
        </div>
        <div class="question-count">Câu ${questionIndex + 1} / ${questions.length}</div>
        <div class="question-text">${item.text}</div>
        <div class="translated-text" id="translated-text">${item.translated}</div>
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
        
        <div class="ai-explain-box" id="ai-explain-box">
           <h4><span class="ai-icon">✨</span> Phân tích từ AI</h4>
           <p>${item.ai_explain}</p>
        </div>
        
        <div class="modal-footer" style="margin-top: 30px; border-top: 1px solid var(--line); padding-top: 20px;">
           <button class="text-button" id="prev-question" ${questionIndex === 0 ? 'style="opacity:0; pointer-events:none;"' : ''}>← Câu trước</button>
           <button class="primary" id="next-question">${questionIndex === questions.length - 1 ? (hasAnswered ? 'Xem kết quả' : 'Nộp bài') : 'Câu tiếp theo →'}</button>
        </div>
      `;
      $('#exam-main-area').innerHTML = html;
      
      $$('.option:not([disabled])').forEach(button => button.addEventListener('click', () => chooseAnswer(Number(button.dataset.choice))));
      
      $('#btn-translate').addEventListener('click', function() {
          this.classList.toggle('active');
          $('#translated-text').classList.toggle('show');
      });
      
      $('#btn-ai-explain').addEventListener('click', function() {
          if (!hasAnswered) return;
          this.classList.toggle('active');
          $('#ai-explain-box').classList.toggle('show');
      });
      
      $('#prev-question')?.addEventListener('click', () => {
          if (questionIndex > 0) { questionIndex--; renderQuestion(); renderQuestionGrid(); }
      });
      
      $('#next-question').addEventListener('click', () => {
          if (questionIndex < questions.length - 1) {
              questionIndex++;
              renderQuestion();
              renderQuestionGrid();
          } else {
              finishExam();
          }
      });
    }

    function chooseAnswer(choice) {
      if (userAnswers[questionIndex] !== null) return;
      userAnswers[questionIndex] = choice;
      if (choice === questions[questionIndex].answer) correctAnswers++;
      renderQuestion();
      renderQuestionGrid();
    }

    function finishExam() {
      clearInterval(examTimer);
      const percentage = Math.round(correctAnswers / questions.length * 100);
      
      const history = JSON.parse(localStorage.getItem('lingua-history') || '[]');
      history.unshift({
         title: $('#exam-label').textContent,
         date: new Date().toISOString(),
         score: percentage,
         correct: correctAnswers,
         total: questions.length,
         timeSpent: (15 * 60) - timeLeft
      });
      localStorage.setItem('lingua-history', JSON.stringify(history.slice(0, 50)));
      
      $('#exam-content').innerHTML = `<div class="result" style="margin-top: 40px;"><div class="result-score">${percentage}%</div><h2>${percentage >= 67 ? 'Làm tốt lắm!' : 'Cứ luyện thêm nhé!'}</h2><p>Bạn trả lời đúng ${correctAnswers}/${questions.length} câu. Kết quả đã được lưu vào tiến độ học.</p><button class="primary" id="finish-exam">Quay lại học</button></div>`;
      
      updateScores();
      $('#finish-exam').addEventListener('click', closeExam);
    }

    function closeExam() {
      clearInterval(examTimer);
      $('#exam-backdrop').classList.remove('open');
      document.body.style.overflow = '';
    }

    function updateScores() {
      const history = JSON.parse(localStorage.getItem('lingua-history') || '[]');
      
      if (history.length === 0) {
         const pastDate = new Date();
         pastDate.setDate(pastDate.getDate() - 1);
         history.push({
            title: 'TOEIC Reading · Part 5',
            date: pastDate.toISOString(),
            score: 75,
            correct: 9,
            total: 12,
            timeSpent: 420
         });
         localStorage.setItem('lingua-history', JSON.stringify(history));
      }
      
      const totalExams = history.length;
      const totalQuestions = history.reduce((sum, item) => sum + item.total, 0);
      const totalCorrect = history.reduce((sum, item) => sum + item.correct, 0);
      const average = totalQuestions > 0 ? Math.round((totalCorrect / totalQuestions) * 100) : 0;
      
      $('#progress-exams').textContent = totalExams;
      $('#progress-questions').textContent = totalQuestions;
      $('#progress-average').textContent = `${average}%`;
      
      $('#question-total').innerHTML = `${totalQuestions} <small>câu</small>`;
      $('#average-score').innerHTML = `${average}<small>%</small>`;
      
      const list = $('#history-list');
      if (list) {
          list.innerHTML = history.slice(0, 5).map(item => {
              const d = new Date(item.date);
              const dateStr = `${d.getDate()}/${d.getMonth()+1}/${d.getFullYear()} ${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`;
              const m = Math.floor(item.timeSpent / 60);
              const s = item.timeSpent % 60;
              return `<div class="history-item">
                 <div class="history-info">
                    <h4>${item.title}</h4>
                    <p>${dateStr} · Thời gian: ${m}p ${s}s</p>
                 </div>
                 <div class="history-score">${item.score}%</div>
              </div>`;
          }).join('');
      }
      
      const chart = $('#score-chart');
      if (chart) {
          const recent = history.slice(0, 7).reverse();
          chart.innerHTML = recent.map((item, i) => `
            <div class="bar-wrap" style="align-items: center; justify-content: flex-end; display: flex; flex-direction: column; height: 100%; gap: 7px;">
               <div class="bar" style="height:${Math.max(item.score, 5)}%; background: ${item.score >= 80 ? 'var(--green)' : (item.score >= 50 ? '#94bd6f' : 'var(--coral)')}; width: 100%;"></div>
               <span>#${i+1}</span>
            </div>
          `).join('');
      }
    }"""
content = content.replace(js_logic_old, js_logic_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Update complete")
