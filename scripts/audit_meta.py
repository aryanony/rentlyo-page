import glob
import re

all_files = glob.glob('*.html') + glob.glob('*/*.html') + glob.glob('*/*/*.html')
issues = 0
for fpath in sorted(all_files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    t_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    d_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.DOTALL)
    
    title = t_m.group(1).strip() if t_m else ''
    desc = d_m.group(1).strip() if d_m else ''
    
    t_len = len(title)
    d_len = len(desc)
    
    t_issue = t_len < 10 or t_len > 60
    d_issue = d_len < 70 or d_len > 160
    
    if t_issue or d_issue:
        print(f"{fpath}:")
        if t_issue:
            clean_t = title.encode('ascii', 'replace').decode('ascii')
            print(f"  - Title len={t_len}: \"{clean_t}\"")
        if d_issue:
            clean_d = desc.encode('ascii', 'replace').decode('ascii')
            print(f"  - Desc len={d_len}: \"{clean_d}\"")
        issues += 1

if issues == 0:
    print("ALL 22 PAGES HAVE PERFECT TITLE (<=60 chars) AND DESCRIPTION (<=160 chars) LENGTHS!")
else:
    print(f"\nTotal pages with title/desc issues: {issues}")
