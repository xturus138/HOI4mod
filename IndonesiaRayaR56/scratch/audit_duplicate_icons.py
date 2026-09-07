import os
import re
from collections import defaultdict
import hashlib

base_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
tree_path = os.path.join(base_dir, "common", "national_focus", "DEI_indonesia_focus_tree.txt")
gfx_path = os.path.join(base_dir, "interface", "DEI_goals.gfx")

# Parse sprite definitions in DEI_goals.gfx
sprite_map = {}
with open(gfx_path, "r", encoding="utf-8") as f:
    gfx_txt = f.read()

for m in re.finditer(r'name\s*=\s*"(GFX_[a-zA-Z0-9_]+)"\s*texturefile\s*=\s*"([^"]+)"', gfx_txt):
    sname, tpath = m.group(1), m.group(2)
    # normalize path
    full_tpath = os.path.join(base_dir, tpath.replace("/", "\\"))
    sprite_map[sname] = full_tpath

# Parse tree focuses
with open(tree_path, "r", encoding="utf-8") as f:
    tree_txt = f.read()

focus_icons = []
for m in re.finditer(r'id\s*=\s*([a-zA-Z0-9_]+)[^}]+?icon\s*=\s*([a-zA-Z0-9_]+)', tree_txt):
    fid, icon = m.group(1), m.group(2)
    focus_icons.append((fid, icon))

print(f"Total focuses with icons: {len(focus_icons)}")

# Group focuses by sprite name
by_sprite = defaultdict(list)
for fid, icon in focus_icons:
    by_sprite[icon].append(fid)

print("\n--- FOCUSES SHARING THE SAME SPRITE NAME ---")
for icon, fids in by_sprite.items():
    if len(fids) > 1:
        print(f"Sprite '{icon}' used by {len(fids)} focuses: {fids}")

# Also check DDS file hash duplicates in gfx/interface/goals/
print("\n--- DDS FILE CONTENT DUPLICATES IN gfx/interface/goals/ ---")
goals_dir = os.path.join(base_dir, "gfx", "interface", "goals")
hashes = defaultdict(list)
for fn in os.listdir(goals_dir):
    if fn.endswith(".dds"):
        fp = os.path.join(goals_dir, fn)
        h = hashlib.md5(open(fp, "rb").read()).hexdigest()
        hashes[h].append(fn)

for h, fns in hashes.items():
    if len(fns) > 1:
        print(f"Identical DDS content ({h[:8]}): {fns}")
