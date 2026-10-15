import shutil, os, sys
sys.stdout.reconfigure(encoding='utf-8')

# Copy candidate_1.html to test_rebuild.html
shutil.copyfile('candidate_1.html', 'test_rebuild.html')
print("1. Copied candidate_1.html to test_rebuild.html (size:", os.path.getsize('test_rebuild.html'), ")")

# We will test each script modifying test_rebuild.html
def run_script_on_file(script_path, target_file='test_rebuild.html'):
    with open(script_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Replace 'index.html' with target_file
    code_mod = code.replace("'index.html'", f"'{target_file}'").replace('"index.html"', f'"{target_file}"')
    
    # execute
    globs = {'__name__': '__main__'}
    exec(code_mod, globs)
    print(f"Executed {script_path} -> {target_file} size is now {os.path.getsize(target_file)}")

print("\n--- Running pipeline ---")
for script in [
    'update_nav.py',
    'update_banner.py',
    'inject_admin.py',
    'update_right_panel.py',
    'apply_all_fixes_restored.py',
    'apply_menu2_menu3_fixes.py',
    'do_replace.py',
    'apply_alignment_and_view_isolation.py'
]:
    print(f"\nRunning {script}...")
    run_script_on_file(script)

print("\n--- Final Check on test_rebuild.html ---")
with open('test_rebuild.html', 'r', encoding='utf-8') as f:
    final_text = f.read()

print("Final size:", len(final_text))
print("Has view-overview:", 'id="view-overview"' in final_text)
print("Has view-practice:", 'id="view-practice"' in final_text)
print("Has view-analyzer:", 'id="view-analyzer"' in final_text)
print("Has view-profile:", 'id="view-profile"' in final_text)
print("Has view-vocabulary:", 'id="view-vocabulary"' in final_text)
print("Has view-admin:", 'id="view-admin"' in final_text)
print("Has Admin Dashboard:", 'Admin Dashboard' in final_text)
print("Has KHONG GIAN QUAN TRI:", 'KHÔNG GIAN QUẢN TRỊ' in final_text)
print("Has syncAdminExamsToSystem:", 'syncAdminExamsToSystem' in final_text)
