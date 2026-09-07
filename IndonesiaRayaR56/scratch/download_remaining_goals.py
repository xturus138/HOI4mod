import requests, time, os, io
import math
from PIL import Image, ImageEnhance

base_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
goals_dir = os.path.join(base_dir, "gfx", "interface", "goals")
headers = {'User-Agent': 'IndonesiaRayaModAssetBot/1.0 (raditya@gmail.com)'}

def get_direct_url(title):
    api = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'titles': title,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'format': 'json'
    }
    r = requests.get(api, params=params, headers=headers).json()
    pages = r.get('query', {}).get('pages', {})
    for p in pages.values():
        if 'imageinfo' in p and p['imageinfo']:
            return p['imageinfo'][0]['url']
    return None

def create_circular_goal_badge(src_im, out_dds_path):
    size = 82
    center = size / 2.0
    outer_r = 38.0
    inner_r = 34.0

    im = src_im.convert("RGBA")
    w, h = im.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    sq = im.crop((left, top, left + min_dim, top + min_dim))
    sq = sq.resize((size, size), Image.Resampling.LANCZOS)

    enhancer = ImageEnhance.Contrast(sq)
    sq = enhancer.enhance(1.25)
    gray_data = []
    for p in sq.getdata():
        g = int(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2])
        gray_data.append((g, g, g, 255))
    sq.putdata(gray_data)

    badge = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sq_pixels = list(sq.getdata())
    badge_pixels = []

    for y in range(size):
        for x in range(size):
            dx = x - center + 0.5
            dy = y - center + 0.5
            dist = math.hypot(dx, dy)

            if dist > outer_r + 1.0:
                badge_pixels.append((0, 0, 0, 0))
            elif dist > outer_r:
                alpha = int(255 * (1.0 - (dist - outer_r)))
                badge_pixels.append((140, 140, 140, alpha))
            elif dist >= inner_r:
                angle_factor = (dx - dy) / (2.0 * outer_r)
                val = int(140 + angle_factor * 60)
                val = max(80, min(220, val))
                badge_pixels.append((val, val, val, 255))
            else:
                p = sq_pixels[y * size + x]
                if dist > inner_r - 1.5:
                    shade = int(p[0] * 0.7)
                    badge_pixels.append((shade, shade, shade, 255))
                else:
                    badge_pixels.append(p)

    badge.putdata(badge_pixels)
    badge.save(out_dds_path, format="DDS")
    print(f"Successfully created badge: {os.path.basename(out_dds_path)}")

items = [
    ('focus_dei_dharmaputra.dds', 'File:Relief Candi Penataran.jpg'),
    ('focus_dei_penobatan_maharaja.dds', 'File:Mahkota Sultan Kutai 1.jpg'),
    ('focus_dei_trikora.dds', 'File:Yos Sudarso Postage Stamp.jpg')
]

for fn, title in items:
    time.sleep(1)
    u = get_direct_url(title)
    print(f"URL for {title}: {u}")
    if u:
        time.sleep(2)
        resp = requests.get(u, headers=headers)
        print(f"Download {fn}: HTTP {resp.status_code}")
        if resp.status_code == 200:
            src = Image.open(io.BytesIO(resp.content))
            out_p = os.path.join(goals_dir, fn)
            create_circular_goal_badge(src, out_p)
