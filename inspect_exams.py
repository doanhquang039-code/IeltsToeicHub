with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re

# Find courses
courses_match = re.search(r'const courses = \[(.*?)\];', text, re.DOTALL)
if courses_match:
    titles = re.findall(r'title:\s*[\'"]([^\'"]+)[\'"]', courses_match.group(1))
    print(f"Total courses: {len(titles)}")
    for t in titles:
        print(" -", t)

# Find examDatabase keys
exam_db_match = re.search(r'const examDatabase = \{(.*?)\n    \};', text, re.DOTALL)
if exam_db_match:
    keys = re.findall(r'[\'"]([^\'"]+)[\'"]:\s*\{', exam_db_match.group(1))
    print(f"\nTotal examDatabase keys: {len(keys)}")
    for k in keys:
        print(" *", k)
