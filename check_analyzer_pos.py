import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="view-analyzer"')
print("pos of view-analyzer:", pos)
if pos != -1:
    print(text[pos-50:pos+300])
