import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('**/*.html', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', c, re.DOTALL)
    print(f"{f}: {len(scripts)} json-ld blocks")
    for s in scripts:
        try:
            data = json.loads(s.strip())
            types = [item.get('@type') for item in data.get('@graph', [data])]
            print(f"   Types: {types}")
        except Exception as e:
            print(f"   JSON parse error: {e}")
