"""
Simple flat glyph icons for focus tree buttons — light glyph on TRANSPARENT
background (matches how HOI4 renders focus icons inside its own button frame).
Not AI art: plain geometric shapes drawn with PIL.
"""
from PIL import Image, ImageDraw
import math, os

OUT = "/home/claude/assets_src/focus_icons"
os.makedirs(OUT, exist_ok=True)
S = 256
GLYPH = (238, 232, 210, 255)   # warm cream, reads well on dark wood button frame

def canvas():
    return Image.new("RGBA", (S, S), (0, 0, 0, 0))

def save(img, name):
    img.save(f"{OUT}/{name}.png")
    print("wrote", name)

def star(draw, cx, cy, r_outer, r_inner, points, fill):
    pts = []
    for i in range(points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        ang = -math.pi/2 + i * math.pi / points
        pts.append((cx + r*math.cos(ang), cy + r*math.sin(ang)))
    draw.polygon(pts, fill=fill)

# --- dei_focus_root: colonial administration building (simple pediment) ---
img = canvas(); d = ImageDraw.Draw(img)
cx, cy = S/2, S/2
d.polygon([(cx-90, cy-10), (cx, cy-80), (cx+90, cy-10)], fill=GLYPH)          # roof
d.rectangle([cx-80, cy-10, cx+80, cy+10], fill=GLYPH)                         # architrave
for i in range(5):
    x = cx - 70 + i*35
    d.rectangle([x-8, cy+10, x+8, cy+90], fill=GLYPH)                        # columns
save(img, "DEI_root")

# --- dei_focus_momentum_kemerdekaan: crossroads / compass ---
img = canvas(); d = ImageDraw.Draw(img)
cx, cy = S/2, S/2
for ang in (0, 90, 180, 270):
    a = math.radians(ang)
    d.line([(cx, cy), (cx+95*math.cos(a), cy+95*math.sin(a))], fill=GLYPH, width=16)
star(d, cx, cy, 34, 15, 4, GLYPH)
save(img, "DEI_momentum")

# --- Jalur A root: ballot star (democratic proclamation) ---
img = canvas(); d = ImageDraw.Draw(img)
star(d, S/2, S/2 - 6, 100, 42, 5, GLYPH)
save(img, "DEI_path_a_root")

# --- Jalur B root: shield (colonial/federal authority) ---
img = canvas(); d = ImageDraw.Draw(img)
cx, cy = S/2, S/2
pts = [(cx-85, cy-95), (cx+85, cy-95), (cx+85, cy+20), (cx, cy+100), (cx-85, cy+20)]
d.polygon(pts, outline=GLYPH, width=16)
d.line([(cx, cy-95), (cx, cy+70)], fill=GLYPH, width=14)
save(img, "DEI_path_b_root")

# --- Jalur C root: red-star analogue as plain glyph star with hammer bar ---
img = canvas(); d = ImageDraw.Draw(img)
star(d, S/2, S/2, 95, 40, 5, GLYPH)
save(img, "DEI_path_c_root")

# --- Jalur D root: raised fist (radical/militant) ---
img = canvas(); d = ImageDraw.Draw(img)
cx, cy = S/2, S/2
d.rectangle([cx-26, cy-20, cx+26, cy+90], fill=GLYPH)          # forearm
d.ellipse([cx-60, cy-100, cx+60, cy-2], fill=GLYPH)             # fist mass
for i in range(3):
    x = cx - 40 + i*40
    d.rectangle([x-10, cy-120, x+10, cy-60], fill=GLYPH)        # knuckle notches (subtractive look)
save(img, "DEI_path_d_root")

# --- Jalur E root: crescent + star (Islamic state) ---
img = canvas(); d = ImageDraw.Draw(img)
cx, cy = S/2, S/2
d.ellipse([cx-90, cy-90, cx+90, cy+90], fill=GLYPH)
d.ellipse([cx-55, cy-95, cx+115, cy+85], fill=(0,0,0,0))
star(d, cx+70, cy-30, 28, 12, 5, GLYPH)
save(img, "DEI_path_e_root")

# --- Jalur F root: ancient temple / stupa silhouette (abstract, not a real building) ---
img = canvas(); d = ImageDraw.Draw(img)
cx, cy = S/2, S/2 + 40
tiers = [(150, 30), (110, 30), (75, 30), (40, 40)]
y = cy
for w, h in tiers:
    d.polygon([(cx-w, y), (cx+w, y), (cx+w*0.7, y-h), (cx-w*0.7, y-h)], fill=GLYPH)
    y -= h
d.polygon([(cx-14, y), (cx+14, y), (cx, y-45)], fill=GLYPH)
save(img, "DEI_path_f_root")

print("done")

# --- FIX: Jalur C root needs to be visually distinct from Jalur A (both were stars) ---
# Replace with a simple cog/gear glyph (industrial/working-class motif).
img = canvas(); d = ImageDraw.Draw(img)
cx, cy = S/2, S/2
outer_r, inner_r, tooth_r, teeth = 78, 55, 95, 10
pts = []
for i in range(teeth * 2):
    ang = i * math.pi / teeth
    r = tooth_r if i % 2 == 0 else outer_r
    pts.append((cx + r*math.cos(ang), cy + r*math.sin(ang)))
d.polygon(pts, fill=GLYPH)
d.ellipse([cx-inner_r, cy-inner_r, cx+inner_r, cy+inner_r], fill=(0,0,0,0))
d.ellipse([cx-30, cy-30, cx+30, cy+30], fill=GLYPH)
save(img, "DEI_path_c_root")
