const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Extract sampleDocuments and analyzeTextWithAI
const sampleDocsCode = html.slice(html.indexOf('const sampleDocuments = {'), html.indexOf('function triggerDocUpload'));
const analyzeFnCode = html.slice(html.indexOf('function analyzeTextWithAI('), html.indexOf('function renderDocQuiz('));

console.log('Sample docs found:', sampleDocsCode.length);
console.log('Analyze fn found:', analyzeFnCode.length);
