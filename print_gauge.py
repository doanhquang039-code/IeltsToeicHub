with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = 71607
print(text[idx:idx+800].encode('ascii', 'ignore').decode('ascii'))
