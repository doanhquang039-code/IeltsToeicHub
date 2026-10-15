with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

html_part = text[:text.find('<script')]
import re
print("Occurrences of vocab-list in HTML:")
for m in re.finditer(r'vocab-list', html_part):
    pos = m.start()
    line = text.count('\n', 0, pos) + 1
    print(f"Line {line}")
