import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['<main', '</main>', '<div class="page">', '<section class="view"', '</section>']):
        print(f"L{i+1}: {line.strip()[:100]}")
