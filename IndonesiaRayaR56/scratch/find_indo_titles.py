import re

loc_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"

with open(loc_path, "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

indo_stems = [
    "pembangkangan", "retaknya", "kemerdekaan", "perundingan", "agresi militer", 
    "meja bundar", "tata kelola", "kedaulatan & diplomasi", "pemberontakan",
    "ambang revolusi", "momentum kemerdekaan", "seruan", "deklarasi", "sidang", "pemogokan"
]

print("Scanning for titles with Indonesian phrases:")
for i, line in enumerate(lines, 1):
    m = re.match(r'^\s*([a-zA-Z0-9_\.]+):\s*"([^"]+)"', line)
    if m:
        k, v = m.group(1), m.group(2)
        # ignore desc and options
        if any(k.endswith(x) for x in ['_desc', '.d', '.a', '.b', '.c', '.d_opt', '.e', '.f', '.g', '.h', '.i']):
            continue
        v_lower = v.lower()
        for stem in indo_stems:
            if stem in v_lower:
                print(f"Line {i}: [{k}] = \"{v}\"")
                break
