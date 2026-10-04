import urllib.request

html = urllib.request.urlopen('http://localhost:3000/').read().decode('utf-8')
idx = html.find('id="live-demo"')
end_idx = html.find('</section>', idx)
snippet = html[idx:end_idx]

print("Snippet length of #live-demo:", len(snippet))
assert 'Demo Login Credentials:' in snippet
assert '9308489230' in snippet
assert 'Rentlyo123' in snippet
assert 'Tenant Access:' in snippet
print("ALL ASSERTIONS PASSED! Live demo section actively contains demo credentials and tenant access boxes.")
