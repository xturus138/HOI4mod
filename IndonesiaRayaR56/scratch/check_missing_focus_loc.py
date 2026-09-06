import os, re

r56_loc = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\localisation\english\INS_l_english.yml"
dei_loc = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"
mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"

# Load R56 loc dict
r56_dict = {}
with open(r56_loc, "r", encoding="utf-8-sig", errors="ignore") as f:
    for line in f:
        m = re.match(r'^\s*([a-zA-Z0-9_\.]+):(?:\d+)?\s*"(.*)"', line)
        if m:
            r56_dict[m.group(1)] = m.group(2)

# Load DEI loc keys
loc_keys = {}
with open(dei_loc, "r", encoding="utf-8-sig") as f:
    for line in f:
        m = re.match(r'^\s*([a-zA-Z0-9_\.]+):(?:\d+)?\s*"(.*)"', line)
        if m:
            loc_keys[m.group(1)] = m.group(2)

# Get focuses from master_audit logic
import glob
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
                    focuses[fid] = os.path.basename(ff)
                    i = pos + 1
                    break
            pos += 1
        else: break

print(f"Total focuses: {len(focuses)}")
missing = []
for fid in focuses:
    if fid not in loc_keys:
        missing.append((fid, 'name', focuses[fid]))
    if f"{fid}_desc" not in loc_keys:
        missing.append((f"{fid}_desc", 'desc', focuses[fid]))

print(f"Total missing: {len(missing)}")
for m, t, src in missing:
    in_r56 = m in r56_dict
    val = r56_dict.get(m, "NOT FOUND IN R56")
    print(f"Key: {m} | In R56: {in_r56} | File: {src} | Val: {val[:40] if in_r56 else val}")
