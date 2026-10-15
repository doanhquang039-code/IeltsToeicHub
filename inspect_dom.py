with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

idx_page = text.find('<div class="page">')
idx_analyzer = text.find('id="view-analyzer"')
idx_main = text.find('</main>')

sub = text[idx_page:idx_analyzer]
open_divs = sub.count('<div')
close_divs = sub.count('</div>')
print(f"Between <div class='page'> and #view-analyzer: Open divs={open_divs}, Close divs={close_divs}")

# Check what comes right before #view-analyzer
print("100 chars before view-analyzer:\n", text[idx_analyzer-200:idx_analyzer])

# Check after view-analyzer
sub2 = text[idx_analyzer:idx_main]
print("After view-analyzer up to </main>:\n", sub2[-300:])
