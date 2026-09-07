import os, glob
from PIL import Image

events_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\gfx\event_pictures"
files = sorted(glob.glob(os.path.join(events_dir, "*.dds")))
print(f"Total event pictures: {len(files)}")
for f in files:
    im = Image.open(f)
    print(f"{os.path.basename(f):35}: {im.size} {im.mode}")
