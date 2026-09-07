import os, re

r56_base = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968'
mod_base = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'

r56_hits = {}
for root, dirs, files in os.walk(r56_base):
    for f in files:
        if f.endswith(('.txt', '.gui', '.gfx')):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, r56_base).replace('\\', '/')
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                    content = fl.read()
                    matches = []
                    if re.search(r'\b(tag = INS|INS =|has_war_with = INS|INS_)\b', content):
                        matches.append('INS')
                    if re.search(r'\b(tag = DEI|DEI =|has_war_with = DEI|DEI_)\b', content):
                        matches.append('DEI')
                    if matches:
                        r56_hits[rel] = matches
            except: pass

print(f'Total R56 files interacting with INS/DEI: {len(r56_hits)}')
for k in sorted(r56_hits.keys()):
    print(f'  {k}')
