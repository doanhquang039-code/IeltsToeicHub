import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT step_payload FROM steps WHERE idx = 4072")
p = cur.fetchone()[0]

pos = 1371158
dt = p.rfind(b'<!doctype html>', 0, pos)
if dt == -1: dt = p.rfind(b'<!DOCTYPE html>', 0, pos)
end = p.find(b'</html>', pos)

print(f"dt={dt}, end={end}, len={end-dt+7 if (dt!=-1 and end!=-1) else 0}")
if dt != -1 and end != -1:
    doc = p[dt:end+7]
    print("Doc len:", len(doc))
    print("Doc start:", doc[:100])
    print("Doc end:", doc[-100:])
    with open('perfect_recovered_index.html', 'wb') as f:
        f.write(doc)
    print("Wrote perfect_recovered_index.html successfully!")
