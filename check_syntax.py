import os
import subprocess

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract script content
start = content.rfind("<script>")
if start != -1:
    end = content.find("</script>", start)
    js_content = content[start+8:end]
    
    with open("temp.js", "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print("Extracted JS. Running node -c temp.js...")
    result = subprocess.run(["node", "-c", "temp.js"], capture_output=True, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
else:
    print("No script tag found")
