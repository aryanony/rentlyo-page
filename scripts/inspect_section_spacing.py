import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find each section
sec_matches = list(re.finditer(r'<section([^>]*)>(.*?)(?=</section>|<section|$)', html, re.DOTALL))
print(f'Total sections found: {len(sec_matches)}\n')

for i, m in enumerate(sec_matches):
    attrs = m.group(1)
    body = m.group(2)[:1500] # first 1500 chars of section body
    
    # Extract id and class from attrs
    id_m = re.search(r'id=["\']([^"\']+)["\']', attrs)
    sec_id = id_m.group(1) if id_m else 'NO_ID'
    
    class_m = re.search(r'class=["\']([^"\']+)["\']', attrs)
    sec_class = class_m.group(1) if class_m else 'NO_CLASS'
    
    # First heading
    h_m = re.search(r'<(h[1-3])[^>]*>(.*?)</\1>', body, re.DOTALL)
    heading = re.sub(r'<[^>]+>', '', h_m.group(2)).strip() if h_m else 'NO_HEADING'
    heading = re.sub(r'\s+', ' ', heading)[:60]
    
    # First container with max-w
    cw_m = re.search(r'<div[^>]*class=["\']([^"\']*max-w-[^"\']*)["\']', body)
    c_class = cw_m.group(1) if cw_m else 'NO_CONTAINER'
    
    print(f'[{i+1}] #{sec_id} | {heading}')
    print(f'     sec class: {sec_class}')
    print(f'     cnt class: {c_class}\n')
