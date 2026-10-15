with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Check lines 620 to 990
stack = []
for i in range(620, min(1000, len(lines))):
    line = lines[i]
    # find all tags
    import re
    tags = re.findall(r'<(/?[a-zA-Z0-9]+)(?:\s+[^>]*)?>', line)
    for tag in tags:
        if tag.startswith('/'):
            closing = tag[1:].lower()
            if closing in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                continue
            if stack and stack[-1][0] == closing:
                stack.pop()
            else:
                print(f"Line {i+1}: Mismatched closing tag </{closing}>. Expected </{stack[-1][0] if stack else 'NONE'}> (opened line {stack[-1][1] if stack else 'NONE'})")
        else:
            opening = tag.lower()
            if opening in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                continue
            stack.append((opening, i+1))

print("Remaining unclosed tags at line 1000:", stack)
