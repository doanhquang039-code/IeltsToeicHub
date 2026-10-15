import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('candidate_1.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="view-' in l:
        print(f"{i+1}: {l.strip()[:100]}")

print("Total lines:", len(lines))
