from PIL import Image

img = Image.open(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/.user_uploaded/media_1791730827205.png')
w, h = img.size

# Check at y=200 (where vocabulary cards are)
# Find the x boundary where sidebar ends and main content begins
for x in range(0, w, 10):
    px = img.getpixel((x, 200))
    # print when color changes from dark to light
    if x in [10, 50, 100, 140, 150, 160, 200, 250, 300]:
        print(f"y=200, x={x}: {px}")

# Now check at y=480 (where analyzer view is)
for x in range(0, w, 10):
    px = img.getpixel((x, 480))
    if x in [10, 50, 100, 140, 150, 160, 200, 250, 300]:
        print(f"y=480, x={x}: {px}")
