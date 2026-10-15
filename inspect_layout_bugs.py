import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check viewport meta tag
viewport_match = re.search(r'<meta\s+name=["\']viewport["\'][^>]*>', text)
print("Viewport meta:", viewport_match.group(0) if viewport_match else "None")

# Let's check overflow-x or fixed width styles in html
fixed_widths = re.findall(r'(width\s*:\s*\d{3,}px)', text)
print("Large fixed widths count:", len(fixed_widths))
print("Sample fixed widths:", set(fixed_widths[:20]))

# Let's check grid-template-columns with fixed px
fixed_grids = re.findall(r'grid-template-columns\s*:\s*([^;\}]+)', text)
print("\nGrid template columns samples:")
for g in set(fixed_grids[:15]):
    print(" -", g.strip())
