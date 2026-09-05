"""
Simple banner-style event pictures: color-graded background (matching each
path's flag palette) plus the path's icon glyph centered. Flat/geometric,
not AI-illustrated art.
"""
from PIL import Image, ImageDraw
import math, os

OUT = "/home/claude/assets_src/event_pictures"
os.makedirs(OUT, exist_ok=True)
W, H = 912, 456  # 2:1 banner, 2x scale for crispness before downscale

def save(img, name):
    img.save(f"{OUT}/{name}.png")
    print("wrote", name)

def vgradient(c_top, c_bottom):
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        r = int(c_top[0] + (c_bottom[0]-c_top[0])*t)
        g = int(c_top[1] + (c_bottom[1]-c_top[1])*t)
        b = int(c_top[2] + (c_bottom[2]-c_top[2])*t)
        for x in range(W):
            px[x, y] = (r, g, b)
    return img

def star(draw, cx, cy, r_outer, r_inner, points, fill):
    pts = []
    for i in range(points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        ang = -math.pi/2 + i * math.pi / points
        pts.append((cx + r*math.cos(ang), cy + r*math.sin(ang)))
    draw.polygon(pts, fill=fill)

GLYPH = (238, 232, 210)

# --- dei_trunk.6: Titik Balik Sejarah (crossroads, warm neutral) ---
img = vgradient((40, 40, 45), (75, 60, 40))
d = ImageDraw.Draw(img)
cx, cy = W/2, H/2
for ang in (0, 90, 180, 270):
    a = math.radians(ang)
    d.line([(cx, cy), (cx+150*math.cos(a), cy+150*math.sin(a))], fill=GLYPH, width=22)
star(d, cx, cy, 55, 24, 4, GLYPH)
save(img, "DEI_event_trunk6")

# --- Path A: Proklamasi (red/white, star) ---
img = vgradient((150, 20, 28), (230, 230, 225))
d = ImageDraw.Draw(img)
star(d, W/2, H/2, 130, 55, 5, (250, 250, 248))
save(img, "DEI_event_path_a")

# --- Path B: Padamkan Revolusi (teal/cream, shield) ---
img = vgradient((0, 45, 48), (0, 70, 68))
d = ImageDraw.Draw(img)
cx, cy = W/2, H/2
pts = [(cx-140, cy-150), (cx+140, cy-150), (cx+140, cy+30), (cx, cy+170), (cx-140, cy+30)]
d.polygon(pts, outline=GLYPH, width=22)
d.line([(cx, cy-150), (cx, cy+110)], fill=GLYPH, width=18)
save(img, "DEI_event_path_b")

# --- Path C: Front Rakyat (deep red, gear) ---
img = vgradient((90, 15, 18), (150, 20, 24))
d = ImageDraw.Draw(img)
cx, cy = W/2, H/2
outer_r, tooth_r, inner_r, teeth = 130, 158, 92, 10
pts = []
for i in range(teeth * 2):
    ang = i * math.pi / teeth
    r = tooth_r if i % 2 == 0 else outer_r
    pts.append((cx + r*math.cos(ang), cy + r*math.sin(ang)))
d.polygon(pts, fill=GLYPH)
d.ellipse([cx-inner_r, cy-inner_r, cx+inner_r, cy+inner_r], fill=(120, 18, 21))
d.ellipse([cx-45, cy-45, cx+45, cy+45], fill=GLYPH)
save(img, "DEI_event_path_c")

# --- Path D: Kudeta Militer (dark charcoal, fist) ---
img = vgradient((25, 25, 27), (45, 30, 30))
d = ImageDraw.Draw(img)
cx, cy = W/2, H/2 + 20
d.rectangle([cx-40, cy-30, cx+40, cy+140], fill=GLYPH)
d.ellipse([cx-95, cy-160, cx+95, cy-5], fill=GLYPH)
save(img, "DEI_event_path_d")

# --- Path E: Negara Islam (deep green, crescent+star) ---
img = vgradient((10, 55, 40), (15, 80, 58))
d = ImageDraw.Draw(img)
cx, cy = W/2, H/2
d.ellipse([cx-130, cy-130, cx+130, cy+130], fill=GLYPH)
d.ellipse([cx-80, cy-138, cx+170, cy+122], fill=(12, 62, 46))
star(d, cx+95, cy-45, 40, 17, 5, GLYPH)
save(img, "DEI_event_path_e")

# --- Path F: Majapahit (warm gold/brown, temple) ---
img = vgradient((60, 40, 20), (110, 75, 30))
d = ImageDraw.Draw(img)
cx, cy = W/2, H/2 + 90
tiers = [(210, 42), (155, 42), (105, 42), (55, 56)]
y = cy
for w, h in tiers:
    d.polygon([(cx-w, y), (cx+w, y), (cx+w*0.7, y-h), (cx-w*0.7, y-h)], fill=GLYPH)
    y -= h
d.polygon([(cx-20, y), (cx+20, y), (cx, y-60)], fill=GLYPH)
save(img, "DEI_event_path_f")

print("done")

# --- FIX: Path D banner -- add knuckle notches so it reads more clearly as a fist ---
img = vgradient((25, 25, 27), (45, 30, 30))
d = ImageDraw.Draw(img)
cx, cy = W/2, H/2 + 20
d.rectangle([cx-40, cy-30, cx+40, cy+140], fill=GLYPH)
d.ellipse([cx-95, cy-160, cx+95, cy-5], fill=GLYPH)
for i in range(3):
    x = cx - 60 + i*60
    d.rectangle([x-14, cy-195, x+14, cy-120], fill=(45,30,30))
save(img, "DEI_event_path_d")
