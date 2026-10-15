with open('recovered_index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('<script>')
print('script_pos:', pos)
lines = text[:pos].splitlines()
print('Number of lines before script:', len(lines))
for idx, l in enumerate(lines):
    if 'id="view-' in l:
        print(f"{idx+1}: {l.strip()}")
