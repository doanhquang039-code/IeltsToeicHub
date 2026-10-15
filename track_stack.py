with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Let's track open tags from line 535 (<div class="app">) to line 1225 (<section class="view" id="view-analyzer">)
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
            # Close tag
            if stack and stack[-1] == tag_name:
                stack.pop()
            else:
                print(f"Line {line_num}: Unmatched close tag </{tag_name}>! Current top of stack: {stack[-1] if stack else 'EMPTY'}")
        else:
            # Open tag
            stack.append(tag_name)

print(f"Stack at line 1225 (start of view-analyzer): {stack}")
