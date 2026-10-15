import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT step_payload FROM steps WHERE idx = 3648")
p = cur.fetchone()[0]
print("Step 3648 payload len:", len(p))

import re
matches = [m.start() for m in re.finditer(b'<!doctype html>', p, re.IGNORECASE)]
print("Doctypes count in 3648:", len(matches))
for i, pos in enumerate(matches):
    end = p.find(b'</html>', pos)
    print(f"Doc {i}: start {pos}, end {end}, len {end - pos + 7 if end != -1 else 0}")
    if end != -1 and (end - pos + 7) > 300000:
        chunk = p[pos:end+7]
        print(f"  Starts with: {chunk[:60]}")
        print(f"  Ends with: {chunk[-60:]}")
        print(f"  Contains view-admin: {b'id=\"view-admin\"' in chunk}")
        print(f"  Contains KHONG GIAN QUAN TRI: {b'KH\\xc3\\x94NG GIAN QU\\xe1\\xba\\xa2N TR\\xe1\\xbb\\x8a' in chunk}")
        with open('candidate_3648.html', 'wb') as out:
            out.write(chunk)
        print("  Saved candidate_3648.html!")
