import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find all nav buttons
nav_part = text[text.find('<nav class="nav">'):text.find('</nav>')]
print("Nav buttons:")
print(nav_part)
