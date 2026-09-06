from PIL import Image
import glob, os

print("--- Existing Goals ---")
for f in glob.glob("gfx/interface/goals/*.dds"):
    im = Image.open(f)
    print(os.path.basename(f), im.size, im.mode, im.format)

print("--- Existing Tech ---")
for f in glob.glob("gfx/interface/technologies/*.dds"):
    im = Image.open(f)
    print(os.path.basename(f), im.size, im.mode, im.format)
