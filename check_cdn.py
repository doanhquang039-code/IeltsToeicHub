import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

if "cdn.jsdelivr.net/npm/@supabase/supabase-js" in content:
    print("CDN script is in the file")
else:
    print("CDN script is MISSING!")
