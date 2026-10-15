import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'C:\Users\admoi\.gemini\antigravity-ide\conversations\6ddaaadb-e7a8-4052-83b9-c01fb37afc86.db')
cur = conn.cursor()

cur.execute("SELECT step_payload FROM steps WHERE idx = 4072")
p = cur.fetchone()[0]

pos = 1371158
# Search backwards for <!doctype html> or <!DOCTYPE html>
dt1 = p.rfind(b'<!doctype html>', 0, pos)
dt2 = p.rfind(b'<!DOCTYPE html>', 0, pos)
dt3 = p.rfind(b'<html', 0, pos)
print(f"dt1 (doctype lowercase): {dt1}")
print(f"dt2 (doctype uppercase): {dt2}")
print(f"dt3 (<html): {dt3}")

# What is around dt3?
print("Around dt3:", p[dt3-30:dt3+100])

# And search forward for </html> from pos
end = p.find(b'</html>', pos)
print(f"end of html: {end}")
print("Around end:", p[end-100:end+30])

if dt3 != -1 and end != -1:
    actual_start = p.rfind(b'<!', 0, dt3)
    if actual_start == -1 or (dt3 - actual_start > 50):
        actual_start = dt3
    print(f"actual_start: {actual_start}")
    print("Actual start text:", p[actual_start:actual_start+80])
    doc = p[actual_start:end+7]
    print("Extracted length:", len(doc))
    with open('exact_index.html', 'wb') as f:
        f.write(doc)
    print("Saved to exact_index.html!")
