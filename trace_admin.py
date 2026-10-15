import sqlite3, sys, re
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT idx, step_payload FROM steps WHERE idx > 3150 AND idx < 3200")
for idx, p in cur.fetchall():
    t = p.decode('utf-8', errors='ignore')
    if 'create_admin' in t or 'admin' in t.lower():
        cmds = re.findall(r'"CommandLine":\s*"[^"]+"', t)
        targets = re.findall(r'"TargetFile":\s*"[^"]+"', t)
        if cmds or targets:
            print(f"Step {idx}: cmds={cmds}, targets={targets}")
