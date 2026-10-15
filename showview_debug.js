function showView(name) {
      const allViews = $$('.view');
      allViews.forEach(view => {
          const isTarget = view.id === `view-${name}`;
          view.classList.toggle('active', isTarget);
          view.style.display = isTarget ? 'block' : 'none';
      });

      $$('.nav button').forEach(button => {
          button.classList.toggle('active', button.dataset.view === name);
      });
      
      const breadcrumbNames = {
          overview: 'Tổng quan',
          practice: 'Luyện đề 4 kỹ năng',
          vocabulary: 'Sổ tay từ vựng theo chủ đề & CEFR',
          progress: 'Tiến độ & Lịch sử',
          bookmarks: 'Đã lưu & Báo cáo',
          profile: 'Hồ sơ mục tiêu',
          analyzer: 'AI Phân tích tài liệu (PDF & Word)'
      };
      if ($('#crumb-current')) $('#crumb-current').textContent = breadcrumbNames[name] || 'Không gian học';
      
      if (name === 'practice') renderCourses();
      if (name === 'vocabulary') { applyVocabFilters(); }
      if (name === 'analyzer') { 
          setupDropzone(); 
          const results = $('#analyzer-results');
          if (results && (results.style.display === 'none' || !$('#res-doc-summary')?.innerHTML.trim())) {
              const s = sampleDocuments.ielts;
              analyzeTextWithAI(s.title, s.text, s.type);
          }
      }
      if (name === 'bookmarks') renderBookmarksView();
      if (name === 'profile') renderProfileView();
      if (name === 'progress') updateScores();
      
      window.s