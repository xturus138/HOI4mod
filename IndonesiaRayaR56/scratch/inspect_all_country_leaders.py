import os, re, glob

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
r56_dir = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968"

# Collect all sprite to texture mappings
sprite_map = {}
for gf in glob.glob(os.path.join(mod_dir, 'interface', '*.gfx')) + glob.glob(os.path.join(r56_dir, 'interface', '*.gfx')):
    try:
        with open(gf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        matches = re.findall(r'spriteType\s*=\s*\{[^}]*name\s*=\s*"([^"]+)"[^}]*texturefile\s*=\s*"([^"]+)"', c)
        for sname, tfile in matches:
            sprite_map[sname] = tfile
    except:
        pass

# Check leaders in characters
chars = {}
for cf in glob.glob(os.path.join(mod_dir, 'common', 'characters', '*.txt')) + glob.glob(os.path.join(r56_dir, 'common', 'characters', 'INS*.txt')):
    try:
        with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        # Find character definitions
        i = 0
        while True:
            m = re.search(r'([a-zA-Z0-9_]+)\s*=\s*\{', c[i:])
            if not m: break
            cid = m.group(1)
            # check if country_leader in block
            start = i + m.end() - 1
            pos = start
            bc = 0
            while pos < len(c):
                if c[pos] == '{': bc += 1
                elif c[pos] == '}':
                    bc -= 1
                    if bc == 0:
                        block = c[start:pos+1]
                        if 'country_leader' in block or 'civilian' in block:
                            # get name and portrait
                            nm = re.search(r'name\s*=\s*"([^"]+)"', block)
                            pt = re.search(r'(?:civilian|army|navy)\s*=\s*\{[^}]*large\s*=\s*"([^"]+)"', block)
                            chars[cid] = {
                                'name': nm.group(1) if nm else cid,
                                'portrait': pt.group(1) if pt else None,
                                'file': os.path.basename(cf)
                            }
                        i = pos + 1
                        break
                pos += 1
            else: break
    except:
        pass

print(f"Total country leaders found in character files: {len(chars)}")
for cid, dat in sorted(chars.items()):
    p_sprite = dat['portrait']
    tex = sprite_map.get(p_sprite, "NO_SPRITE_MAPPING")
    print(f"[{dat['file']}] {cid:30} Name: {dat['name']:25} Sprite: {str(p_sprite):35} Tex: {tex}")
