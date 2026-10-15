import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('test_rebuild.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix flashcard from <button> to <div>
old_fc = '<button type="button" class="flashcard" id="flashcard" onclick="toggleFlashcard()" aria-label="Lật thẻ từ vựng" style="cursor:pointer;">'
new_fc = '<div class="flashcard" id="flashcard" onclick="toggleFlashcard()" role="button" tabindex="0" aria-label="Lật thẻ từ vựng" style="cursor:pointer; width:100%; box-sizing:border-box;">'

assert old_fc in content, "old_fc not found!"

# Find corresponding </button> for flashcard
pos_fc = content.find(old_fc)
pos_hint = content.find('id="flashcard-hint"', pos_fc)
pos_end_fc = content.find('</button>', pos_hint)

content = content[:pos_fc] + new_fc + content[pos_fc+len(old_fc):pos_end_fc] + '</div>' + content[pos_end_fc+len('</button>'):]
print("✓ Fixed flashcard button -> div")

# 2. Extract sections
def extract_section(text, sec_id):
    pattern = rf'(<section class="view[^"]*" id="{sec_id}".*?</section>)'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        raise ValueError(f"Section {sec_id} not found!")
    return m.group(1)

sec_overview = extract_section(content, 'view-overview')
sec_practice = extract_section(content, 'view-practice')
sec_analyzer = extract_section(content, 'view-analyzer')
sec_profile = extract_section(content, 'view-profile')
sec_vocabulary = extract_section(content, 'view-vocabulary')
sec_progress = extract_section(content, 'view-progress')
sec_bookmarks = extract_section(content, 'view-bookmarks')
sec_admin = extract_section(content, 'view-admin')

print("✓ All 8 sections extracted cleanly:")
print(f"  overview: {len(sec_overview)}")
print(f"  practice: {len(sec_practice)}")
print(f"  analyzer: {len(sec_analyzer)}")
print(f"  profile: {len(sec_profile)}")
print(f"  vocabulary: {len(sec_vocabulary)}")
print(f"  progress: {len(sec_progress)}")
print(f"  bookmarks: {len(sec_bookmarks)}")
print(f"  admin: {len(sec_admin)}")

# Find boundary of views in content
# Start is start of view-overview
start_boundary = content.find('<section class="view active" id="view-overview">')
if start_boundary == -1:
    start_boundary = content.find('<section class="view" id="view-overview">')

# End is end of view-admin (or whichever was last)
end_admin = content.find(sec_admin) + len(sec_admin)

reordered_views = "\n\n        ".join([
    sec_overview,
    sec_practice,
    sec_analyzer,
    sec_profile,
    sec_vocabulary,
    sec_progress,
    sec_bookmarks,
    sec_admin
])

content_reordered = content[:start_boundary] + reordered_views + content[end_admin:]

# Verify CSS isolation in <style>
# Make sure .view { display: none !important; } and .view.active { display: block !important; }
if '.view { display: none !important; }' not in content_reordered:
    content_reordered = content_reordered.replace('.view { display: none;', '.view { display: none !important;')
if '.view.active { display: block !important;' not in content_reordered:
    content_reordered = content_reordered.replace('.view.active { display: block;', '.view.active { display: block !important;')

with open('test_rebuild.html', 'w', encoding='utf-8') as f:
    f.write(content_reordered)

print("✓ Successfully saved reordered views to test_rebuild.html!")
