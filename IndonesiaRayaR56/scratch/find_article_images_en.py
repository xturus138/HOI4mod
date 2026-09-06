import urllib.request, urllib.parse, json

def get_images_in_article(title, lang='en'):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(title)}&prop=images&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'HOI4SubmodBot/1.0 (https://github.com/xturus138/HOI4mod; bot@hoi4indonesia.org)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('parse', {}).get('images', [])
    except Exception as e:
        return [str(e)]

for art in ["Sultan_Hamid_II", "Wahid_Hasyim", "Suharto"]:
    imgs = get_images_in_article(art, "en")
    print(f"{art} (en): {imgs[:5]}")
