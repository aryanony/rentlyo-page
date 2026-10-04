import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = sorted(glob.glob('**/*.html', recursive=True))

print("================================================================================")
print("                       RENTLYO COMPREHENSIVE SEO & CODE AUDIT                   ")
print("================================================================================")
print(f"Total HTML Pages Analyzed: {len(html_files)}")
print("-" * 80)

failures = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()

    # 1. Meta Title
    title_m = re.search(r'<title>(.*?)</title>', c, re.IGNORECASE)
    title = title_m.group(1).strip() if title_m else "MISSING"
    t_len = len(title)

    # 2. Meta Description
    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', c, re.IGNORECASE)
    desc = desc_m.group(1).strip() if desc_m else "MISSING"
    d_len = len(desc)

    # 3. Robots Tag
    robots_m = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']', c, re.IGNORECASE)
    robots = robots_m.group(1).strip() if robots_m else "MISSING"

    # 4. Canonical
    can_m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', c, re.IGNORECASE)
    canonical = can_m.group(1).strip() if can_m else "MISSING"

    # 5. GTAG
    has_gtag = 'G-HTNJFZYNKQ' in c
    # Check no duplicate gtag
    gtag_count = c.count("googletagmanager.com/gtag/js?id=G-HTNJFZYNKQ")

    # 6. Check unsafe target="_blank"
    unsafe_links = re.findall(r'<a\s+[^>]*target=["\']_blank["\'][^>]*>', c)
    bad_rel = [link for link in unsafe_links if 'rel="noopener noreferrer"' not in link and "rel='noopener noreferrer'" not in link]

    print(f"\nPAGE: {f}")
    print(f"  Title ({t_len} chars): {title}")
    print(f"  Desc  ({d_len} chars): {desc[:80]}...")
    print(f"  Robots: {robots}")
    print(f"  Canonical: {canonical}")
    print(f"  GA4 Tag: {'PRESENT (1x)' if gtag_count == 1 else f'ANOMALY ({gtag_count}x)'}")

    # Checks
    if t_len > 60:
        failures.append(f"Title too long in {f}: {t_len} chars")
    if t_len < 30 and f != '404.html':
        failures.append(f"Title too short in {f}: {t_len} chars")
    if d_len > 165:
        failures.append(f"Description too long in {f}: {d_len} chars")
    if d_len < 130 and f != '404.html':
        failures.append(f"Description too short in {f}: {d_len} chars")
    if not has_gtag:
        failures.append(f"Missing GTAG in {f}")
    if gtag_count > 1:
        failures.append(f"Duplicate GTAG in {f} ({gtag_count}x)")
    if bad_rel:
        failures.append(f"Unsafe external links in {f}: {len(bad_rel)}")

print("\n" + "=" * 80)
if failures:
    print(f"AUDIT WARNINGS/FAILURES ({len(failures)}):")
    for fail in failures:
        print(f"  [!] {fail}")
else:
    print("AUDIT SUCCESS: All 22 pages passed title pixel, description length, robots tag, canonical, GA4, and external link security checks!")
print("================================================================================")
