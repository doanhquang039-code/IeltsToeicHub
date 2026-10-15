import sys, sqlite3
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT idx, length(step_payload) FROM steps WHERE instr(step_payload, 'write_to_file') > 0 AND instr(step_payload, 'index.html') > 0 ORDER BY idx DESC")
for idx, l in cur.fetchall():
    print(f"write_to_file with index.html at step {idx}, payload len {l}")
