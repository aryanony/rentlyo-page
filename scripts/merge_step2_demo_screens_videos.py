import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate #live-demo
s_demo_start = content.find('<!-- SECTION 6: KHUD DEKHO, VISHWAS KARO')
assert s_demo_start != -1, "Cannot find #live-demo start"
s_demo_end = content.find('<!-- SECTION 6: INTERACTIVE COST CALCULATOR', s_demo_start)
assert s_demo_end != -1, "Cannot find #live-demo end"

# Locate Section 7 (Screenshots)
s_screens_start = content.find('<!-- SECTION 7: SCREENSHOT PREVIEWS -->')
assert s_screens_start != -1, "Cannot find Section 7 start"
s_screens_end = content.find('<!-- SECTION 8: VIDEO WALKTHROUGH PREVIEW', s_screens_start)
assert s_screens_end != -1, "Cannot find Section 7 end"
screens_section_full = content[s_screens_start:s_screens_end]

# Locate Section 8 (Video walkthrough)
s_video_start = s_screens_end
s_video_end = content.find('<!-- SECTION 9: LIVE PROOF', s_video_start)
assert s_video_end != -1, "Cannot find Section 8 end"
video_section_full = content[s_video_start:s_video_end]

print("Found all sections for Step 2:")
print(f"  #live-demo: [{s_demo_start}:{s_demo_end}] ({s_demo_end - s_demo_start} chars)")
print(f"  Screenshots: [{s_screens_start}:{s_screens_end}] ({s_screens_end - s_screens_start} chars)")
print(f"  Video section: [{s_video_start}:{s_video_end}] ({s_video_end - s_video_start} chars)")

# Extract Carousel Inner HTML (from Section 7)
carousel_track_m = re.search(r'<div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8">\s*(<div class="flex flex-col md:flex-row md:items-end justify-between.*?</div>\s*<div id="carousel-dots".*?</div>)\s*</div>\s*</section>', screens_section_full, re.DOTALL)
assert carousel_track_m is not None, "Carousel track match failed"
carousel_inner_html = carousel_track_m.group(1).strip()

# Extract Video Cards from Section 8
video_cards_m = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\s*<!-- Video 1 Preview Card -->.*?</div>\s*<!-- Video 2 Preview Card -->.*?</div>\s*</div>)', video_section_full, re.DOTALL)
assert video_cards_m is not None, "Video cards match failed"
video_cards_html = video_cards_m.group(1).strip()

# Extract the two portal cards from current #live-demo
demo_cards_m = re.search(r'(<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\s*<!-- Admin / Owner App Live Card -->.*?</div>\s*<!-- Tenant Companion App Live Card -->.*?</div>\s*</div>)', content[s_demo_start:s_demo_end], re.DOTALL)
assert demo_cards_m is not None, "Demo cards match failed"
demo_cards_html = demo_cards_m.group(1).strip()

# Extract the personal walkthrough banner
walkthrough_banner_m = re.search(r'(<!-- Personal Guided Walkthrough Callout -->\s*<div class="p-6 sm:p-8 rounded-3xl bg-amber-50/70.*?</div>\s*</div>\s*</div>)', content[s_demo_start:s_demo_end], re.DOTALL)
assert walkthrough_banner_m is not None, "Walkthrough banner match failed"
walkthrough_banner_html = walkthrough_banner_m.group(1).strip()

# Build the unified #live-demo section
new_unified_live_demo = f'''<!-- SECTION 5: KHUD DEKHO, VISHWAS KARO — COMPLETE INTERACTIVE EXPERIENCE CENTER -->
  <section id="live-demo" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-white border-b border-brand-border-light">
    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-12 sm:space-y-16 lg:space-y-20">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <div class="badge-teal" data-i18n="demo_eyebrow">KHUD DEKHO, VISHWAS KARO • INTERACTIVE EXPERIENCE CENTER</div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark" data-i18n="demo_title">
          Live demo, real screens aur complete video walkthrough.
        </h2>
        <p class="text-base sm:text-lg text-gray-600" data-i18n="demo_subtitle">
          Ye koi mockup nahi hai. Live web portals test karein, actual screens swipe karein, ya 5-minute video walkthrough dekhein.
        </p>
      </div>

      <!-- Experience Part 1: Live Web Apps & Native Android Sandboxes -->
      {demo_cards_html}

      <!-- Experience Part 2: Interactive Real Screen Previews (Carousel) -->
      <div class="pt-8 border-t border-brand-border-light space-y-6 sm:space-y-8">
        {carousel_inner_html}
      </div>

      <!-- Experience Part 3: Video Walkthroughs & Guided Founder Tour -->
      <div class="pt-8 border-t border-brand-border-light space-y-8">
        <div class="text-center max-w-3xl mx-auto space-y-2">
          <span class="badge-gold">5-Minute Video Tours</span>
          <h3 class="text-2xl sm:text-3xl font-extrabold text-brand-dark">
            Watch Rentlyo in action before deciding
          </h3>
          <p class="text-xs sm:text-sm text-gray-600 max-w-xl mx-auto">
            See the exact click-by-click workflows in high definition on genuine Android and desktop setups.
          </p>
        </div>

        {video_cards_html}

        {walkthrough_banner_html}
      </div>

    </div>
  </section>

  '''

# Replace current #live-demo with the new unified section
content = content[:s_demo_start] + new_unified_live_demo + content[s_demo_end:]

# Now remove the old Section 7 (Screenshots) and Section 8 (Videos)
assert screens_section_full in content, "screens_section_full missing"
content = content.replace(screens_section_full, '', 1)

assert video_section_full in content, "video_section_full missing"
content = content.replace(video_section_full, '', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Unified #live-demo created, Sections 7 & 8 removed from index.html!")
