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

    await new Promise(r => setTimeout(r, 1000));

    // Close auth modal, fake login or close modal, then click analyzer button
    const evalRes = await send('Runtime.evaluate', {
        expression: `
            (() => {
                const authScreen = document.getElementById('auth-screen');
                if (authScreen) authScreen.style.display = 'none';
                const appMain = document.getElementById('app-main');
                if (appMain) {
                    appMain.classList.add('authenticated');
                    appMain.style.display = 'flex';
                }
                
                showView('profile');

                const v = document.getElementById('view-profile');
                
                return JSON.stringify({
                    id: v?.id,
                    className: v?.className,
                    parentElement: v?.parentElement?.tagName + '#' + v?.parentElement?.id + '.' + v?.parentElement?.className,
                    offsetWidth: v?.offsetWidth,
                    offsetHeight: v?.offsetHeight,
                    clientRect: v?.getBoundingClientRect(),
                    childrenCount: v?.children.length
                });
            })()
        `
    });

    console.log('Eval result:', evalRes.result.value);

    // Capture screenshot
    const screenshot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('edge_test_click_analyzer.png', Buffer.from(screenshot.data, 'base64'));
    console.log('Saved edge_test_click_analyzer.png');

    ws.close();
    edge.kill();
    process.exit(0);
}

run().catch(err => {
    console.error(err);
    edge.kill();
    process.exit(1);
});
