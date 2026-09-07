import os, re

base = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"

# 1. Check all DDS files referenced in GFX
gfx_files = []
for root, dirs, files in os.walk(os.path.join(base, "interface")):
    for f in files:
        if f.endswith(".gfx"):
            gfx_files.append(os.path.join(root, f))

missing_textures = []
for gf in gfx_files:
    with open(gf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    textures = re.findall(r'texturefile\s*=\s*"([^"]+)"', content, re.IGNORECASE)
    for tex in textures:
        # normalized path
        tex_clean = tex.replace("/", "\\")
        full_p = os.path.join(base, tex_clean)
        if not os.path.exists(full_p):
            # check if it is vanilla / r56 texture
            if "dei" in tex.lower():
                missing_textures.append((gf, tex))

print(f"Missing custom textures in GFX files: {len(missing_textures)}")
for m in missing_textures[:10]:
    print(" ", m)

# 2. Check all braces across all txt, gfx, gui
unbalanced = []
for root, dirs, files in os.walk(base):
    if "scratch" in root or ".git" in root: continue
    for f in files:
        if f.endswith((".txt", ".gfx", ".gui")):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as fl:
                t = fl.read()
            o = t.count("{")
            c = t.count("}")
            if o != c:
                unbalanced.append((os.path.relpath(p, base), o, c))

print(f"Unbalanced brace files: {len(unbalanced)}")
for u in unbalanced:
    print(" ", u)
