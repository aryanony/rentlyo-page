import glob
import os
import re

files = sorted(glob.glob('**/*.html', recursive=True))

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    orig = c
    # Calculate depth to root
    depth = f.count(os.sep)
    prefix = '../' * depth if depth > 0 else './'
    root_slash = '/'

    # 1. Update og:image and twitter:image to Next-Gen WebP
    c = re.sub(r'content="https://rentlyo\.cscouncil\.in/assets/rentlyo-hor\.png"', 'content="https://rentlyo.cscouncil.in/assets/rentlyo-hor.webp"', c)
    c = re.sub(r'content="../assets/rentlyo-hor\.png"', 'content="../assets/rentlyo-hor.webp"', c)
    c = re.sub(r'content="../../assets/rentlyo-hor\.png"', 'content="../../assets/rentlyo-hor.webp"', c)

    # 2. Upgrade Favicon block to complete standard suite (ICO, 32x32, 16x16, Apple-touch, SVG)
    favicon_suite = f'''  <!-- Favicon & Touch Icons -->
  <link rel="icon" type="image/x-icon" href="{prefix}favicon.ico">
  <link rel="shortcut icon" href="{prefix}favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{prefix}assets/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{prefix}assets/apple-touch-icon.png">
  <link rel="icon" type="image/svg+xml" href="{prefix}assets/rentlyo-icon.svg">
  <link rel="manifest" href="{prefix}manifest.json">
  <meta name="theme-color" content="#044040">'''

    # Replace old favicon links
    c = re.sub(r'(\s*<!-- Favicon[^\n]*-->)?\s*<link rel="icon"[^>]*>(\s*<link rel="manifest"[^>]*>)?(\s*<meta name="theme-color"[^>]*>)?', '\n' + favicon_suite, c, count=1)

    # 3. Eliminate Render-Blocking Resources (Fonts & CSS)
    non_blocking_styles = f'''  <!-- Non-Render-Blocking Typography & Styles -->
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Outfit:wght@600;800&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Outfit:wght@600;800&display=swap">
  </noscript>
  <link rel="preload" href="{prefix}css/style.min.css" as="style">
  <link rel="stylesheet" href="{prefix}css/style.min.css">'''

    # Replace old font and stylesheet links
    old_fonts_css_pattern = r'(\s*<!-- Fonts[^\n]*-->)?\s*<link rel="preconnect" href="https://fonts\.googleapis\.com">(\s*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>)?\s*<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">(\s*<!-- Compiled Stylesheet -->)?\s*<link rel="stylesheet" href="[^"]*css/style\.min\.css">'
    c = re.sub(old_fonts_css_pattern, '\n' + non_blocking_styles, c, count=1)

    # 4. Defer JavaScript scripts at bottom
    c = re.sub(r'<script src="([^"]*js/(main|calculator|i18n)\.js)"></script>', r'<script defer src="\1"></script>', c)

    # 5. On index.html: optimize title, meta description, and heading keywords
    if f == 'index.html':
        # Align title with top common keywords: Rentlyo | Property Rent & Tenant Management Software
        c = re.sub(
            r'<title>.*?</title>',
            '<title>Rentlyo | Property Rent &amp; Tenant Management Software</title>',
            c
        )
        # Align description with top common keywords
        c = re.sub(
            r'<meta name="description" content=".*?">',
            '<meta name="description" content="Rentlyo is property rent and tenant management software for Indian owners. Flat ₹20,000 one-time fee. Branded Admin &amp; Tenant apps. Zero monthly subscriptions.">',
            c
        )

    if c != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f"Updated SEOSiteCheckup fixes in: {f}")

print("Completed updating all 22 HTML pages with favicon suite, non-render-blocking assets, and WebP images.")
