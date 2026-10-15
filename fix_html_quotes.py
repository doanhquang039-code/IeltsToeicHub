import subprocess
import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# English word-internal apostrophe: e.g. don't, Henderson's, o'clock, etc.
# Match single quote between letters if not already escaped
pattern = r"(?<!\\)(?<=[a-zA-Z])'(?=[a-zA-Z])"
matches = len(re.findall(pattern, text))
print(f"Found {matches} unescaped word apostrophes.")
text = re.sub(pattern, r"\'", text)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

# Run check_syntax
res = subprocess.run(["python", "check_syntax.py"], capture_output=True, text=True)
print(res.stdout)
print(res.stderr)
