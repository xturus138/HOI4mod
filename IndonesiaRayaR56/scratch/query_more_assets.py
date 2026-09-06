import urllib.request
import urllib.parse
import json

def get_image_url_from_title(title, lang='id'):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"
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

def search_commons(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'HOI4ModAssetBot/1.0 (contact: radit@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = data.get('query', {}).get('search', [])
            return [r['title'] for r in results[:5]]
    except Exception as e:
        return [str(e)]

moestopo_url = get_image_url_from_title("Berkas:Prof-Dr-Moestopo1.jpg", "id")
print("Moestopo URL:", moestopo_url)

print("CTLS search:", search_commons("Marmon Herrington tank"))
print("B-25 Indonesia search:", search_commons("B-25 Mitchell Indonesia"))
print("ITB Aula Barat search:", search_commons("Aula Barat ITB"))
print("Plaju refinery search:", search_commons("Plaju refinery oil"))
