with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re

# Find all occurrences of class="...view..."
matches = re.findall(r'<[a-zA-Z0-9]+\s+[^>]*class=["\'][^"\']*view[^"\']*["\'][^>]*>', text)
for m in matches:
    print(m)
