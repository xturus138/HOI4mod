import urllib.request
import urllib.parse
import json

def search_files(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'HOI4ModAssetBot/1.0 (contact: radit@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return [r['title'] for r in data.get('query', {}).get('search', [])[:5]]
    except Exception as e:
        return [str(e)]

def get_commons_file_url(title):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'HOI4ModAssetBot/1.0 (contact: radit@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if 'imageinfo' in pdata and pdata['imageinfo']:
                    return pdata['imageinfo'][0]['url']
    except Exception as e:
        return str(e)
    return None

for q in ["CTLS-4TA", "Marmon-Herrington", "B-25 Indonesian Air Force", "B-25 Mitchell", "Aula Barat", "Technische Hoogeschool Bandung", "Plaju", "Balikpapan refinery"]:
    hits = search_files(q)
    print(f"Query: {q} -> {hits[:2]}")
    if hits and not hits[0].startswith("Error"):
        u = get_commons_file_url(hits[0])
        print(f"   URL: {u}")
