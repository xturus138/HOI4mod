import urllib.request, urllib.parse, json

url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=Sultan+Hamid+II&srnamespace=6&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'HOI4SubmodBot/1.0 (https://github.com/xturus138/HOI4mod; bot@hoi4indonesia.org)'})
with urllib.request.urlopen(req) as resp:
    d = json.loads(resp.read().decode('utf-8'))
    results = [r['title'] for r in d.get('query', {}).get('search', []) if r['title'].lower().endswith(('.jpg', '.png'))]
    print("Sultan Hamid II on Commons:", results[:5])

# Also get URLs for Wahid Hasyim and Suharto
for tit in ["File:KHA_Wahid_Hasyim,_Pekan_Buku_Indonesia_1954,_p242.jpg", "File:Jenderal_TNI_Soeharto.png"]:
    u_req = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(tit)}&prop=imageinfo&iiprop=url&format=json"
    req_f = urllib.request.Request(u_req, headers={'User-Agent': 'HOI4SubmodBot/1.0 (https://github.com/xturus138/HOI4mod; bot@hoi4indonesia.org)'})
    with urllib.request.urlopen(req_f) as resp2:
        d2 = json.loads(resp2.read().decode('utf-8'))
        for pid, pdata in d2.get('query', {}).get('pages', {}).items():
            print(f"{tit} -> {pdata.get('imageinfo', [{}])[0].get('url')}")
