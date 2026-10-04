with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

import re

for i, line in enumerate(lines):
    if '<section' in line:
        print(f"Line {i+1}: {line.strip()}")
        # print next 10 lines
        for j in range(i+1, min(i+15, len(lines))):
            if any(k in lines[j] for k in ['class=', '<h2', '<h1', '<div']):
                print(f"   L{j+1}: {lines[j].strip()[:100]}")
            if '</section>' in lines[j]:
                break
        print("-" * 60)
