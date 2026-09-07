import os, re

r56_states = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\history\states'

target_states = [1126, 335, 976, 1143, 446, 1127]

for s in target_states:
    for f in os.listdir(r56_states):
        if f.startswith(f'{s}-') or f == f'{s}.txt':
            full = os.path.join(r56_states, f)
            with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            m_prov = re.search(r'provinces\s*=\s*\{([^}]+)\}', c)
            provs = m_prov.group(1).split() if m_prov else []
            vp = re.findall(r'victory_points\s*=\s*\{\s*(\d+)\s+(\d+)', c)
            print(f'State {s} ({f}): Victory Points={vp}, First 4 Provs={provs[:4]}')
