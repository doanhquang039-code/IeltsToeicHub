import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
views = re.findall(r'<section class="view[^"]*" id="([^"]+)"', text)
print("Views:", views)

for v in views:
    # Check if any other element has class="view"
    pass

all_view_classes = re.findall(r'<[a-z0-9]+\s+[^>]*class="[^"]*\bview\b[^"]*"[^>]*>', text)
print("All elements with class 'view':", len(all_view_classes))
for el in all_view_classes:
    print(" -", el[:80])
