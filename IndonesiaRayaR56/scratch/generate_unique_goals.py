import os, io, requests, math
from PIL import Image, ImageOps, ImageDraw, ImageFilter, ImageEnhance

base_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
goals_dir = os.path.join(base_dir, "gfx", "interface", "goals")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Referer': 'https://commons.wikimedia.org/'
}

# Image sources:
# 1. Baitul Mal: Gold Dinar Coin of Samudera Pasai
# 2. Akademi Mujahidin: PETA / Hizbullah Cadet soldiers
# 3. Dharmaputra: Candi Penataran Warrior Relief
# 4. Penobatan Maharaja: Golden Crown of Kutai / Nusantara
# 5. Trikora: Yos Sudarso / Naval Operation Stamp
downloads = {
    "focus_dei_baitul_mal.dds": "https://upload.wikimedia.org/wikipedia/commons/a/a5/MUS_Koin_emas_Samudera_Pasai_1326-1345%3B_1.jpg",
    "focus_dei_akademi_mujahidin.dds": "https://upload.wikimedia.org/wikipedia/commons/7/79/Tentara_Pembela_Tanah_Air_in_Indonesia%2C_1944_No.01.png",
    "focus_dei_dharmaputra.dds": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Relief_Candi_Penataran.jpg",
    "focus_dei_penobatan_maharaja.dds": "https://upload.wikimedia.org/wikipedia/commons/b/be/Mahkota_Sultan_Kutai_1.jpg",
    "focus_dei_trikora.dds": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Yos_Sudarso_Postage_Stamp.jpg"
}

def create_circular_goal_badge(src_img, out_dds_path):
    size = 82
    center = size / 2.0
    outer_r = 38.0
    inner_r = 34.0

    im = src_img.convert("RGBA")
    w, h = im.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    sq = im.crop((left, top, left + min_dim, top + min_dim))
    sq = sq.resize((size, size), Image.Resampling.LANCZOS)

    # Convert to vintage monochrome grayish
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
    print(f"Saved badge: {os.path.basename(out_dds_path)}")

for fname, url in downloads.items():
    try:
        print(f"Downloading {fname} from {url}...")
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code == 200:
            src_im = Image.open(io.BytesIO(r.content))
            out_path = os.path.join(goals_dir, fname)
            create_circular_goal_badge(src_im, out_path)
        else:
            print(f"Failed download {fname}: HTTP {r.status_code}")
    except Exception as e:
        print(f"Error {fname}: {e}")

print("UNIQUE GOAL ASSETS GENERATION COMPLETE.")
