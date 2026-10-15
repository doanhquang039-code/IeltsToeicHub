import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

pos_voc = text.find('id="view-vocabulary"')
pos_prog = text.find('id="view-progress"')
pos_book = text.find('id="view-bookmarks"')
pos_prof = text.find('id="view-profile"')
pos_ana = text.find('id="view-analyzer"')

print("Length of view-vocabulary chunk:", pos_prog - pos_voc)
chunk_voc = text[pos_voc:pos_prog]
print("Open sections in chunk_voc:", chunk_voc.count('<section'))
print("Close sections in chunk_voc:", chunk_voc.count('</section>'))
print("Open divs in chunk_voc:", chunk_voc.count('<div'))
print("Close divs in chunk_voc:", chunk_voc.count('</div>'))

# Let's inspect chunk_ana
end_ana = text.find('</section>', pos_ana)
chunk_ana = text[pos_ana:end_ana+10]
print("\nOpen divs in chunk_ana:", chunk_ana.count('<div'))
print("Close divs in chunk_ana:", chunk_ana.count('</div>'))

# Let's check view-profile chunk
chunk_prof = text[pos_prof:pos_ana]
print("\nOpen divs in chunk_prof:", chunk_prof.count('<div'))
print("Close divs in chunk_prof:", chunk_prof.count('</div>'))
