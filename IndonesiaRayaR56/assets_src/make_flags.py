"""
Generate simple, original flat-design placeholder flags for the mod.
Not AI-illustrated art -- geometric/flat shapes only, drawn with PIL.
Output: PNG at large size (820x520), later downscaled per HOI4 size via ImageMagick.
"""
from PIL import Image, ImageDraw
import math, os

OUT = "/home/claude/assets_src/flags"
os.makedirs(OUT, exist_ok=True)

W, H = 820, 520  # 10x scale of HOI4 "large" 82x52, downscale later for crisp result

def save(img, name):
    img.save(f"{OUT}/{name}.png")
    print("wrote", name)

def star(draw, cx, cy, r_outer, r_inner, points, fill):
    pts = []
    for i in range(points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        ang = math.pi/2 + i * math.pi / points
        pts.append((cx + r*math.cos(ang), cy - r*math.sin(ang)))
    draw.polygon(pts, fill=fill)

# --- Neutrality / colonial administration (DEI default, also B/E/F) ---
img = Image.new("RGB", (W, H), (0, 51, 51))          # dark teal field
d = ImageDraw.Draw(img)
d.rectangle([0, H*0.62, W, H], fill=(230, 230, 220))  # off-white lower band
# simple anchor-like admin mark (abstract, not a real coat of arms)
cx, cy = W*0.5, H*0.4
d.line([(cx, cy-90), (cx, cy+90)], fill=(230,230,220), width=18)
d.arc([cx-70, cy+10, cx+70, cy+150], start=0, end=180, fill=(230,230,220), width=18)
d.ellipse([cx-14, cy-110, cx+14, cy-82], outline=(230,230,220), width=14)
save(img, "DEI_neutrality")

# --- Democratic / Republik (red-white, historical Indonesian bicolor + star) ---
img = Image.new("RGB", (W, H), (200, 30, 40))
d = ImageDraw.Draw(img)
d.rectangle([0, H*0.5, W, H], fill=(250, 250, 248))
star(d, W*0.5, H*0.5, 95, 40, 5, (250, 250, 248))
save(img, "DEI_democratic")

# --- Communism (red field, yellow star) ---
img = Image.new("RGB", (W, H), (150, 20, 24))
d = ImageDraw.Draw(img)
star(d, W*0.32, H*0.42, 110, 46, 5, (250, 210, 60))
d.rectangle([0, 0, W*0.06, H], fill=(250,210,60))
save(img, "DEI_communism")

# --- Fascism (dark field, bold angular emblem) ---
img = Image.new("RGB", (W, H), (35, 35, 38))
d = ImageDraw.Draw(img)
d.rectangle([0, H*0.42, W, H*0.58], fill=(160, 20, 20))
# abstract angular sunburst (no real-world hate symbols)
cx, cy = W*0.5, H*0.5
for i in range(8):
    ang = i * math.pi / 4
    x2 = cx + 150*math.cos(ang)
    y2 = cy + 150*math.sin(ang)
    d.line([(cx, cy), (x2, y2)], fill=(220, 190, 60), width=14)
d.ellipse([cx-38, cy-38, cx+38, cy+38], fill=(220,190,60))
save(img, "DEI_fascism")

print("done")
