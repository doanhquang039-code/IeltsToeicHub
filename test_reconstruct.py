import sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('candidate_1.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Base candidate_1 len:", len(html))
print("Has view-analyzer:", 'id="view-analyzer"' in html)
print("Has view-admin:", 'id="view-admin"' in html)

# Let's inspect inject_admin.py logic
with open('admin_view_snippet.html', 'r', encoding='utf-8') as f:
    admin_view_html = f.read()

with open('admin_js_snippet.js', 'r', encoding='utf-8') as f:
    admin_js_code = f.read()

# 1. Check sidebar nav for admin button
print("Has nav-btn-admin:", 'id="nav-btn-admin"' in html)
# Let's see the nav section in candidate_1.html
nav_start = html.find('<nav class="nav"')
nav_end = html.find('</nav>', nav_start)
print("Current nav in candidate_1:")
print(html[nav_start:nav_end+6])
