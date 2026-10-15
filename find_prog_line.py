with open("index.html", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        if 'id="view-progress"' in line:
            print(f"view-progress line: {i}")
