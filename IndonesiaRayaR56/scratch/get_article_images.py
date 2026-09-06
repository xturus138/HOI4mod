import urllib.request
import urllib.parse
import json

def get_images_in_article(title, lang='id'):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(title)}&prop=images&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'HOI4ModAssetBot/1.0 (contact: radit@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('parse', {}).get('images', [])
    except Exception as e:
        return [str(e)]

for art, lang in [("Moestopo", "id"), ("Marmon-Herrington_CTLS", "en"), ("Technische_Hoogeschool_te_Bandoeng", "id"), ("B-25_Mitchell", "en")]:
    imgs = get_images_in_article(art, lang)
    print(f"Article: {art} ({lang}): {imgs[:5]}")
