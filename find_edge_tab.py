import subprocess, time, json, urllib.request

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
proc = subprocess.Popen([
    edge_path,
    "--headless",
    "--disable-gpu",
    "--remote-debugging-port=9222",
    "--window-size=1280,800",
    "http://localhost:8080/index.html"
])

time.sleep(2)
try:
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
    target_tab = None
    for t in tabs:
        if "8080" in t.get("url", ""):
            target_tab = t
            break
    if not target_tab:
        target_tab = tabs[0]
    
    ws_url = target_tab.get("webSocketDebuggerUrl")
    print("WebSocket URL:", ws_url)
finally:
    proc.terminate()
