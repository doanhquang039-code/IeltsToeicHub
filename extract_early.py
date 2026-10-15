import sqlite3, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

for s in [3140, 3141, 3144, 3145, 3150, 3151, 3152, 3153, 3156, 3157, 3164, 3165]:
    cur.execute("SELECT step_payload FROM steps WHERE idx = ?", (s,))
    p = cur.fetchone()[0]
    t = p.decode('utf-8', errors='ignore')
    targets = re.findall(r'"TargetFile":\s*"([^"]+)"', t)
    if targets:
        fname = targets[0].split('\\')[-1].split('/')[-1]
        pos = t.find('CodeContent":"')
        pos_end = t.rfind('","Description"')
        if pos != -1 and pos_end != -1:
            code = t[pos + len('CodeContent":"'):pos_end]
            try:
                code_str = json.loads('"' + code + '"')
                with open(fname, 'w', encoding='utf-8') as out:
                    out.write(code_str)
                print(f"Extracted {fname} from step {s} (len {len(code_str)})")
            except Exception as e:
                print(f"Error {fname}:", e)
