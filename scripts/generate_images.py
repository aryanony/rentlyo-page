from PIL import Image
import os

assets_dir = 'assets'

# 1. Load icon image
icon_path = os.path.join(assets_dir, 'rentlyo-icon.png')
if os.path.exists(icon_path):
    img = Image.open(icon_path).convert('RGBA')

    # Generate root favicon.ico (16, 32, 48)
    favicon_ico_path = 'favicon.ico'
    img.save(favicon_ico_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print("Generated: favicon.ico")

    # Generate assets/favicon.ico
    img.save(os.path.join(assets_dir, 'favicon.ico'), format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print("Generated: assets/favicon.ico")

    # Generate apple-touch-icon.png (180x180)
    apple_icon = img.resize((180, 180), Image.Resampling.LANCZOS)
    apple_icon.save(os.path.join(assets_dir, 'apple-touch-icon.png'), format='PNG', optimize=True)
    apple_icon.save('apple-touch-icon.png', format='PNG', optimize=True)
    print("Generated: apple-touch-icon.png")

    # Generate 32x32 and 16x16 PNGs
    img.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(assets_dir, 'favicon-32x32.png'), 'PNG')
    img.resize((16, 16), Image.Resampling.LANCZOS).save(os.path.join(assets_dir, 'favicon-16x16.png'), 'PNG')
    print("Generated: favicon-32x32.png and favicon-16x16.png")

# 2. Convert all PNGs in assets to WebP
png_files = [
    'rentlyo-hor.png',
    'rentlyo-icon.png',
    'rentlyo-logo.png',
    'arya_plaza_full.png',
    'logo.png',
    'rentlyo_full.png'
]

for p in png_files:
    full_p = os.path.join(assets_dir, p)
    if os.path.exists(full_p):
        webp_name = os.path.splitext(p)[0] + '.webp'
        webp_path = os.path.join(assets_dir, webp_name)
        im = Image.open(full_p).convert('RGBA')
        im.save(webp_path, format='WEBP', quality=90, method=6)
        print(f"Converted {p} -> {webp_name} ({os.path.getsize(webp_path)} bytes)")

print("All image conversions complete!")
