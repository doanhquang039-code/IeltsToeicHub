import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute('SELECT step_payload FROM steps WHERE idx = 3157')
p = cur.fetchone()[0]
print(p.decode('utf-8', errors='ignore'))
