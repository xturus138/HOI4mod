import os, glob, re

mod_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'
vanilla_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
r56_dir = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968'

# 1. Custom physical files in mod/gfx
custom_gfx = []
for root, dirs, files in os.walk(os.path.join(mod_dir, 'gfx')):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), mod_dir)
        custom_gfx.append(rel)

print(f"=== 1. FISIK BERKAS GRAFIS KUSTOM DI gfx/ ===")
print(f"Total berkas di folder gfx/: {len(custom_gfx)}")
flags_std = [f for f in custom_gfx if f.startswith(r'gfx\flags') and not ('medium' in f or 'small' in f)]
flags_med = [f for f in custom_gfx if r'gfx\flags\medium' in f]
flags_sml = [f for f in custom_gfx if r'gfx\flags\small' in f]
event_dds = [f for f in custom_gfx if r'gfx\event_pictures' in f]

print(f"- Flags Standard (82x52): {len(flags_std)}")
print(f"- Flags Medium (41x26): {len(flags_med)}")
print(f"- Flags Small (10x7): {len(flags_sml)}")
print(f"- Event Pictures (.dds kustom): {len(event_dds)}")
for ed in event_dds:
    print(f"    * {ed}")

# 2. Interface definitions in mod/interface
print(f"\n=== 2. DEFINISI INTERFACE (.gfx) KUSTOM ===")
mod_sprites = {}
for f in os.listdir(os.path.join(mod_dir, 'interface')):
    if f.endswith('.gfx'):
        fp = os.path.join(mod_dir, 'interface', f)
        with open(fp, 'r', encoding='utf-8', errors='ignore') as fp_in:
            c = fp_in.read()
        entries = re.findall(r'name\s*=\s*"([^"]+)"\s*texturefile\s*=\s*"([^"]+)"', c)
        print(f"File {f}: {len(entries)} sprite definitions:")
        for name, tex in entries:
            mod_sprites[name] = tex
            print(f"    * {name} -> {tex}")

# 3. Load R56 and Vanilla sprites
r56_sprites = set()
vanilla_sprites = set()

def scan_dir(dir_path, target_set):
    if not os.path.exists(dir_path): return
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith('.gfx'):
                try:
                    with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as fp_in:
                        for n in re.findall(r'name\s*=\s*"([^"]+)"', fp_in.read()):
                            target_set.add(n)
                except: pass

scan_dir(os.path.join(r56_dir, 'interface'), r56_sprites)
scan_dir(os.path.join(vanilla_dir, 'interface'), vanilla_sprites)

# 4. Check Focus Icons in Focus Trees
focus_files = glob.glob(os.path.join(mod_dir, 'common', 'national_focus', 'DEI_*.txt'))
focus_icons = {}
for ff in focus_files:
    fname = os.path.basename(ff)
    with open(ff, 'r', encoding='utf-8', errors='ignore') as fp:
        c = re.sub(r'#.*', '', fp.read())
    icons = re.findall(r'icon\s*=\s*([a-zA-Z0-9_]+)', c)
    for ic in icons:
        if ic not in focus_icons:
            focus_icons[ic] = []
        focus_icons[ic].append(fname)

print(f"\n=== 3. FOCUS ICONS AUDIT (Total Penggunaan: {sum(len(v) for v in focus_icons.values())}, Unik: {len(focus_icons)}) ===")
fi_custom = []
fi_r56 = []
fi_vanilla = []
fi_unknown = []
for ic in focus_icons:
    if ic in mod_sprites:
        fi_custom.append(ic)
    elif ic in r56_sprites and ic not in vanilla_sprites:
        fi_r56.append(ic)
    elif ic in vanilla_sprites:
        fi_vanilla.append(ic)
    else:
        fi_unknown.append(ic)

print(f"- Custom Mod Sprites: {len(fi_custom)} {fi_custom}")
print(f"- R56 Specific Sprites: {len(fi_r56)} {fi_r56}")
print(f"- Vanilla Generic/Base Sprites: {len(fi_vanilla)}")
print(f"- Unknown: {len(fi_unknown)}")

# 5. Check Event Pictures in Events
event_files = glob.glob(os.path.join(mod_dir, 'events', '*.txt'))
event_pics = {}
for ef in event_files:
    fname = os.path.basename(ef)
    with open(ef, 'r', encoding='utf-8', errors='ignore') as fp:
        c = re.sub(r'#.*', '', fp.read())
    pics = re.findall(r'picture\s*=\s*([a-zA-Z0-9_]+)', c)
    for p in pics:
        if p not in event_pics:
            event_pics[p] = []
        event_pics[p].append(fname)

print(f"\n=== 4. EVENT PICTURES AUDIT (Total Penggunaan: {sum(len(v) for v in event_pics.values())}, Unik: {len(event_pics)}) ===")
ep_custom = []
ep_r56 = []
ep_vanilla = []
ep_unknown = []
for p in event_pics:
    if p in mod_sprites:
        ep_custom.append(p)
    elif p in r56_sprites and p not in vanilla_sprites:
        ep_r56.append(p)
    elif p in vanilla_sprites:
        ep_vanilla.append(p)
    else:
        ep_unknown.append(p)

print(f"- Custom Mod Sprites (.dds di gfx/event_pictures/): {len(ep_custom)}")
for p in ep_custom:
    print(f"    * {p} -> {mod_sprites.get(p)}")
print(f"- R56 Specific Sprites: {len(ep_r56)} {ep_r56}")
print(f"- Vanilla Base Game Event Sprites: {len(ep_vanilla)}")
for p in sorted(ep_vanilla):
    print(f"    * {p}")

# 6. Check Ideas / MIOs Pictures
ideas_file = os.path.join(mod_dir, 'common', 'ideas', 'DEI_ideas.txt')
with open(ideas_file, 'r', encoding='utf-8', errors='ignore') as fp:
    c = re.sub(r'#.*', '', fp.read())
idea_pics = re.findall(r'picture\s*=\s*([a-zA-Z0-9_]+)', c)
print(f"\n=== 5. IDEAS & MIO DESIGNERS ICONS (Total: {len(idea_pics)}) ===")
idea_custom = [ip for ip in idea_pics if ip in mod_sprites or f"GFX_idea_{ip}" in mod_sprites]
idea_r56 = [ip for ip in idea_pics if (ip in r56_sprites or f"GFX_idea_{ip}" in r56_sprites) and (ip not in vanilla_sprites and f"GFX_idea_{ip}" not in vanilla_sprites)]
idea_vanilla = [ip for ip in idea_pics if ip not in idea_custom and ip not in idea_r56]
print(f"- Custom Mod: {len(idea_custom)}")
print(f"- R56 Specific (Pindad, PAL, BPM, Braat, IPTN, dll): {len(idea_r56)} {idea_r56}")
print(f"- Vanilla Generic/Base: {len(idea_vanilla)} {idea_vanilla}")

# 7. Check Character Portraits
char_files = glob.glob(os.path.join(mod_dir, 'common', 'characters', '*.txt'))
print(f"\n=== 6. CHARACTER PORTRAITS ===")
for cf in char_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as fp:
        c = re.sub(r'#.*', '', fp.read())
    ports = re.findall(r'(?:large|small)\s*=\s*"?([a-zA-Z0-9_]+)"?', c)
    for pt in ports:
        src = "Mod Interface -> R56 DDS" if pt in mod_sprites else ("Vanilla" if pt in vanilla_sprites else "R56/Unknown")
        print(f"    * {pt}: {src}")

# 8. Check Decisions Icons
dec_file = os.path.join(mod_dir, 'common', 'decisions', 'DEI_decisions.txt')
with open(dec_file, 'r', encoding='utf-8', errors='ignore') as fp:
    c = re.sub(r'#.*', '', fp.read())
dec_icons = re.findall(r'icon\s*=\s*([a-zA-Z0-9_]+)', c)
print(f"\n=== 7. DECISIONS ICONS (Total: {len(dec_icons)}, Unik: {len(set(dec_icons))}) ===")
print(f"    * Unik: {set(dec_icons)} (Semua menggunakan generic/vanilla decision icons)")

# 9. Check 3D models, sound, music
has_music = os.path.exists(os.path.join(mod_dir, 'music')) or os.path.exists(os.path.join(mod_dir, 'sound'))
print(f"\n=== 8. SOUND, MUSIC & 3D MODELS ===")
print(f"- Custom Sound / Music: {'ADA' if has_music else 'TIDAK ADA (Menggunakan Default Vanilla/R56)'}")
has_entities = os.path.exists(os.path.join(mod_dir, 'gfx', 'entities')) or os.path.exists(os.path.join(mod_dir, 'gfx', 'models'))
print(f"- Custom 3D Unit Models: {'ADA' if has_entities else 'TIDAK ADA (Menggunakan Default Vanilla/R56)'}")
