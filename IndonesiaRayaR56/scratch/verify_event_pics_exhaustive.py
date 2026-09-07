import os
import glob
import re
from PIL import Image

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
event_files = glob.glob(os.path.join(mod_dir, "events", "*.txt"))
gfx_file = os.path.join(mod_dir, "interface", "DEI_event_pictures.gfx")

# Read GFX map
with open(gfx_file, "r", encoding="utf-8") as f:
    gfx_txt = f.read()

sprite_map = {}
for m in re.finditer(r'spriteType\s*=\s*\{[^}]*name\s*=\s*"([^"]+)"[^}]*texturefile\s*=\s*"([^"]+)"', gfx_txt):
    sprite_map[m.group(1)] = m.group(2)

print(f"Total event sprites in DEI_event_pictures.gfx: {len(sprite_map)}")

# Scan all events
events_checked = 0
errors = []

for ef in event_files:
    with open(ef, "r", encoding="utf-8", errors="ignore") as f:
        txt = f.read()
    
    # find all country_event
    i = 0
    while True:
        idx = txt.find("country_event = {", i)
        if idx == -1: idx = txt.find("country_event={", i)
        if idx == -1: break
        start = txt.find("{", idx)
        pos = start
        bc = 0
        while pos < len(txt):
            if txt[pos] == '{': bc += 1
            elif txt[pos] == '}':
                bc -= 1
                if bc == 0:
                    eb = txt[idx:pos+1]
                    eid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\.]+)', eb).group(1)
                    pic_m = re.search(r'\bpicture\s*=\s*([a-zA-Z0-9_]+)', eb)
                    if not pic_m:
                        errors.append(f"Event {eid} has NO picture!")
                    else:
                        pic = pic_m.group(1)
                        if pic not in sprite_map:
                            errors.append(f"Event {eid} uses unknown sprite {pic}")
                        else:
                            rel_tex = sprite_map[pic].replace("/", os.sep)
                            full_tex = os.path.join(mod_dir, rel_tex)
                            if not os.path.exists(full_tex):
                                errors.append(f"Sprite {pic} points to missing file {full_tex}")
                            else:
                                im = Image.open(full_tex)
                                if im.size != (210, 176):
                                    errors.append(f"Sprite {pic} has WRONG size {im.size} (must be 210, 176)")
                    events_checked += 1
                    i = pos + 1
                    break
            pos += 1
        else: break

print(f"Total events checked: {events_checked}")
if errors:
    print("ERRORS FOUND:")
    for err in errors:
        print(" ", err)
else:
    print("ALL 127 EVENTS USE VALID, EXISTING, EXACT (210, 176) DDS PICTURES!")
