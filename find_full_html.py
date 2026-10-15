import sqlite3

db_path = r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Find largest blobs that contain <!doctype html> or <!DOCTYPE html>
cur.execute("SELECT idx, length(step_payload) FROM steps WHERE instr(step_payload, 'view-analyzer') > 0 ORDER BY length(step_payload) DESC LIMIT 20")
rows = cur.fetchall()
print("Found steps containing view-analyzer:")
for r in rows:
    print(r)
