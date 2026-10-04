with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'<section\b([^>]*)>', text))

# Section 8 in 1-based index is index 7 (0-based)
s8_start = matches[7].start()
s8_end = matches[8].start()
print("SECTION 8 LENGTH:", s8_end - s8_start)
print(text[s8_start:s8_end])
