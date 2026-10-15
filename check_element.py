import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I will add an alert immediately after the socialProviders loop to verify
# if the button was actually found!

old_code = """    const socialProviders = ['google', 'github', 'azure']; // Azure = Microsoft trong Supabase
    socialProviders.forEach(provider => {
        $(`#btn-${provider === 'azure' ? 'microsoft' : provider}`)?.addEventListener('click', async () => {
            console.log('Clicked', provider); alert('Đang kết nối ' + provider + '...'); await supabase.auth.signInWithOAuth({ provider, options: { redirectTo: window.location.href } });
        });
    });"""

new_code = """    const socialProviders = ['google', 'github', 'azure']; // Azure = Microsoft trong Supabase
    socialProviders.forEach(provider => {
        const btnId = `#btn-${provider === 'azure' ? 'microsoft' : provider}`;
        const btn = $(btnId);
        if (!btn) {
            alert('Lỗi: Không tìm thấy nút ' + btnId + ' trong DOM!');
        } else {
            btn.addEventListener('click', async () => {
                console.log('Clicked', provider); alert('Đang kết nối ' + provider + '...'); await supabase.auth.signInWithOAuth({ provider, options: { redirectTo: window.location.href } });
            });
        }
    });"""

content = content.replace(old_code, new_code)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Element check alert added")
