import os, sys

scripts = [
    'update.py',
    'update_login.py',
    'update_auth.py',
    'update_real_auth.py',
    'upgrade_full_features.py',
    'inject_full_engine.py',
    'patch_full_auth.py',
    'upgrade_advanced_suite.py',
    'inject_advanced_engine.py',
    'fix_all_user_feedback.py',
    'update_auth_fix.py',
    'apply_fixes.py',
    'upgrade_all_requested_features.py',
    'upgrade_js_features.py',
    'add_profile_survey.py',
    'apply_alignment_and_view_isolation.py'
]

print("Pipeline scripts:")
for s in scripts:
    print(f"Exists: {s}: {os.path.exists(s)}")
