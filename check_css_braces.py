with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

css = text[text.find('<style>')+7:text.find('</style>')]

# Check brace balance in CSS
open_braces = css.count('{')
close_braces = css.count('}')
print(f"CSS open braces: {open_braces}, close braces: {close_braces}")

if open_braces != close_braces:
    print("WARNING: CSS braces mismatched!")
    # Find where mismatch happens
    count = 0
    lines = css.split('\n')
    for i, line in enumerate(lines):
        count += line.count('{') - line.count('}')
        if count < 0:
            print(f"Line {i+1}: Negative brace count! {line}")
            break
