import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update container horizontal padding on mobile
content = re.sub(r'px-4 sm:px-6 lg:px-8', 'px-3.5 sm:px-6 lg:px-8', content)

# 2. Update vertical section padding on mobile
content = re.sub(r'py-16 sm:py-24', 'py-10 sm:py-16 lg:py-20', content)
content = re.sub(r'py-12 sm:py-20', 'py-8 sm:py-14 lg:py-18', content)

# 3. Update space-y on mobile
content = re.sub(r'space-y-16', 'space-y-8 sm:space-y-12 lg:space-y-16', content)
content = re.sub(r'space-y-12', 'space-y-6 sm:space-y-10 lg:space-y-12', content)

# 4. Update large card padding on mobile so content isn't compressed
content = re.sub(r'p-8 sm:p-12', 'p-4 sm:p-8 lg:p-12', content)
content = re.sub(r'p-8 sm:p-10', 'p-4 sm:p-7 lg:p-10', content)
content = re.sub(r'p-6 sm:p-8', 'p-3.5 sm:p-6 lg:p-8', content)
content = re.sub(r'p-6 rounded-2xl', 'p-4 sm:p-5 lg:p-6 rounded-2xl', content)
content = re.sub(r'p-6 rounded-3xl', 'p-4 sm:p-5 lg:p-6 rounded-3xl', content)
content = re.sub(r'p-6 bg-white rounded-2xl', 'p-4 sm:p-5 lg:p-6 bg-white rounded-2xl', content)

# 5. Fix Section 7 Verticals Grid (tab view + 8th card for perfect 2-col on tab and 4-col on desktop)
old_grid = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
new_grid = '<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 sm:gap-5 lg:gap-6">'
content = content.replace(old_grid, new_grid, 1)

# Clean up Vertical 7 col-span
content = content.replace('md:col-span-2 lg:col-span-1', '')

# Insert Vertical 8 right after Vertical 7 if not already present
if 'Mixed-Use & Custom Portfolios' not in content:
    vertical_7_end = '<!-- Vertical 7: Housing Societies & RWAs -->'
    vertical_8 = '''<!-- Vertical 8: Mixed-Use & Custom Portfolios -->
        <div class="p-4 sm:p-5 lg:p-6 rounded-2xl bg-white border border-brand-border-light shadow-sm hover-lift glass-sheen space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-brand-gold/20 to-amber-100 border border-brand-gold/30 text-amber-900 flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6 text-brand-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
            </div>
            <div>
              <div class="text-[10px] font-bold text-amber-800 uppercase tracking-wider">Multi-Tier Complexes</div>
              <h3 class="text-lg font-bold text-brand-dark">Mixed-Use & Custom Portfolios</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">
              Ground-floor retail shops with residential flats above and basement godown storage. Unified cashflow, split power tariffs, and consolidated owner statements.
            </p>
            <ul class="text-xs text-gray-500 space-y-1.5 pt-1">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-brand-gold"></span>
                <span>Combined commercial + residential hisaab</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-brand-gold"></span>
                <span>Custom database rules configured by founder</span>
              </li>
            </ul>
          </div>
          <div class="pt-3 border-t border-gray-100">
            <a href="https://wa.me/916205650368?text=Hello%20Aaryan,%20I%20have%20a%20mixed-use%20property%20and%20need%20custom%20setup." target="_blank" rel="noopener noreferrer" class="text-xs font-bold text-brand-teal hover:text-brand-gold transition inline-flex items-center gap-1.5">
              <span>Discuss Custom Setup</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>

      '''
    
    # We find where Vertical 7 ends before </div> <!-- 7 Property Verticals Grid -->
    target_needle = '<!-- Vertical 7: Housing Societies & RWAs -->'
    idx = content.find(target_needle)
    if idx != -1:
        # Find the closing </div> of card 7
        end_card_7 = content.find('</div>\n\n      </div>', idx)
        if end_card_7 != -1:
            content = content[:end_card_7 + 6] + '\n\n        ' + vertical_8 + content[end_card_7 + 6:]
            print("Successfully added Vertical 8 (Mixed-Use & Custom Portfolios)!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile padding and tab grid optimization complete!")
