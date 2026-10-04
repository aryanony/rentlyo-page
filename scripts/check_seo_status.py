import glob
import os

files = glob.glob('**/*.html', recursive=True)

print(f"{'FILE':<55} | {'BC':<5} | {'CANONICAL':<10} | {'GTAG':<6} | {'ROBOTS':<7}")
print("-" * 92)

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    has_bc = 'BreadcrumbList' in content
    has_canonical = 'canonical' in content
    has_gtag = 'G-HTNJFZYNKQ' in content
    has_robot = 'name="robots"' in content
    print(f"{f:<55} | {str(has_bc):<5} | {str(has_canonical):<10} | {str(has_gtag):<6} | {str(has_robot):<7}")
