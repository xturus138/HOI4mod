import urllib.request, urllib.parse, json

url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=nuclear+reactor+core&srnamespace=6&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'HOI4SubmodBot/1.0 (https://github.com/xturus138/HOI4mod; bot@hoi4indonesia.org)'})
with urllib.request.urlopen(req) as resp:
    d = json.loads(resp.read().decode('utf-8'))
    results = [r['title'] for r in d.get('query', {}).get('search', []) if r['title'].lower().endswith('.jpg') or r['title'].lower().endswith('.png')]
    print("Found files:", results[:3])
    if results:
        title = results[0]
        url_file = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"
        req_f = urllib.request.Request(url_file, headers={'User-Agent': 'HOI4SubmodBot/1.0 (https://github.com/xturus138/HOI4mod; bot@hoi4indonesia.org)'})
        with urllib.request.urlopen(req_f) as resp2:
            d2 = json.loads(resp2.read().decode('utf-8'))
            for pid, pdata in d2.get('query', {}).get('pages', {}).items():
                print("Direct url:", pdata['imageinfo'][0]['url'])
