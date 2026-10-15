import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('candidate_1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's track sections properly using tag stack!
lines = text.splitlines()

stack = []
for i, line in enumerate(lines):
    if '<section' in line:
        count = line.count('<section')
        # check id
        import re
        ids = re.findall(r'<section[^>]*id="([^"]+)"', line)
        print(f"Line {i+1} OPEN section (depth before={len(stack)}): {ids}")
        for _ in range(count):
            stack.append((i+1, ids))
    if '</section>' in line:
        count = line.count('</section>')
        for _ in range(count):
            opened = stack.pop() if stack else None
            print(f"Line {i+1} CLOSE section (opened at {opened[0]} id={opened[1]}, depth after={len(stack)})")
