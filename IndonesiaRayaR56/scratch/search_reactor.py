import urllib.request
import urllib.parse
import json

url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=TRIGA+Mark+II+Bandung&srnamespace=6&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'HOI4SubmodBot/1.0 (https://github.com/xturus138/HOI4mod; bot@hoi4indonesia.org)'})
with urllib.request.urlopen(req) as resp:
    d = json.loads(resp.read().decode('utf-8'))
    print("TRIGA Bandung search:", [r['title'] for r in d.get('query', {}).get('search', [])])

url2 = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=Kartini+reactor&srnamespace=6&format=json"
req2 = urllib.request.Request(url2, headers={'User-Agent': 'HOI4SubmodBot/1.0 (https://github.com/xturus138/HOI4mod; bot@hoi4indonesia.org)'})
with urllib.request.urlopen(req2) as resp:
    d2 = json.loads(resp.read().decode('utf-8'))
    print("Kartini search:", [r['title'] for r in d2.get('query', {}).get('search', [])])
