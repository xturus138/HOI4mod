import os
from PIL import Image, ImageDraw

goals_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\gfx\interface\goals"

# Create an 82x82 circular alpha mask
mask = Image.new("L", (82, 82), 0)
draw = ImageDraw.Draw(mask)
# Draw anti-aliased circle
draw.ellipse((2, 2, 79, 79), fill=255)

icons_to_fix = [
    "focus_dei_radar_nusantara.dds",
    "focus_dei_itb_bandung.dds",
    "focus_dei_kilang_minyak.dds",
    "focus_dei_fisika_atom.dds"
]

for fname in icons_to_fix:
    fpath = os.path.join(goals_dir, fname)
    im = Image.open(fpath).convert("RGBA")
    
    # Apply circular mask to the existing image
    r, g, b, _ = im.split()
    im_circular = Image.merge("RGBA", (r, g, b, mask))
    
    # Save as DDS uncompressed RGBA
    im_circular.save(fpath, format="DDS")
    print(f"Fixed circular alpha mask for {fname}")

# Verify corners are now 0 alpha
for fname in icons_to_fix:
    fpath = os.path.join(goals_dir, fname)
    im = Image.open(fpath)
    alpha = im.split()[3]
    print(f"{fname}: Corner (0,0) alpha = {alpha.getpixel((0,0))}, Center (41,41) alpha = {alpha.getpixel((41,41))}")
