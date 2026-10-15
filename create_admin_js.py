admin_js_code = '''
    // ==============================================================
    // 11. ADMIN DASHBOARD - QUẢN LÝ & UPLOAD ĐỀ THI ĐỊNH KỲ
    // ==============================================================
    let adminExamFilter = 'all';

    function getAdminUploadedCourses() {
        try {
            return JSON.parse(localStorage.getItem('lingua-admin-courses') || '[]');
        } catch(e) {
            return [];
        }
    }

    function saveAdminUploadedCourses(list) {
        localStorage.setItem('lingua-admin-courses', JSON.stringify(list));
    }

    function getAdminUploadedExams() {
        try {
            return JSON.parse(localStorage.getItem('lingua-admin-exams') || '{}');
        } catch(e) {
            return {};
        }
    }

    function saveAdminUploadedExams(map) {
        localStorage.setItem('lingua-admin-exams', JSON.stringify(map));
    }

    function syncAdminExamsToSystem() {
        const customCourses = getAdminUploadedCourses();
        const customExams = getAdminUploadedExams();
        
        // Gộp vào courses nếu chưa có
        customCourses.forEach(cc => {
            const exists = courses.find(c => c.title === cc.title);
            if (!exists) {
                courses.unshift(cc);
            }
        });

        // Gộp vào examDatabase
        Object.assign(examDatabase, customExams);
    }

    function switchAdminUploadMode(mode) {
        const fileTab = $('#btn-tab-upload-file');
        const manualTab = $('#btn-tab-upload-manual');
        const filePane = $('#admin-upload-file-pane');
        if (fileTab) fileTab.classList.toggle('active', mode === 'file');
        if (manualTab) manualTab.classList.toggle('active', mode === 'manual');
        if (filePane) filePane.style.display = mode === 'file' ? 'block' : 'none';
    }

    function handleAdminFileSelected(event) {
        const file = event.target.files?.[0];
        if (!file) return;

        const reader = new FileReader();
        const fname = file.name.toLowerCase();

        if (fname.endsWith('.json')) {
            reader.onload = (e) => {
                try {
                    const parsed = JSON.parse(e.target.result);
                    if (parsed.title) $('#admin-exam-title').value = parsed.title;
                    if (parsed.kind) $('#admin-exam-kind').value = parsed.kind;
                    if (parsed.skill) $('#admin-exam-skill').value = parsed.skill;
                    if (parsed.source) $('#admin-exam-source').value = parsed.source;
                    if (parsed.time) $('#admin-exam-time').value = parseInt(parsed.time) || 15;
                    if (parsed.questions) {
                        $('#admin-exam-questions-json').value = JSON.stringify(parsed.questions, null, 2);
                    }
                    notify('Đã nạp dữ liệu đề thi từ file JSON thành công!');
                } catch(err) {
                    notify('Lỗi đọc file JSON: Định dạng không đúng.');
                }
            };
            reader.readAsText(file);
        } else if (fname.endsWith('.txt')) {
            reader.onload = (e) => {
                const text = e.target.result;
                $('#admin-exam-title').value = file.name.replace('.txt', '');
                // Auto generate sample questions from text lines
                const qs = [
                    {
                        text: text.slice(0, 150) + '...',
                        choices: ['Đáp án A (Khởi đầu)', 'Đáp án B (Chiến lược)', 'Đáp án C (Tối ưu)', 'Đáp án D (Đánh giá)'],
                        answer: 1,
                        explain: 'Dựa trên phân tích trọng tâm văn bản đề bài.'
                    }
                ];
                $('#admin-exam-questions-json').value = JSON.stringify(qs, null, 2);
                notify('Đã nạp văn bản đề thi từ file text.');
            };
            reader.readAsText(file);
        } else {
            notify(`Đã nhận file ${file.name}. Vui lòng kiểm tra lại thông tin và xác nhận upload.`);
            $('#admin-exam-title').value = file.name.replace(/\.[^/.]+$/, "");
        }
    }

    function fillAdminQuestionTemplate() {
        const tmpl = [
            {
                text: "The financial committee decided to postpone the annual audit until all branch reports are _____ submitted.",
                choices: ["full", "fully", "fullness", "fulfilling"],
                answer: 1,
                explain: "Chọn trạng từ 'fully' để bổ nghĩa cho động từ phân từ 'submitted'."
            },
            {
                text: "Customer satisfaction rates have shown a _____ increase following the rollout of the 24/7 support line.",
                choices: ["notable", "notably", "noted", "noting"],
                answer: 0,
                explain: "Trước danh từ 'increase' cần tính từ 'notable' (đáng kể)."
            },
            {
                text: "Neither the regional manager _____ the department heads were aware of the unexpected policy change.",
                choices: ["and", "nor", "or", "also"],
                answer: 1,
                explain: "Cặp liên từ tương quan 'Neither ... nor'."
            }
        ];
        $('#admin-exam-questions-json').value = JSON.stringify(tmpl, null, 2);
        notify('Đã chèn bộ 3 câu hỏi mẫu chuẩn!');
    }

    function resetAdminForm() {
        $('#admin-upload-exam-form')?.reset();
        $('#admin-exam-questions-json').value = '';
    }

    function loadSampleAdminExam(type) {
        if (type === 'toeic_listening_actual') {
            $('#admin-exam-title').value = 'TOEIC Listening · Part 3: Short Conversations (ETS Actual Test 2025)';
            $('#admin-exam-kind').value = 'TOEIC';
            $('#admin-exam-skill').value = 'Listening';
            $('#admin-exam-source').value = 'Actual Test';
            $('#admin-exam-time').value = 18;
            $('#admin-exam-questions-json').value = JSON.stringify([
                {
                    text: "Where most likely are the speakers talking?",
                    choices: ["At an advertising agency", "In a train station cafe", "At an electronics showroom", "In a medical laboratory"],
                    answer: 0,
                    explain: "Người phụ nữ đề cập đến 'our client's billboard campaign schedule'."
                },
                {
                    text: "What problem does the man mention?",
                    choices: ["A shipment arrived damaged", "A graphic designer is unavailable", "The budget was exceeded", "The deadline was moved up"],
                    answer: 1,
                    explain: "Người đàn ông nói: 'Sarah called in sick so we are short on graphic design staff'."
                },
                {
                    text: "What will the speakers do next?",
                    choices: ["Contact the freelance contractor", "Cancel the afternoon presentation", "Request an extension from the client", "Review the printed drafts"],
                    answer: 0,
                    explain: "Người phụ nữ kết luận: 'Let me call our reliable freelance contractor right away'."
                }
            ], null, 2);
            notify('Đã tải mẫu đề TOEIC Listening 2025!');
        } else {
            $('#admin-exam-title').value = 'Cambridge IELTS 19 Academic Reading: Ocean Microplastics & Marine Ecology';
            $('#admin-exam-kind').value = 'IELTS';
            $('#admin-exam-skill').value = 'Reading';
            $('#admin-exam-source').value = 'Cambridge';
            $('#admin-exam-time').value = 20;
            $('#admin-exam-questions-json').value = JSON.stringify([
                {
                    text: "According to paragraph 1, what is the primary consequence of oceanic synthetic polymer degradation?",
                    choices: ["Immediate thermal elevation of surface water", "Formation of microscopic toxic particulate matrices", "Rapid depletion of atmospheric oxygen", "Eradication of coastal kelp forests"],
                    answer: 1,
                    explain: "Đoạn 1 nêu: 'fragmentation yields microscopic toxic particulate matrices which infiltrate the benthic food web'."
                },
                {
                    text: "The author uses the term 'bioaccumulation' to demonstrate that:",
                    choices: ["Microplastics concentrate upwards through trophic levels", "Marine species adapt naturally to chemical pollutants", "Industrial filtration systems have achieved efficacy", "Pelagic organisms avoid ingesting plastic particles"],
                    answer: 0,
                    explain: "'bioaccumulation' chứng minh độc tố tích tụ dần từ sinh vật phù du lên động vật săn mồi cấp cao."
                }
            ], null, 2);
            notify('Đã tải mẫu đề Cambridge IELTS 19!');
        }
    }

    function handleAdminSubmitExam(event) {
        event.preventDefault();
        const title = $('#admin-exam-title')?.value.trim();
        const kind = $('#admin-exam-kind')?.value || 'TOEIC';
        const skill = $('#admin-exam-skill')?.value || 'Reading';
        const source = $('#admin-exam-source')?.value || 'ETS';
        const time = parseInt($('#admin-exam-time')?.value) || 15;
        const qJsonStr = $('#admin-exam-questions-json')?.value.trim();

        if (!title || !qJsonStr) {
            notify('Vui lòng điền đầy đủ tiêu đề và nội dung câu hỏi.');
            return;
        }

        let questions = [];
        try {
            questions = JSON.parse(qJsonStr);
            if (!Array.isArray(questions) || questions.length === 0) {
                throw new Error('Dữ liệu câu hỏi phải là một danh sách các câu hỏi.');
            }
        } catch(e) {
            alert('Lỗi định dạng câu hỏi (JSON Error): ' + e.message);
            return;
        }

        const newCourse = {
            id: 'admin_course_' + Date.now(),
            title: title,
            kind: kind,
            skill: skill,
            detail: skill === 'Listening' ? 'Nghe hiểu' : (skill === 'Reading' ? 'Đọc hiểu' : (skill === 'Writing' ? 'Viết luận' : 'Nói & Phỏng vấn')),
            questions: questions.length,
            time: `${time} phút`,
            mark: kind === 'TOEIC' ? (skill === 'Listening' ? '🎧' : '📖') : (skill === 'Listening' ? '🎧' : '🏛️'),
            source: source,
            isActualTest: source === 'Actual Test' || source.includes('Actual'),
            isAdminUpload: true,
            createdAt: new Date().toISOString()
        };

        const newExamData = {
            title: title,
            kind: kind,
            skill: skill,
            timeLimitMin: time,
            questions: questions
        };

        // Lưu vào LocalStorage của Admin
        const customCourses = getAdminUploadedCourses();
        customCourses.unshift(newCourse);
        saveAdminUploadedCourses(customCourses);

        const customExams = getAdminUploadedExams();
        customExams[title] = newExamData;
        saveAdminUploadedExams(customExams);

        // Đồng bộ ngay lập tức vào runtime
        courses.unshift(newCourse);
        examDatabase[title] = newExamData;

        // Cập nhật giao diện
        renderCourses();
        renderAdminDashboard();
        resetAdminForm();
        notify(`🎉 Đề thi "${title}" đã được đăng tải thành công vào hệ thống!`);
    }

    function deleteAdminExam(title) {
        if (!confirm(`Bạn có chắc chắn muốn xóa đề thi "${title}" khỏi hệ thống?`)) return;

        let customCourses = getAdminUploadedCourses();
        customCourses = customCourses.filter(c => c.title !== title);
        saveAdminUploadedCourses(customCourses);

        const customExams = getAdminUploadedExams();
        delete customExams[title];
        saveAdminUploadedExams(customExams);

        // Remove from runtime
        const idx = courses.findIndex(c => c.title === title);
        if (idx !== -1) courses.splice(idx, 1);
        delete examDatabase[title];

        renderCourses();
        renderAdminDashboard();
        notify(`Đã xóa đề thi "${title}".`);
    }

    function filterAdminExams(k) {
        adminExamFilter = k;
        $$('[data-admin-filter]').forEach(btn => btn.classList.toggle('active', btn.dataset.adminFilter === k));
        renderAdminDashboard();
    }

    function renderAdminDashboard() {
        const totalCourses = courses.length;
        const customCourses = getAdminUploadedCourses();
        const reports = JSON.parse(localStorage.getItem('lingua-reports') || '[]');

        if ($('#admin-total-courses')) $('#admin-total-courses').textContent = totalCourses;
        if ($('#admin-custom-courses-count')) $('#admin-custom-courses-count').textContent = customCourses.length;
        if ($('#admin-pending-reports-count')) $('#admin-pending-reports-count').textContent = reports.length;
        if ($('#admin-exam-count-badge')) $('#admin-exam-count-badge').textContent = totalCourses;

        const listContainer = $('#admin-exams-list-container');
        if (!listContainer) return;

        const displayList = courses.filter(c => adminExamFilter === 'all' || c.kind === adminExamFilter);

        listContainer.innerHTML = displayList.map(c => {
            const isCustom = c.isAdminUpload || false;
            return `
              <div style="background:#fff; border:1px solid var(--line); border-radius:10px; padding:12px 14px; display:flex; justify-content:space-between; align-items:center; gap:10px; flex-wrap:wrap; transition:background .15s;">
                <div style="flex:1; min-width:220px;">
                  <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px;">
                    <span class="skill-pill ${c.skill ? c.skill.toLowerCase() : 'reading'}" style="font-size:10px;">${c.kind} · ${c.skill || 'Reading'}</span>
                    <span style="font-size:11px; background:#f1f5f9; color:#475569; padding:2px 6px; border-radius:4px; font-weight:600;">${c.source || 'ETS'}</span>
                    ${isCustom ? '<span style="font-size:10px; background:#fef3c7; color:#b45309; padding:1px 6px; border-radius:4px; font-weight:700;">★ Admin Upload</span>' : ''}
                  </div>
                  <strong style="font-size:13.5px; color:var(--ink);">${c.title}</strong>
                  <div style="font-size:11px; color:var(--muted); margin-top:2px;">${c.questions} câu hỏi · ${c.time}</div>
                </div>
                <div style="display:flex; gap:8px; align-items:center;">
                  <button type="button" class="tool-btn" style="padding:6px 12px; font-size:12px; border:1px solid var(--line); border-radius:6px; cursor:pointer;" onclick="openExam('${c.title}')">
                    👁️ Làm thử
                  </button>
                  ${isCustom ? `
                    <button type="button" class="text-button" style="color:#ef4444; border:1px solid #fecaca; padding:6px 10px; border-radius:6px; font-size:12px; cursor:pointer;" onclick="deleteAdminExam('${c.title}')">
                      🗑️ Xóa
                    </button>
                  ` : `
                    <span style="font-size:11px; color:var(--muted); background:#f8fafc; padding:4px 8px; border-radius:4px;">Mặc định</span>
                  `}
                </div>
              </div>
            `;
        }).join('');
    }
'''

with open('admin_js_snippet.js', 'w', encoding='utf-8') as f:
    f.write(admin_js_code)
print("Admin JS snippet written")
