import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Target block for flashcard
target_snippet = '''                <!-- Flashcard tương tác -->
                <button type="button" class="flashcard" id="flashcard" onclick="toggleFlashcard()" aria-label="Lật thẻ từ vựng" style="cursor:pointer;">
                  <div class="flashcard-inner">
                    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:8px;">
                       <small id="flashcard-label">Từ 1 trong 5 · Nhấn để lật thẻ</small>
                       <div id="flashcard-badges" style="display:flex; gap:6px;"></div>
                    </div>
                    <div style="display:flex; align-items:center; justify-content:center; gap:8px;">
                       <h2 id="flashcard-word" style="margin:0;">allocate</h2>
                       <button class="speak-btn" id="btn-speak-flashcard" title="Nghe phát âm">🔊</button>
                    </div>
                    <p id="flashcard-detail">/ˈæləkeɪt/ · động từ</p>
                    <p class="reveal-hint" id="flashcard-hint">Chạm để xem nghĩa và ví dụ</p>
                  </div>
                </button>'''

replacement_snippet = '''                <!-- Flashcard tương tác -->
                <div class="flashcard" id="flashcard" onclick="toggleFlashcard()" role="button" tabindex="0" aria-label="Lật thẻ từ vựng" style="cursor:pointer; width:100%; box-sizing:border-box;">
                  <div class="flashcard-inner">
                    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:8px;">
                       <small id="flashcard-label">Từ 1 trong 5 · Nhấn để lật thẻ</small>
                       <div id="flashcard-badges" style="display:flex; gap:6px;"></div>
                    </div>
                    <div style="display:flex; align-items:center; justify-content:center; gap:8px;">
                       <h2 id="flashcard-word" style="margin:0;">allocate</h2>
                       <button class="speak-btn" id="btn-speak-flashcard" title="Nghe phát âm">🔊</button>
                    </div>
                    <p id="flashcard-detail">/ˈæləkeɪt/ · động từ</p>
                    <p class="reveal-hint" id="flashcard-hint">Chạm để xem nghĩa và ví dụ</p>
                  </div>
                </div>'''

# Normalize newlines for matching
c_norm = content.replace('\r\n', '\n')
t_norm = target_snippet.replace('\r\n', '\n')
r_norm = replacement_snippet.replace('\r\n', '\n')

assert t_norm in c_norm, "Target snippet not found in normalized content!"

c_norm_fixed = c_norm.replace(t_norm, r_norm)

# Also remove duplicate event listener at $('#flashcard')?.addEventListener('click'
dup_listener = "$('#flashcard')?.addEventListener('click', () => toggleFlashcard());"
if dup_listener in c_norm_fixed:
    c_norm_fixed = c_norm_fixed.replace(dup_listener, "// $('#flashcard') handled via inline onclick to prevent double toggle")
    print("Replaced duplicate listener!")

# Restore CRLF
content_final = c_norm_fixed.replace('\n', '\r\n')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content_final)

print("Successfully replaced flashcard button with div!")
