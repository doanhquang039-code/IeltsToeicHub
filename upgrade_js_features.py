import re

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# -----------------------------------------------------------------
# 1. ADD EXCEL PARSER & SAMPLE IN ANALYZER LOGIC
# -----------------------------------------------------------------
old_file_parser = """            if (ext === 'txt') {
                extractedText = await file.text();
            } else if (ext === 'pdf') {"""

new_file_parser = """            if (ext === 'txt') {
                extractedText = await file.text();
            } else if (ext === 'xlsx' || ext === 'xls') {
                statusText.textContent = 'Đang đọc và phân tích bảng tính Excel (.xlsx/.xls)...';
                if (window.XLSX) {
                    const arrayBuffer = await file.arrayBuffer();
                    const workbook = XLSX.read(arrayBuffer, { type: 'array' });
                    let sheetContents = [];
                    workbook.SheetNames.forEach(sheetName => {
                        const worksheet = workbook.Sheets[sheetName];
                        const csv = XLSX.utils.sheet_to_csv(worksheet);
                        if (csv.trim()) {
                            sheetContents.push(`--- Bảng tính: ${sheetName} ---\\n` + csv.slice(0, 3500));
                        }
                    });
                    extractedText = sheetContents.join('\\n\\n') || ('Bảng tính Excel: ' + file.name);
                } else {
                    extractedText = 'Tệp bảng tính Excel tải lên: ' + file.name;
                }
            } else if (ext === 'pdf') {"""

if old_file_parser in content:
    content = content.replace(old_file_parser, new_file_parser, 1)
    print("SUCCESS: Added Excel file parsing support")
else:
    print("WARNING: old_file_parser not matched")

# Add Excel sample document data
old_sample_docs = """        toeic: {
            title: 'Q3 Financial Performance & Tech Expansion Strategy Report',
            type: 'TOEIC Business Strategic Report',
            text: `To: Executive Board of Directors, Apex Global Technologies\\nFrom: Marcus Vance, Chief Operations Officer\\nDate: October 10, 2024\\nSubject: Third-Quarter Operational Performance & Logistics Optimization\\n\\nI am pleased to report that our consolidated third-quarter gross revenue expanded by fourteen percent year-over-year, reaching eighty-two million dollars. This robust financial performance was primarily propelled by unprecedented demand for our automated cloud enterprise infrastructure.\\n\\nLogistical overhead expenditure declined significantly following the implementation of automated inventory management across our four primary regional fulfillment centers. Our strategic vendor negotiations successfully mitigated potential supply chain disruptions caused by overseas maritime shipping delays. We recommend allocating fifteen million dollars toward artificial intelligence research and customer support automation throughout the upcoming fiscal year.`
        },"""

new_sample_docs = """        toeic: {
            title: 'Q3 Financial Performance & Tech Expansion Strategy Report',
            type: 'TOEIC Business Strategic Report (.docx)',
            text: `To: Executive Board of Directors, Apex Global Technologies\\nFrom: Marcus Vance, Chief Operations Officer\\nDate: October 10, 2024\\nSubject: Third-Quarter Operational Performance & Logistics Optimization\\n\\nI am pleased to report that our consolidated third-quarter gross revenue expanded by fourteen percent year-over-year, reaching eighty-two million dollars. This robust financial performance was primarily propelled by unprecedented demand for our automated cloud enterprise infrastructure.\\n\\nLogistical overhead expenditure declined significantly following the implementation of automated inventory management across our four primary regional fulfillment centers. Our strategic vendor negotiations successfully mitigated potential supply chain disruptions caused by overseas maritime shipping delays. We recommend allocating fifteen million dollars toward artificial intelligence research and customer support automation throughout the upcoming fiscal year.`
        },
        excel: {
            title: 'Bảng tính Tài chính Doanh nghiệp & Vận hành Logistics Q3 (.xlsx)',
            type: 'Excel Spreadsheet & Business Analytics',
            text: `--- Bảng tính: Financial_Performance ---\\nQuarter,Territory,Gross_Revenue,Operating_Expense,Net_Margin,Variance_YoY\\nQ1,North America,$45200000,$32100000,28.9%,+4.2%\\nQ2,EMEA Europe,$38400000,$28600000,25.5%,+3.1%\\nQ3,Asia-Pacific,$58700000,$39200000,33.2%,+12.8%\\n\\n--- Bảng tính: Supply_Chain_KPIs ---\\nMetric,Target,Actual,Evaluation\\nFulfillment_Latency,48_hours,36.5_hours,Exceeded\\nLogistics_Overhead_Ratio,14.5%,11.8%,Optimized\\nCustomer_Retention_Rate,88.0%,92.4%,Superior\\n\\nSummary: Consolidated Q3 gross receipts totaled $142,300,000, yielding an aggregate gross margin of 29.2%. Logistical optimization through predictive algorithmic allocation reduced shipping turnaround times significantly.`
        },"""

if old_sample_docs in content:
    content = content.replace(old_sample_docs, new_sample_docs, 1)
    print("SUCCESS: Added Excel sample document data")
else:
    print("WARNING: old_sample_docs not matched")

# -----------------------------------------------------------------
# 2. CUSTOM VOCABULARY ENGINE (Add Word from Keyboard, LocalStorage, Filter)
# -----------------------------------------------------------------
custom_vocab_js = """    // ==========================================
    // 0.2 QUẢN LÝ TỪ VỰNG TỰ NHẬP (CUSTOM VOCABULARY ENGINE)
    // ==========================================
    function getCustomVocabList() {
        return JSON.parse(localStorage.getItem('lingua-custom-vocab') || '[]');
    }

    function saveCustomVocabList(list) {
        localStorage.setItem('lingua-custom-vocab', JSON.stringify(list));
        updateCustomVocabCountBadge();
    }

    function updateCustomVocabCountBadge() {
        const list = getCustomVocabList();
        const badge = $('#custom-vocab-count-badge');
        if (badge) badge.textContent = list.length;
    }

    function handleAddNewWord(event) {
        event.preventDefault();
        const word = $('#inp-custom-word')?.value.trim();
        const meaning = $('#inp-custom-meaning')?.value.trim();
        const topic = $('#inp-custom-topic')?.value || 'business';
        const level = $('#inp-custom-level')?.value || 'B2';
        const example = $('#inp-custom-example')?.value.trim() || `I regularly practice using "${word}" in daily communication.`;
        
        if (!word || !meaning) {
            notify('Vui lòng điền từ tiếng Anh và nghĩa tiếng Việt.');
            return;
        }

        const topicLabels = {
            business: '🏢 Công sở',
            daily: '☕ Đời sống',
            tech: '💻 Công nghệ',
            travel: '✈️ Du lịch',
            health: '🏥 Sức khỏe',
            environment: '🌿 Môi trường',
            academic: '🎓 Học thuật'
        };

        const newEntry = {
            id: 'custom_' + Date.now(),
            word: word,
            phonetic: '/' + word.toLowerCase() + '/',
            pos: 'từ vựng',
            meaning: meaning,
            example: example,
            level: level,
            topic: topic,
            topicLabel: topicLabels[topic] || 'Đời sống',
            isCustom: true
        };

        const customList = getCustomVocabList();
        customList.unshift(newEntry);
        saveCustomVocabList(customList);

        // Đưa vào đầu danh sách allVocabDatabase
        allVocabDatabase.unshift(newEntry);

        // Reset form
        $('#inp-custom-word').value = '';
        $('#inp-custom-meaning').value = '';
        if ($('#inp-custom-example')) $('#inp-custom-example').value = '';

        applyVocabFilters();
        notify(`Đã thêm thành công từ "${word}" vào sổ tay của bạn! 🎉`);
    }

    function deleteCustomWord(wordText) {
        let customList = getCustomVocabList().filter(item => item.word.toLowerCase() !== wordText.toLowerCase());
        saveCustomVocabList(customList);

        // Xóa khỏi allVocabDatabase
        const idx = allVocabDatabase.findIndex(item => item.word.toLowerCase() === wordText.toLowerCase() && item.isCustom);
        if (idx !== -1) allVocabDatabase.splice(idx, 1);

        applyVocabFilters();
        notify(`Đã xóa từ "${wordText}" khỏi sổ tay.`);
    }

    // Nạp các từ tự thêm đã lưu trong LocalStorage vào allVocabDatabase lúc khởi động
    function loadSavedCustomVocab() {
        const saved = getCustomVocabList();
        if (saved && saved.length > 0) {
            saved.forEach(item => {
                if (!allVocabDatabase.some(v => v.word.toLowerCase() === item.word.toLowerCase())) {
                    allVocabDatabase.unshift(item);
                }
            });
        }
        updateCustomVocabCountBadge();
    }
"""

if 'handleAddNewWord' not in content:
    # Insert before applyVocabFilters
    idx = content.find('    function applyVocabFilters() {')
    if idx != -1:
        content = content[:idx] + custom_vocab_js + "\n" + content[idx:]
        print("SUCCESS: Added custom vocabulary JavaScript engine")

# Update applyVocabFilters to support 'custom' level filter
old_apply_filters = """    function applyVocabFilters() {
        currentFilteredVocab = allVocabDatabase.filter(item => {
            const matchLevel = currentVocabLevel === 'all' || item.level === currentVocabLevel;
            const matchTopic = currentVocabTopic === 'all' || item.topic === currentVocabTopic;
            return matchLevel && matchTopic;
        });"""

new_apply_filters = """    function applyVocabFilters() {
        currentFilteredVocab = allVocabDatabase.filter(item => {
            let matchLevel = false;
            if (currentVocabLevel === 'all') matchLevel = true;
            else if (currentVocabLevel === 'custom') matchLevel = item.isCustom === true;
            else matchLevel = item.level === currentVocabLevel;

            const matchTopic = currentVocabTopic === 'all' || item.topic === currentVocabTopic;
            return matchLevel && matchTopic;
        });"""

if old_apply_filters in content:
    content = content.replace(old_apply_filters, new_apply_filters, 1)
    print("SUCCESS: Updated applyVocabFilters for custom words filter")

# -----------------------------------------------------------------
# 3. AI STUDY ROADMAP GENERATOR IN PROFILE VIEW
# -----------------------------------------------------------------
roadmap_generator_js = """    // ==========================================
    // 0.3 AI PERSONALIZED STUDY ROADMAP GENERATOR
    // ==========================================
    function generateStudyRoadmap(event) {
        if (event) event.preventDefault();
        const targetScore = $('#survey-target-score')?.value || 'TOEIC 750+';
        const currentLevel = $('#survey-current-level')?.value || 'B1';
        const weakSkill = $('#survey-weak-skill')?.value || 'Listening';
        const dailyTime = parseInt($('#survey-daily-time')?.value) || 45;

        // Lưu thiết lập vào profile
        try {
            const prof = JSON.parse(localStorage.getItem('lingua-profile') || '{}');
            prof.targetExam = targetScore;
            prof.currentLevel = currentLevel;
            prof.weakSkill = weakSkill;
            prof.dailyTime = dailyTime;
            localStorage.setItem('lingua-profile', JSON.stringify(prof));
        } catch(e) {}

        const roadmapBox = $('#ai-roadmap-box');
        const badge = $('#roadmap-badge');
        const summary = $('#roadmap-summary');
        const phases = $('#roadmap-phases');

        if (badge) badge.textContent = targetScore;

        let levelName = currentLevel === 'A2' ? 'Cơ bản (A2)' : (currentLevel === 'B1' ? 'Trung cấp (B1)' : (currentLevel === 'B2' ? 'Khá (B2)' : 'Nâng cao (C1)'));
        let weeksEst = currentLevel === 'A2' ? 12 : (currentLevel === 'B1' ? 8 : 4);
        if (dailyTime >= 90) weeksEst = Math.round(weeksEst * 0.65);

        if (summary) {
            summary.innerHTML = `Dựa trên trình độ hiện tại <strong>${levelName}</strong>, mục tiêu <strong>${targetScore}</strong> với thời gian học <strong>${dailyTime} phút/ngày</strong>, AI tính toán bạn cần khoảng <strong>${weeksEst} tuần</strong> để đạt điểm số mong muốn. Trọng tâm đào sâu: <strong>${weakSkill}</strong>.`;
        }

        const phase1Focus = weakSkill === 'Listening' ? 'Củng cố phát âm chuẩn IPA & Nghe hiểu từ khóa (Keywords/Paraphrasing)' : 
                           (weakSkill === 'Reading' ? 'Mở rộng 150 từ vựng cốt lõi & Phương pháp Skimming/Scanning' : 
                           (weakSkill === 'Writing' ? 'Nắm vững cấu trúc đoạn văn PEEL & Collocations học thuật' : 'Luyện phản xạ Shadowing & Ngữ điệu giao tiếp tự nhiên'));

        const phase2Focus = targetScore.includes('IELTS') ? 
            'Luyện các bộ đề Cambridge IELTS 18 & 19 chính thức theo từng Section/Passage chuyên sâu' : 
            'Luyện đề thi ETS TOEIC 2024 Actual Test với tốc độ thực tế 1.0x - 1.25x';

        const phase3Focus = 'Thi thử Full Test bấm giờ áp lực phòng thi thật, tổng ôn câu sai và tối ưu tốc độ làm bài';

        if (phases) {
            phases.innerHTML = `
               <div style="background:#fff; border-left:3px solid #0284c7; padding:10px 14px; border-radius:6px; font-size:12.5px;">
                  <strong style="color:#0369a1;">Giai đoạn 1 (Tuần 1 - ${Math.max(1, Math.round(weeksEst*0.35))}): Nền tảng cốt lõi & Khắc phục ${weakSkill}</strong>
                  <div style="color:#334155; margin-top:3px;">${phase1Focus}. Học mỗi ngày ${dailyTime} phút trong Sổ tay từ vựng & AI Doc.</div>
               </div>
               <div style="background:#fff; border-left:3px solid #16a34a; padding:10px 14px; border-radius:6px; font-size:12.5px;">
                  <strong style="color:#15803d;">Giai đoạn 2 (Tuần ${Math.max(2, Math.round(weeksEst*0.35)+1)} - ${Math.round(weeksEst*0.75)}): Thực chiến đề thi theo kỹ năng</strong>
                  <div style="color:#334155; margin-top:3px;">${phase2Focus}. Chấm điểm real-time và đọc kỹ giải thích AI chi tiết sau mỗi đề.</div>
               </div>
               <div style="background:#fff; border-left:3px solid #f59e0b; padding:10px 14px; border-radius:6px; font-size:12.5px;">
                  <strong style="color:#b45309;">Giai đoạn 3 (Tuần ${Math.round(weeksEst*0.75)+1} - ${weeksEst}): Tăng tốc về đích chạm ${targetScore}</strong>
                  <div style="color:#334155; margin-top:3px;">${phase3Focus}. Rút ngắn thời gian mỗi câu, hoàn thiện mục tiêu điểm số.</div>
               </div>
            `;
        }

        if (roadmapBox) roadmapBox.style.display = 'block';

        if ($('#profile-target-title')) $('#profile-target-title').textContent = targetScore;
        if ($('#profile-countdown')) $('#profile-countdown').textContent = `Dự kiến: ${weeksEst} tuần`;

        notify('AI đã cập nhật lộ trình học tập cá nhân hóa của bạn! 🎯');
    }
"""

if 'generateStudyRoadmap' not in content:
    idx = content.find('    function updateScores() {')
    if idx != -1:
        content = content[:idx] + roadmap_generator_js + "\n" + content[idx:]
        print("SUCCESS: Added AI Study Roadmap Generator function")

# -----------------------------------------------------------------
# 4. ENHANCE LANDING PAGE AUTH FLOW:
#    - Don't block screen on startup: default to Guest on overview page
#    - Add closeLoginModal()
# -----------------------------------------------------------------
content = content.replace(
    """    function closeExamAndGoHome() {
        closeExam();
        showView('overview');
    }""",
    """    function closeExamAndGoHome() {
        closeExam();
        showView('overview');
    }

    function closeLoginModal() {
        const authEl = $('#auth-screen');
        if (authEl) {
            authEl.classList.add('hidden');
            authEl.style.display = 'none';
        }
    }"""
)

# Update initAuth to allow browsing landing page as Guest without being locked out
old_init_auth_end = """        // Bước 4: Kiểm tra session trực tiếp từ Supabase
        if (sbClient) {
            try {
                const { data: { session } } = await sbClient.auth.getSession();
                if (session && session.user) {
                    const u = session.user;
                    const name = u.user_metadata?.full_name || u.user_metadata?.name || (u.email ? u.email.split('@')[0] : 'Học viên');
                    localStorage.setItem('lingua-user', name);
                    showApp(name);
                    return;
                }
            } catch(e) {
                console.warn('Lỗi getSession:', e);
            }
        }
        
        showLogin();
    }"""

new_init_auth_end = """        // Bước 4: Kiểm tra session trực tiếp từ Supabase
        if (sbClient) {
            try {
                const { data: { session } } = await sbClient.auth.getSession();
                if (session && session.user) {
                    const u = session.user;
                    const name = u.user_metadata?.full_name || u.user_metadata?.name || (u.email ? u.email.split('@')[0] : 'Học viên');
                    localStorage.setItem('lingua-user', name);
                    showApp(name);
                    return;
                }
            } catch(e) {
                console.warn('Lỗi getSession:', e);
            }
        }

        // Mặc định cho phép người dùng vào xem và khám phá toàn bộ trang chủ Lingua với tư cách Khách
        showApp('Khách Trải Nghiệm');
    }"""

if old_init_auth_end in content:
    content = content.replace(old_init_auth_end, new_init_auth_end, 1)
    print("SUCCESS: Updated initAuth to welcome guest on landing page instead of blocking screen")

# Update showApp to show login button on topbar if Guest, or user name if authenticated
old_show_app = """        if ($('#sidebar-name')) $('#sidebar-name').textContent = displayName;
        if ($('#welcome-name')) $('#welcome-name').textContent = `Chào bạn, ${displayName}`;"""

new_show_app = """        if ($('#sidebar-name')) $('#sidebar-name').textContent = displayName;
        if ($('#welcome-name')) $('#welcome-name').textContent = displayName === 'Khách Trải Nghiệm' ? 'Chào bạn đến với Lingua English Hub' : `Chào mừng ${displayName} trở lại`;
        
        const topbarLoginBtn = $('#topbar-login-btn');
        const topbarLoginText = $('#topbar-login-text');
        if (topbarLoginBtn) {
            if (displayName === 'Khách Trải Nghiệm') {
                topbarLoginBtn.style.display = 'flex';
                if (topbarLoginText) topbarLoginText.textContent = '🔑 Đăng nhập / Đăng ký';
            } else {
                topbarLoginBtn.style.display = 'flex';
                if (topbarLoginText) topbarLoginText.textContent = `👤 ${displayName} (Tài khoản)`;
            }
        }"""

if old_show_app in content:
    content = content.replace(old_show_app, new_show_app, 1)
    print("SUCCESS: Enhanced showApp with dynamic topbar login button")

# Call loadSavedCustomVocab at startup
content = content.replace(
    """    // KHỞI CHẠY TẤT CẢ
    renderCourses();""",
    """    // KHỞI CHẠY TẤT CẢ
    loadSavedCustomVocab();
    renderCourses();"""
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("PART 2 JAVASCRIPT UPDATES WRITTEN TO FILE!")
