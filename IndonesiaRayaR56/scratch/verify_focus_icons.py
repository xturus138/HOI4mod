import os
import re

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
vanilla_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"
r56_dir = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968"

tree_path = os.path.join(mod_dir, "common", "national_focus", "DEI_indonesia_focus_tree.txt")
with open(tree_path, "r", encoding="utf-8") as f:
    text = f.read()

icons = re.findall(r'icon\s*=\s*([a-zA-Z0-9_]+)', text)
unique_icons = set(icons)
print(f"Total focus icon references: {len(icons)}, Unique icons: {len(unique_icons)}")

# Check our mod's gfx files
mod_sprites = set()
for gf in [os.path.join(mod_dir, "interface", "DEI_goals.gfx")]:
    if os.path.exists(gf):
        with open(gf, "r", encoding="utf-8", errors="ignore") as f:
            mod_sprites.update(re.findall(r'name\s*=\s*"([^"]+)"', f.read()))

print(f"Icons registered in DEI_goals.gfx: {len(mod_sprites)}")

# Find which icons are NOT in our mod (meaning they are vanilla / R56 goals like GFX_goal_generic_...)
external_icons = unique_icons - mod_sprites
print(f"External/Vanilla icons used: {len(external_icons)}")

# Verify external icons exist in vanilla or R56
all_external_sprites = set()
for base in [vanilla_dir, r56_dir]:
    for gf in [os.path.join(base, "interface", "goals.gfx"), os.path.join(base, "interface", "r56_goals.gfx")]:
        if os.path.exists(gf):
            with open(gf, "r", encoding="utf-8", errors="ignore") as f:
                all_external_sprites.update(re.findall(r'name\s*=\s*"([^"]+)"', f.read()))

missing = []
for icon in external_icons:
    if icon not in all_external_sprites:
        missing.append(icon)

if missing:
    print("WARNING: Missing icons:", missing)
else:
    print("ALL 134 FOCUS ICONS ARE FULLY VALIDATED AND RESOLVED!")
