import sqlite3, sys, re
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute('SELECT step_payload FROM steps WHERE idx = 3153')
p = cur.fetchone()[0]
text = p.decode('utf-8', errors='ignore')
print('TargetFile:', re.findall(r'"TargetFile":\s*"[^"]+"', text))
print('CommandLines:', re.findall(r'"CommandLine":\s*"[^"]+"', text))
print('Text snippet:', text[:1000])
