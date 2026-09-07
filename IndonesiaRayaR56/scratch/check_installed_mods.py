import glob, os, re

paradox_mod_dir = r"C:\Users\radit\Documents\Paradox Interactive\Hearts of Iron IV\mod"
workshop_dir = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360"

print("=== User Installed Mods in Paradox Mod Folder ===")
for m in sorted(glob.glob(os.path.join(paradox_mod_dir, "*.mod"))):
    try:
        with open(m, 'r', encoding='utf-8', errors='ignore') as fp:
            c = fp.read()
        name_match = re.search(r'name\s*=\s*"([^"]+)"', c)
        name = name_match.group(1) if name_match else os.path.basename(m)
        replace_paths = re.findall(r'replace_path\s*=\s*"([^"]+)"', c)
        print(f"File: {os.path.basename(m)}")
        print(f"  Name: {name}")
        if replace_paths:
            print(f"  Replace paths: {replace_paths}")
    except Exception as e:
        print(f"  Error reading {m}: {e}")

print("\n=== Workshop Folders in 394360 ===")
if os.path.exists(workshop_dir):
    w_folders = os.listdir(workshop_dir)
    print(f"Total workshop items: {len(w_folders)}")
    for wf in w_folders[:25]:
        desc_path = os.path.join(workshop_dir, wf, "descriptor.mod")
        name = wf
        if os.path.exists(desc_path):
            try:
                with open(desc_path, 'r', encoding='utf-8', errors='ignore') as fp:
                    c = fp.read()
                nm = re.search(r'name\s*=\s*"([^"]+)"', c)
                if nm:
                    name = f"{nm.group(1)} (ID: {wf})"
            except Exception:
                pass
        print(f"  - {name}")
