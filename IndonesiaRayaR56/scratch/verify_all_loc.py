import os, glob, re

mod_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'

# 1. Parse loc keys
loc_file = os.path.join(mod_dir, 'localisation', 'english', 'DEI_indonesia_l_english.yml')
with open(loc_file, 'r', encoding='utf-8') as f:
    loc_lines = f.readlines()

loc_keys = set()
for line in loc_lines:
    line_clean = line.strip()
    if not line_clean or line_clean.startswith('#') or line_clean.startswith('l_english:'):
        continue
    km = re.match(r'^([a-zA-Z0-9_\.]+):(?:\d+)?\s*"(.*)"', line_clean)
    if km:
        loc_keys.add(km.group(1))

print(f'Total submod localisation keys: {len(loc_keys)}')

missing_loc = []

# 2. Check all custom focuses
focus_files = glob.glob(os.path.join(mod_dir, 'common', 'national_focus', 'DEI_*.txt'))
for ff in focus_files:
    with open(ff, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = re.findall(r'focus\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', content)
    for b in blocks:
        id_m = re.search(r'\bid\s*=\s*(dei_[a-zA-Z0-9_]+)', b)
        if not id_m: continue
        fid = id_m.group(1)
        if fid not in loc_keys: missing_loc.append(('custom focus name', fid))
        if f'{fid}_desc' not in loc_keys: missing_loc.append(('custom focus desc', f'{fid}_desc'))

# 3. Check all events
def extract_blocks(text, keyword):
    blocks = []
    idx = 0
    while True:
        pos = text.find(keyword, idx)
        if pos == -1:
            break
        brace_pos = text.find('{', pos)
        if brace_pos == -1:
            break
        depth = 1
        cur = brace_pos + 1
        while cur < len(text) and depth > 0:
            if text[cur] == '{':
                depth += 1
            elif text[cur] == '}':
                depth -= 1
            cur += 1
        if depth == 0:
            blocks.append(text[brace_pos+1:cur-1])
            idx = cur
        else:
            break
    return blocks

event_files = glob.glob(os.path.join(mod_dir, 'events', 'DEI_*.txt'))
for ef in event_files:
    with open(ef, 'r', encoding='utf-8') as f:
        c = re.sub(r'#.*', '', f.read())
    eblocks = extract_blocks(c, 'country_event')
    for eb in eblocks:
        t_m = re.search(r'\btitle\s*=\s*([a-zA-Z0-9_\.]+)', eb)
        d_m = re.search(r'\bdesc\s*=\s*([a-zA-Z0-9_\.]+)', eb)
        if t_m and t_m.group(1) not in loc_keys: missing_loc.append(('event title', t_m.group(1)))
        if d_m and d_m.group(1) not in loc_keys: missing_loc.append(('event desc', d_m.group(1)))
        opt_blocks = extract_blocks(eb, 'option')
        for ob in opt_blocks:
            om = re.search(r'\bname\s*=\s*([a-zA-Z0-9_\.]+)', ob)
            if om and om.group(1) not in loc_keys:
                missing_loc.append(('event option', om.group(1)))

# 4. Check leader traits (country leader & unit leader)
trait_files = glob.glob(os.path.join(mod_dir, 'common', 'country_leader', '*.txt')) + glob.glob(os.path.join(mod_dir, 'common', 'unit_leader', '*.txt'))
for tf in trait_files:
    with open(tf, 'r', encoding='utf-8') as f:
        tc = re.sub(r'#.*', '', f.read())
    for tm in re.findall(r'\b(trait_dei_[a-zA-Z0-9_]+)\s*=\s*\{', tc):
        if tm not in loc_keys: missing_loc.append(('leader trait name', tm))
        if f'{tm}_desc' not in loc_keys: missing_loc.append(('leader trait desc', f'{tm}_desc'))

# 5. Check decisions
dec_file = os.path.join(mod_dir, 'common', 'decisions', 'DEI_decisions.txt')
with open(dec_file, 'r', encoding='utf-8') as f:
    dtxt = re.sub(r'#.*', '', f.read())
cat_blocks = re.findall(r'decisions_category\s*=\s*\{([^}]+)\}', dtxt)
for cb in cat_blocks:
    cm = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', cb)
    if cm and cm.group(1) not in loc_keys:
        missing_loc.append(('decision category', cm.group(1)))

dec_blocks = re.findall(r'(dei_decision_[a-zA-Z0-9_]+)\s*=\s*\{', dtxt)
for db in dec_blocks:
    if db not in loc_keys: missing_loc.append(('decision name', db))
    if f'{db}_desc' not in loc_keys: missing_loc.append(('decision desc', f'{db}_desc'))

print(f'Total missing loc keys: {len(missing_loc)}')
if missing_loc:
    for m in missing_loc[:20]:
        print(f'  Missing {m[0]}: {m[1]}')
assert len(missing_loc) == 0, f'{len(missing_loc)} missing localization keys!'
print('ALL LOCALISATION KEYS VALIDATED SUCCESSFULLY!')
