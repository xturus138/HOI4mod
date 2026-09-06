import urllib.request, urllib.parse, json

def get_wiki_lead_image(title, lang='id'):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=500"
    req = urllib.request.Request(url, headers={'User-Agent': 'HOI4SubmodBot/1.0 (https://github.com/xturus138/HOI4mod; bot@hoi4indonesia.org)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if 'thumbnail' in pdata:
                    return pdata['thumbnail']['source']
            return None
    except Exception as e:
        return str(e)

targets = [
    ("Sultan_Hamid_II", "id"),
    ("Hamengkubuwana_IX", "id"),
    ("Wahid_Hasyim", "id"),
    ("Suharto", "id"),
    ("Pakubuwana_X", "id")
]

for t, lang in targets:
    print(f"{t}: {get_wiki_lead_image(t, lang)}")
