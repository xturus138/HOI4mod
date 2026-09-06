import os, glob, re

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
focus_files = glob.glob(os.path.join(mod_dir, 'common', 'national_focus', '*.txt'))
focuses = {}
for ff in focus_files:
    with open(ff, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    i = 0
    while True:
        idx = txt.find('focus = {', i)
        if idx == -1: idx = txt.find('focus={', i)
        if idx == -1: break
        start = txt.find('{', idx)
        pos = start
        bc = 0
        while pos < len(txt):
            if txt[pos] == '{': bc += 1
            elif txt[pos] == '}':
                bc -= 1
                if bc == 0:
                    fb = txt[idx:pos+1]
                    fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', fb).group(1)
                    x = int(re.search(r'\bx\s*=\s*(-?\d+)', fb).group(1))
                    y = int(re.search(r'\by\s*=\s*(-?\d+)', fb).group(1))
                    rel = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', fb)
                    rel_id = rel.group(1) if rel else None
                    focuses[fid] = {'x': x, 'y': y, 'rel': rel_id, 'file': os.path.basename(ff)}
                    i = pos + 1
                    break
            pos += 1
        else: break

abs_pos = {}
def get_abs(fid):
    if fid in abs_pos: return abs_pos[fid]
    dat = focuses[fid]
    if dat['rel'] is None or dat['rel'] not in focuses:
        abs_pos[fid] = (dat['x'], dat['y'])
    else:
        px, py = get_abs(dat['rel'])
        abs_pos[fid] = (px + dat['x'], py + dat['y'])
    return abs_pos[fid]

all_coords = {}
for fid in focuses:
    all_coords[fid] = get_abs(fid)

print("Coordinates near X in range 25..31:")
for fid, (x, y) in sorted(all_coords.items(), key=lambda item: (item[1][0], item[1][1])):
    if 25 <= x <= 32:
        print(f"X={x:2}, Y={y:2} : {fid:35} in {focuses[fid]['file']}")
