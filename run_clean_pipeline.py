import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('test_rebuild.html', 'r', encoding='utf-8') as f:
    # First, let's look at test_rebuild.html before apply_reorder_and_fix was run
    pass

# We have candidate_1.html as the clean base!
# Let's run the pipeline on candidate_1.html WITHOUT the broken regex reordering:
with open('candidate_1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update nav
with open('update_nav.py', 'r', encoding='utf-8') as f:
    exec(f.read().replace("'index.html'", "'candidate_1.html'"), {'__name__': '__main__'})

# 2. Update banner
with open('update_banner.py', 'r', encoding='utf-8') as f:
    exec(f.read().replace("'index.html'", "'candidate_1.html'"), {'__name__': '__main__'})

# 3. Inject admin
with open('inject_admin.py', 'r', encoding='utf-8') as f:
    exec(f.read().replace("'index.html'", "'candidate_1.html'"), {'__name__': '__main__'})

# 4. Update right panel
with open('update_right_panel.py', 'r', encoding='utf-8') as f:
    exec(f.read().replace("'index.html'", "'candidate_1.html'"), {'__name__': '__main__'})

# 5. Apply all fixes restored
with open('apply_all_fixes_restored.py', 'r', encoding='utf-8') as f:
    exec(f.read().replace("'index.html'", "'candidate_1.html'"), {'__name__': '__main__'})

# 6. Apply menu2 menu3 fixes
with open('apply_menu2_menu3_fixes.py', 'r', encoding='utf-8') as f:
    exec(f.read().replace("'index.html'", "'candidate_1.html'"), {'__name__': '__main__'})

# 7. Do replace
with open('do_replace.py', 'r', encoding='utf-8') as f:
    exec(f.read().replace("'index.html'", "'candidate_1.html'"), {'__name__': '__main__'})

# 8. Apply alignment and view isolation
with open('apply_alignment_and_view_isolation.py', 'r', encoding='utf-8') as f:
    exec(f.read().replace("'index.html'", "'candidate_1.html'"), {'__name__': '__main__'})

print("Pipeline executed cleanly on candidate_1.html!")
