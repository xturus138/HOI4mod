import re, glob, os

sprites = set()
# check .gui and .gfx files in interface
gfx_files = glob.glob(r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\interface\*.gfx")
r56_gfx = glob.glob(r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\interface\*.gfx")

for f in gfx_files + r56_gfx:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.search(r'name\s*=\s*"([^"]+)"', line)
                if m:
                    sprites.add(m.group(1))
    except:
        pass

test_icons = [
    "GFX_focus_research",
    "GFX_goal_generic_radar",
    "GFX_goal_generic_secret_weapon",
    "GFX_focus_wonderweapons",
    "GFX_goal_generic_oil_refinery",
    "GFX_goal_generic_scientific_exchange",
    "GFX_goal_tfv_generic_tech_sharing"
]

for ic in test_icons:
    print(f"{ic}: {ic in sprites}")
