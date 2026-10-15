with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

print("pdfjs in index.html:", "pdf.js" in text or "pdfjsLib" in text)
print("mammoth in index.html:", "mammoth" in text)
print("xlsx in index.html:", "xlsx" in text)
