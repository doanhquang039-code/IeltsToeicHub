with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_a = text.find('id="view-analyzer"')
pos_b = text.find('</section>', pos_a)
chunk = text[pos_a:pos_b]

import re
# check for negative margins or position absolute/fixed
print("Negative margins in analyzer:", re.findall(r'margin[^;:]*:\s*-[0-9]', chunk))
print("Position fixed/absolute in analyzer:", re.findall(r'position:\s*(?:fixed|absolute)', chunk))
print("Width 100vw or 100% in analyzer:", re.findall(r'width:\s*(?:100vw|100%)', chunk))
