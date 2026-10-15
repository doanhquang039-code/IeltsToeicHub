import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT step_payload FROM steps WHERE idx = 4072")
p = cur.fetchone()[0]

for pos in [1371158, 1402921, 1416352, 1525269]:
    print(f"--- Pos {pos} ---")
    print(p[pos-80:pos+120])
    dt = p.rfind(b'<!doctype html>', 0, pos)
    end = p.find(b'</html>', pos)
    print(f"  dt={dt}, end={end}, len={end-dt+7 if (dt!=-1 and end!=-1) else 0}")
