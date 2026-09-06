import urllib.request
import urllib.parse
import json
import os
from PIL import Image, ImageOps

url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote('File:North American B-25 Mitchell Góraszka 2007.jpg')}&prop=imageinfo&iiprop=url&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'HOI4ModAssetBot/1.0 (contact: test@example.com)'})
with urllib.request.urlopen(req) as resp:
    d = json.loads(resp.read().decode('utf-8'))
    pages = d.get('query', {}).get('pages', {})
    for pid, pdata in pages.items():
        direct_url = pdata['imageinfo'][0]['url']
        print("Direct URL:", direct_url)

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
tech_dir = os.path.join(mod_dir, "gfx", "interface", "technologies")
scratch_dir = os.path.join(mod_dir, "scratch", "tmp_downloads")

tmp_path = os.path.join(scratch_dir, "b25_mitchell.jpg")
out_dds = os.path.join(tech_dir, "INS_b25_mitchell.dds")

req_img = urllib.request.Request(direct_url, headers={'User-Agent': 'HOI4ModAssetBot/1.0 (contact: test@example.com)'})
with urllib.request.urlopen(req_img, timeout=20) as resp:
    with open(tmp_path, "wb") as f:
        f.write(resp.read())

with Image.open(tmp_path) as im:
    im = im.convert("RGBA")
    im = ImageOps.fit(im, (120, 50), method=Image.Resampling.LANCZOS)
    im.save(out_dds)
    print("Saved B-25 Mitchell DDS successfully!")
