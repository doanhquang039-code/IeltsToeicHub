import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('final_clean_index.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

stack = []
views = []
for i, line in enumerate(lines):
    if '<section' in line:
        count = line.count('<section')
        ids = re.findall(r'<section[^>]*id="([^"]+)"', line)
        for _ in range(count):
            stack.append((i, ids[0] if ids else None, len(stack)))
    if '</section>' in line:
        count = line.count('</section>')
        for _ in range(count):
            opened = stack.pop() if stack else None
            if opened and opened[1] and opened[1].startswith('view-'):
                views.append({
                    'id': opened[1],
                    'start_line': opened[0] + 1,
                    'end_line': i + 1,
                    'depth': opened[2]
                })

print("Views in final_clean_index.html:")
for v in views:
    print(v)
print("Remaining open sections in stack:", len(stack))
