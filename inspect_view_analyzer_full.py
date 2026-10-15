import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="view-analyzer"')
end = text.find('</section>', start)

chunk = text[start:end+10]
print("LENGTH:", len(chunk))
print("--- FIRST 500 CHARS ---")
print(chunk[:500])
print("--- LAST 500 CHARS ---")
print(chunk[-500:])

# Does chunk contain vocab-list or Negotiate?
print("Contains 'vocab-list'?", 'vocab-list' in chunk)
print("Contains 'Negotiate'?", 'Negotiate' in chunk)
print("Contains 'Danh sách từ'?", 'Danh sách từ' in chunk)
