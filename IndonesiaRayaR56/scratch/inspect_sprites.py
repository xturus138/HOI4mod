import glob, re, os

vanilla_interface = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface'
r56_interface = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\interface'

def inspect_tech(p):
    results = []
    if not os.path.exists(p):
        return results
    for f in glob.glob(os.path.join(p, "*.gfx")):
        try:
            with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            names = re.findall(r'name\s*=\s*"([^"]+)"', c)
            for n in names:
                if n.endswith("_medium") and ("weapons" in n or "tank" in n or "fighter" in n or "artillery" in n or "armored" in n):
                    results.append((os.path.basename(f), n))
        except Exception:
            pass
    return results

print("Tech sprites sample in Vanilla:")
v_tech = inspect_tech(vanilla_interface)
for f in glob.glob(os.path.join(r56_interface, '*tech*.gfx')) + glob.glob(os.path.join(r56_interface, '*Tech*.gfx')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    names = re.findall(r'name\s*=\s*"([^"]+)"', c)
    tech_sprites = [n for n in names if n.endswith("_medium")]
    print(os.path.basename(f), f"total medium sprites: {len(tech_sprites)}")
    tags = set([n.split('_')[1] for n in tech_sprites if len(n.split('_')) > 2 and len(n.split('_')[1]) == 3 and n.split('_')[1].isupper()])
    print("  tags:", sorted(list(tags))[:10])
    for n in tech_sprites[:10]:
        print("  ", n)
