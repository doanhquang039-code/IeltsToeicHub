import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

views = re.findall(r'id=["\']view-([^"\']+)["\']', text)
print('Views found:', views)

modals = re.findall(r'id=["\']([^"\']*(?:modal|screen|backdrop)[^"\']*)["\']', text)
print('Modals/Backdrops found:', modals)

# Check all media query contents
mq_blocks = re.findall(r'(@media[^{]+\{[\s\S]*?\n    \})', text)
print(f'Total media query blocks: {len(mq_blocks)}')
for b in mq_blocks:
    print('--- MQ ---')
    print(b[:120].strip() + '...')
