import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('candidate_1.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Using exact 1-indexed lines:
# view-overview: 603 to 774
# view-practice: 776 to 819
# view-vocabulary: 821 to 963
# view-progress: 965 to 972
# view-bookmarks: 975 to 997
# view-profile: 1000 to 1222
# view-analyzer: 1225 to 1344
# view-admin: 1349 to 1527

def get_block(start, end):
    return lines[start-1:end]

block_overview = get_block(603, 774)
block_practice = get_block(776, 819)
block_vocab = get_block(821, 963)
block_progress = get_block(965, 972)
block_bookmarks = get_block(975, 997)
block_profile = get_block(1000, 1222)
block_analyzer = get_block(1225, 1344)
block_admin = get_block(1349, 1527)

# Fix flashcard button in block_vocab:
vocab_text = "".join(block_vocab)
old_fc = '<button type="button" class="flashcard" id="flashcard" onclick="toggleFlashcard()" aria-label="Lật thẻ từ vựng" style="cursor:pointer;">'
new_fc = '<div class="flashcard" id="flashcard" onclick="toggleFlashcard()" role="button" tabindex="0" aria-label="Lật thẻ từ vựng" style="cursor:pointer; width:100%; box-sizing:border-box;">'
if old_fc in vocab_text:
    pos_fc = vocab_text.find(old_fc)
    pos_hint = vocab_text.find('id="flashcard-hint"', pos_fc)
    pos_end_fc = vocab_text.find('</button>', pos_hint)
    vocab_text = vocab_text[:pos_fc] + new_fc + vocab_text[pos_fc+len(old_fc):pos_end_fc] + '</div>' + vocab_text[pos_end_fc+len('</button>'):]
    print("✓ Fixed flashcard button -> div in block_vocab")
block_vocab = [vocab_text]

# Pre-overview lines (from line 1 to 602):
head_lines = lines[:602]

# Post-admin lines (from line 1528 to end):
tail_lines = lines[1527:]

# Desired visual order matching Sidebar Menu:
# 1. overview (Trang chủ)
# 2. practice (1. Luyện đề 4 kỹ năng)
# 3. analyzer (2. AI Phân tích tài liệu)
# 4. profile (3. Hồ sơ & Lộ trình AI)
# 5. vocabulary (4. Sổ tay từ vựng)
# 6. progress (Tiến độ)
# 7. bookmarks (Đã lưu)
# 8. admin (⚡ Admin Dashboard)

reordered_lines = (
    head_lines +
    block_overview + ['\n'] +
    block_practice + ['\n'] +
    block_analyzer + ['\n'] +
    block_profile + ['\n'] +
    block_vocab + ['\n'] +
    block_progress + ['\n'] +
    block_bookmarks + ['\n'] +
    block_admin +
    tail_lines
)

with open('final_clean_index.html', 'w', encoding='utf-8') as f:
    f.writelines(reordered_lines)

print("✓ Saved final_clean_index.html!")
