const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";

const edge = spawn(edgePath, [
    '--headless',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--window-size=1280,800',
    'http://localhost:8080/index.html'
]);

async function run() {
    await new Promise(r => setTimeout(r, 2000));
    
    // Get tab info
    const tabs = await new Promise((resolve, reject) => {
        http.get('http://localhost:9222/json', res => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(JSON.parse(data)));
        }).on('error', reject);
    });

    const tab = tabs.find(t => t.url.includes('8080')) || tabs[0];
    console.log('Connecting to tab:', tab.url);

    const ws = new WebSocket(tab.webSocketDebuggerUrl);

    let id = 1;
    function send(method, params = {}) {
        return new Promise((resolve) => {
            const curId = id++;
            const handler = (event) => {
                const msg = JSON.parse(event.data);
                if (msg.id === curId) {
                    ws.removeEventListener('message', handler);
                    resolve(msg.result);
                }
            };
            ws.addEventListener('message', handler);
            ws.send(JSON.stringify({ id: curId, method, params }));
        });
    }

    await new Promise(resolve => ws.onopen = resolve);
    console.log('WebSocket connected!');

    // Wait 1s for page load
    await new Promise(r => setTimeout(r, 1000));

    // Evaluate showView('analyzer')
    console.log('Calling showView("analyzer")...');
    const evalRes = await send('Runtime.evaluate', {
        expression: `
            showView('analyzer');
            const res = [];
            document.querySelectorAll('.view').forEach(v => {
                const cs = window.getComputedStyle(v);
                res.push({
                    id: v.id,
                    active: v.classList.contains('active'),
                    inlineDisplay: v.style.display,
                    computedDisplay: cs.display,
                    rect: v.getBoundingClientRect()
                });
            });
            JSON.stringify(res);
        `
    });

    console.log('Views state after showView("analyzer"):');
    const viewsState = JSON.parse(evalRes.result.value);
    console.table(viewsState);

    // Capture screenshot
    const screenshot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('edge_analyzer_view.png', Buffer.from(screenshot.data, 'base64'));
    console.log('Screenshot saved to edge_analyzer_view.png!');

    ws.close();
    edge.kill();
    process.exit(0);
}

run().catch(err => {
    console.error('Error:', err);
    edge.kill();
    process.exit(1);
});
