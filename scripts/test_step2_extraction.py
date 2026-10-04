with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# 1. Locate Section #live-demo
sec_live_demo_m = re.search(r'(<!-- SECTION 6: KHUD DEKHO.*?-->\s*<section id="live-demo".*?)(?=<!-- SECTION 6: INTERACTIVE COST CALCULATOR|\Z)', content, re.DOTALL)
assert sec_live_demo_m is not None, "Could not find #live-demo section"

# 2. Locate Section 7 (Screens carousel)
sec_screens_m = re.search(r'(<!-- SECTION 7: INTERACTIVE SCREENSHOT GALLERY.*?-->\s*<section class="py-12[^"]*bg-white overflow-hidden">.*?)(?=<!-- SECTION 8: VIDEO WALKTHROUGH|\Z)', content, re.DOTALL)
assert sec_screens_m is not None, "Could not find screens carousel section"
sec_screens_full = sec_screens_m.group(1)

# 3. Locate Section 8 (Video walkthrough)
sec_video_m = re.search(r'(<!-- SECTION 8: VIDEO WALKTHROUGH PREVIEW.*?-->\s*<section class="py-12[^"]*bg-brand-surface border-y border-brand-border-light">.*?)(?=<!-- SECTION 7: DEMO NAHI — ASLI HAI|\Z)', content, re.DOTALL)
assert sec_video_m is not None, "Could not find video walkthrough section"
sec_video_full = sec_video_m.group(1)

print("Found #live-demo, screens carousel, and video section successfully!")

# Let's extract the Carousel Container from Section 7
# The carousel container starts with <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8"> ... up to </section>
carousel_inner_m = re.search(r'<div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8">\s*(<div class="flex flex-col md:flex-row md:items-end justify-between.*?)</div>\s*</section>', sec_screens_full, re.DOTALL)
assert carousel_inner_m is not None, "Could not extract carousel inner HTML"
carousel_html = carousel_inner_m.group(1)

# Let's extract the 2 Video Cards from Section 8
# The video cards are inside <div class="grid grid-cols-1 md:grid-cols-2 gap-8"> ... </div>
videos_inner_m = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\s*<!-- Video 1 Preview Card -->.*?</div>\s*<!-- Video 2 Preview Card -->.*?</div>\s*</div>)', sec_video_full, re.DOTALL)
assert videos_inner_m is not None, "Could not extract video cards HTML"
videos_html = videos_inner_m.group(1)

print("Extracted carousel and video cards successfully!")
