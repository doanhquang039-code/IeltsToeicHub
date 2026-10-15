from PIL import Image

# Find the latest user uploaded media
import glob, os

files = glob.glob(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/.user_uploaded/*.png')
latest = max(files, key=os.path.getmtime)
print("Latest media:", latest)

img = Image.open(latest)
w, h = img.size
print(f"Size: {w}x{h}")

# Crop top part (from y=0 to y=200)
crop_top = img.crop((0, 0, w, min(200, h)))
crop_top.save(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/latest_top.png')

# Crop middle part (from y=200 to y=min(400, h))
crop_mid = img.crop((0, 200, w, min(400, h)))
crop_mid.save(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/latest_mid.png')

print("Saved crops!")
