r56_loc = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\localisation\english\INS_l_english.yml"
with open(r56_loc, "r", encoding="utf-8-sig", errors="ignore") as f:
    lines = f.readlines()
for i in range(190, 205):
    if i < len(lines):
        print(f"{i}: {lines[i].strip()}")
