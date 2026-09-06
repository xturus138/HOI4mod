import glob, os, re

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"

leaders_found = []
# check events and decisions for add_country_leader_role or character =
for root, dirs, files in os.walk(mod_dir):
    for f in files:
        if f.endswith('.txt'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as fp_in:
                c = fp_in.read()
                # find add_country_leader_role
                m = re.findall(r'character\s*=\s*([a-zA-Z0-9_]+)[^}]*country_leader\s*=\s*\{([^}]+)\}', c)
                for char_id, dat in m:
                    leaders_found.append((char_id, dat.strip().replace('\n', ' '), os.path.basename(fp)))

print(f"Total country leaders assigned in scripts: {len(leaders_found)}")
for char_id, dat, src in leaders_found:
    print(f"[{src}] {char_id}: {dat}")
