import os
from PIL import Image

base = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
flags_dir = os.path.join(base, "gfx", "flags")

converted = 0
for root, dirs, files in os.walk(flags_dir):
    for f in files:
        if f.endswith(".tga"):
            p = os.path.join(root, f)
            try:
                im = Image.open(p)
                if im.mode != "RGBA":
                    rgba = im.convert("RGBA")
                    rgba.save(p)
                    converted += 1
            except Exception as e:
                print(f"Error on {f}: {e}")

print(f"Converted {converted} flags to 32bpp RGBA!")
