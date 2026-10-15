const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf-8');

// Check all views in HTML
const viewMatches = [...html.matchAll(/<section class="view[^"]*" id="([^"]+)"/g)].map(m => m[1]);
console.log('Views found:', viewMatches);

// Check if any view has inline style
const inlineDisplays = [...html.matchAll(/id="(view-[^"]+)"[^>]*style="([^"]*)"/g)].map(m => [m[1], m[2]]);
console.log('Inline styles on views:', inlineDisplays);
