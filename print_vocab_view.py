import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

pos_voc = text.find('id="view-vocabulary"')
pos_prog = text.find('id="view-progress"')
print(text[pos_voc:pos_prog])
