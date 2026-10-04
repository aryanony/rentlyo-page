import glob
import re

# 1. Update footer h4 -> h3 in all html files
html_files = glob.glob('*.html') + glob.glob('*/*.html') + glob.glob('*/*/*.html')
count = 0
for fpath in html_files:
    if fpath == 'index.html':
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace footer h4 with h3
    new_content = re.sub(
        r'<h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">(.*?)</h4>',
        r'<h3 class="text-white font-bold text-xs uppercase tracking-wider mb-3">\1</h3>',
        content
    )
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated footer in: {fpath}")

print(f"Total files with footer updated: {count}")

# 2. Fix for-property-owners steps h4 -> h3
fpath = 'for-property-owners/index.html'
with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<h4 class="font-bold text-gray-900">1st of the month: Automated Rent Calculation</h4>', '<h3 class="font-bold text-gray-900">1st of the month: Automated Rent Calculation</h3>')
c = c.replace('<h4 class="font-bold text-gray-900">Tenant Pays via UPI: One-Tap Handoff</h4>', '<h3 class="font-bold text-gray-900">Tenant Pays via UPI: One-Tap Handoff</h3>')
c = c.replace('<h4 class="font-bold text-gray-900">1-Tap Confirmation & WhatsApp Receipt</h4>', '<h3 class="font-bold text-gray-900">1-Tap Confirmation & WhatsApp Receipt</h3>')
with open(fpath, 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated steps in for-property-owners/index.html")

# 3. Add h2 section headers to for-* pages before the grid
for_pages = [
    ('for-commercial-complex/index.html', 'Commercial Property Management Capabilities', 'Specialized tooling for shopping complexes, retail spaces, and multi-unit plazas.'),
    ('for-coworking-spaces/index.html', 'Coworking Space Management Capabilities', 'Desk allocation, flexible billing periods, and automated member statements.'),
    ('for-pg-hostel-owners/index.html', 'PG & Hostel Management Capabilities', 'Bed-level occupancy, advance security deposits, and mess meal fee accounting.'),
    ('for-property-owners/index.html', 'Built Specifically for Independent Residential Landlords', 'Everything required to automate tenant rent collection, electric meter billing, and maintenance tracking.'),
    ('for-shop-owners-market-complex/index.html', 'Market Complex Management Capabilities', 'Contiguous unit leases, commercial tariff tracking, and formal accounting ledgers.'),
    ('for-society-management/index.html', 'Society & RWA Management Capabilities', 'Maintenance dues, common area utility distribution, and digital notice boards.'),
    ('for-warehouse-godown-owners/index.html', 'Warehouse & Godown Management Capabilities', 'Multi-year lease agreements, scheduled step-up escalations, and commercial ledgers.')
]

for rel_path, title, subtitle in for_pages:
    with open(rel_path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # We want to insert the h2 header right after <main ...> and before the grid
    target = '<main class="py-16 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">'
    if target in c and title not in c:
        replacement = f'''<main class="py-16 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
    <div class="text-center max-w-3xl mx-auto mb-10">
      <h2 class="text-2xl sm:text-3xl font-bold text-brand-dark">{title}</h2>
      <p class="text-sm text-gray-600 mt-2">{subtitle}</p>
    </div>'''
        c = c.replace(target, replacement, 1)
        with open(rel_path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Added h2 section header to: {rel_path}")
    else:
        print(f"Target pattern or already present in: {rel_path}")
