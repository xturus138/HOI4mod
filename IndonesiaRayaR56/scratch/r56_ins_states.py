import os, re

r56_states = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\history\states'

states = {}
for f in os.listdir(r56_states):
    if f.endswith('.txt'):
        full = os.path.join(r56_states, f)
        with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
            c = fp.read()
        if 'owner = INS' in c:
            m_id = re.search(r'id\s*=\s*(\d+)', c)
            m_name = re.search(r'name\s*=\s*"([^"]+)"', c)
            sid = int(m_id.group(1)) if m_id else 0
            sname = m_name.group(1) if m_name else f
            states[sid] = (sname, f)

print(f'R56 INS states count: {len(states)}')
for sid in sorted(states.keys()):
    print(f'State {sid:4d}: {states[sid][0]:30} ({states[sid][1]})')
