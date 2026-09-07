import os
import re

focus_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus"

files = [
    "DEI_00_shared_trunk.txt",
    "DEI_01_path_a_republik.txt",
    "DEI_02_path_b_kolonial.txt",
    "DEI_03_path_c_komunis.txt",
    "DEI_04_path_d_otoriter.txt",
    "DEI_05_path_e_islamis.txt",
    "DEI_06_path_f_majapahit.txt",
    "DEI_r56_industry.txt",
    "DEI_r56_armed_forces.txt"
]

header = """# =====================================================================
# INDONESIA RAYA: ROAD TO MERDEKA — Master National Focus Tree
# Tag: INS (Indonesia / Hindia Belanda)
# Total: 134 focuses (Shared Prologue, Paths A-F, Industry, Armed Forces)
# =====================================================================

focus_tree = {
\tid = dei_focus_tree

\tcountry = {
\t\tfactor = 0
\t\tmodifier = {
\t\t\tadd = 50
\t\t\ttag = INS
\t\t}
\t}

\tdefault = no
\treset_on_civilwar = no
"""

body = [header]

for fname in files:
    fpath = os.path.join(focus_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the first 'focus = {'
    first_focus = content.find("focus = {")
    if first_focus == -1:
        # try tabs
        m = re.search(r"^\s*focus\s*=\s*\{", content, re.MULTILINE)
        if m:
            first_focus = m.start()
        else:
            print(f"ERROR: No focus found in {fname}")
            continue

    # Find the last closing brace '}'
    last_brace = content.rfind("}")
    inner = content[first_focus:last_brace].rstrip()
    body.append(f"\n\n\t# ---------------------------------------------------------------------\n\t# SECTION: {fname}\n\t# ---------------------------------------------------------------------\n")
    body.append(inner)

body.append("\n}\n")

master_file = os.path.join(focus_dir, "DEI_indonesia_focus_tree.txt")
with open(master_file, "w", encoding="utf-8") as f:
    f.write("\n".join(body))

# Count focuses in master
with open(master_file, "r", encoding="utf-8") as f:
    master_content = f.read()

total = len(re.findall(r"^\s*focus\s*=\s*\{", master_content, re.MULTILINE))
print(f"SUCCESS: Master tree created at {master_file} with {total} focuses!")
