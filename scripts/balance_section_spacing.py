import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero section
old_hero = '<section id="hero" class="relative overflow-hidden pt-6 pb-10 sm:pt-10 sm:pb-16 lg:pt-12 lg:pb-16 xl:pt-14 xl:pb-20 bg-gradient-to-b from-brand-surface via-white to-brand-surface">'
new_hero = '<section id="hero" class="relative overflow-hidden pt-12 pb-16 sm:pt-16 sm:pb-20 lg:pt-20 lg:pb-24 xl:pt-24 xl:pb-28 bg-gradient-to-b from-brand-surface via-white to-brand-surface">'
if old_hero in content:
    content = content.replace(old_hero, new_hero, 1)
    print("1. Hero section updated")

# 2. Problems section
old_problems = '<section id="problems" class="py-10 sm:py-16 lg:py-20 bg-white border-y border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-6 sm:space-y-10 lg:space-y-12">'
new_problems = '<section id="problems" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-white border-y border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-12 lg:space-y-16">'
if old_problems in content:
    content = content.replace(old_problems, new_problems, 1)
    print("2. Problems section updated")

# 3. Solution section
old_solution = '<section id="solution" class="py-10 sm:py-16 lg:py-20 bg-brand-surface border-b border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-6 sm:space-y-10 lg:space-y-12 lg:space-y-16">'
new_solution = '<section id="solution" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-brand-surface border-b border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-12 lg:space-y-16">'
if old_solution in content:
    content = content.replace(old_solution, new_solution, 1)
    print("3. Solution section updated")

# 4. Features section
old_features = '<section id="features" class="py-10 sm:py-16 lg:py-20 bg-white border-b border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-6 sm:space-y-10 lg:space-y-12 lg:space-y-16">'
new_features = '<section id="features" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-white border-b border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-12 lg:space-y-16">'
if old_features in content:
    content = content.replace(old_features, new_features, 1)
    print("4. Features section updated")

# 5. Device & Payment Flexibility section
old_flex = '<section class="py-10 sm:py-16 lg:py-20 bg-brand-surface border-b border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-6 sm:space-y-10 lg:space-y-12">'
new_flex = '<section class="py-12 sm:py-16 lg:py-20 xl:py-24 bg-brand-surface border-b border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-10 lg:space-y-12">'
if old_flex in content:
    content = content.replace(old_flex, new_flex, 1)
    print("5. Device/Payment Flexibility section updated")

# 6. Live demo section
old_demo = '<section id="live-demo" class="py-10 sm:py-16 lg:py-20 bg-white border-b border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-6 sm:space-y-10 lg:space-y-12">'
new_demo = '<section id="live-demo" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-white border-b border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-12 lg:space-y-16">'
if old_demo in content:
    content = content.replace(old_demo, new_demo, 1)
    print("6. Live demo section updated")

# 7. Calculator section
old_calc = '<section id="calculator" class="py-10 sm:py-16 lg:py-20 bg-brand-dark text-white relative overflow-hidden">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 relative z-10">\n      <div class="text-center max-w-3xl mx-auto mb-16">'
new_calc = '<section id="calculator" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-brand-dark text-white relative overflow-hidden">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 relative z-10">\n      <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-12 lg:mb-16">'
if old_calc in content:
    content = content.replace(old_calc, new_calc, 1)
    print("7. Calculator section updated")

# 8. Real screens preview section
old_screens = '<section class="py-10 sm:py-16 lg:py-20 bg-white overflow-hidden">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8">\n      <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">'
new_screens = '<section class="py-12 sm:py-16 lg:py-20 xl:py-24 bg-white overflow-hidden">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8">\n      <div class="flex flex-col md:flex-row md:items-end justify-between mb-6 sm:mb-8 lg:mb-10">'
if old_screens in content:
    content = content.replace(old_screens, new_screens, 1)
    print("8. Real screens section updated")

# 9. Video tours & APK Sandboxes section
old_tours = '<section class="py-10 sm:py-16 lg:py-20 bg-brand-surface border-y border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8">\n      <div class="text-center max-w-3xl mx-auto mb-16">'
new_tours = '<section class="py-12 sm:py-16 lg:py-20 xl:py-24 bg-brand-surface border-y border-brand-border-light">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8">\n      <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-10 lg:mb-12">'
if old_tours in content:
    content = content.replace(old_tours, new_tours, 1)

old_tour_inner = '<div class="mb-12 bg-white rounded-3xl p-3.5 sm:p-6 lg:p-8 border border-brand-border-light shadow-card space-y-6 hover-lift">'
new_tour_inner = '<div class="mb-8 sm:mb-10 lg:mb-12 bg-white rounded-3xl p-3.5 sm:p-6 lg:p-8 border border-brand-border-light shadow-card space-y-6 hover-lift">'
if old_tour_inner in content:
    content = content.replace(old_tour_inner, new_tour_inner, 1)
print("9. Video tours section updated")

# 10. Live proof section
old_proof = '<section id="live-proof" class="py-10 sm:py-16 lg:py-20 bg-white">'
new_proof = '<section id="live-proof" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-white">'
if old_proof in content:
    content = content.replace(old_proof, new_proof, 1)
print("10. Live proof section updated")

# 11. Verticals section
old_verticals = '<section id="verticals" class="py-10 sm:py-16 lg:py-20 bg-brand-surface border-t border-brand-border-light relative overflow-hidden">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-6 sm:space-y-10 lg:space-y-12 lg:space-y-16">'
new_verticals = '<section id="verticals" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-brand-surface border-t border-brand-border-light relative overflow-hidden">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-12 lg:space-y-16">'
if old_verticals in content:
    content = content.replace(old_verticals, new_verticals, 1)
print("11. Verticals section updated")

# 12. Founder section
old_founder = '<section id="founder" class="py-10 sm:py-16 lg:py-20 bg-brand-surface border-y border-brand-border-light">'
new_founder = '<section id="founder" class="py-12 sm:py-16 lg:py-20 xl:py-24 bg-brand-surface border-y border-brand-border-light">'
if old_founder in content:
    content = content.replace(old_founder, new_founder, 1)
print("12. Founder section updated")

# 13. Pricing section
old_pricing_start = '<section id="pricing" class="py-10 sm:py-16 lg:py-20 bg-white">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8">\n      \n      <!-- Section Header (Page 8) -->\n      <div class="text-center max-w-3xl mx-auto mb-16">'
new_pricing_start = '<section id="pricing" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-white">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8">\n      \n      <!-- Section Header (Page 8) -->\n      <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-12 lg:mb-16">'
assert old_pricing_start in content, "old_pricing_start not found"
content = content.replace(old_pricing_start, new_pricing_start, 1)

old_pricing_grid = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">'
new_pricing_grid = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8 sm:mb-12 lg:mb-16">'
assert old_pricing_grid in content, "old_pricing_grid not found"
content = content.replace(old_pricing_grid, new_pricing_grid, 1)

old_pricing_box1 = '<div class="bg-gradient-to-br from-[#f8fbfb] to-[#edf6f7] rounded-3xl p-4 sm:p-8 lg:p-12 border border-brand-teal/20 shadow-lg mb-16 hover-lift">'
new_pricing_box1 = '<div class="bg-gradient-to-br from-[#f8fbfb] to-[#edf6f7] rounded-3xl p-4 sm:p-8 lg:p-12 border border-brand-teal/20 shadow-lg mb-8 sm:mb-12 lg:mb-16 hover-lift">'
assert old_pricing_box1 in content, "old_pricing_box1 not found"
content = content.replace(old_pricing_box1, new_pricing_box1, 1)

old_pricing_box2 = '<div class="bg-gradient-to-br from-brand-dark via-[#042830] to-brand-dark rounded-3xl p-4 sm:p-8 lg:p-12 text-white border border-white/10 shadow-2xl mb-16 hover-lift relative overflow-hidden">'
new_pricing_box2 = '<div class="bg-gradient-to-br from-brand-dark via-[#042830] to-brand-dark rounded-3xl p-4 sm:p-8 lg:p-12 text-white border border-white/10 shadow-2xl mb-8 sm:mb-12 lg:mb-16 hover-lift relative overflow-hidden">'
assert old_pricing_box2 in content, "old_pricing_box2 not found"
content = content.replace(old_pricing_box2, new_pricing_box2, 1)
print("13. Pricing section & sub-blocks updated")

# 14. Factsheet section
old_factsheet = '<section id="factsheet" class="py-10 sm:py-16 lg:py-20 bg-white border-t border-brand-border-light relative overflow-hidden" itemscope itemtype="https://schema.org/AboutPage">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-6 sm:space-y-10 lg:space-y-12 sm:space-y-8 sm:space-y-6 sm:space-y-10 lg:space-y-12 lg:space-y-16">'
new_factsheet = '<section id="factsheet" class="py-12 sm:py-16 lg:py-20 xl:py-24 bg-white border-t border-brand-border-light relative overflow-hidden" itemscope itemtype="https://schema.org/AboutPage">\n    <div class="max-w-7xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-12 lg:space-y-16">'
assert old_factsheet in content, "old_factsheet not found"
content = content.replace(old_factsheet, new_factsheet, 1)
print("14. Factsheet section updated")

# 15. FAQ section
old_faq = '<section id="faq" class="py-10 sm:py-16 lg:py-20 bg-brand-surface border-t border-brand-border-light">\n    <div class="max-w-4xl mx-auto px-3.5 sm:px-6 lg:px-8">\n      <div class="text-center mb-16">'
new_faq = '<section id="faq" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-brand-surface border-t border-brand-border-light">\n    <div class="max-w-4xl mx-auto px-3.5 sm:px-6 lg:px-8">\n      <div class="text-center mb-8 sm:mb-12 lg:mb-16">'
assert old_faq in content, "old_faq not found"
content = content.replace(old_faq, new_faq, 1)
print("15. FAQ section updated")

# 16. Final CTA section
old_final = '<section class="py-10 sm:py-16 lg:py-20 bg-gradient-to-b from-brand-dark via-[#042026] to-[#021317] text-white text-center relative overflow-hidden">'
new_final = '<section class="py-16 sm:py-24 lg:py-28 xl:py-32 bg-gradient-to-b from-brand-dark via-[#042026] to-[#021317] text-white text-center relative overflow-hidden">'
assert old_final in content, "old_final not found"
content = content.replace(old_final, new_final, 1)
print("16. Final CTA section updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nSuccessfully updated all 16 sections with balanced vertical spacing!")
