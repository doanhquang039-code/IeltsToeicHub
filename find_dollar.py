with open("index.html", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        if 'const $$' in line or 'function $$' in line or 'let $$' in line or 'var $$' in line:
            print(f"{i}: {line.strip()}")
