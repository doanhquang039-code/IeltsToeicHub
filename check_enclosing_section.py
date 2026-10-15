import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 82710 # position of Danh sách từ vựng

# Find the opening <section before pos
sec_open = text.rfind('<section', 0, pos)
sec_id = text[sec_open:text.find('>', sec_open)+1]
print("Section opening before 'Danh sách từ vựng':", sec_id)

# Find the closing </section> after pos
sec_close = text.find('</section>', pos)
print("Distance to </section>:", sec_close - pos)

# Find the next <section after pos
next_sec = text.find('<section', pos)
print("Next section after pos:", text[next_sec:text.find('>', next_sec)+1] if next_sec != -1 else 'NONE')
