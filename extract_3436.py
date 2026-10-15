import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT step_payload FROM steps WHERE idx = 3436")
p = cur.fetchone()[0]

text = p.decode('utf-8', errors='ignore')
pos = text.find('CodeContent":"')
pos_end = text.rfind('","Description"')
if pos != -1 and pos_end != -1:
    code = text[pos + len('CodeContent":"'):pos_end]
    # unescape json string
    import json
    code = json.loads('"' + code + '"')
    print("code len:", len(code))
    with open('apply_all_fixes_restored.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Saved to apply_all_fixes_restored.py!")
