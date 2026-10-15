import sqlite3

db_path = r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT idx, length(step_payload) FROM steps WHERE instr(step_payload, 'id=\"filtered-vocab-count\"') > 0")
rows = cur.fetchall()
print("Steps with id=\"filtered-vocab-count\":", len(rows))
for r in rows:
    print(r)
