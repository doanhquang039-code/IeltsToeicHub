const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');

// Extract scripts
const scriptMatch = html.match(/<script\b[^>]*>([\s\S]*?)<\/script>/gi);
const jsCode = scriptMatch[scriptMatch.length - 1].replace(/<script\b[^>]*>/i, '').replace(/<\/script>/i, '');

console.log("Testing JS execution in Node...");
try {
    // Check if there are syntax errors or unexpected tokens
    new Function(jsCode);
    console.log("No syntax errors in main JS block.");
} catch(e) {
    console.error("Syntax error:", e);
}
