import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

void_tags = {'img', 'input', 'br', 'hr', 'meta', 'link'}
stack = []

for line_no, line in enumerate(lines, start=1):
    # Strip comments
    line_clean = re.sub(r'<!--.*?-->', '', line)
    # Find all tags
    for match in re.finditer(r'<(/?[a-zA-Z0-9]+)(\s+[^>]*)?/?>', line_clean):
        tag_str = match.group(0)
        tag_name = match.group(1).lower()
        
        if tag_name.startswith('/'):
            close_tag = tag_name[1:]
            if not stack:
                print(f"L{line_no}: Unexpected closing tag </{close_tag}>")
            elif stack[-1][0] == close_tag:
                stack.pop()
            else:
                print(f"L{line_no}: Mismatched </{close_tag}>, expected </{stack[-1][0]}> (opened at L{stack[-1][1]})")
        elif tag_str.endswith('/>') or tag_name in void_tags:
            continue
        else:
            # Check id or class if view
            tag_id = ""
            m_id = re.search(r'id=["\']([^"\']+)["\']', tag_str)
            if m_id:
                tag_id = f"#{m_id.group(1)}"
            stack.append((tag_name, line_no, tag_id))

print("Total unclosed tags in entire file:", len(stack))
for t in stack[-10:]:
    print(f"  Unclosed <{t[0]}{t[2]}> at L{t[1]}")
