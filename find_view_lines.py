with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if 'id="view-analyzer"' in line:
        print("view-analyzer line:", i)
    if 'id="view-profile"' in line:
        print("view-profile line:", i)
    if 'id="view-overview"' in line:
        print("view-overview line:", i)
