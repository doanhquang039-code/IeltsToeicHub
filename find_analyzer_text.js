const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');

const lines = html.split('\n');
lines.forEach((l, i) => {
    if (l.includes('TRỢ LÝ HỌC THUẬT AI') || l.includes('Phân tích tài liệu học tập')) {
        console.log(`L${i+1}: ${l}`);
    }
});
