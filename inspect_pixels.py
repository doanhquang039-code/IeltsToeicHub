from PIL import Image

img = Image.open(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/.user_uploaded/media_1791730827205.png')
w, h = img.size

# Let's inspect column x=10 across all y
# In sidebar, color should be dark green rgb(12, 31, 24)
for y in range(0, h, 20):
    pixel = img.getpixel((10, y))
    print(f"y={y:3d}, x=10: pixel={pixel}")
