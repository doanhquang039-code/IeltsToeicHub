with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

pos_app = text.find('id="app-main"')
pos_sidebar = text.find('class="sidebar"')
pos_main = text.find('<main')
pos_page = text.find('class="page"')
pos_ana = text.find('id="view-analyzer"')

print("id=app-main:", pos_app)
print("sidebar:", pos_sidebar)
print("main:", pos_main)
print("page:", pos_page)
print("view-analyzer:", pos_ana)

# Check all closing tags between pos_app and pos_ana
chunk = text[pos_app:pos_ana]
print("</main> in chunk before view-analyzer?", '</main>' in chunk)
print("</aside> in chunk before view-analyzer?", '</aside>' in chunk)
print("class=\"sidebar\" close count:", chunk.count('</aside>'))
print("Open divs in chunk:", chunk.count('<div'))
print("Close divs in chunk:", chunk.count('</div>'))
print("Open sections in chunk:", chunk.count('<section'))
print("Close sections in chunk:", chunk.count('</section>'))
