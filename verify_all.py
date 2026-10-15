import urllib.request

html = urllib.request.urlopen("http://localhost:8080/").read().decode("utf-8")
checks = [
    ("SheetJS CDN", "xlsx.full.min.js" in html),
    ("Excel sample doc", "Bảng tính Tài chính Doanh nghiệp & Vận hành Logistics Q3" in html),
    ("Custom vocab form", "add-custom-vocab-form" in html),
    ("Custom vocab JS", "handleAddNewWord" in html),
    ("Survey form", "ai-study-plan-form" in html),
    ("AI Roadmap JS", "generateStudyRoadmap" in html),
    ("Landing banner", "NỀN TẢNG LUYỆN THI THÔNG MINH TOEIC & IELTS 4 KỸ NĂNG" in html),
    ("Topbar login button", "topbar-login-btn" in html),
    ("Auth card close X", "closeLoginModal" in html),
]

all_ok = True
for name, ok in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        all_ok = False

if all_ok:
    print("\nALL 9 CHECKS PASSED PERFECTLY ON LIVE SERVER (http://localhost:8080/)!")
else:
    print("\nSOME CHECKS FAILED!")
