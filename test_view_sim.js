const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Find all matches for class="view" or class="view active"
const re = /<section\s+class="view[^"]*"\s+id="([^"]+)"/g;
let match;
const views = [];
while ((match = re.exec(html)) !== null) {
    views.push(match[1]);
}
console.log('Views found by querySelectorAll(".view"):', views);

// Check if showView('analyzer') correctly targets view-analyzer
const targetId = 'view-analyzer';
console.log('Target ID in views?', views.includes(targetId));
console.log('Is view-vocabulary in views?', views.includes('view-vocabulary'));
