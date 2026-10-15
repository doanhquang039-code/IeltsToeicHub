import sys, sqlite3
sys.stdout.reconfigure(encoding='utf-8')

db_path = r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

for s in [3901, 3935, 4096, 4108]:
    cur.execute("SELECT step_payload FROM steps WHERE idx = ?", (s,))
    p = cur.fetchone()[0]
    print(f"Step {s}: length {len(p)}")
    try:
        t = p.decode('utf-8', errors='ignore')
        import re
        cmds = re.findall(r'\{"CommandLine":.*?\}|\{"TargetFile":.*?\}', t)
        for c in cmds[:3]:
            print(f"  {c[:120]}")
    except Exception as e:
        print("  Error:", e)
