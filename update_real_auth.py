import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Credentials
old_creds = """    // Thay thế bằng Credentials thật của dự án Supabase
    const SUPABASE_URL = 'https://YOUR_PROJECT_ID.supabase.co';
    const SUPABASE_KEY = 'YOUR_ANON_KEY';
    
    // Khởi tạo Supabase client (hiện tại dùng URL giả nên sẽ catch error để demo UI)
    let supabase = null;
    try {
        supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
    } catch (e) {
        console.warn("Supabase chưa được cấu hình đúng. Dùng dữ liệu mô phỏng.");
    }"""

new_creds = """    const SUPABASE_URL = 'https://tgcgdgmgxjuvwedwcvlf.supabase.co';
    const SUPABASE_KEY = 'sb_publishable_t_n3odLV8Icio8GY1DqSsg_3-KLku0E';
    const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);"""

content = content.replace(old_creds, new_creds)

# Replace initAuth session check
old_init = """        // Kiểm tra session thực tế từ Supabase nếu có
        /*
        supabase?.auth.getSession().then(({ data: { session } }) => {
            if (session) {
                const name = session.user.user_metadata.full_name || session.user.email;
                localStorage.setItem('lingua-user', name);
                showApp(name);
            }
        });
        */"""

new_init = """        // Kiểm tra session thực tế từ Supabase nếu có
        supabase.auth.getSession().then(({ data: { session } }) => {
            if (session) {
                const name = session.user.user_metadata.full_name || session.user.email;
                localStorage.setItem('lingua-user', name);
                showApp(name);
            }
        });"""
content = content.replace(old_init, new_init)

# Replace Send OTP
old_send_otp = """        // Đoạn code thực tế gọi Supabase
        /*
        const { error } = await supabase.auth.signInWithOtp({ email });
        if (error) {
            setAuthMessage(error.message);
            $('#btn-send-otp').disabled = false;
            return;
        }
        */
        
        // Mô phỏng thành công
        setTimeout(() => {
            $('#login-otp-section').classList.add('active');
            $('#btn-send-otp').style.display = 'none';
            setAuthMessage('Đã gửi mã OTP!', false);
        }, 1000);"""

new_send_otp = """        const { error } = await supabase.auth.signInWithOtp({ email });
        if (error) {
            setAuthMessage(error.message);
            $('#btn-send-otp').disabled = false;
            return;
        }
        
        $('#login-otp-section').classList.add('active');
        $('#btn-send-otp').style.display = 'none';
        setAuthMessage('Đã gửi mã OTP! Vui lòng kiểm tra hộp thư email.', false);"""
content = content.replace(old_send_otp, new_send_otp)

# Replace Verify OTP
old_verify_otp = """        // Đoạn code thực tế gọi Supabase
        /*
        const { data, error } = await supabase.auth.verifyOtp({ email, token: otp, type: 'email' });
        if (error) return setAuthMessage('Mã OTP không hợp lệ');
        const user = data.user;
        */
        
        // Mô phỏng
        localStorage.setItem('lingua-user', email);
        showApp(email);"""

new_verify_otp = """        const { data, error } = await supabase.auth.verifyOtp({ email, token: otp, type: 'email' });
        if (error) return setAuthMessage('Mã OTP không hợp lệ hoặc đã hết hạn.');
        
        localStorage.setItem('lingua-user', email);
        showApp(email);"""
content = content.replace(old_verify_otp, new_verify_otp)

# Replace Sign Up
old_signup = """        // Đoạn code thực tế gọi Supabase
        /*
        const { data, error } = await supabase.auth.signUp({ 
            email, password, options: { data: { full_name: name } } 
        });
        if (error) return setAuthMessage(error.message);
        */
        
        // Mô phỏng
        setAuthMessage('Đăng ký thành công! Đang đăng nhập...', false);
        setTimeout(() => {
            localStorage.setItem('lingua-user', name);
            showApp(name);
        }, 1000);"""

new_signup = """        const { data, error } = await supabase.auth.signUp({ 
            email, password, options: { data: { full_name: name } } 
        });
        if (error) return setAuthMessage(error.message);
        
        setAuthMessage('Đăng ký thành công! Vui lòng kiểm tra email để xác nhận.', false);
        if (data.session) {
            localStorage.setItem('lingua-user', name);
            showApp(name);
        }"""
content = content.replace(old_signup, new_signup)

# Replace Social Login
old_social = """            // Đoạn code thực tế gọi Supabase
            /*
            await supabase.auth.signInWithOAuth({ provider });
            */
            
            // Mô phỏng
            const mockName = `${provider.charAt(0).toUpperCase() + provider.slice(1)} User`;
            localStorage.setItem('lingua-user', mockName);
            showApp(mockName);"""

new_social = """            await supabase.auth.signInWithOAuth({ provider });"""
content = content.replace(old_social, new_social)

# Replace Sign Out
old_signout = """        // Đoạn code thực tế
        // await supabase?.auth.signOut();"""

new_signout = """        await supabase.auth.signOut();"""
content = content.replace(old_signout, new_signout)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Real Auth enabled")
