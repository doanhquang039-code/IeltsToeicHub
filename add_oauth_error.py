import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add error handling to OAuth
old_oauth = "await supabase.auth.signInWithOAuth({ provider, options: { redirectTo: window.location.href } });"
new_oauth = """const { data, error } = await supabase.auth.signInWithOAuth({ provider, options: { redirectTo: window.location.href } });
                if (error) {
                    alert('Lỗi OAuth: ' + error.message);
                    console.error('OAuth Error:', error);
                }"""

content = content.replace(old_oauth, new_oauth)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added error handling to OAuth")
