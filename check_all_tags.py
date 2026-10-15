with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

import re
tag_regex = re.compile(r'<\/?([a-zA-Z0-9]+)(\s+[^>]*)?>')

stack = []
void_tags = {'img', 'input', 'br', 'hr', 'meta', 'link', '!doctype'}

for line_idx, line in enumerate(lines):
    for match in tag_regex.finditer(line):
        full = match.group(0)
        tag = match.group(1).lower()
        if tag in void_tags:
            continue
        if full.endswith('/>'):
            continue
        if full.startswith('</'):
            if stack and stack[-1][0] == tag:
                stack.pop()
            else:
                top = stack[-1] if stack else ('NONE', 0)
                print(f"Line {line_idx+1}: Mismatch! Closing </{tag}> but top of stack is <{top[0]}> (opened at line {top[1]})")
        else:
            stack.append((tag, line_idx+1, line.strip()[:40]))

print(f"Total unclosed tags remaining: {len(stack)}")
for s in stack[:10]:
    print(s)
