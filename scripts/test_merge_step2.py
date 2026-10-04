with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Match Section 7 (Screenshots)
s7_m = re.search(r'\s*<!-- SECTION 7: SCREENSHOT PREVIEWS -->\s*<section class="py-12[^"]*bg-white overflow-hidden">(.*?)</section>', content, re.DOTALL)
assert s7_m is not None, "Section 7 match failed"
s7_full = s7_m.group(0)
s7_inner = s7_m.group(1).strip()

# Match Section 8 (Video preview)
s8_m = re.search(r'\s*<!-- SECTION 8: VIDEO WALKTHROUGH PREVIEW[^>]*-->\s*<section class="py-12[^"]*bg-brand-surface border-y border-brand-border-light">(.*?)</section>', content, re.DOTALL)
assert s8_m is not None, "Section 8 match failed"
s8_full = s8_m.group(0)
s8_inner = s8_m.group(1).strip()

# Extract the video cards from Section 8 (the 2 video cards are inside <div class="grid grid-cols-1 md:grid-cols-2 gap-8">...</div>)
v_cards_m = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\s*<!-- Video 1 Preview Card -->.*?</div>\s*</div>\s*</div>)', s8_inner, re.DOTALL)
assert v_cards_m is not None, "Video cards match failed"
video_cards_html = v_cards_m.group(1)

print("Screenshots inner len:", len(s7_inner))
print("Video cards len:", len(video_cards_html))
print("Extraction success!")
