import os, re

fpath = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_r56_industry.txt"

with open(fpath, "r", encoding="utf-8") as f:
    txt = f.read()

i = 0
focuses = {}
while True:
    idx = txt.find("focus = {", i)
    if idx == -1: idx = txt.find("focus={", i)
    if idx == -1: break
    start = txt.find("{", idx)
    pos = start
    bc = 0
    while pos < len(txt):
        if txt[pos] == "{": bc += 1
        elif txt[pos] == "}":
            bc -= 1
            if bc == 0:
                fb = txt[idx:pos+1]
                fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', fb).group(1)
                x = int(re.search(r'\bx\s*=\s*(-?\d+)', fb).group(1))
                y = int(re.search(r'\by\s*=\s*(-?\d+)', fb).group(1))
                rel = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', fb)
                rel_id = rel.group(1) if rel else None
                prereqs = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_]+)', fb)
                focuses[fid] = {'x': x, 'y': y, 'rel': rel_id, 'prereqs': prereqs}
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

print(f"Total industry focuses: {len(focuses)}")
for fid in focuses:
    p = get_abs(fid)
    print(f"{fid:35} Abs: ({p[0]:2}, {p[1]:2}) Rel: {str(focuses[fid]['rel']):25} ({focuses[fid]['x']:2}, {focuses[fid]['y']:2}) Prereqs: {focuses[fid]['prereqs']}")
