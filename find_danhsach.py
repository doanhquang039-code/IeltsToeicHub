import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Danh sách từ', text)]
print("Matches of Danh sách từ:", len(matches))
for pos in matches:
    print(pos, text[pos-60:pos+80].replace('\n', ' '))
