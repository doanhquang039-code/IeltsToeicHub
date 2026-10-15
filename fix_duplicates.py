import sys

file_path = r"e:\EngLish-IE-Toeic\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# We need to find the duplicated block.
# We know it starts with `const SUPABASE_URL` and ends with `setAuthMessage('');\n    });\n\n    initAuth();`
start_marker = "const SUPABASE_URL = 'https://tgcgdgmgxjuvwedwcvlf.supabase.co';"
end_marker = "setAuthMessage('');\n    });"

# Find one instance of the block
idx1 = content.find(start_marker)
idx2 = content.find(end_marker, idx1) + len(end_marker)

if idx1 != -1 and idx2 != -1:
    block = content[idx1:idx2]
    
    # The full string that replaced `renderCourses();` is:
    # block + "\n\n    initAuth();\n"
    # Wait, let's just do a regex or string replacement.
    
    # Replace all occurrences of block + some spaces + initAuth();
    import re
    # Match the block, followed by any whitespace, followed by initAuth();
    pattern = re.escape(block) + r"\s*initAuth\(\);\s*"
    
    # We will replace it with empty string, but keep the renderCourses() which comes after.
    # Actually, the original replacement was: block + "\n    initAuth();\n    renderCourses();"
    # So `renderCourses();` is still there.
    # Let's replace the pattern with just empty string.
    cleaned_content = re.sub(pattern, "", content)
    
    # Now we need to insert the block ONE time, at the very beginning of the script tag (or right after the variable declarations)
    # Let's insert it right after `const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];`
    insertion_point = "const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];"
    
    one_time_block = "\n\n    " + block + "\n\n    initAuth();\n"
    
    final_content = cleaned_content.replace(insertion_point, insertion_point + one_time_block)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print("Fixed duplicates")
else:
    print("Could not find the block")
