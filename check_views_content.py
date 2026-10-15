import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
views = re.findall(r'<section class="view[^"]*" id="([^"]+)">', text)
for v in views:
    idx = text.find(f'id="{v}"')
    end_idx = text.find('</section>', idx)
    content = text[idx:end_idx]
    has_vocab_words = 'Deadline' in content or 'vocab-list' in content
    print(f"View {v}: length={len(content)}, has_vocab_list={has_vocab_words}")
