import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

for s in [3486, 3487, 3496, 3497]:
    cur.execute("SELECT step_payload FROM steps WHERE idx = ?", (s,))
    p = cur.fetchone()[0]
    t = p.decode('utf-8', errors='ignore')
    import re
    targets = re.findall(r'"TargetFile":\s*"[^"]+"', t)
    print(f"Step {s}: targets={targets}")
    if targets:
        pos = t.find('CodeContent":"')
        pos_end = t.rfind('","Description"')
        if pos != -1 and pos_end != -1:
            code = t[pos + len('CodeContent":"'):pos_end]
            import json
            try:
                code_str = json.loads('"' + code + '"')
                fname = re.findall(r'[^\\/]+\.py', targets[0])[0]
                with open(fname, 'w', encoding='utf-8') as out:
                    out.write(code_str)
                print(f"  Extracted {fname} (len {len(code_str)})")
            except Exception as e:
                print("  Extract error:", e)
