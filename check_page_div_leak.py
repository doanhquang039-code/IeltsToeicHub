import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_page = text.find('<div class="page">')
pos_analyzer = text.find('id="view-analyzer"')
pos_page_close = text.find('</div>', pos_page)

print(f"pos_page: {pos_page}")
print(f"pos_analyzer: {pos_analyzer}")
print(f"pos_page_close: {pos_page_close}")

# Let's count open/close divs between pos_page and pos_analyzer
sub = text[pos_page:pos_analyzer]
print("Opens between page and analyzer:", sub.count('<div'))
print("Closes between page and analyzer:", sub.count('</div'))
