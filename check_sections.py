with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if '<section class="view' in line:
        print(f"Start view at line {i}: {line.strip()[:60]}".encode('ascii', 'ignore').decode('ascii'))
    if '</section>' in line:
        print(f"End section at line {i}: {line.strip()[:60]}".encode('ascii', 'ignore').decode('ascii'))
