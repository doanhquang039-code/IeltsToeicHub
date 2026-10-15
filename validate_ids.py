import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

element_ids = set(re.findall(r"\$\('#([a-zA-Z0-9_-]+)'\)", content))
print(f"Total {len(element_ids)} element IDs referenced with $('#...'):")

missing = []
for el_id in sorted(element_ids):
    if f'id="{el_id}"' not in content and f"id='{el_id}'" not in content:
        # Check if dynamically generated in JS template literals
        if f'id="${{item' in content or f'id="${{sk' in content or f'id="${{tab' in content:
            continue
        missing.append(el_id)

print(f"Missing element IDs in static HTML: {missing}")
