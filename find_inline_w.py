import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

inline_fixed = re.findall(r'style=["\'][^"\']*(?:min-width|width)\s*:\s*(\d{3,}px)[^"\']*["\']', text)
print("Inline fixed widths >= 100px:", set(inline_fixed))

# Let's see which lines they occur on
for w in set(inline_fixed):
    matches = re.finditer(rf'style=["\'][^"\']*{w}[^"\']*["\']', text)
    for m in matches:
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + 40)
        print(f"[{w}]:", text[start:end].replace('\n', ' '))
