import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_code = "await supabase.auth.signInWithOAuth({ provider });"
new_code = "console.log('Clicked', provider); alert('Đang kết nối ' + provider + '...'); await supabase.auth.signInWithOAuth({ provider, options: { redirectTo: window.location.href } });"

content = content.replace(old_code, new_code)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated OAuth click handler")
