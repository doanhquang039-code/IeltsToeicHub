import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

large_w_re = re.compile(r'width:\s*(?:1240|480|440|430|355)px')
for i, line in enumerate(lines):
    if large_w_re.search(line):
        print(f"Line {i+1}: {line.strip()[:100]}")
