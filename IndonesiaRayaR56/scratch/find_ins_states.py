import os, re

r56_states = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\history\states'
vanilla_states = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states'

ins_states = []

for s_dir in [vanilla_states, r56_states]:
    for root, dirs, files in os.walk(s_dir):
        for f in files:
            if f.endswith('.txt'):
                full = os.path.join(root, f)
                with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                if 'owner = INS' in content:
                    state_id = re.search(r'id\s*=\s*(\d+)', content)
                    name = re.search(r'name\s*=\s*"([^"]+)"', content)
                    sid = state_id.group(1) if state_id else '?'
                    sname = name.group(1) if name else f
                    ins_states.append((int(sid), sname, f))

# deduplicate by id (R56 overrides vanilla)
states_dict = {}
for sid, sname, fname in ins_states:
    states_dict[sid] = (sname, fname)

print(f'Total INS states found: {len(states_dict)}')
for sid in sorted(states_dict.keys()):
    print(f'State {sid:4d}: {states_dict[sid][0]:30} ({states_dict[sid][1]})')
