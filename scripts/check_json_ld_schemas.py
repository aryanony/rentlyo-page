import re, json

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.DOTALL)
print(f"Found {len(matches)} JSON-LD blocks:")
for i, m in enumerate(matches):
    try:
        data = json.loads(m.strip())
        t = data.get('@type', 'Graph or Multi')
        if '@graph' in data:
            types = [item.get('@type') for item in data['@graph']]
            print(f"[{i+1}] @graph with types: {types}")
        else:
            print(f"[{i+1}] Type: {t}")
    except Exception as e:
        print(f"[{i+1}] Error parsing: {e}")
