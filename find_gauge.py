with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('target-gauge')
print("target-gauge index:", idx)
if idx != -1:
    print(text[idx-50:idx+300].encode('ascii', 'ignore').decode('ascii'))
