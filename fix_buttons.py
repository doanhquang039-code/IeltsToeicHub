import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add type="button" to the social buttons to prevent accidental form submission
content = content.replace('<button class="social-btn" id="btn-google"', '<button type="button" class="social-btn" id="btn-google"')
content = content.replace('<button class="social-btn" id="btn-github"', '<button type="button" class="social-btn" id="btn-github"')
content = content.replace('<button class="social-btn" id="btn-microsoft"', '<button type="button" class="social-btn" id="btn-microsoft"')

# Ensure preventDefault is called in the event listener
old_js = "btn.addEventListener('click', async () => {"
new_js = "btn.addEventListener('click', async (e) => {\n                e.preventDefault();"
content = content.replace(old_js, new_js)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added type='button' and preventDefault")
