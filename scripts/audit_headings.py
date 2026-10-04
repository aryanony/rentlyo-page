import glob
import re
from html.parser import HTMLParser

class HeadingAuditor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self.current_tag = None
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        if re.match(r'^h[1-6]$', tag):
            self.current_tag = tag
            self.current_text = []

    def handle_endtag(self, tag):
        if tag == self.current_tag:
            self.headings.append((int(self.current_tag[1]), ''.join(self.current_text).strip()))
            self.current_tag = None
            self.current_text = []

    def handle_data(self, data):
        if self.current_tag:
            self.current_text.append(data)

all_files = glob.glob('*.html') + glob.glob('*/*.html') + glob.glob('*/*/*.html')
print(f"Auditing {len(all_files)} HTML files for SEO heading structure...")

total_issues = 0
for fpath in sorted(all_files):
    parser = HeadingAuditor()
    with open(fpath, 'r', encoding='utf-8') as f:
        parser.feed(f.read())
    
    h1s = [h for h in parser.headings if h[0] == 1]
    issues = []
    if len(h1s) == 0:
        issues.append('No <h1> found')
    elif len(h1s) > 1:
        issues.append(f'{len(h1s)} <h1> elements found (should be exactly 1)')
    
    last_level = 0
    for level, text in parser.headings:
        if last_level != 0 and level > last_level + 1:
            issues.append(f'Skipped heading level: <h{last_level}> directly to <h{level}>: "{text[:40]}"')
        last_level = level
        
    if issues:
        total_issues += len(issues)
        print(f"\n[!] {fpath}:")
        for iss in issues:
            print(f"    - {iss}")

if total_issues == 0:
    print("\n[SUCCESS] All HTML pages have perfect heading hierarchy (exactly 1 h1, and no skipped heading levels)!")
else:
    print(f"\n[SUMMARY] Total heading issues found: {total_issues}")
