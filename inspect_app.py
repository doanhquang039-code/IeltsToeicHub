import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

views = re.findall(r'<section class="view" id="([^"]+)"', text)
print("Current views in index.html:", views)

nav_buttons = re.findall(r'<button [^>]*data-view="([^"]+)"[^>]*>([^<]+)</button>', text)
print("Current nav buttons:", nav_buttons)
