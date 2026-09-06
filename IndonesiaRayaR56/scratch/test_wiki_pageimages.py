import urllib.request
import urllib.parse
import json

def get_wiki_lead_image(title, lang='id'):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=500"
    req = urllib.request.Request(url, headers={'User-Agent': 'HOI4ModAssetBot/1.0 (contact: radit@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if 'thumbnail' in pdata:
                    return pdata['thumbnail']['source']
                if 'title' in pdata:
                    print(f"Page found: {pdata['title']} (no thumbnail)")
            return None
    except Exception as e:
        return str(e)

targets = [
    ("Yos_Sudarso", "id"),
    ("Soerjadi_Soerjadarma", "id"),
    ("Halim_Perdanakusuma", "id"),
    ("R._E._Martadinata", "id"),
    ("Moestopo", "id"),
    ("Braat_Overvalwagen", "en"),
    ("Overvalwagen", "en"),
    ("Marmon-Herrington_CTLS", "en"),
    ("Curtiss-Wright_CW-21", "en"),
    ("Institut_Teknologi_Bandung", "id"),
    ("Stasiun_Radio_Malabar", "id")
]

for t, lang in targets:
    res = get_wiki_lead_image(t, lang)
    print(f"{t} ({lang}): {res}")
