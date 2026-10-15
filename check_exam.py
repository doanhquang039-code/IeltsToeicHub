with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'title:\s*[\'"]([^\'"]*IELTS[^\'"]*)[\'"]', text)
print("IELTS titles in courses:", matches)

keys = re.findall(r'[\'"]([^\'"]*IELTS[^\'"]*)[\'"]:\s*\{', text)
print("IELTS keys in examDatabase:", keys)
