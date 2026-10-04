import glob
import re
import os

files = sorted(glob.glob('**/*.html', recursive=True))

resource_hints = '''  <!-- Resource Hints & DNS Prefetching for Speed -->
  <link rel="dns-prefetch" href="https://www.googletagmanager.com">
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="dns-prefetch" href="https://fonts.gstatic.com">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://www.googletagmanager.com">
  <meta http-equiv="content-language" content="en-IN, hi-IN">'''

smo_extra = '''  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Rentlyo Property Management Platform">
  <meta name="twitter:image:alt" content="Rentlyo Property Management Platform">'''

updated_pages = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    orig_c = c

    # 1. Add Resource Hints if not present
    if 'rel="dns-prefetch"' not in c:
        # Insert after <meta charset="UTF-8"> or viewport
        if '<meta name="viewport"' in c:
            c = re.sub(r'(<meta name="viewport"[^>]*>)', r'\1\n' + resource_hints, c, count=1)

    # 2. Add SMO dimensions if not present
    if 'property="og:image:width"' not in c and 'property="og:image"' in c:
        c = re.sub(r'(<meta property="og:image"[^>]*>)', r'\1\n' + smo_extra, c, count=1)

    # 3. Image tag optimization
    # Header logo: fetchpriority="high" decoding="async"
    c = re.sub(
        r'<img\s+src="([^"]*rentlyo-logo\.svg)"\s+alt="([^"]*)"\s+class="([^"]*)"(?!\s+fetchpriority)([^>]*)>',
        r'<img src="\1" alt="\2" class="\3" fetchpriority="high" decoding="async"\4>',
        c
    )
    # Footer logo or any other images: loading="lazy" decoding="async"
    # Match images that don't have loading="
    def fix_img(m):
        tag = m.group(0)
        if 'loading=' not in tag and 'fetchpriority=' not in tag:
            # Add loading="lazy" decoding="async"
            tag = tag[:-1].strip() + ' loading="lazy" decoding="async">'
        elif 'decoding=' not in tag:
            tag = tag[:-1].strip() + ' decoding="async">'
        return tag

    c = re.sub(r'<img\s+[^>]*>', fix_img, c)

    # Specific fix for index.html footer logo missing width/height
    c = c.replace('<img src="assets/rentlyo-logo.svg" alt="Rentlyo" class="h-8 w-auto">', '<img src="assets/rentlyo-logo.svg" alt="Rentlyo" class="h-8 w-auto" width="130" height="36" loading="lazy" decoding="async">')
    c = c.replace('<img src="assets/rentlyo-icon.svg" class="w-5 h-5" alt="Icon">', '<img src="assets/rentlyo-icon.svg" class="w-5 h-5" alt="Rentlyo App Icon" width="20" height="20" loading="lazy" decoding="async">')

    if c != orig_c:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        updated_pages += 1
        print(f"Optimized technical assets in: {f}")

print(f"\nTotal files updated with performance and SMO tags: {updated_pages}")
