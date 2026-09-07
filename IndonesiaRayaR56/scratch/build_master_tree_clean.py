import os
import re

archive_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\scratch\archive_focus_fragments"
output_file = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"

master_header = """# =====================================================================
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

body = [master_header]

def parse_focus_blocks(text):
    """Linear brace-matching parser to extract each focus block."""
    blocks = []
    i = 0
    while True:
        idx = text.find("focus = {", i)
        if idx == -1: idx = text.find("focus={", i)
        if idx == -1: break
        start = text.find("{", idx)
        pos = start
        bc = 0
        while pos < len(text):
            if text[pos] == '{': bc += 1
            elif text[pos] == '}':
                bc -= 1
                if bc == 0:
                    blocks.append(text[idx:pos+1])
                    i = pos + 1
                    break
            pos += 1
        else: break
    return blocks

# --- 1. PROLOGUE: Revolusi Nasional 1936 (x=28, y=0, 1, 2) ---
with open(os.path.join(archive_dir, "DEI_00_shared_trunk.txt"), "r", encoding="utf-8") as f:
    txt = f.read()

p_blocks = parse_focus_blocks(txt)
prologue_str = []
for b in p_blocks:
    if "id = dei_focus_root" in b:
        b = re.sub(r'\bx\s*=\s*\d+', 'x = 28', b)
        b = re.sub(r'\by\s*=\s*\d+', 'y = 0', b)
    elif "id = dei_focus_pembangkangan" in b:
        b = re.sub(r'\bx\s*=\s*\d+', 'x = 28', b)
        b = re.sub(r'\by\s*=\s*\d+', 'y = 1', b)
    elif "id = dei_focus_momentum_kemerdekaan" in b:
        b = re.sub(r'\bx\s*=\s*\d+', 'x = 28', b)
        b = re.sub(r'\by\s*=\s*\d+', 'y = 2', b)
    prologue_str.append(b)

body.append("\n\n\t# =====================================================================\n\t# PROLOGUE: Revolusi Nasional 1936\n\t# =====================================================================\n")
body.append("\n\n".join(prologue_str))

# --- 2. PATHS A TO F (Roots at x = 8, 16, 24, 32, 40, 48) ---
# In archive:
# Path A root was x=-8, y=9. Target root abs x=8. Momentum is at 28. Rel x = 8 - 28 = -20. dx = -20 - (-8) = -12.
# Path B root was x=-2, y=9. Target root abs x=16. Rel x = 16 - 28 = -12. dx = -12 - (-2) = -10.
# Path C root was x=4, y=9. Target root abs x=24. Rel x = 24 - 28 = -4. dx = -4 - 4 = -8.
# Path D root was x=10, y=9. Target root abs x=32. Rel x = 32 - 28 = +4. dx = 4 - 10 = -6.
# Path E root was x=16, y=9. Target root abs x=40. Rel x = 40 - 28 = +12. dx = 12 - 16 = -4.
# Path F root was x=22, y=9. Target root abs x=48. Rel x = 48 - 28 = +20. dx = 20 - 22 = -2.
# dy = -8 for all (y=9 -> y=1 rel to Momentum at y=2, abs y=3).

path_configs = [
    ("DEI_01_path_a_republik.txt", "PATH A: Republik Nasionalis-Demokratis", -12, -8, "dei_focus_a_proklamasi", "dei_path_a_chosen", "dei_path_a_chosen_tt"),
    ("DEI_02_path_b_kolonial.txt", "PATH B: Kolonial / Federalis", -10, -8, "dei_focus_b_root", "dei_path_b_chosen", "dei_path_b_chosen_tt"),
    ("DEI_03_path_c_komunis.txt", "PATH C: Komunis (Front Rakyat)", -8, -8, "dei_focus_c_root", "dei_path_c_chosen", "dei_path_c_chosen_tt"),
    ("DEI_04_path_d_otoriter.txt", "PATH D: Otoriter Militeristik", -6, -8, "dei_focus_d_root", "dei_path_d_chosen", "dei_path_d_chosen_tt"),
    ("DEI_05_path_e_islamis.txt", "PATH E: Islamis (Negara Islam Indonesia)", -4, -8, "dei_focus_e_root", "dei_path_e_chosen", "dei_path_e_chosen_tt"),
    ("DEI_06_path_f_majapahit.txt", "PATH F: Kemaharajaan Majapahit", -2, -8, "dei_focus_f_root", "dei_path_f_chosen", "dei_path_f_chosen_tt")
]

for fname, title, dx, dy, root_id, flag_name, tt_key in path_configs:
    with open(os.path.join(archive_dir, fname), "r", encoding="utf-8") as f:
        txt = f.read()
    
    p_blocks = parse_focus_blocks(txt)
    path_str = []
    for b in p_blocks:
        # Shift x
        def repl_x(m):
            return f"x = {int(m.group(1)) + dx}"
        b = re.sub(r'\bx\s*=\s*(-?\d+)', repl_x, b)

        # Shift y
        def repl_y(m):
            return f"y = {int(m.group(1)) + dy}"
        b = re.sub(r'\by\s*=\s*(-?\d+)', repl_y, b)

        # Enhance available block on path root with readable custom tooltip
        if f"id = {root_id}" in b:
            ab = f"\t\tallow_branch = {{\n\t\t\tOR = {{\n\t\t\t\tNOT = {{ has_country_flag = dei_jalur_dipilih }}\n\t\t\t\thas_country_flag = {flag_name}\n\t\t\t}}\n\t\t}}\n"
            b = re.sub(r'(\bcost\s*=\s*\d+\n)', r'\1' + ab, b)
            
            # Replace raw available = { has_country_flag = ... } with custom tooltip
            b = re.sub(
                r'available\s*=\s*\{\s*has_country_flag\s*=\s*' + flag_name + r'\s*\}',
                f'available = {{\n\t\t\tcustom_trigger_tooltip = {{\n\t\t\t\ttooltip = {tt_key}\n\t\t\t\thas_country_flag = {flag_name}\n\t\t\t}}\n\t\t}}',
                b
            )

            # Ensure completion reward sets flags
            flag_fx = f"\n\t\t\tset_country_flag = dei_jalur_dipilih\n\t\t\tset_country_flag = {flag_name}"
            b = re.sub(r'(completion_reward\s*=\s*\{)', r'\1' + flag_fx, b)

        path_str.append(b)

    body.append(f"\n\n\t# =====================================================================\n\t# {title}\n\t# =====================================================================\n")
    body.append("\n\n".join(path_str))

# --- 3. INDUSTRY & ADVANCED TECH (Root at x = 56) ---
with open(os.path.join(archive_dir, "DEI_r56_industry.txt"), "r", encoding="utf-8") as f:
    txt = f.read()

ind_blocks = parse_focus_blocks(txt)
ind_str = []
for b in ind_blocks:
    if "id = INS_industrial_centralisation" in b:
        b = re.sub(r'\bx\s*=\s*28', 'x = 56', b)
    elif "id = INS_advanced_telecommunications" in b:
        b = re.sub(r'\bx\s*=\s*26', 'x = 54', b)
    elif "id = INS_institut_teknologi_bandung" in b:
        b = re.sub(r'\bx\s*=\s*27', 'x = 56', b)
    elif "id = INS_pusat_metalurgi_sintesis" in b:
        b = re.sub(r'\bx\s*=\s*29', 'x = 58', b)
    elif "id = INS_proyek_riset_atom_dirgantara" in b:
        b = re.sub(r'\bx\s*=\s*27', 'x = 56', b)
    ind_str.append(b)

body.append("\n\n\t# =====================================================================\n\t# CABANG INDUSTRI & RISET ROAD TO 56\n\t# =====================================================================\n")
body.append("\n\n".join(ind_str))

# --- 4. ARMED FORCES (Root at x = 64) ---
with open(os.path.join(archive_dir, "DEI_r56_armed_forces.txt"), "r", encoding="utf-8") as f:
    txt = f.read()

af_blocks = parse_focus_blocks(txt)
af_str = []
for b in af_blocks:
    if "id = INS_koninklijk_nederlands_indisch_leger" in b:
        b = re.sub(r'\bx\s*=\s*35', 'x = 64', b)
    af_str.append(b)

body.append("\n\n\t# =====================================================================\n\t# CABANG MILITER AD / AU / AL ROAD TO 56\n\t# =====================================================================\n")
body.append("\n\n".join(af_str))

body.append("\n}\n")

full_content = "\n".join(body)
with open(output_file, "w", encoding="utf-8") as f:
    f.write(full_content)

total_focuses = len(re.findall(r'^\s*focus\s*=\s*\{', full_content, re.MULTILINE))
print(f"SUCCESS: Master focus tree generated with {total_focuses} focuses!")
