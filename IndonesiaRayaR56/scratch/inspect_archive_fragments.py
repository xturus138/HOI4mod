import os
import re

archive_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\scratch\archive_focus_fragments"

files = sorted(os.listdir(archive_dir))
for f in files:
    fp = os.path.join(archive_dir, f)
    with open(fp, "r", encoding="utf-8") as fl:
        txt = fl.read()
    print(f"\n==================== {f} ====================")
    i = 0
    while True:
        idx = txt.find("focus = {", i)
        if idx == -1: idx = txt.find("focus={", i)
        if idx == -1: break
        start = txt.find("{", idx)
        pos = start
        bc = 0
        while pos < len(txt):
            if txt[pos] == '{': bc += 1
            elif txt[pos] == '}':
                bc -= 1
                if bc == 0:
                    b = txt[idx:pos+1]
                    fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b).group(1)
                    xm = re.search(r'\bx\s*=\s*(-?\d+)', b)
                    ym = re.search(r'\by\s*=\s*(-?\d+)', b)
                    rm = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', b)
                    pm = re.findall(r'prerequisite\s*=\s*\{[^}]*focus\s*=\s*([a-zA-Z0-9_]+)', b)
                    x = int(xm.group(1)) if xm else 0
                    y = int(ym.group(1)) if ym else 0
                    rel = rm.group(1) if rm else None
                    print(f"  {fid:35} | x={x:3}, y={y:2} | rel={str(rel):30} | prereqs={pm}")
                    i = pos + 1
                    break
            pos += 1
        else: break
