import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT idx, step_payload FROM steps WHERE idx > 3100 AND idx < 4200 ORDER BY idx ASC")
for idx, p in cur.fetchall():
    t = p.decode('utf-8', errors='ignore')
    import re
    cmds = re.findall(r'"CommandLine":\s*"python\s+([^"]+)"', t)
    for c in cmds:
        if not c.startswith('-c'):
            print(f"Step {idx}: python {c}")
