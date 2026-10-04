import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

styles = re.findall(r'style=["\'][^"\']*["\']', content)
print(f"Total style attributes found: {len(styles)}")
for s in styles:
    print("  ", s)
