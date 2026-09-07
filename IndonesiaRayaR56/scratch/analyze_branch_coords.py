import re

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect each path's internal (relative) coordinates
paths = {
    'Path A': 'SECTION: DEI_01_path_a_republik.txt',
    'Path B': 'SECTION: DEI_02_path_b_kolonial.txt',
    'Path C': 'SECTION: DEI_03_path_c_komunis.txt',
    'Path D': 'SECTION: DEI_04_path_d_otoriter.txt',
    'Path E': 'SECTION: DEI_05_path_e_islamis.txt',
    'Path F': 'SECTION: DEI_06_path_f_majapahit.txt',
    'Industry': 'SECTION: DEI_r56_industry.txt',
    'Armed Forces': 'SECTION: DEI_r56_armed_forces.txt'
}

for pname, sec_header in paths.items():
    idx = text.find(sec_header)
    if idx == -1: continue
    # find next section or end
    next_idx = len(text)
    for other_pname, other_header in paths.items():
        if other_pname != pname:
            oidx = text.find(other_header, idx + len(sec_header))
            if oidx != -1 and oidx < next_idx:
                next_idx = oidx
    chunk = text[idx:next_idx]
    
    # parse focuses in chunk
    f_list = []
    i = 0
    while True:
        f_idx = chunk.find("focus = {", i)
        if f_idx == -1: f_idx = chunk.find("focus={", i)
        if f_idx == -1: break
        start = chunk.find("{", f_idx)
        pos = start
        bc = 0
        while pos < len(chunk):
            if chunk[pos] == '{': bc += 1
            elif chunk[pos] == '}':
                bc -= 1
                if bc == 0:
                    b = chunk[f_idx:pos+1]
                    fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b).group(1)
                    xm = re.search(r'\bx\s*=\s*(-?\d+)', b)
                    ym = re.search(r'\by\s*=\s*(-?\d+)', b)
                    rm = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', b)
                    pm = re.findall(r'prerequisite\s*=\s*\{[^}]*focus\s*=\s*([a-zA-Z0-9_]+)', b)
                    x = int(xm.group(1)) if xm else 0
                    y = int(ym.group(1)) if ym else 0
                    rel = rm.group(1) if rm else None
                    f_list.append((fid, x, y, rel, pm))
                    i = pos + 1
                    break
            pos += 1
        else: break
    
    print(f"\n==================== {pname} ({len(f_list)} focuses) ====================")
    xs = [f[1] for f in f_list]
    ys = [f[2] for f in f_list]
    print(f"X range: min={min(xs)}, max={max(xs)} (span = {max(xs) - min(xs) + 1})")
    print(f"Y range: min={min(ys)}, max={max(ys)} (span = {max(ys) - min(ys) + 1})")
    for fid, x, y, rel, pm in f_list:
        print(f"  {fid:35} | x={x:3}, y={y:2} | rel={str(rel):30} | prereq={pm}")
