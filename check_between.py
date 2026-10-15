import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

pos_prof = text.find('id="view-profile"')
end_prof = text.find('</section>', pos_prof)
pos_ana = text.find('id="view-analyzer"')

print(f"end_prof={end_prof}, pos_ana={pos_ana}")
print("Between view-profile and view-analyzer:\n", text[end_prof:pos_ana+50])
