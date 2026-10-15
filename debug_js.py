import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the supabase init to catch errors and alert them
old_init = """    const SUPABASE_URL = 'https://tgcgdgmgxjuvwedwcvlf.supabase.co';
    const SUPABASE_KEY = 'sb_publishable_t_n3odLV8Icio8GY1DqSsg_3-KLku0E';
    const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);"""

new_init = """    const SUPABASE_URL = 'https://tgcgdgmgxjuvwedwcvlf.supabase.co';
    const SUPABASE_KEY = 'sb_publishable_t_n3odLV8Icio8GY1DqSsg_3-KLku0E';
    let supabase;
    try {
        if (!window.supabase) {
            alert('Lỗi: Thư viện Supabase không tải được. Vui lòng kiểm tra mạng hoặc tắt trình chặn quảng cáo.');
        } else {
            supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
        }
    } catch (err) {
        alert('Lỗi khởi tạo Supabase: ' + err.message);
    }"""

content = content.replace(old_init, new_init)

# Add a global error listener to alert any other errors
global_err = """    window.addEventListener('error', function(e) {
        alert('Lỗi JavaScript: ' + e.message + ' ở dòng ' + e.lineno);
    });\n"""

# Insert global err right after <script>
if "window.addEventListener('error'" not in content:
    content = content.replace("<script>\n    const courses", "<script>\n" + global_err + "    const courses")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Debug JS added")
