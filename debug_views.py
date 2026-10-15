import sys
sys.stdout.reconfigure(encoding='utf-8')
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
views = re.findall(r'<section class="view[^"]*" id="([^"]+)"', text)
print("Views found:", views)

for v in views:
    pos = text.find(f'id="{v}"')
    # Find next view or </section>
    next_sec = text.find('</section>', pos)
    print(f"View {v}: start={pos}, end={next_sec}")
    
# Check what is inside view-vocabulary, view-profile, view-analyzer
print("\n--- view-vocabulary tail ---")
pos_voc = text.find('id="view-vocabulary"')
end_voc = text.find('</section>', pos_voc)
print(text[end_voc-200:end_voc+100])

print("\n--- view-profile tail ---")
pos_prof = text.find('id="view-profile"')
end_prof = text.find('</section>', pos_prof)
print(text[end_prof-200:end_prof+100])

print("\n--- view-analyzer tail ---")
pos_ana = text.find('id="view-analyzer"')
end_ana = text.find('</section>', pos_ana)
print(text[end_ana-200:end_ana+100])
