import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

for s in [3436, 3465, 3537]:
    cur.execute("SELECT step_payload FROM steps WHERE idx = ?", (s,))
    p = cur.fetchone()[0]
    print(f"--- Step {s} (len {len(p)}) ---")
    t = p.decode('utf-8', errors='ignore')
    import re
    targets = re.findall(r'"TargetFile":\s*"[^"]+"', t)
    cmds = re.findall(r'"CommandLine":\s*"[^"]+"', t)
    print("  targets:", targets)
    print("  cmds:", cmds)
    if not targets and not cmds:
        print("  Snippet:", t[:300])
