import glob, os, re

r56_dir = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\interface"
for gf in glob.glob(os.path.join(r56_dir, "*.gfx")):
    with open(gf, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
        if "GFX_portrait_INS_sudirman" in c:
            print("Found in R56:", gf)
            m = re.search(r'spriteType\s*=\s*\{[^}]*name\s*=\s*"GFX_portrait_INS_sudirman"[^}]*texturefile\s*=\s*"([^"]+)"', c)
            if m: print(m.group(0))

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\interface"
for gf in glob.glob(os.path.join(mod_dir, "*.gfx")):
    with open(gf, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
        if "GFX_portrait_INS" in c or "portrait" in c:
            print("Found in Mod:", gf)
