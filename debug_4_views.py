with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re

views = ['progress', 'bookmarks', 'profile', 'analyzer']
for v in views:
    pattern = r'<section class="view[^"]*" id="view-' + v + r'".*?</section>'
    m = re.search(pattern, text, re.DOTALL)
    if m:
        print(f"view-{v} found! Length: {len(m.group(0))}")
        # check if it has opening and closing tags balance inside
        chunk = m.group(0)
        open_divs = chunk.count('<div')
        close_divs = chunk.count('</div>')
        print(f"  open divs: {open_divs}, close divs: {close_divs}")
    else:
        print(f"view-{v} NOT FOUND with regex!")
