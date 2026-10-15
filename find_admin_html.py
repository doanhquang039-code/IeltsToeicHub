import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

# Check step 4072 for any occurrence of 371415
cur.execute("SELECT step_payload FROM steps WHERE idx = 4072")
p = cur.fetchone()[0]
print("p len:", len(p))
print("Contains '371415':", b'371415' in p)
print("Contains 'id=\"view-admin\"':", b'id="view-admin"' in p)

# Find all occurrences of b'id="view-admin"' in p
import re
admin_positions = [m.start() for m in re.finditer(b'id="view-admin"', p)]
print("admin_positions:", admin_positions)

for pos in admin_positions:
    dt = p.rfind(b'<!doctype html>', 0, pos)
    end = p.find(b'</html>', pos)
    print(f"  At pos {pos}: dt={dt}, end={end}, len={end-dt+7 if (dt!=-1 and end!=-1) else 0}")
    if dt != -1 and end != -1:
        full_doc = p[dt:end+7]
        with open('recovered_admin_index.html', 'wb') as f:
            f.write(full_doc)
        print("  Wrote recovered_admin_index.html, size:", len(full_doc))
        break
