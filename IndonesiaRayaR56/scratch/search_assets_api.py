import urllib.request, urllib.parse, json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) HOI4AssetTool/1.0'}

def search_commons(query, limit=3):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&format=json&srlimit={limit}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = data.get('query', {}).get('search', [])
            return [r['title'] for r in results]
    except Exception as e:
        print(f"Err {query}: {e}")
        return []

def get_image_url(file_title, width=500):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&iiurlwidth={width}&format=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                ii = pdata.get('imageinfo', [])
                if ii:
                    return ii[0].get('thumburl') or ii[0].get('url')
    except Exception as e:
        return None

queries = [
    "Garuda Pancasila",
    "Sukarno Proklamasi",
    "Gedung Merdeka Bandung",
    "Sukarno Trikora",
    "Sukarno Dwikora",
    "Dekrit Presiden 5 Juli 1959",
    "Sultan Hamid II BFO",
    "Candi Bajang Ratu Trowulan",
    "Relief Gajah Mada Borobudur",
    "Keris Majapahit",
    "Bambu runcing",
    "Hembrug M.95",
    "P-51 Mustang AURI",
    "Dakota RI-001 Seulawah",
    "KRI Gadjah Mada",
    "KRI Irian",
    "Overvalwagen Braat",
    "Marmon Herrington CTLS",
    "Curtiss-Wright CW-21",
    "B-25 Mitchell TNI AU"
]

for q in queries:
    titles = search_commons(q, 2)
    print(f"=== {q} ===")
    for t in titles:
        u = get_image_url(t)
        print(f"  {t} -> {u}")
