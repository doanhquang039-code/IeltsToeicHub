with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    for tag in ['<aside', '</aside>', '<main', '</main>', 'class="app', 'class="page"', 'id="view-']:
        if tag in line:
            print(f"{idx+1}: {line.strip()[:100]}")
            break
