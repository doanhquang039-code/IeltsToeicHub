import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

views = re.findall(r'<section class="view[^"]*" id="([^"]+)">([\s\S]*?)(?=<section class="view|</div>\s*<!-- end \.page -->|</main>)', text)

for v_id, v_body in views:
    opens = len(re.findall(r'<div\b', v_body))
    closes = len(re.findall(r'</div\b', v_body))
    diff = opens - closes
    print(f"View {v_id:15}: <div = {opens:3}, </div = {closes:3}, diff = {diff:2}")
