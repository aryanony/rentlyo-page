import glob
import re

files = glob.glob('**/*.html', recursive=True)
updated_count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # 1. Update target="_blank" rel="noopener" to target="_blank" rel="noopener noreferrer"
    new_c = re.sub(r'target="_blank"\s+rel="noopener"', 'target="_blank" rel="noopener noreferrer"', c)
    new_c = re.sub(r"target='_blank'\s+rel='noopener'", "target='_blank' rel='noopener noreferrer'", new_c)
    
    # 2. Check for target="_blank" without rel
    new_c = re.sub(r'target="_blank"(?!\s+rel=)', 'target="_blank" rel="noopener noreferrer"', new_c)

    if new_c != c:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_c)
        updated_count += 1
        print(f"Updated external link security in: {f}")

print(f"Total files updated: {updated_count}")
