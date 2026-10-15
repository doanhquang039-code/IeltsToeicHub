import sqlite3

db_path = r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT idx, step_payload FROM steps WHERE idx >= 4072 AND idx <= 4250 ORDER BY idx ASC")
for idx, payload in cur.fetchall():
    try:
        text = payload.decode('utf-8', errors='ignore')
        if any(kw in text for kw in ['run_command', 'replace_file_content', 'write_to_file', 'multi_replace']):
            # find function name and arguments
            import json, re
            calls = re.findall(r'\{"CommandLine":.*?\}|\{"TargetFile":.*?\}', text)
            for c in calls:
                print(f"Step {idx}: {c[:120]}")
    except:
        pass
