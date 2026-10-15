from PIL import Image

img = Image.open(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/.user_uploaded/media_1791730827205.png')
w, h = img.size
print(f"Image size: {w}x{h}")

# Crop top-left (sidebar area)
crop_sidebar = img.crop((0, 0, 300, h))
crop_sidebar.save(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/crop_sidebar.png')

# Crop bottom area (analyzer area)
crop_bottom = img.crop((0, int(h * 0.7), w, h))
crop_bottom.save(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/crop_bottom.png')

print("Cropped successfully!")
