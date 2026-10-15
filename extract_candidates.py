import sys, sqlite3
sys.stdout.reconfigure(encoding='utf-8')

db_path = r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT step_payload FROM steps WHERE idx = 4072")
payload = cur.fetchone()[0]

import re
matches = [m.start() for m in re.finditer(b'<!doctype html>', payload, re.IGNORECASE)]
print("Matches count:", len(matches))
for i, pos in enumerate(matches):
    end = payload.find(b'</html>', pos)
    print(f"Match {i}: start {pos}, end {end}, length {end - pos + 7 if end != -1 else 0}")
    if end != -1 and (end - pos + 7) > 300000:
        html = payload[pos:end+7]
        print(f"  Starts with: {html[:60]}")
        print(f"  Ends with: {html[-60:]}")
        print(f"  Contains view-analyzer: {b'view-analyzer' in html}")
        print(f"  Contains Admin Dashboard: {b'Admin Dashboard' in html}")
        print(f"  Contains S\xe1\xbb\x95 tay t\xe1\xbb\xab v\xe1\xbb\xb1ng: {b'filtered-vocab-count' in html}")
        with open(f'candidate_{i}.html', 'wb') as out:
            out.write(html)
        print(f"  Written to candidate_{i}.html")
