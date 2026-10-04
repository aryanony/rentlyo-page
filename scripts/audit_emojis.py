import glob
import unicodedata
import sys

# Reconfigure stdout for utf-8
sys.stdout.reconfigure(encoding='utf-8')

emoji_ranges = [
    (0x1F600, 0x1F64F), # Emoticons
    (0x1F300, 0x1F5FF), # Misc Symbols and Pictographs
    (0x1F680, 0x1F6FF), # Transport and Map
    (0x1F1E0, 0x1F1FF), # Flags
    (0x2600, 0x26FF),   # Misc symbols
    (0x2700, 0x27BF),   # Dingbats
    (0x1F900, 0x1F9FF), # Supplemental Symbols and Pictographs
    (0x1FA70, 0x1FAFF), # Symbols and Pictographs Extended-A
]

def is_emoji(char):
    cp = ord(char)
    # Allow common typographical and rupee/currency marks
    if char in ['₹', '•', '—', '–', '©', '®', '™', '→', '↗', '←', '↑', '↓', '✓', '✕', '★', '☆', '”', '“', '’', '‘', '…', '«', '»', '·']:
        return False
    for start, end in emoji_ranges:
        if start <= cp <= end:
            return True
    return False

files = glob.glob('**/*.html', recursive=True) + glob.glob('js/**/*.js', recursive=True)
found_any = False

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for lnum, line in enumerate(lines):
        emojis_in_line = [ch for ch in line if is_emoji(ch)]
        if emojis_in_line:
            found_any = True
            print(f"EMOJI in {f}:{lnum+1} -> {set(emojis_in_line)}")

if not found_any:
    print("VERIFIED: Exactly 0 emojis found across all HTML and JS files in the project.")
