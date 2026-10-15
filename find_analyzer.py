with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'analyzer', text)]
print("Total analyzer occurrences:", len(matches))
for pos in matches:
    line_no = text[:pos].count('\n') + 1
    print(f"L{line_no}: {text[pos-25:pos+45].strip()}")
