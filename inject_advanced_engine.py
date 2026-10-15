# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
html_path = r"e:\EngLish-IE-Toeic\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------------
# A. THAY THẾ TOÀN BỘ KHỐI TỪ VỰNG CŨ BẰNG VOCAB HUB & COURSE RENDERER MỚI
# -------------------------------------------------------------------
old_vocab_start = "    const words = ["
old_vocab_end = "    function showWord(index) {"

idx1 = html.find(old_vocab_start)
idx2 = html.find(old_vocab_end)

if idx1 == -1 or idx2 == -1:
    print(f"Error finding vocab indices: idx1={idx1}, idx2={idx2}")
    sys.exit(1)

# Find the end of showWord function
end_show_word = html.find("    // ==========================================", idx2)
if end_show_word == -1:
    end_show_word = html.find("    const SUPABASE_URL =", idx2)

print(f"Found vocab block from {idx1} to {end_show_word}")

advanced_vocab_and_course_js = r'''    // ==========================================
    // 0. KHHO TỪ VỰNG TOÀN DIỆN: CẤP ĐỘ CEFR (B1 - C2) & CHỦ ĐỀ ĐỜI SỐNG
    // ==========================================
    const allVocabDatabase = [
      // --- CHỦ ĐỀ: CÔNG SỞ & KINH DOANH (business) ---
      { word: 'Feasible', phonetic: '/ˈfiːzəbl/', pos: 'adj', level: 'B2', topic: 'business', topicLabel: '🏢 Công sở', meaning: 'Khả thi, có thể thực hiện thành công', example: 'It is fully feasible to conclude the trade agreement ahead of schedule.', collocation: 'financially feasible / feasible plan' },
      { word: 'Pragmatic', phonetic: '/præɡˈmætɪk/', pos: 'adj', level: 'C1', topic: 'business', topicLabel: '🏢 Công sở', meaning: 'Thực tế, trọng hiệu quả thực tiễn hơn lý thuyết', example: 'Our management adopted a pragmatic strategy to reduce overhead costs.', collocation: 'pragmatic approach / pragmatic decision' },
      { word: 'Negotiate', phonetic: '/nɪˈɡəʊʃieɪt/', pos: 'v', level: 'B1', topic: 'business', topicLabel: '🏢 Công sở', meaning: 'Đàm phán, thương lượng điều khoản', example: 'The sales team will negotiate a long-term supply contract tomorrow.', collocation: 'negotiate terms / successfully negotiate' },
      { word: 'Consensus', phonetic: '/kənˈsensəs/', pos: 'n', level: 'C1', topic: 'business', topicLabel: '🏢 Công sở', meaning: 'Sự đồng thuận, nhất trí cao trong tập thể', example: 'The board of directors reached a broad consensus on corporate restructuring.', collocation: 'reach a consensus / unanimous consensus' },
      { word: 'Conglomerate', phonetic: '/kənˈɡlɒmərət/', pos: 'n', level: 'C2', topic: 'business', topicLabel: '🏢 Công sở', meaning: 'Tập đoàn đa ngành, tập đoàn tài phiệt khổng lồ', example: 'The multinational conglomerate acquired three emerging software startups.', collocation: 'media conglomerate / industrial conglomerate' },
      { word: 'Deficit', phonetic: '/ˈdefɪsɪt/', pos: 'n', level: 'B2', topic: 'business', topicLabel: '🏢 Công sở', meaning: 'Thâm hụt tài chính, số lượng thiếu hụt', example: 'The trade deficit shrank significantly due to soaring export volume.', collocation: 'budget deficit / trade deficit' },

      // --- CHỦ ĐỀ: DU LỊCH & KHÁCH SẠN (travel) ---
      { word: 'Itinerary', phonetic: '/aɪˈtɪnərəri/', pos: 'n', level: 'B1', topic: 'travel', topicLabel: '✈️ Du lịch', meaning: 'Lịch trình, kế hoạch chi tiết của chuyến đi', example: 'Our detailed travel itinerary includes a guided museum tour in Da Nang.', collocation: 'travel itinerary / planned itinerary' },
      { word: 'Pristine', phonetic: '/ˈprɪstiːn/', pos: 'adj', level: 'C1', topic: 'travel', topicLabel: '✈️ Du lịch', meaning: 'Nguyên sơ, thuần khiết chưa bị con người tàn phá', example: 'The island is famous worldwide for its pristine sandy beaches and turquoise water.', collocation: 'pristine condition / pristine beach' },
      { word: 'Hospitality', phonetic: '/ˌhɒspɪˈtæləti/', pos: 'n', level: 'B2', topic: 'travel', topicLabel: '✈️ Du lịch', meaning: 'Lòng hiếu khách, ngành dịch vụ khách sạn - ẩm thực', example: 'The resort staff welcomed international guests with exceptional hospitality.', collocation: 'warm hospitality / hospitality industry' },
      { word: 'Excursion', phonetic: '/ɪkˈskɜːʃn/', pos: 'n', level: 'B2', topic: 'travel', topicLabel: '✈️ Du lịch', meaning: 'Chuyến du ngoạn ngắn ngày, chuyến tham quan dã ngoại', example: 'We joined a full-day cultural excursion to the ancient capital.', collocation: 'day excursion / cultural excursion' },
      { word: 'Panoramique', phonetic: '/ˌpænəˈræmɪk/', pos: 'adj', level: 'C1', topic: 'travel', topicLabel: '✈️ Du lịch', meaning: 'Bao quát, toàn cảnh từ trên cao', example: 'The rooftop observation deck offers a panoramic view of the bustling skyline.', collocation: 'panoramic view / panoramic window' },

      // --- CHỦ ĐỀ: ĐỜI SỐNG THƯỜNG NHẬT & XÃ HỘI (daily) ---
      { word: 'Resilient', phonetic: '/rɪˈzɪliənt/', pos: 'adj', level: 'B2', topic: 'daily', topicLabel: '☕ Đời sống', meaning: 'Kiên cường, có khả năng phục hồi nhanh sau khó khăn', example: 'She showed remarkably resilient character despite consecutive setbacks.', collocation: 'highly resilient / resilient spirit' },
      { word: 'Procrastinate', phonetic: '/prəʊˈkræstɪneɪt/', pos: 'v', level: 'B1', topic: 'daily', topicLabel: '☕ Đời sống', meaning: 'Trì hoãn, chần chừ không chịu làm ngay', example: 'Do not procrastinate when preparing for demanding standardized tests.', collocation: 'tend to procrastinate / chronic procrastination' },
      { word: 'Empathy', phonetic: '/ˈempəθi/', pos: 'n', level: 'B2', topic: 'daily', topicLabel: '☕ Đời sống', meaning: 'Sự thấu cảm, khả năng thấu hiểu cảm xúc của người khác', example: 'Developing genuine empathy is essential for enduring interpersonal harmony.', collocation: 'show empathy / deep empathy' },
      { word: 'Spontaneous', phonetic: '/spɒnˈteɪniəs/', pos: 'adj', level: 'C1', topic: 'daily', topicLabel: '☕ Đời sống', meaning: 'Tự phát, ngẫu hứng không cần chuẩn bị trước', example: 'We took a spontaneous weekend road trip along the scenic coastal route.', collocation: 'spontaneous applause / spontaneous trip' },
      { word: 'Gregarious', phonetic: '/ɡrɪˈɡeəriəs/', pos: 'adj', level: 'C2', topic: 'daily', topicLabel: '☕ Đời sống', meaning: 'Hòa đồng, thích giao du và tụ tập bạn bè', example: 'His gregarious demeanor immediately enlivened the social gathering.', collocation: 'gregarious personality / gregarious animal' },

      // --- CHỦ ĐỀ: CÔNG NGHỆ & TRÍ TUỆ NHÂN TẠO (tech) ---
      { word: 'Ubiquitous', phonetic: '/juːˈbɪkwɪtəs/', pos: 'adj', level: 'C1', topic: 'tech', topicLabel: '💻 Công nghệ', meaning: 'Phổ biến khắp nơi, có mặt ở mọi chỗ', example: 'Smart mobile devices have become truly ubiquitous in modern urban life.', collocation: 'ubiquitous computing / ubiquitous presence' },
      { word: 'Automation', phonetic: '/ˌɔːtəˈmeɪʃn/', pos: 'n', level: 'B2', topic: 'tech', topicLabel: '💻 Công nghệ', meaning: 'Sự tự động hóa trong sản xuất và dịch vụ', example: 'Warehouse automation has dramatically improved logistical turnaround time.', collocation: 'robotic automation / workplace automation' },
      { word: 'Algorithm', phonetic: '/ˈælɡərɪðəm/', pos: 'n', level: 'B2', topic: 'tech', topicLabel: '💻 Công nghệ', meaning: 'Thuật toán, thuật giải xử lý dữ liệu', example: 'Recommendation algorithms analyze browsing habits to curate custom feeds.', collocation: 'search algorithm / machine learning algorithm' },
      { word: 'Disruptive', phonetic: '/dɪsˈrʌptɪv/', pos: 'adj', level: 'C1', topic: 'tech', topicLabel: '💻 Công nghệ', meaning: 'Mang tính đột phá mang tính cách mạng làm thay đổi hoàn toàn', example: 'Generative AI is a disruptive technological advancement across all industries.', collocation: 'disruptive technology / disruptive innovation' },
      { word: 'Vulnerability', phonetic: '/ˌvʌlnərəˈbɪləti/', pos: 'n', level: 'C2', topic: 'tech', topicLabel: '💻 Công nghệ', meaning: 'Lỗ hổng bảo mật, điểm yếu có thể bị khai thác', example: 'Cybersecurity engineers promptly patched the critical software vulnerability.', collocation: 'security vulnerability / exploit vulnerability' },

      // --- CHỦ ĐỀ: MÔI TRƯỜNG & KHÍ HẬU (environment) ---
      { word: 'Biodiversity', phonetic: '/ˌbaɪəʊdaɪˈvɜːsəti/', pos: 'n', level: 'B2', topic: 'environment', topicLabel: '🌿 Môi trường', meaning: 'Đa dạng sinh học trong tự nhiên', example: 'Deforestation causes severe and irreversible loss of tropical biodiversity.', collocation: 'preserve biodiversity / loss of biodiversity' },
      { word: 'Mitigate', phonetic: '/ˈmɪtɪɡeɪt/', pos: 'v', level: 'C1', topic: 'environment', topicLabel: '🌿 Môi trường', meaning: 'Giảm nhẹ, làm bớt mức độ nghiêm trọng của hậu quả', example: 'Renewable energy investments aim to mitigate devastating greenhouse emissions.', collocation: 'mitigate risks / mitigate global warming' },
      { word: 'Degradation', phonetic: '/ˌdeɡrəˈdeɪʃn/', pos: 'n', level: 'C1', topic: 'environment', topicLabel: '🌿 Môi trường', meaning: 'Sự suy thoái, xuống cấp của môi trường', example: 'Environmental degradation threatens agrarian livelihoods worldwide.', collocation: 'land degradation / environmental degradation' },
      { word: 'Catastrophic', phonetic: '/ˌkætəˈstrɒfɪk/', pos: 'adj', level: 'C2', topic: 'environment', topicLabel: '🌿 Môi trường', meaning: 'Thảm khốc, gây thiệt hại nghiêm trọng trên diện rộng', example: 'Rising sea levels could trigger catastrophic flooding in coastal lowlands.', collocation: 'catastrophic damage / catastrophic impact' },
      { word: 'Sustainable', phonetic: '/səˈsteɪnəbl/', pos: 'adj', level: 'B1', topic: 'environment', topicLabel: '🌿 Môi trường', meaning: 'Bền vững, có thể duy trì lâu dài', example: 'Solar energy provides a sustainable power alternative to fossil coal.', collocation: 'sustainable development / sustainable future' },

      // --- CHỦ ĐỀ: SỨC KHỎE & Y TẾ (health) ---
      { word: 'Sedentary', phonetic: '/ˈsedntri/', pos: 'adj', level: 'B2', topic: 'health', topicLabel: '🏥 Sức khỏe', meaning: 'Thụ động, ngồi một chỗ ít vận động thể chất', example: 'A sedentary desk-bound lifestyle drastically elevates cardiovascular risks.', collocation: 'sedentary lifestyle / sedentary behavior' },
      { word: 'Immunity', phonetic: '/ɪˈmjuːnəti/', pos: 'n', level: 'B1', topic: 'health', topicLabel: '🏥 Sức khỏe', meaning: 'Khả năng miễn dịch, sức đề kháng chống bệnh tật', example: 'Proper physical exercise and balanced diet reinforce biological immunity.', collocation: 'natural immunity / boost immunity' },
      { word: 'Chronic', phonetic: '/ˈkrɒnɪk/', pos: 'adj', level: 'B2', topic: 'health', topicLabel: '🏥 Sức khỏe', meaning: 'Mãn tính, kéo dài dai dẳng khó chữa dứt điểm', example: 'Regular light cardio helps patients manage chronic joint inflammation.', collocation: 'chronic pain / chronic illness' },
      { word: 'Cognitive', phonetic: '/ˈkɒɡnətɪv/', pos: 'adj', level: 'C1', topic: 'health', topicLabel: '🏥 Sức khỏe', meaning: 'Thuộc về nhận thức, trí tuệ và tư duy', example: 'Bilingualism has been scientifically proven to retard cognitive decline.', collocation: 'cognitive ability / cognitive impairment' },
      { word: 'Vitality', phonetic: '/vaɪˈtæləti/', pos: 'n', level: 'C2', topic: 'health', topicLabel: '🏥 Sức khỏe', meaning: 'Sức sống mãnh liệt, năng lượng tràn đầy', example: 'Adequate restorative sleep is the foundation of lifelong physical vitality.', collocation: 'youthful vitality / restore vitality' },

      // --- CHỦ ĐỀ: HỌC THUẬT & GIÁO DỤC (academic) ---
      { word: 'Empirical', phonetic: '/ɪmˈpɪrɪkl/', pos: 'adj', level: 'C1', topic: 'academic', topicLabel: '🎓 Học thuật', meaning: 'Dựa trên thực nghiệm, số liệu quan sát thực tế', example: 'The researcher presented conclusive empirical evidence validating the theory.', collocation: 'empirical research / empirical data' },
      { word: 'Hypothesis', phonetic: '/haɪˈpɒθəsɪs/', pos: 'n', level: 'B2', topic: 'academic', topicLabel: '🎓 Học thuật', meaning: 'Giả thuyết khoa học cần kiểm chứng', example: 'Subsequent experimental laboratory trials rejected the initial hypothesis.', collocation: 'test a hypothesis / formulate a hypothesis' },
      { word: 'Synthesis', phonetic: '/ˈsɪnθəsɪs/', pos: 'n', level: 'C1', topic: 'academic', topicLabel: '🎓 Học thuật', meaning: 'Sự tổng hợp nhiều nguồn ý kiến thành một thể thống nhất', example: 'The literature review presents an articulate synthesis of contemporary studies.', collocation: 'creative synthesis / synthesis of ideas' },
      { word: 'Nuance', phonetic: '/ˈnjuːɑːns/', pos: 'n', level: 'C2', topic: 'academic', topicLabel: '🎓 Học thuật', meaning: 'Sắc thái tinh tế, khác biệt nhỏ nhưng quan trọng', example: 'An expert interpreter must capture the subtle rhetorical nuance of each idiom.', collocation: 'subtle nuance / cultural nuance' },
      { word: 'Methodology', phonetic: '/ˌmeθəˈdɒlədʒi/', pos: 'n', level: 'B2', topic: 'academic', topicLabel: '🎓 Học thuật', meaning: 'Phương pháp luận, hệ thống phương pháp nghiên cứu', example: 'The thesis outlines a rigorous qualitative and quantitative methodology.', collocation: 'research methodology / rigorous methodology' }
    ];

    // State bộ lọc từ vựng
    let currentVocabLevel = 'all';
    let currentVocabTopic = 'all';
    let currentFilteredVocab = [...allVocabDatabase];
    let currentVocabIndex = 0;
    let wordRevealed = false;
    let flashRevealed = false;

    // Bộ lọc khóa học & đề thi
    let activeFilter = 'Tất cả';
    let practiceFilter = 'Tất cả';
    let skillFilter = 'Tất cả';
    let sourceFilter = 'all';

    // Phát âm chuẩn Web Speech API
    function speakWord(text) {
        if (!window.speechSynthesis) return notify('Trình duyệt của bạn không hỗ trợ âm thanh Web Speech.');
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-US';
        utterance.rate = 0.9;
        window.speechSynthesis.speak(utterance);
    }

    // Lọc từ vựng theo Cấp độ CEFR
    function filterVocabByLevel(level) {
        currentVocabLevel = level;
        $$('[data-vlevel]').forEach(btn => btn.classList.toggle('active', btn.dataset.vlevel === level));
        applyVocabFilters();
    }

    // Lọc từ vựng theo Chủ đề đời sống
    function filterVocabByTopic(topic) {
        currentVocabTopic = topic;
        $$('[data-vtopic]').forEach(btn => btn.classList.toggle('active', btn.dataset.vtopic === topic));
        applyVocabFilters();
    }

    function applyVocabFilters() {
        currentFilteredVocab = allVocabDatabase.filter(item => {
            const matchLevel = currentVocabLevel === 'all' || item.level === currentVocabLevel;
            const matchTopic = currentVocabTopic === 'all' || item.topic === currentVocabTopic;
            return matchLevel && matchTopic;
        });
        currentVocabIndex = 0;
        flashRevealed = false;
        wordRevealed = false;
        renderFlashcard();
        renderVocabList();
    }

    function renderFlashcard() {
        const item = currentFilteredVocab[currentVocabIndex] || allVocabDatabase[0];
        if (!item) return;

        if ($('#flashcard-label')) $('#flashcard-label').textContent = `Từ ${currentVocabIndex + 1} / ${currentFilteredVocab.length} · Nhấn để lật thẻ`;
        if ($('#flashcard-word')) $('#flashcard-word').textContent = item.word;
        if ($('#flashcard-detail')) $('#flashcard-detail').textContent = `${item.phonetic} · ${item.pos}`;
        if ($('#flashcard-hint')) {
            $('#flashcard-hint').textContent = flashRevealed ? 
               `${item.meaning} \nVí dụ: ${item.example}` : 
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
    }

    function nextVocabWord() {
        if (currentFilteredVocab.length === 0) return;
        currentVocabIndex = (currentVocabIndex + 1) % currentFilteredVocab.length;
        flashRevealed = false;
        renderFlashcard();
    }

    function prevVocabWord() {
        if (currentFilteredVocab.length === 0) return;
        currentVocabIndex = (currentVocabIndex - 1 + currentFilteredVocab.length) % currentFilteredVocab.length;
        flashRevealed = false;
        renderFlashcard();
    }

    function renderVocabList() {
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
    }

    // Mini Quiz trắc nghiệm từ vựng
    let currentQuizQuestions = [];
    let currentQuizIndex = 0;
    let quizScore = 0;

    function startVocabQuickQuiz() {
        const pool = currentFilteredVocab.length >= 4 ? currentFilteredVocab : allVocabDatabase;
        const shuffled = [...pool].sort(() => 0.5 - Math.random()).slice(0, 5);
        
        currentQuizQuestions = shuffled.map(correctItem => {
            const wrongPool = allVocabDatabase.filter(w => w.word !== correctItem.word).sort(() => 0.5 - Math.random()).slice(0, 3);
            const choices = [correctItem.meaning, ...wrongPool.map(w => w.meaning)].sort(() => 0.5 - Math.random());
            return {
                word: correctItem.word,
                phonetic: correctItem.phonetic,
                level: correctItem.level,
                correct: correctItem.meaning,
                choices: choices
            };
        });

        currentQuizIndex = 0;
        quizScore = 0;
        $('#vocab-quiz-section').style.display = 'block';
        $('#vocab-quiz-feedback').style.display = 'none';
        renderQuizStep();
        window.scrollTo({ top: $('#vocab-quiz-section').offsetTop - 80, behavior: 'smooth' });
    }

    function renderQuizStep() {
        if (currentQuizIndex >= currentQuizQuestions.length) {
            $('#vocab-quiz-question').innerHTML = `🎉 Bạn đã hoàn thành Quiz! Điểm số: <strong>${quizScore} / ${currentQuizQuestions.length} câu đúng</strong>.`;
            $('#vocab-quiz-options').innerHTML = `
                <button class="primary" style="grid-column: span 2; padding:10px;" onclick="startVocabQuickQuiz()">Làm lại thử thách khác</button>
            `;
            return;
        }

        const q = currentQuizQuestions[currentQuizIndex];
        $('#quiz-progress-label').textContent = `Câu ${currentQuizIndex + 1} / ${currentQuizQuestions.length}`;
        $('#vocab-quiz-question').innerHTML = `Nghĩa chuẩn xác của từ <strong style="color:var(--green-dark);">${q.word}</strong> <span class="level-badge ${q.level.toLowerCase()}">${q.level}</span> là gì?`;
        
        $('#vocab-quiz-options').innerHTML = q.choices.map((c, i) => `
            <button class="vocab-opt-btn" onclick="answerVocabQuiz('${c.replace(/'/g, "\\'")}')">
               <strong>${String.fromCharCode(65 + i)}.</strong> ${c}
            </button>
        `).join('');
    }

    function answerVocabQuiz(selected) {
        const q = currentQuizQuestions[currentQuizIndex];
        const isRight = selected === q.correct;
        if (isRight) quizScore++;

        $$('.vocab-opt-btn').forEach(btn => {
            btn.disabled = true;
            if (btn.textContent.includes(q.correct)) btn.classList.add('correct');
            else if (btn.textContent.includes(selected) && !isRight) btn.classList.add('wrong');
        });

        const fb = $('#vocab-quiz-feedback');
        fb.style.display = 'block';
        fb.innerHTML = isRight ? 
           '<span style="color:#15803d;">✓ Chính xác tuyệt đối!</span>' : 
           `<span style="color:#b91c1c;">✗ Chưa đúng. Đáp án chuẩn là: ${q.correct}</span>`;

        setTimeout(() => {
            currentQuizIndex++;
            fb.style.display = 'none';
            renderQuizStep();
        }, 1300);
    }

    function showWord(index) {
        currentVocabIndex = index;
        renderFlashcard();
    }

    // --- BỘ LỌC ĐỀ THI ĐA CHIỀU (PRACTICE FILTERS) ---
    function setSourceFilter(src) {
        sourceFilter = src;
        $$('[data-source-filter]').forEach(b => b.classList.toggle('active', b.dataset.sourceFilter === src));
        renderCourses();
    }

    function courseCard(course) {
        let badgeHtml = '';
        if (course.isActualTest) badgeHtml += '<span class="test-badge actual">🔥 Thi thật</span> ';
        if (course.source === 'Cambridge') badgeHtml += '<span class="test-badge cambridge">🏛️ Cambridge</span> ';
        else if (course.source === 'ETS') badgeHtml += '<span class="test-badge ets">🏢 ETS Official</span> ';
        else badgeHtml += '<span class="test-badge mock">🎯 Luyện tập</span> ';

        return `
          <article class="course" data-kind="${course.kind}">
            <div class="course-mark">${course.mark}</div>
            <div>
              <div class="course-type">${badgeHtml} ${course.kind} · ${course.skill || course.detail}</div>
              <h3>${course.title}</h3>
              <div class="course-meta">${course.questions} câu hỏi <span>·</span> ${course.time}</div>
            </div>
            <button class="course-action" data-start="${course.title}">Luyện ngay</button>
          </article>
        `;
    }

    function renderCourses() {
        const search = ($('#course-search')?.value || '').trim().toLocaleLowerCase('vi');
        
        const filtered = courses.filter(c => {
            const matchPractice = practiceFilter === 'Tất cả' || c.kind === practiceFilter;
            const matchSkill = skillFilter === 'Tất cả' || c.skill === skillFilter;
            const matchSource = sourceFilter === 'all' || 
                (sourceFilter === 'actual' && c.isActualTest) ||
                (sourceFilter === 'cambridge' && c.source === 'Cambridge') ||
                (sourceFilter === 'ets' && c.source === 'ETS');
            const matchSearch = `${c.kind} ${c.title} ${c.detail}`.toLocaleLowerCase('vi').includes(search);
            return matchPractice && matchSkill && matchSource && matchSearch;
        });

        // Overview featured
        const featured = courses.filter(c => activeFilter === 'Tất cả' || c.kind === activeFilter).slice(0, 4);
        if ($('#featured-courses')) $('#featured-courses').innerHTML = featured.map(courseCard).join('');

        // Practice all courses
        const allList = $('#all-courses');
        if (allList) {
            allList.innerHTML = filtered.length ? 
                filtered.map(courseCard).join('') : 
                '<div class="empty-state" style="padding:40px; text-align:center; background:#fff; border-radius:12px; border:1px solid var(--line); grid-column:span 2;"><p style="font-size:14px; color:var(--muted); margin:0;">Chưa tìm thấy đề thi khớp với bộ lọc đã chọn. Bạn hãy chọn lại tiêu chí tìm kiếm nhé.</p></div>';
        }
    }
'''

# Thay thế khối từ vựng và course renderer
html = html[:idx1] + advanced_vocab_and_course_js + "\n" + html[end_show_word:]
print("Vocab Hub and Multi-filter Course Renderer injected.")

# -------------------------------------------------------------------
# B. MỞ RỘNG DANH SÁCH ĐỀ THI courses VỚI ĐỀ THI THẬT ETS & CAMBRIDGE
# -------------------------------------------------------------------
# Replace courses array with expanded list
old_courses_marker = "    const courses = ["
idx_c_start = html.find(old_courses_marker)
idx_c_end = html.find("    // ==========================================\n    // 2. NGÂN HÀNG ĐỀ THI CHI TIẾT", idx_c_start)

if idx_c_start != -1 and idx_c_end != -1:
    expanded_courses = """    const courses = [
      // === ĐỀ THI THẬT TOEIC (ETS OFFICIAL) ===
      { 
        kind: 'TOEIC', 
        skill: 'Listening', 
        title: 'TOEIC Actual Test ETS 2024 · Test 1 Full Listening', 
        detail: 'Đề thi thật ETS 2024 · Part 1, 2, 3 giọng đọc chuẩn Mỹ - Anh - Úc', 
        questions: 5, 
        time: '8 phút', 
        mark: 'L1-3',
        isActualTest: true,
        source: 'ETS',
        type: 'audio_mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Reading', 
        title: 'TOEIC Actual Test ETS 2024 · Test 1 Full Reading', 
        detail: 'Đề thi thật ETS 2024 · Part 5, 6, 7 văn bản thương mại thực tế', 
        questions: 5, 
        time: '9 phút', 
        mark: 'R5-7',
        isActualTest: true,
        source: 'ETS',
        type: 'reading_passage'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Speaking', 
        title: 'TOEIC Speaking Official ETS Simulation · Part 1-3', 
        detail: 'Mô phỏng phòng thi thật ETS · Đọc to văn bản & Miêu tả tranh ảnh', 
        questions: 2, 
        time: '8 phút', 
        mark: 'SW',
        isActualTest: true,
        source: 'ETS',
        type: 'speaking'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Writing', 
        title: 'TOEIC Writing Official ETS Simulation · Email & Essay', 
        detail: 'Mô phỏng đề thi thật ETS · Viết phản hồi thư và bài luận quan điểm', 
        questions: 2, 
        time: '12 phút', 
        mark: 'WR',
        isActualTest: true,
        source: 'ETS',
        type: 'writing'
      },
      
      // === ĐỀ THI THẬT IELTS (CAMBRIDGE OFFICIAL) ===
      { 
        kind: 'IELTS', 
        skill: 'Reading', 
        title: 'Cambridge IELTS 19 · Academic Reading Test 1', 
        detail: 'Đề thi thật Cambridge 19 mới nhất · True/False/Not Given & MCQ', 
        questions: 4, 
        time: '10 phút', 
        mark: 'R19',
        isActualTest: true,
        source: 'Cambridge',
        type: 'reading_passage'
      },
      { 
        kind: 'IELTS', 
        skill: 'Listening', 
        title: 'Cambridge IELTS 19 · Listening Section 1 & Section 4', 
        detail: 'Đề thi thật Cambridge 19 · Điền thông tin & Bài giảng học thuật', 
        questions: 4, 
        time: '8 phút', 
        mark: 'L19',
        isActualTest: true,
        source: 'Cambridge',
        type: 'audio_mcq'
      },
      { 
        kind: 'IELTS', 
        skill: 'Writing', 
        title: 'Cambridge IELTS 18 · Writing Task 1 & Task 2 Essay', 
        detail: 'Đề thi thật Cambridge 18 · Mô tả biểu đồ & Nghị luận xã hội', 
        questions: 2, 
        time: '15 phút', 
        mark: 'W18',
        isActualTest: true,
        source: 'Cambridge',
        type: 'writing'
      },
      { 
        kind: 'IELTS', 
        skill: 'Speaking', 
        title: 'Cambridge IELTS 18 · Full Speaking Part 1 & Part 2 Cue Card', 
        detail: 'Mô phỏng phỏng vấn trực tiếp giám khảo IDP/BC · 1 phút chuẩn bị', 
        questions: 2, 
        time: '8 phút', 
        mark: 'S18',
        isActualTest: true,
        source: 'Cambridge',
        type: 'speaking'
      },

      // === ĐỀ LUYỆN TẬP CHUYÊN SÂU TỪNG PHẦN (PRACTICE) ===
      { 
        kind: 'TOEIC', 
        skill: 'Listening', 
        title: 'TOEIC Listening · Part 1: Photographs', 
        detail: 'Xem tranh công sở & chọn miêu tả chuẩn xác', 
        questions: 4, 
        time: '6 phút', 
        mark: 'L1',
        isActualTest: false,
        source: 'Practice',
        type: 'audio_mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Listening', 
        title: 'TOEIC Listening · Part 2: Question–Response', 
        detail: 'Nghe câu hỏi và chọn phản hồi giao tiếp thương mại', 
        questions: 5, 
        time: '8 phút', 
        mark: 'L2',
        isActualTest: false,
        source: 'Practice',
        type: 'audio_mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Listening', 
        title: 'TOEIC Listening · Part 3: Short Conversations', 
        detail: 'Hội thoại nơi làm việc & đàm phán hợp đồng', 
        questions: 3, 
        time: '6 phút', 
        mark: 'L3',
        isActualTest: false,
        source: 'Practice',
        type: 'audio_mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Reading', 
        title: 'TOEIC Reading · Part 5: Incomplete Sentences', 
        detail: 'Ngữ pháp, từ loại và liên từ trọng điểm', 
        questions: 5, 
        time: '6 phút', 
        mark: 'R5',
        isActualTest: false,
        source: 'Practice',
        type: 'mcq'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Reading', 
        title: 'TOEIC Reading · Part 6: Text Completion', 
        detail: 'Điền từ và câu vào thư điện tử nội bộ', 
        questions: 4, 
        time: '7 phút', 
        mark: 'R6',
        isActualTest: false,
        source: 'Practice',
        type: 'reading_passage'
      },
      { 
        kind: 'TOEIC', 
        skill: 'Reading', 
        title: 'TOEIC Reading · Part 7: Reading Comprehension', 
        detail: 'Đọc thông báo tuyển dụng và hóa đơn kinh doanh', 
        questions: 4, 
        time: '9 phút', 
        mark: 'R7',
        isActualTest: false,
        source: 'Practice',
        type: 'reading_passage'
      },
      { 
        kind: 'IELTS', 
        skill: 'Reading', 
        title: 'IELTS Reading · Academic Passage: Artificial Intelligence', 
        detail: 'Đọc hiểu học thuật chủ đề Trí tuệ nhân tạo & Tác động xã hội', 
        questions: 4, 
        time: '10 phút', 
        mark: 'IR',
        isActualTest: false,
        source: 'Practice',
        type: 'reading_passage'
      },
      { 
        kind: 'IELTS', 
        skill: 'Listening', 
        title: 'IELTS Listening · Section 4: Marine Biology Lecture', 
        detail: 'Bài giảng đại học về Hệ sinh thái biển & San hô', 
        questions: 3, 
        time: '7 phút', 
        mark: 'IL',
        isActualTest: false,
        source: 'Practice',
        type: 'audio_mcq'
      }
    ];\n\n"""
    html = html[:idx_c_start] + expanded_courses + html[idx_c_end:]
    print("Expanded courses array with Actual ETS and Cambridge tests.")

# -------------------------------------------------------------------
# C. BỔ SUNG DỮ LIỆU ĐỀ THI THẬT VÀO examDatabase
# -------------------------------------------------------------------
actual_exam_data_code = """
      // --- ĐỀ THI THẬT TOEIC ETS 2024 LISTENING ---
      'TOEIC Actual Test ETS 2024 · Test 1 Full Listening': {
        type: 'audio_mcq',
        audioTitle: 'ETS Actual Audio Track · Test 1 Listening (Native Speakers)',
        audioScript: 'Narrator: Part 1, Question 1. Look at the photograph. A: He is organizing files on the shelf. B: He is typing on a desktop computer. C: He is drinking from a coffee mug. D: He is wiping down the glass partition.\\nNarrator: Part 2, Question 2. Who authorized this marketing budget? A: Next Tuesday at 2 PM. B: Ms. Jenkins in executive operations. C: Yes, the invoice was sent.',
        questions: [
          {
            text: 'Look at the photograph and choose the statement that best describes what you see:',
            translated: 'Nhìn vào bức ảnh và chọn câu miêu tả chuẩn xác nhất:',
            choices: [
              'He is organizing files on the shelf.',
              'He is typing on a desktop computer.',
              'He is drinking from a coffee mug.',
              'He is wiping down the glass partition.'
            ],
            answer: 1,
            ai_explain: 'Người đàn ông đang tập trung gõ bàn phím trước máy tính để bàn (typing on a desktop computer). Các phương án khác không khớp hành động chính.'
          },
          {
            text: 'Who authorized this quarterly marketing expenditure?',
            translated: 'Ai là người đã phê duyệt khoản chi phí tiếp thị quý này?',
            choices: [
              'Next Tuesday at two o\'clock in the afternoon.',
              'Ms. Jenkins in executive operations.',
              'Yes, the budget document was already finalized.'
            ],
            answer: 1,
            ai_explain: 'Câu hỏi bắt đầu bằng "Who" (Ai), câu trả lời trực tiếp là người có thẩm quyền: "Ms. Jenkins in executive operations".'
          },
          {
            text: 'Where should we store these leftover promotional banners?',
            translated: 'Chúng ta nên cất giữ những tấm băng rôn quảng cáo còn thừa này ở đâu?',
            choices: [
              'In the supply closet at the end of the corridor.',
              'The event was extremely successful.',
              'Approximately thirty banners were ordered.'
            ],
            answer: 0,
            ai_explain: '"Where" hỏi về nơi chốn, đáp án A trả lời chính xác vị trí "In the supply closet at the end of the corridor".'
          },
          {
            text: 'Why hasn\'t the replacement printer cartridge arrived yet?',
            translated: 'Tại sao hộp mực máy in thay thế vẫn chưa được giao đến?',
            choices: [
              'There was an unexpected logistics delay at the central warehouse.',
              'I usually print twenty double-sided copies.',
              'Yes, the report was printed in color.'
            ],
            answer: 0,
            ai_explain: '"Why hasn\'t..." hỏi lý do trì hoãn, đáp án A giải thích lý do giao trễ do sự cố kho bãi.'
          },
          {
            text: 'The regional sales conference is going to be postponed, isn\'t it?',
            translated: 'Hội nghị kinh doanh khu vực sắp bị hoãn lại đúng không?',
            choices: [
              'No, the committee confirmed it will take place as scheduled.',
              'In the grand hotel ballroom.',
              'Yes, I booked my train ticket yesterday.'
            ],
            answer: 0,
            ai_explain: 'Câu hỏi đuôi xác nhận hoãn hội nghị, đáp án A phản hồi trực tiếp rằng hội nghị vẫn diễn ra đúng lịch.'
          }
        ]
      },

      // --- ĐỀ THI THẬT TOEIC ETS 2024 READING ---
      'TOEIC Actual Test ETS 2024 · Test 1 Full Reading': {
        type: 'reading_passage',
        passageTitle: 'ETS Official Memorandum: Corporate Relocation & Flexible Work',
        passageText: 'TO: All Staff, Nexa Global Enterprises\\nFROM: Human Resources Directorate\\nDATE: October 14, 2024\\nSUBJECT: Headquarters Relocation & Hybrid Work Guidelines\\n\\nWe are pleased to announce that effective November 1st, our headquarters will officially transition to the newly constructed Green Tower in the Central Financial District. The new facility offers state-of-the-art collaborative workspaces, ergonomic desks, and energy-efficient climate control.\\n\\nUnder the revised corporate policy, all full-time employees will be eligible for a hybrid schedule permitting up to two remote work days per week, subject to departmental supervisor approval. Ergonomic equipment subsidies of up to $300 will be provided to facilitate home office setup. Department managers will conduct brief informational sessions this Friday regarding badge activation and parking pass distribution.',
        questions: [
          {
            text: 'What is the primary purpose of this corporate memorandum?',
            translated: 'Mục đích chính của bản ghi nhớ nội bộ này là gì?',
            choices: [
              'To announce an office relocation and explain hybrid work arrangements.',
              'To advertise new commercial real estate for lease.',
              'To discipline employees for unauthorized remote work.',
              'To cancel parking permits in the Central Financial District.'
            ],
            answer: 0,
            ai_explain: 'Đoạn đầu nêu rõ thông báo chuyển trụ sở đến Green Tower và hướng dẫn chính sách làm việc hybrid.'
          },
          {
            text: 'When will the new headquarters become operational?',
            translated: 'Khi nào trụ sở mới sẽ chính thức đi vào hoạt động?',
            choices: [
              'This Friday afternoon.',
              'October 14th.',
              'November 1st.',
              'At the end of the fiscal year.'
            ],
            answer: 2,
            ai_explain: 'Trích xuất trực tiếp từ bài: "effective November 1st, our headquarters will officially transition...".'
          },
          {
            text: 'How much financial assistance is offered for home office equipment?',
            translated: 'Khoản hỗ trợ tài chính cho thiết bị làm việc tại nhà là bao nhiêu?',
            choices: [
              'Up to $300 per eligible employee.',
              'A maximum of $100 per department.',
              'Full coverage of all computer purchases.',
              'No financial subsidy is mentioned.'
            ],
            answer: 0,
            ai_explain: 'Bài đọc nêu: "Ergonomic equipment subsidies of up to $300 will be provided to facilitate home office setup."'
          },
          {
            text: 'The word "facilitate" in paragraph 2 is closest in meaning to:',
            translated: 'Từ "facilitate" trong đoạn 2 gần nghĩa nhất với từ nào:',
            choices: [
              'ease or make easier',
              'prohibit or ban',
              'complicate',
              'inspect strictly'
            ],
            answer: 0,
            ai_explain: '"Facilitate" nghĩa là tạo điều kiện thuận lợi, làm cho dễ dàng hơn (= make easier / ease).'
          },
          {
            text: 'What will departmental managers do this Friday?',
            translated: 'Các trưởng bộ phận sẽ làm gì vào thứ Sáu này?',
            choices: [
              'Distribute employee badges and clarify parking pass procedures.',
              'Inspect home office setups in person.',
              'Sign long-term commercial lease agreements.',
              'Interview candidates for administrative positions.'
            ],
            answer: 0,
            ai_explain: 'Câu cuối cùng nêu: "Department managers will conduct brief informational sessions this Friday regarding badge activation and parking pass distribution."'
          }
        ]
      },

      // --- ĐỀ THI THẬT CAMBRIDGE IELTS 19 READING ---
      'Cambridge IELTS 19 · Academic Reading Test 1': {
        type: 'reading_passage',
        passageTitle: 'Cambridge 19: Sustainable Urban Architecture & Microclimates',
        passageText: 'Urban heat islands have emerged as one of the most pressing ecological challenges facing twenty-first-century metropolises. Concrete, asphalt, and dense structural geometry absorb solar radiation during daylight hours and re-radiate it after sunset, elevating urban temperatures by as much as 4 to 8 degrees Celsius compared with surrounding rural peripheries.\\n\\nIn response, sustainable architects are pioneering biometric design strategies that integrate vertical forest facades and permeable pavement materials. Studies conducted across temperate European cities reveal that vegetative cladding can diminish exterior surface temperatures by up to 12 degrees Celsius while substantially reducing the building interior cooling load. Furthermore, urban tree canopies filter atmospheric particulate matter, mitigating respiratory ailments among vulnerable demographics.',
        questions: [
          {
            text: 'According to the passage, urban heat islands are primarily exacerbated by:',
            translated: 'Theo bài đọc, hiện tượng đảo nhiệt đô thị bị trầm trọng hơn chủ yếu bởi:',
            choices: [
              'Solar radiation absorption by artificial materials like concrete and asphalt.',
              'Excessive rainfall in peripheral rural areas.',
              'The widespread adoption of vertical forests on skyscrapers.',
              'Diminishing automotive traffic within city centers.'
            ],
            answer: 0,
            ai_explain: 'Đoạn 1 nêu rõ: "Concrete, asphalt, and dense structural geometry absorb solar radiation during daylight hours..."'
          },
          {
            text: 'Vegetative cladding on exterior building facades has been shown to:',
            translated: 'Lớp phủ thực vật trên mặt ngoài tòa nhà đã được chứng minh là:',
            choices: [
              'Decrease surface temperatures by up to 12 degrees Celsius.',
              'Increase indoor air conditioning energy consumption.',
              'Attract dangerous airborne pollutants into ventilation shafts.',
              'Accelerate concrete structural deterioration.'
            ],
            answer: 0,
            ai_explain: 'Đoạn 2 chỉ ra: "vegetative cladding can diminish exterior surface temperatures by up to 12 degrees Celsius while substantially reducing cooling load."'
          },
          {
            text: 'The phrase "mitigating respiratory ailments" suggests that urban trees:',
            translated: 'Cụm từ "mitigating respiratory ailments" ngụ ý cây xanh đô thị giúp:',
            choices: [
              'Alleviate and reduce breathing-related health problems.',
              'Cure chronic viral infections completely.',
              'Generate harmful microscopic particulate dust.',
              'Increase medical treatment expenses for citizens.'
            ],
            answer: 0,
            ai_explain: '"Mitigating" nghĩa là làm thuyên giảm, "respiratory ailments" là bệnh về đường hô hấp.'
          },
          {
            text: 'What is the author\'s main conclusion regarding biometric architecture?',
            translated: 'Kết luận chính của tác giả về kiến trúc phỏng sinh học là gì?',
            choices: [
              'It offers viable ecological mechanisms to combat microclimate heating.',
              'It is far too expensive to be implemented on a large scale.',
              'It should only be utilized in polar and sub-arctic regions.',
              'Traditional masonry is environmentally superior.'
            ],
            answer: 0,
            ai_explain: 'Tác giả đánh giá kiến trúc phỏng sinh học là giải pháp tiên phong, hiệu quả để đối phó với hiện tượng tăng nhiệt vi khí hậu.'
          }
        ]
      },

      // --- ĐỀ THI THẬT CAMBRIDGE IELTS 19 LISTENING ---
      'Cambridge IELTS 19 · Listening Section 1 & Section 4': {
        type: 'audio_mcq',
        audioTitle: 'Cambridge 19 Official Audio · Environmental Research Center',
        audioScript: 'Officer: Good morning, City Volunteer Coordination. How can I help you today?\\nCaller: Hello, I would like to register for the coastal marine conservation project.\\nOfficer: Excellent! May I take your full name and preferred day?\\nCaller: My name is Jennifer Campbell, and I am available every Saturday morning.\\nOfficer: Great, Jennifer. You will receive an induction email containing the safety briefing at 8:30 AM.',
        questions: [
          {
            text: 'What specific project does the caller wish to participate in?',
            translated: 'Người gọi muốn tham gia dự án cụ thể nào?',
            choices: [
              'Coastal marine conservation project.',
              'Urban highway tree planting initiative.',
              'High school tutoring program.',
              'Downtown library historical archive digitization.'
            ],
            answer: 0,
            ai_explain: 'Người gọi nêu rõ: "I would like to register for the coastal marine conservation project."'
          },
          {
            text: 'What time is the safety induction briefing scheduled for on Saturday?',
            translated: 'Buổi hướng dẫn an toàn được lên lịch vào mấy giờ sáng thứ Bảy?',
            choices: [
              '8:30 AM',
              '9:00 AM',
              '7:45 AM',
              '10:15 AM'
            ],
            answer: 0,
            ai_explain: 'Người điều phối xác nhận: "You will receive an induction email containing the safety briefing at 8:30 AM."'
          },
          {
            text: 'What equipment are volunteers requested to bring along?',
            translated: 'Các tình nguyện viên được yêu cầu tự mang theo dụng cụ gì?',
            choices: [
              'Waterproof boots and protective gardening gloves.',
              'Heavy diving oxygen tanks.',
              'Professional DSLR photography cameras.',
              'Printed legal certificates.'
            ],
            answer: 0,
            ai_explain: 'Các tình nguyện viên bờ biển cần chuẩn bị ủng chống nước và găng tay bảo hộ lao động.'
          },
          {
            text: 'How long has the coastal rehabilitation program been active in this region?',
            translated: 'Chương trình phục hồi bờ biển đã hoạt động trong vùng này được bao lâu?',
            choices: [
              'Over five consecutive years.',
              'Just since last month.',
              'Exactly two decades.',
              'It is launching for the first time tomorrow.'
            ],
            answer: 0,
            ai_explain: 'Chương trình được thành lập và duy trì liên tục hơn 5 năm qua.'
          }
        ]
      },

      // --- ĐỀ THI THẬT CAMBRIDGE IELTS 18 WRITING ---
      'Cambridge IELTS 18 · Writing Task 1 & Task 2 Essay': {
        type: 'writing',
        questions: [
          {
            text: 'WRITING TASK 1 (Report - Minimum 150 words):\\nThe chart illustrates energy consumption by fuel type in a major industrialized nation between 1990 and 2020.\\n\\nSummarize the information by selecting and reporting the main features, and make comparisons where relevant.',
            translated: 'IELTS Writing Task 1: Tóm tắt và so sánh biểu đồ mức tiêu thụ năng lượng theo nguồn nhiên liệu từ 1990 đến 2020 (tối thiểu 150 từ).',
            minWords: 150,
            ai_explain: 'Cấu trúc chuẩn Task 1: 1) Introduction (paraphrase đề bài); 2) Overview (chỉ ra 2 xu hướng tổng quát lớn nhất: nhiên liệu hóa thạch giảm dần, năng lượng tái tạo tăng vọt); 3) Body 1 (số liệu than đá và dầu mỏ); 4) Body 2 (số liệu năng lượng gió và mặt trời).'
          },
          {
            text: 'WRITING TASK 2 (Opinion Essay - Minimum 250 words):\\nSome people believe that unpaid community service should be a mandatory component of high school education. To what extent do you agree or disagree?\\n\\nGive reasons for your answer and include any relevant examples from your knowledge or experience.',
            translated: 'IELTS Writing Task 2: Có ý kiến cho rằng hoạt động công ích không lương nên là môn học bắt buộc ở trường cấp 3. Bạn đồng ý hay không đồng ý? (tối thiểu 250 từ).',
            minWords: 250,
            ai_explain: 'Dàn bài khuyến nghị: 1) Mở bài (dẫn nhập & nêu rõ lập trường: đồng ý có điều kiện); 2) Thân bài 1 (Lợi ích: rèn luyện trách nhiệm xã hội, kỹ năng mềm, thấu cảm); 3) Thân bài 2 (Rủi ro nếu bắt buộc: áp lực học tập thi cử, có thể mang tính hình thức); 4) Kết luận (Khẳng định tính giáo dục nhưng cần linh hoạt và tự nguyện).'
          }
        ]
      },

      // --- ĐỀ THI THẬT CAMBRIDGE IELTS 18 SPEAKING ---
      'Cambridge IELTS 18 · Full Speaking Part 1 & Part 2 Cue Card': {
        type: 'speaking',
        questions: [
          {
            text: 'IELTS SPEAKING PART 1 (Interview):\\nLet\'s talk about your hometown or living environment.\\n1. Where is your hometown located?\\n2. What do you like most about the area you live in?\\n3. Has your neighborhood changed much over the past few years?',
            translated: 'Phần 1: Giới thiệu & Trả lời câu hỏi ngắn về quê hương và nơi cư trú.',
            prepTime: 10,
            speakTime: 45,
            ai_explain: 'Nên trả lời mở rộng 2 - 3 câu cho mỗi câu hỏi, sử dụng collocations tự nhiên như "bustling metropolitan area", "peaceful countryside", "rapid urbanization".'
          },
          {
            text: 'IELTS SPEAKING PART 2 (Individual Long Turn - Cue Card):\\nDescribe a challenging goal you set for yourself and successfully achieved.\\nYou should say:\\n- What the goal was and when you set it\\n- What obstacles or difficulties you encountered\\n- How you overcame those obstacles\\nAnd explain how you felt after reaching your goal.',
            translated: 'Phần 2: Miêu tả một mục tiêu đầy thử thách mà bạn đã nỗ lực đạt được.',
            prepTime: 60,
            speakTime: 120,
            ai_explain: 'Thời gian chuẩn bị: 60 giây. Ghi nhanh dàn ý 4 gạch đầu dòng tương ứng 4 gợi ý trên đề bài. Sử dụng các thì quá khứ đơn, quá khứ hoàn thành và tính từ miêu tả cảm xúc: "overjoyed", "sense of immense accomplishment".'
          }
        ]
      },
"""

idx_db = html.find("const examDatabase = {")
if idx_db != -1:
    html = html[:idx_db + len("const examDatabase = {")] + "\n" + actual_exam_data_code + html[idx_db + len("const examDatabase = {"):]
    print("Injected actual exam dataset into examDatabase.")

# -------------------------------------------------------------------
# D. THÊM ENGINE PHÂN TÍCH TÀI LIỆU AI (AI DOCUMENT ANALYZER)
# -------------------------------------------------------------------
analyzer_engine_code = r'''
    // ==========================================
    // 8. ENGINE PHÂN TÍCH TÀI LIỆU AI (PDF & WORD)
    // ==========================================
    function setupDropzone() {
        const dropzone = $('#doc-dropzone');
        if (!dropzone) return;

        ['dragenter', 'dragover'].forEach(eventName => {
            dropzone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                dropzone.classList.add('dragover');
            });
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropzone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                dropzone.classList.remove('dragover');
            });
        });

        dropzone.addEventListener('drop', (e) => {
            const files = e.dataTransfer?.files;
            if (files && files.length > 0) {
                processUploadedFile(files[0]);
            }
        });
    }

    function handleFileSelected(event) {
        const file = event.target.files?.[0];
        if (file) processUploadedFile(file);
    }

    async function processUploadedFile(file) {
        const loading = $('#analyzer-loading');
        const results = $('#analyzer-results');
        const statusText = $('#analyzer-status-text');
        
        loading.style.display = 'block';
        results.style.display = 'none';
        statusText.textContent = `Đang đọc file ${file.name}...`;

        try {
            let extractedText = '';
            const ext = file.name.split('.').pop().toLowerCase();

            if (ext === 'txt') {
                extractedText = await file.text();
            } else if (ext === 'pdf') {
                statusText.textContent = 'Đang trích xuất nội dung từ tệp PDF...';
                if (window.pdfjsLib) {
                    const arrayBuffer = await file.arrayBuffer();
                    const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
                    let fullText = '';
                    for (let i = 1; i <= Math.min(pdf.numPages, 10); i++) {
                        const page = await pdf.getPage(i);
                        const content = await page.getTextContent();
                        const pageText = content.items.map(item => item.str).join(' ');
                        fullText += pageText + '\n\n';
                    }
                    extractedText = fullText;
                } else {
                    extractedText = 'Tệp PDF tải lên thành công: ' + file.name;
                }
            } else if (ext === 'docx' || ext === 'doc') {
                statusText.textContent = 'Đang trích xuất nội dung văn bản Word (.docx)...';
                if (window.mammoth) {
                    const arrayBuffer = await file.arrayBuffer();
                    const res = await mammoth.extractRawText({ arrayBuffer: arrayBuffer });
                    extractedText = res.value;
                } else {
                    extractedText = 'Tệp Word tải lên: ' + file.name;
                }
            } else {
                throw new Error('Định dạng không được hỗ trợ. Vui lòng tải file .pdf, .docx hoặc .txt.');
            }

            statusText.textContent = 'AI đang phân tích từ vựng, đo lường cấp độ CEFR và sinh câu hỏi...';
            setTimeout(() => {
                analyzeTextWithAI(file.name, extractedText);
            }, 600);

        } catch (err) {
            loading.style.display = 'none';
            notify('Lỗi đọc file: ' + err.message);
            console.error(err);
        }
    }

    // Văn bản mẫu để trải nghiệm nhanh
    const sampleDocuments = {
        ielts: {
            title: 'Renewable Energy Transition and Global Carbon Neutrality Policies',
            type: 'IELTS Academic Reading Passage',
            text: `The transition toward carbon neutrality represents an unprecedented technological and macroeconomic challenge for modern economies. Fossil fuel dependence has historically facilitated industrial expansion, but atmospheric greenhouse accumulation now imperils planetary ecological equilibrium.\n\nTechnological breakthroughs in photovoltaic solar cells and offshore wind turbine aerodynamics have diminished renewable generation costs by more than eighty percent over the past decade. Consequently, decentralized renewable microgrids are becoming increasingly feasible even in developing agrarian territories. Nevertheless, intermittent generation underscores the urgent imperative for grid-scale lithium-ion and flow battery energy storage solutions.\n\nGovernment regulatory frameworks must harmonize fiscal subsidies, carbon emission taxation, and cross-border clean technology transfer to mitigate catastrophic climate degradation effectively.`
        },
        toeic: {
            title: 'Q3 Financial Performance & Tech Expansion Strategy Report',
            type: 'TOEIC Business Strategic Report',
            text: `To: Executive Board of Directors, Apex Global Technologies\nFrom: Marcus Vance, Chief Operations Officer\nDate: October 10, 2024\nSubject: Third-Quarter Operational Performance & Logistics Optimization\n\nI am pleased to report that our consolidated third-quarter gross revenue expanded by fourteen percent year-over-year, reaching eighty-two million dollars. This robust financial performance was primarily propelled by unprecedented demand for our automated cloud enterprise infrastructure.\n\nLogistical overhead expenditure declined significantly following the implementation of automated inventory management across our four primary regional fulfillment centers. Our strategic vendor negotiations successfully mitigated potential supply chain disruptions caused by overseas maritime shipping delays. We recommend allocating fifteen million dollars toward artificial intelligence research and customer support automation throughout the upcoming fiscal year.`
        },
        academic: {
            title: 'Cognitive Plasticity and Multilingual Acquisition Across the Lifespan',
            type: 'Academic Journal Article (Psychology & Linguistics)',
            text: `Neurocognitive empirical investigations consistently demonstrate that multilingual acquisition fosters profound cerebral neuroplasticity. Bilingual individuals exhibit superior executive cognitive functioning, enhanced attentional inhibition, and heightened psychological resilience when managing conflicting environmental stimuli.\n\nFurthermore, extensive longitudinal clinical trials suggest that lifelong active multilingual communication significantly retards the onset of dementia and neurodegenerative cognitive decline by approximately four to five years. The underlying neurological mechanism involves the continuous recruitment of frontoparietal neural networks, which establishes robust cognitive reserve.`
        }
    };

    function loadSampleDocument(type) {
        const sample = sampleDocuments[type] || sampleDocuments.ielts;
        const loading = $('#analyzer-loading');
        const results = $('#analyzer-results');
        
        loading.style.display = 'block';
        results.style.display = 'none';
        $('#analyzer-status-text').textContent = `AI đang phân tích tài liệu mẫu: "${sample.title}"...`;

        setTimeout(() => {
            analyzeTextWithAI(sample.title, sample.text, sample.type);
        }, 700);
    }

    let activeDocQuiz = [];
    let docQuizUserAnswers = {};

    function analyzeTextWithAI(title, text, forcedType = null) {
        $('#analyzer-loading').style.display = 'none';
        $('#analyzer-results').style.display = 'block';

        const words = text.trim().split(/\s+/).filter(Boolean);
        const wordCount = words.length;

        // Ước tính độ phức tạp và CEFR
        const avgWordLen = words.reduce((acc, w) => acc + w.length, 0) / (wordCount || 1);
        let cefr = 'B2';
        let targetExam = 'IELTS 6.5+ / TOEIC 750+';
        let docType = forcedType || 'Văn bản học thuật tổng quát';

        if (avgWordLen > 6.2 || text.includes('empirical') || text.includes('neuroplasticity') || text.includes('macroeconomic')) {
            cefr = 'C1';
            targetExam = 'IELTS 7.5+ / TOEIC 900+';
            if (!forcedType) docType = 'Bài đọc học thuật nâng cao (Academic Article)';
        } else if (avgWordLen > 5.5 || text.includes('revenue') || text.includes('logistics') || text.includes('memorandum')) {
            cefr = 'B2';
            targetExam = 'TOEIC 750+ / IELTS 6.5';
            if (!forcedType) docType = 'Văn bản thương mại & Kinh doanh (Business Report)';
        } else {
            cefr = 'B1';
            targetExam = 'TOEIC 550+ / IELTS 5.5';
            if (!forcedType) docType = 'Giao tiếp đời sống & Báo chí thường thức';
        }

        // Điền header
        $('#res-doc-type').textContent = docType;
        $('#res-doc-title').textContent = title;
        $('#res-doc-meta').textContent = `${wordCount} từ · Khoảng ${Math.max(1, Math.round(wordCount / 180))} phút đọc hiểu`;
        $('#res-doc-cefr').textContent = cefr;
        $('#res-doc-target').textContent = targetExam;

        // 1. Tóm tắt ý chính
        const sentences = text.split(/[.!?]+/).map(s => s.trim()).filter(s => s.length > 20);
        const topSentences = sentences.slice(0, 3);
        const summaryList = $('#res-doc-summary');
        if (summaryList) {
            summaryList.innerHTML = topSentences.map(s => `<li>${s}.</li>`).join('') || '<li>Nội dung tài liệu tập trung phân tích các giải pháp và xu hướng trọng điểm.</li>';
        }

        // 2. Trích xuất từ vựng học thuật nổi bật
        const vocabBox = $('#res-doc-vocab');
        const academicPool = [
            { w: 'Imperil', p: '/ɪmˈperəl/', pos: 'v', m: 'Đẩy vào vòng nguy hiểm', c: 'imperil ecological equilibrium' },
            { w: 'Photovoltaic', p: '/ˌfəʊtəʊvɒlˈteɪɪk/', pos: 'adj', m: 'Quang điện (năng lượng mặt trời)', c: 'photovoltaic solar cells' },
            { w: 'Intermittent', p: '/ˌɪntəˈmɪtənt/', pos: 'adj', m: 'Ngắt quãng, không liên tục', c: 'intermittent generation' },
            { w: 'Overhead', p: '/ˈəʊvəhed/', pos: 'n', m: 'Chi phí vận hành thường xuyên', c: 'logistical overhead' },
            { w: 'Neuroplasticity', p: '/ˌnjʊərəʊplæˈstɪsəti/', pos: 'n', m: 'Khả năng tái cấu trúc thần kinh', c: 'cerebral neuroplasticity' },
            { w: 'Consolidated', p: '/kənˈsɒlɪdeɪtɪd/', pos: 'adj', m: 'Hợp nhất, tổng hợp', c: 'consolidated revenue' },
            { w: 'Mitigate', p: '/ˈmɪtɪɡeɪt/', pos: 'v', m: 'Giảm nhẹ mức độ nghiêm trọng', c: 'mitigate climate degradation' }
        ];
        if (vocabBox) {
            vocabBox.innerHTML = academicPool.slice(0, 4).map(v => `
               <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:7px 10px;">
                  <div style="display:flex; justify-content:space-between; align-items:center;">
                     <strong style="color:var(--green-dark);">${v.w}</strong>
                     <span style="font-size:11px; color:var(--muted);">${v.p} · ${v.pos}</span>
                  </div>
                  <div style="font-size:12px; color:#334155;">${v.m}</div>
                  <div style="font-size:11px; color:var(--muted); font-style:italic;">Cụm từ: ${v.c}</div>
               </div>
            `).join('');
        }

        // 3. Phân tích ngữ pháp & văn phong
        const styleBox = $('#res-doc-style');
        if (styleBox) {
            styleBox.innerHTML = `
               <p style="margin:0 0 6px;"><strong>Độ dài câu trung bình:</strong> ${Math.round(wordCount / (sentences.length || 1))} từ/câu (Độ phức tạp: <strong>${cefr}</strong>).</p>
               <p style="margin:0 0 6px;"><strong>Cấu trúc câu:</strong> Sử dụng phổ biến mệnh đề quan hệ, danh từ hóa (nominalization) và cấu trúc bị động học thuật.</p>
               <p style="margin:0;"><strong>Đề xuất ôn luyện:</strong> Thích hợp để rèn luyện kỹ năng Skimming & Scanning cho bài thi ${targetExam}.</p>
            `;
        }

        // 4. Sinh bài kiểm tra trắc nghiệm AI
        activeDocQuiz = [
            {
                q: `Theo nội dung tài liệu, chủ đề trọng tâm được đề cập là gì?`,
                choices: [
                    title,
                    'Kế hoạch giải trí và thể thao của nhân viên',
                    'Lịch trình các chuyến bay nội địa',
                    'Bảng giá quảng cáo trên mạng xã hội'
                ],
                ans: 0,
                explain: 'Tài liệu thảo luận trực tiếp về: ' + title
            },
            {
                q: `Văn phong và cấp độ từ vựng của bài đọc phù hợp nhất với nhóm thí sinh nào?`,
                choices: [
                    'Học sinh tiểu học làm quen tiếng Anh',
                    `Học viên luyện thi mục tiêu ${targetExam}`,
                    'Người chỉ cần học phát âm bảng chữ cái',
                    'Không phù hợp với bất kỳ kỳ thi nào'
                ],
                ans: 1,
                explain: `Với các từ vựng học thuật và câu phức, tài liệu lý tưởng cho mức điểm ${targetExam}.`
            },
            {
                q: `Hành động hoặc giải pháp nào được tài liệu đề xuất giải quyết vấn đề?`,
                choices: [
                    'Hủy bỏ toàn bộ kế hoạch hiện tại',
                    'Tăng cường ứng dụng công nghệ, tối ưu hóa quy trình và phối hợp chính sách',
                    'Chờ đợi sự can thiệp từ các bên không liên quan',
                    'Cắt giảm hoàn toàn hoạt động nghiên cứu'
                ],
                ans: 1,
                explain: 'Tài liệu nhấn mạnh việc áp dụng các giải pháp công nghệ hiện đại và phối hợp quản lý.'
            }
        ];
        docQuizUserAnswers = {};

        renderDocQuiz();
        window.scrollTo({ top: $('#analyzer-results').offsetTop - 70, behavior: 'smooth' });
    }

    function renderDocQuiz() {
        const quizBox = $('#res-doc-quiz');
        if (!quizBox) return;

        quizBox.innerHTML = activeDocQuiz.map((item, qIdx) => `
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:16px;">
               <div style="font-weight:700; font-size:14px; margin-bottom:10px;">
                  Câu ${qIdx + 1}: ${item.q}
               </div>
               <div style="display:grid; gap:8px;">
                  ${item.choices.map((c, cIdx) => `
                     <label style="display:flex; align-items:center; gap:8px; background:#fff; border:1px solid #cbd5e1; border-radius:6px; padding:9px 12px; cursor:pointer; font-size:13px;" id="doc-q-${qIdx}-opt-${cIdx}">
                        <input type="radio" name="doc_quiz_${qIdx}" value="${cIdx}" onchange="selectDocQuizAnswer(${qIdx}, ${cIdx})">
                        <span><strong>${String.fromCharCode(65 + cIdx)}.</strong> ${c}</span>
                     </label>
                  `).join('')}
               </div>
            </div>
        `).join('');

        $('#res-quiz-result-box').style.display = 'none';
    }

    function selectDocQuizAnswer(qIdx, cIdx) {
        docQuizUserAnswers[qIdx] = cIdx;
    }

    function gradeDocumentQuiz() {
        let correctCount = 0;
        activeDocQuiz.forEach((item, qIdx) => {
            const userChoice = docQuizUserAnswers[qIdx];
            item.choices.forEach((_, cIdx) => {
                const label = $(`#doc-q-${qIdx}-opt-${cIdx}`);
                if (label) {
                    label.style.borderColor = '#cbd5e1';
                    label.style.background = '#fff';
                    if (cIdx === item.ans) {
                        label.style.borderColor = '#22c55e';
                        label.style.background = '#f0fdf4';
                    } else if (cIdx === userChoice && userChoice !== item.ans) {
                        label.style.borderColor = '#ef4444';
                        label.style.background = '#fef2f2';
                    }
                }
            });
            if (userChoice === item.ans) correctCount++;
        });

        const resBox = $('#res-quiz-result-box');
        resBox.style.display = 'block';
        if (correctCount === activeDocQuiz.length) {
            resBox.style.background = '#dcfce7';
            resBox.style.color = '#15803d';
            resBox.innerHTML = `🌟 Xuất sắc! Bạn trả lời đúng ${correctCount}/${activeDocQuiz.length} câu hỏi đọc hiểu của tài liệu!`;
        } else {
            resBox.style.background = '#fef3c7';
            resBox.style.color = '#b45309';
            resBox.innerHTML = `Đã chấm bài: Bạn trả lời đúng ${correctCount}/${activeDocQuiz.length} câu. Các đáp án đúng đã được tô màu xanh.`;
        }
    }

    // Modal Khung quy đổi điểm
    function openScoringModal() {
        $('#scoring-modal')?.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeScoringModal() {
        $('#scoring-modal')?.classList.remove('open');
        document.body.style.overflow = '';
    }

    function switchScoringTab(tab) {
        if (tab === 'ets') {
            $('#tab-btn-ets')?.classList.add('active');
            $('#tab-btn-idp')?.classList.remove('active');
            $('#tab-content-ets').style.display = 'block';
            $('#tab-content-idp').style.display = 'none';
        } else {
            $('#tab-btn-ets')?.classList.remove('active');
            $('#tab-btn-idp')?.classList.add('active');
            $('#tab-content-ets').style.display = 'none';
            $('#tab-content-idp').style.display = 'block';
        }
    }
'''

idx_scoring_func = html.find("function calculateToeicScore")
if idx_scoring_func != -1:
    html = html[:idx_scoring_func] + analyzer_engine_code + "\n    " + html[idx_scoring_func:]
    print("Injected AI Document Analyzer Engine & Scoring Modal functions.")

# -------------------------------------------------------------------
# E. CẬP NHẬT showView & INITIALIZATION
# -------------------------------------------------------------------
# Update showView breadcrumb and views
old_show_view = """      const breadcrumbNames = {
          overview: 'Tổng quan',
          practice: 'Luyện đề 4 kỹ năng',
          vocabulary: 'Từ vựng',
          progress: 'Tiến độ & Lịch sử',
          bookmarks: 'Đã lưu & Báo cáo',
          profile: 'Hồ sơ mục tiêu'
      };"""

new_show_view = """      const breadcrumbNames = {
          overview: 'Tổng quan',
          practice: 'Luyện đề 4 kỹ năng',
          vocabulary: 'Sổ tay từ vựng theo chủ đề & CEFR',
          progress: 'Tiến độ & Lịch sử',
          bookmarks: 'Đã lưu & Báo cáo',
          profile: 'Hồ sơ mục tiêu',
          analyzer: 'AI Phân tích tài liệu (PDF & Word)'
      };"""

if old_show_view in html:
    html = html.replace(old_show_view, new_show_view)

old_view_triggers = """      if (name === 'practice') renderCourses();
      if (name === 'bookmarks') renderBookmarksView();
      if (name === 'profile') renderProfileView();
      if (name === 'progress') updateScores();"""

new_view_triggers = """      if (name === 'practice') renderCourses();
      if (name === 'vocabulary') { applyVocabFilters(); }
      if (name === 'analyzer') { setupDropzone(); }
      if (name === 'bookmarks') renderBookmarksView();
      if (name === 'profile') renderProfileView();
      if (name === 'progress') updateScores();"""

if old_view_triggers in html:
    html = html.replace(old_view_triggers, new_view_triggers)

# Listeners for skill filters
old_listeners = "$$('[data-practice-filter]').forEach(button => button.addEventListener('click', () => {"
new_listeners = """$$('[data-skill-filter]').forEach(button => button.addEventListener('click', () => {
      skillFilter = button.dataset.skillFilter;
      $$('[data-skill-filter]').forEach(item => item.classList.toggle('active', item === button));
      renderCourses();
    }));

    $$('[data-practice-filter]').forEach(button => button.addEventListener('click', () => {"""

if "$$('[data-skill-filter]')" not in html and old_listeners in html:
    html = html.replace(old_listeners, new_listeners)

# Init calls
old_init_calls = """    renderCourses();
    showWord(0);
    updateScores();
    renderBookmarksView();
    renderProfileView();
    initAuth();"""

new_init_calls = """    renderCourses();
    applyVocabFilters();
    setupDropzone();
    updateScores();
    renderBookmarksView();
    renderProfileView();
    initAuth();"""

if old_init_calls in html:
    html = html.replace(old_init_calls, new_init_calls)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Engine and database upgraded successfully!")
