import subprocess, time, json, urllib.request

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
proc = subprocess.Popen([
    edge_path,
    "--headless",
    "--disable-gpu",
    "--remote-debugging-port=9222",
    "http://localhost:8080/index.html"
])

time.sleep(2)
try:
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
    print("Edge tabs:", len(tabs))
    print("Tab 0:", tabs[0]['url'])
except Exception as e:
    print("Error:", e)
finally:
    proc.terminate()
