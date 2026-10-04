with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def print_section(start_kw, end_kw, max_lines=40):
    start = -1
    for i, l in enumerate(lines):
        if start_kw in l:
            start = i
            break
    if start == -1:
        print(f"Could not find {start_kw}")
        return
    print(f"=== FOUND {start_kw} at line {start+1} ===")
    for j in range(start, min(start + max_lines, len(lines))):
        print(f"{j+1}: {lines[j].rstrip()}")
        if end_kw and end_kw in lines[j] and j > start:
            break

print("Checking Section 5 (Flexibility):")
print_section('id="features"', '</section>', 160)
