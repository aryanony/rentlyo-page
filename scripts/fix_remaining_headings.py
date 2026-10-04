import glob
import re

for_pages = [
    ('for-coworking-spaces/index.html', 'Coworking Space Management Capabilities', 'Desk allocation, flexible billing periods, and automated member statements.'),
    ('for-shop-owners-market-complex/index.html', 'Market Complex Management Capabilities', 'Contiguous unit leases, commercial tariff tracking, and formal accounting ledgers.'),
    ('for-society-management/index.html', 'Society & RWA Management Capabilities', 'Maintenance dues, common area utility distribution, and digital notice boards.'),
    ('for-warehouse-godown-owners/index.html', 'Warehouse & Godown Management Capabilities', 'Multi-year lease agreements, scheduled step-up escalations, and commercial ledgers.')
]

for rel_path, title, subtitle in for_pages:
    with open(rel_path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    target = '<main class="max-w-5xl mx-auto px-4 py-16 space-y-16">'
    if target in c and title not in c:
        replacement = f'''<main class="max-w-5xl mx-auto px-4 py-16 space-y-16">
    <div class="text-center max-w-3xl mx-auto mb-10">
      <h2 class="text-2xl sm:text-3xl font-bold text-brand-dark font-heading">{title}</h2>
      <p class="text-sm text-gray-600 mt-2">{subtitle}</p>
    </div>'''
        c = c.replace(target, replacement, 1)
        with open(rel_path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Added h2 section header to: {rel_path}")
    else:
        print(f"Already present or mismatch in {rel_path}")
