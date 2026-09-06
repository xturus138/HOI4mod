import os, re

vanilla_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
r56_dir = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968'
mod_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'

all_sprites = set()
def scan_gfx(dir_path):
    if not os.path.exists(dir_path): return
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith('.gfx'):
                fp = os.path.join(root, f)
                try:
                    with open(fp, 'r', encoding='utf-8', errors='ignore') as fp_in:
                        c = fp_in.read()
                    names = re.findall(r'name\s*=\s*"([^"]+)"', c)
                    for n in names: all_sprites.add(n)
                except: pass

scan_gfx(os.path.join(mod_dir, 'interface'))
scan_gfx(os.path.join(r56_dir, 'interface'))
scan_gfx(os.path.join(vanilla_dir, 'interface'))

test_icons = [
    "GFX_focus_research",
    "GFX_goal_generic_radar",
    "GFX_goal_generic_secret_weapon",
    "GFX_focus_wonderweapons",
    "GFX_goal_generic_oil_refinery",
    "GFX_goal_generic_scientific_exchange",
    "GFX_goal_tfv_generic_tech_sharing",
    "GFX_goal_generic_scientific_exchange",
    "GFX_focus_rocketry",
    "GFX_focus_nuclear"
]

for ic in test_icons:
    print(f"{ic}: {ic in all_sprites}")
