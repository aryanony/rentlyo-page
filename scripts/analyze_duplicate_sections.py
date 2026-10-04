import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'<section\b([^>]*)>', text))
print(f"Total sections: {len(matches)}\n")

for i, m in enumerate(matches):
    start = m.start()
    attrs = m.group(1)
    end = matches[i+1].start() if i+1 < len(matches) else len(text)
    section_code = text[start:end]
    lines_count = section_code.count('\n')
    
    id_m = re.search(r'id=["\']([^"\']+)["\']', attrs)
    sec_id = id_m.group(1) if id_m else 'NO_ID'
    
    h_m = re.search(r'<(h[1-3])[^>]*>(.*?)</\1>', section_code, re.DOTALL)
    heading = re.sub(r'<[^>]+>', '', h_m.group(2)).strip() if h_m else 'No heading'
    heading = re.sub(r'\s+', ' ', heading)[:70]

    # Find eyebrows or badges
    badge_m = re.search(r'class=["\'][^"\']*(?:badge|tracking-wider)[^"\']*["\'][^>]*>(.*?)<', section_code, re.DOTALL)
    badge = badge_m.group(1).strip() if badge_m else ''

    print(f"[{i+1}] ID: #{sec_id} (Length: {lines_count} lines)")
    print(f"    Badge: {badge}")
    print(f"    Heading: {heading}")
    
    # Check for specific interactive elements
    has_apk = 'rentlyo-admin.apk' in section_code
    has_creds = '9308489230' in section_code
    has_web_demo = 'rentlyo-admin.vercel.app' in section_code
    has_video = 'walkthrough' in section_code.lower()
    has_faq = 'itemscope' in section_code or 'faq' in sec_id.lower() or 'accordion' in section_code.lower()
    
    features = []
    if has_apk: features.append('APK Download')
    if has_creds: features.append('Demo Credentials')
    if has_web_demo: features.append('Web Demo Link')
    if has_video: features.append('Video Walkthrough')
    if has_faq: features.append('FAQ / Q&A')
    if features:
        print(f"    Elements: {', '.join(features)}")
    print("-" * 60)
