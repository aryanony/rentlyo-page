import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

root_dir = r"c:\Users\aryn1\Documents\Rentlyo\WEB"

print("--- AUDITING ALL 22 HTML FILES FOR SEO & META TAGS ---")

for root, dirs, files in os.walk(root_dir):
    if "node_modules" in dirs or ".git" in dirs:
        continue
    for f in sorted(files):
        if f.endswith(".html"):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, root_dir)
            with open(p, "r", encoding="utf-8") as fl:
                c = fl.read()

            title_m = re.search(r"<title>(.*?)</title>", c, re.DOTALL | re.IGNORECASE)
            desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', c, re.DOTALL | re.IGNORECASE)
            robots_m = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']', c, re.DOTALL | re.IGNORECASE)
            canonical_m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', c, re.DOTALL | re.IGNORECASE)
            og_title_m = re.search(r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']', c, re.DOTALL | re.IGNORECASE)
            schema_m = "<script type=\"application/ld+json\">" in c
            gtag_m = "G-HTNJFZYNKQ" in c

            t = title_m.group(1).strip() if title_m else "NONE"
            d = desc_m.group(1).strip() if desc_m else "NONE"
            r = robots_m.group(1).strip() if robots_m else "NONE"
            can = canonical_m.group(1).strip() if canonical_m else "NONE"
            og_t = og_title_m.group(1).strip() if og_title_m else "NONE"

            print(f"\n[{rel}]")
            print(f"  Title ({len(t)} chars): {t}")
            print(f"  Desc  ({len(d)} chars): {d}")
            print(f"  Robots: {r}")
            print(f"  Canonical: {can}")
            print(f"  Schema: {schema_m} | GTag: {gtag_m}")
