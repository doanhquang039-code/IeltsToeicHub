with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'<section class="view[^"]*" id="([^"]+)"', text))
views_spans = []
for m in matches:
    views_spans.append((m.group(1), m.start()))
views_spans.append(('END', len(text)))

for i in range(len(views_spans)-1):
    vname = views_spans[i][0]
    vstart = views_spans[i][1]
    vend = views_spans[i+1][1]
    vchunk = text[vstart:vend]
    has_vocab_list = 'vocab-list' in vchunk
    has_flashcard = 'flashcard' in vchunk
    print(f"View: {vname:16} | vocab-list: {has_vocab_list} | flashcard: {has_flashcard}")
