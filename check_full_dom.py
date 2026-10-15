with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

import re

stack = []
void_tags = {'br', 'hr', 'img', 'input', 'meta', 'link'}

for i, line in enumerate(lines, 1):
    tags = re.findall(r'<(/?[a-zA-Z0-9]+)(?:\s+[^>]*)?>', line)
    for tag in tags:
        if tag.startswith('/'):
            closing = tag[1:].lower()
            if closing in void_tags:
                continue
            if stack and stack[-1][0] == closing:
                stack.pop()
            else:
                top = stack[-1] if stack else ('NONE', 0)
                print(f"Line {i}: </{closing}> does not match <{top[0]}> (opened line {top[1]})")
        else:
            opening = tag.lower()
            if opening in void_tags or tag.endswith('/'):
                continue
            stack.append((opening, i))

print("Total unclosed tags at EOF:", len(stack))
for t in stack[-10:]:
    print("Unclosed:", t)
