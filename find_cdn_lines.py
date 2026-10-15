with open("index.html", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        if 'pdf.js' in line or 'mammoth' in line:
            print(f"{i}: {line.strip()[:100]}".encode('ascii', 'ignore').decode('ascii'))
