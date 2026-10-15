with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

idx_page = text.find('<div class="page">')
print("page starts at:", idx_page)

# Find all view IDs
import re
views = re.findall(r'<section class="view[^"]*" id="([^"]+)"', text)
for v in views:
    pos = text.find(f'id="{v}"')
    # count open and close divs between idx_page and pos
    sub = text[idx_page:pos]
    diff = sub.count('<div') - sub.count('</div>')
    print(f"View {v} is at char {pos}. Open div depth from .page: {diff}")
