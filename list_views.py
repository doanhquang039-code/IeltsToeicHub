with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if '<section class="view' in line:
        print(f"Line {idx+1}: {line.strip()}")
    if '</section>' in line:
        # print if it closes a view
        pass
