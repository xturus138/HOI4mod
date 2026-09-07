import os
import re
from PIL import Image

vanilla_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"
gfx_file = os.path.join(vanilla_dir, "interface", "eventpictures.gfx")

with open(gfx_file, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

m = re.search(r'name\s*=\s*"GFX_report_event_001"[^}]*texturefile\s*=\s*"([^"]+)"', text)
if m:
    rel_path = m.group(1).replace("/", os.sep)
    full_path = os.path.join(vanilla_dir, rel_path)
    print("Found GFX_report_event_001 path:", full_path)
    if os.path.exists(full_path):
        im = Image.open(full_path)
        print("DIMENSIONS OF GFX_report_event_001:", im.size)
    else:
        print("File not found on disk:", full_path)

# Sample 5 other report events from vanilla
report_matches = re.findall(r'name\s*=\s*"(GFX_report_event_[^"]+)"[^}]*texturefile\s*=\s*"([^"]+)"', text)
print(f"\nTotal report event sprites found in vanilla: {len(report_matches)}")
for name, path in report_matches[:5]:
    fp = os.path.join(vanilla_dir, path.replace("/", os.sep))
    if os.path.exists(fp):
        im = Image.open(fp)
        print(f"  {name} -> {im.size} (DDS)")

# Also check news event sprites
news_matches = re.findall(r'name\s*=\s*"(GFX_news_event_[^"]+)"[^}]*texturefile\s*=\s*"([^"]+)"', text)
print(f"\nTotal news event sprites found in vanilla: {len(news_matches)}")
for name, path in news_matches[:3]:
    fp = os.path.join(vanilla_dir, path.replace("/", os.sep))
    if os.path.exists(fp):
        im = Image.open(fp)
        print(f"  {name} -> {im.size} (DDS)")
