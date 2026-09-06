import os
import re

r56_loc = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\localisation\english\INS_l_english.yml"
dei_loc = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"

with open(r56_loc, "r", encoding="utf-8-sig", errors="ignore") as f:
    r56_text = f.read()

r56_dict = {}
for line in r56_text.splitlines():
    m = re.match(r'^\s*([A-Za-z0-9_]+)(?::\d*)?\s+"([^"]*)"', line)
    if m:
        r56_dict[m.group(1)] = m.group(2)

focus_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus"
focus_ids = []
for fname in os.listdir(focus_dir):
    if fname.endswith(".txt"):
        with open(os.path.join(focus_dir, fname), "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            focus_ids.extend(re.findall(r'id\s*=\s*([A-Za-z0-9_]+)', content))

with open(dei_loc, "r", encoding="utf-8-sig", errors="ignore") as f:
    dei_text = f.read()

missing = []
for fid in focus_ids:
    if fid not in dei_text:
        missing.append(fid)
    if f"{fid}_desc" not in dei_text:
        missing.append(f"{fid}_desc")

print(f"Total missing keys: {len(missing)}")
found_in_r56 = [k for k in missing if k in r56_dict]
not_found = [k for k in missing if k not in r56_dict]
print(f"Found in R56: {len(found_in_r56)}")
print(f"Not found in R56: {len(not_found)}")
if not_found:
    print("Not found keys:", not_found)
