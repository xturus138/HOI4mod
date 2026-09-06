import urllib.request
import urllib.parse
import json

def get_wikimedia_image(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrlimit=3&prop=imageinfo&iiprop=url|size|mime&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'HOI4ModAssetBot/1.0 (test@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            results = []
            for pid, pdata in pages.items():
                title = pdata.get('title')
                imginfo = pdata.get('imageinfo', [{}])[0]
                img_url = imginfo.get('url')
                if img_url:
                    results.append((title, img_url))
            return results
    except Exception as e:
        return [("Error", str(e))]

queries = [
    "Yos Sudarso",
    "Suryadi Suryadarma",
    "Halim Perdanakusuma",
    "R.E. Martadinata",
    "Moestopo",
    "Overvalwagen Braat",
    "Marmon-Herrington CTLS",
    "Curtiss-Wright CW-21",
    "B-25 Mitchell Indonesia",
    "Technische Hoogeschool te Bandoeng",
    "Radio Malabar"
]

for q in queries:
    res = get_wikimedia_image(q)
    print(f"Query: {q}")
    for title, u in res[:2]:
        print(f"  -> {title}: {u}")
