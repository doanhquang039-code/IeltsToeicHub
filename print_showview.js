const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Check showView implementation in index.html
const showViewCode = html.slice(html.indexOf('function showView'), html.indexOf('function showView') + 1200);
console.log('showView function:');
console.log(showViewCode);
