import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT step_payload FROM steps WHERE idx = 4072")
p = cur.fetchone()[0]

# Extract create_admin_snippet.py
pos1 = p.find(b'admin_view_html = \'\'\'')
pos1_end = p.find(b'\'\'\'\n', pos1 + 20)
admin_view_html = p[pos1 + len(b'admin_view_html = \'\'\''):pos1_end].decode('utf-8')
print("admin_view_html len:", len(admin_view_html))
with open('admin_view_snippet.html', 'w', encoding='utf-8') as f:
    f.write(admin_view_html)
print("Saved admin_view_snippet.html!")

# Extract create_admin_js.py
pos2 = p.find(b'admin_js_code = \'\'\'')
pos2_end = p.find(b'\'\'\'\n', pos2 + 20)
admin_js_code = p[pos2 + len(b'admin_js_code = \'\'\''):pos2_end].decode('utf-8')
print("admin_js_code len:", len(admin_js_code))
with open('admin_js_snippet.js', 'w', encoding='utf-8') as f:
    f.write(admin_js_code)
print("Saved admin_js_snippet.js!")
