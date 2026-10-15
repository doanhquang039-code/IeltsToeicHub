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