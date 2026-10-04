import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all headings with their line numbers
headings = []
for m in re.finditer(r'<(h[1-6])(?:\s+[^>]*)?>(.*?)</\1>', content, re.DOTALL | re.IGNORECASE):
    tag = m.group(1).lower()
    text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    headings.append((tag, text[:60]))

print(f"Total Headings Found: {len(headings)}")
prev_level = 0
for tag, text in headings:
    level = int(tag[1])
    indent = "  " * (level - 1)
    skipped = ""
    if prev_level > 0 and level > prev_level + 1:
        skipped = f" <-- SKIPPED FROM h{prev_level} TO h{level}!"
    print(f"{indent}<{tag}> {text}{skipped}")
    prev_level = level
