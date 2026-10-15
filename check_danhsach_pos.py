import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('test_rebuild.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'Danh sách từ vựng' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")
        # check enclosing section
        for b in range(i, max(0, i-200), -1):
            if '<section' in lines[b]:
                print(f"  Enclosing section at line {b+1}: {lines[b].strip()[:80]}")
                break
        for fwd in range(i, min(len(lines), i+200)):
            if '</section>' in lines[fwd]:
                print(f"  Closing section at line {fwd+1}: {lines[fwd].strip()[:80]}")
                break
