import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT idx, length(step_payload) FROM steps WHERE instr(step_payload, '4 KHÔNG GIAN HỌC TẬP') > 0 ORDER BY idx DESC")
rows = cur.fetchall()
print("Steps with '4 KHÔNG GIAN HỌC TẬP':", len(rows))
for r in rows[:10]:
    print(r)
