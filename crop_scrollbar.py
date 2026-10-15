from PIL import Image

img = Image.open(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/.user_uploaded\media_1791734131185.png')
w, h = img.size
crop_scroll = img.crop((w - 50, 0, w, h))
crop_scroll.save(r'C:/Users/admoi/.gemini/antigravity-ide/brain/6ddaaadb-e7a8-4052-83b9-c01fb37afc86/latest_scroll.png')
