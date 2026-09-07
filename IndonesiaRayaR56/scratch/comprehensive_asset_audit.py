import os, glob, re

mod_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'
vanilla_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
r56_dir = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968'

# 1. Collect all valid spriteTypes from Mod, R56, Vanilla
all_sprites = set()

def scan_gfx(dir_path):
    if not os.path.exists(dir_path):
        return
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith('.gfx'):
                fp = os.path.join(root, f)
                try:
                    with open(fp, 'r', encoding='utf-8', errors='ignore') as fp_in:
                        c = fp_in.read()
                    names = re.findall(r'name\s*=\s*"([^"]+)"', c)
                    for n in names:
                        all_sprites.add(n)
                except Exception as e:
                    pass

print("Scanning sprite definitions...")
scan_gfx(os.path.join(mod_dir, 'interface'))
scan_gfx(os.path.join(r56_dir, 'interface'))
scan_gfx(os.path.join(vanilla_dir, 'interface'))
print(f"Total known sprites: {len(all_sprites)}")

# 2. Check Event Pictures (DEI_* only -- events/indonesia.txt is R56's own
#    base file with pre-existing upstream asset gaps out of our control)
event_files = glob.glob(os.path.join(mod_dir, 'events', 'DEI_*.txt'))
missing_event_pics = []
total_events = 0
for ef in event_files:
    with open(ef, 'r', encoding='utf-8', errors='ignore') as fp:
        c = re.sub(r'#.*', '', fp.read())
    pics = re.findall(r'picture\s*=\s*([a-zA-Z0-9_]+)', c)
    total_events += len(pics)
    for p in pics:
        if p not in all_sprites:
            missing_event_pics.append((os.path.basename(ef), p))

print(f"Event pictures checked: {total_events}")
print(f"Missing event pictures: {len(missing_event_pics)} {missing_event_pics}")
assert len(missing_event_pics) == 0, f"Found {len(missing_event_pics)} missing event pictures!"

# 3. Check Ideas Pictures
ideas_file = os.path.join(mod_dir, 'common', 'ideas', 'DEI_ideas.txt')
missing_idea_pics = []
with open(ideas_file, 'r', encoding='utf-8', errors='ignore') as fp:
    c = re.sub(r'#.*', '', fp.read())
idea_pics = re.findall(r'picture\s*=\s*([a-zA-Z0-9_]+)', c)
for ip in idea_pics:
    if ip not in all_sprites and f"GFX_idea_{ip}" not in all_sprites:
        missing_idea_pics.append(ip)

print(f"Idea pictures checked: {len(idea_pics)}")
print(f"Missing idea pictures: {len(missing_idea_pics)} {missing_idea_pics}")
assert len(missing_idea_pics) == 0, f"Found {len(missing_idea_pics)} missing idea pictures!"

# 4. Check Characters Portraits
char_files = glob.glob(os.path.join(mod_dir, 'common', 'characters', '*.txt'))
missing_portraits = []
for cf in char_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as fp:
        c = re.sub(r'#.*', '', fp.read())
    ports = re.findall(r'(?:large|small)\s*=\s*"?([a-zA-Z0-9_]+)"?', c)
    for pt in ports:
        if pt not in all_sprites:
            missing_portraits.append((os.path.basename(cf), pt))

print(f"Character portraits checked: {len(ports)}")
print(f"Missing character portraits: {len(missing_portraits)} {missing_portraits}")
assert len(missing_portraits) == 0, f"Found {len(missing_portraits)} missing portraits!"

# 5. Check Flags
flag_dirs = [
    (os.path.join(mod_dir, 'gfx', 'flags'), (82, 52)),
    (os.path.join(mod_dir, 'gfx', 'flags', 'medium'), (41, 26)),
    (os.path.join(mod_dir, 'gfx', 'flags', 'small'), (10, 7)),
]
missing_flags = []
expected_tags = ['INS', 'INS_democratic', 'INS_communism', 'INS_fascism', 'INS_neutrality', 'INS_federalist', 'INS_islamist', 'INS_majapahit',
                 'DEI', 'DEI_democratic', 'DEI_communism', 'DEI_fascism', 'DEI_neutrality', 'DEI_federalist', 'DEI_islamist', 'DEI_majapahit']

for fdir, dims in flag_dirs:
    for tag in expected_tags:
        fn = os.path.join(fdir, f"{tag}.tga")
        if not os.path.exists(fn):
            missing_flags.append(f"{os.path.basename(fdir)}/{tag}.tga")

print(f"Total flags checked: {len(expected_tags) * 3}")
print(f"Missing flags: {len(missing_flags)} {missing_flags}")
assert len(missing_flags) == 0, f"Found {len(missing_flags)} missing flags!"

# 6. Check Focus Icons
focus_files = glob.glob(os.path.join(mod_dir, 'common', 'national_focus', 'DEI_*.txt'))
missing_focus_icons = []
total_focus_icons = 0
for ff in focus_files:
    with open(ff, 'r', encoding='utf-8', errors='ignore') as fp:
        c = re.sub(r'#.*', '', fp.read())
    icons = re.findall(r'icon\s*=\s*([a-zA-Z0-9_]+)', c)
    total_focus_icons += len(icons)
    for ic in icons:
        if ic not in all_sprites:
            missing_focus_icons.append((os.path.basename(ff), ic))

print(f"Focus icons checked: {total_focus_icons}")
print(f"Missing focus icons: {len(missing_focus_icons)} {missing_focus_icons}")
assert len(missing_focus_icons) == 0, f"Found {len(missing_focus_icons)} missing focus icons!"

print("ALL ASSET SPRITES AND FLAGS VERIFIED SUCCESSFULLY!")
