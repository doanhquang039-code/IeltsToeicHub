with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

stack = []
import re

tag_regex = re.compile(r'<\/?([a-zA-Z0-9]+)(\s+[^>]*)?>')

for line_num in range(535, 1226):
    line = lines[line_num - 1]
    for match in tag_regex.finditer(line):
        full = match.group(0)
        tag_name = match.group(1).lower()
        if tag_name in ['img', 'input', 'br', 'hr', 'meta', 'link']:
            continue
        if full.endswith('/>'):
            continue
        if full.startswith('</'):
            if stack:
                popped = stack.pop()
                if popped[0] != tag_name:
                    print(f"Line {line_num}: mismatched close </{tag_name}>, expected </{popped[0]}> (opened at line {popped[1]})")
        else:
            stack.append((tag_name, line_num, line.strip()[:60]))

print("Unclosed tags at line 1225:")
for tag in stack:
    print(tag)
