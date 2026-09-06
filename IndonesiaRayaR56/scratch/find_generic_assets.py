import os, glob, re

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"

# 1. Focus Icons
generic_focuses = []
for ff in glob.glob(os.path.join(mod_dir, 'common', 'national_focus', '*.txt')):
    with open(ff, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    # match id and icon
    matches = re.findall(r'focus\s*=\s*\{[^{}]*id\s*=\s*([a-zA-Z0-9_]+)[^{}]*icon\s*=\s*([a-zA-Z0-9_]+)', txt, re.DOTALL)
    for fid, icon in matches:
        if 'generic' in icon.lower() or icon.startswith('GFX_focus_'):
            generic_focuses.append((fid, icon, os.path.basename(ff)))

print(f"Generic/Vanilla Focus Icons found: {len(generic_focuses)}")
for fid, icon, fname in generic_focuses:
    print(f" - [{fname}] {fid}: {icon}")

# 2. Characters
print("\nCharacters:")
with open(os.path.join(mod_dir, 'common', 'characters', 'DEI_characters.txt'), 'r', encoding='utf-8') as f:
    ctxt = f.read()
for line in ctxt.splitlines():
    if 'large =' in line or 'name =' in line:
        print("  ", line.strip())

# 3. Ideas
print("\nIdeas with Generic Icons:")
for idf in glob.glob(os.path.join(mod_dir, 'common', 'ideas', '*.txt')):
    with open(idf, 'r', encoding='utf-8', errors='ignore') as f:
        itxt = f.read()
    for m in re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{[^{}]*picture\s*=\s*([a-zA-Z0-9_]+)', itxt):
        idea_id, pic = m.group(1), m.group(2)
        if 'generic' in pic.lower():
            print(f" - [{os.path.basename(idf)}] {idea_id}: {pic}")
