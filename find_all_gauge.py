with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = 0
while True:
    idx = text.find('target-gauge', idx)
    if idx == -1:
        break
    print("Found at:", idx)
    print(text[idx-20:idx+250].encode('ascii', 'ignore').decode('ascii'))
    idx += 12
