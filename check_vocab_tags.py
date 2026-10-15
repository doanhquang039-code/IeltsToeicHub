import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('test_rebuild.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx in range(820, 965):
    line = lines[idx]
    if 'flashcard' in line or 'vocab-layout' in line or 'vocab-list' in line:
        print(f"{idx+1}: {line.strip()[:100]}")
