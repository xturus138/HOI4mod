import os, re

r56_loc = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\localisation\english\INS_l_english.yml"
dei_loc = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"
mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"

# Load R56 loc
r56_dict = {}
with open(r56_loc, "r", encoding="utf-8-sig", errors="ignore") as f:
    for line in f:
        m = re.match(r'^\s*([a-zA-Z0-9_\.]+):(?:\d+)?\s*"(.*)"', line)
        if m:
            r56_dict[m.group(1)] = m.group(2)

# Load existing DEI loc content
with open(dei_loc, "r", encoding="utf-8-sig") as f:
    dei_content = f.read()

# Load focuses
import glob
focus_files = glob.glob(os.path.join(mod_dir, 'common', 'national_focus', '*.txt'))
focuses = set()
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
                    focuses.add(fid)
                    i = pos + 1
                    break
            pos += 1
        else: break

loc_keys = set()
for line in dei_content.splitlines():
    m = re.match(r'^\s*([a-zA-Z0-9_\.]+):(?:\d+)?\s*"(.*)"', line)
    if m:
        loc_keys.add(m.group(1))

entries_to_add = []
for fid in sorted(focuses):
    if fid not in loc_keys:
        val = r56_dict.get(fid, fid.replace("INS_", "").replace("_", " ").title())
        entries_to_add.append((fid, val))
    desc_key = f"{fid}_desc"
    if desc_key not in loc_keys:
        if desc_key in r56_dict:
            val = r56_dict[desc_key]
        else:
            if fid == "INS_modernize_the_military":
                val = "To safeguard the archipelago against rising global tensions, our armed forces must be restructured, rearmed with modern infantry materiel, and trained to modern tactical standards."
            else:
                val = f"Advance national strategic objectives for {fid.replace('INS_', '').replace('_', ' ')}."
        entries_to_add.append((desc_key, val))

print(f"Adding {len(entries_to_add)} entries to DEI_indonesia_l_english.yml...")

new_section = "\n # --- ROAD TO 56 INTEGRATED FOCUS LOCALISATION ---\n"
for k, v in entries_to_add:
    # Escape quotes if necessary
    clean_v = v.replace('"', '\\"')
    new_section += f' {k}:0 "{clean_v}"\n'

full_content = dei_content.rstrip() + "\n" + new_section

# Write with UTF-8 BOM
with open(dei_loc, "wb") as f:
    f.write(b'\xef\xbb\xbf')
    f.write(full_content.encode("utf-8"))

print("Write complete. Validating BOM...")
with open(dei_loc, "rb") as f:
    bom = f.read(3)
    assert bom == b'\xef\xbb\xbf', "BOM missing!"
print("BOM verified!")
