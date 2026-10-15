with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_a = text.find('id="view-analyzer"')
pos_b = text.find('id="view-admin"')

analyzer_html = text[pos_a:pos_b]
print("Analyzer HTML length:", len(analyzer_html))
print("Is 'vocab-list' in analyzer?", 'vocab-list' in analyzer_html)
print("Is 'Deadline' in analyzer?", 'Deadline' in analyzer_html)
print("Is 'Từ vựng' in analyzer?", 'Từ vựng' in analyzer_html)
