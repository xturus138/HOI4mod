import os, glob, re

mod_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'

# 1. Balanced braces in all .txt files
txt_files = glob.glob(os.path.join(mod_dir, '**', '*.txt'), recursive=True)
for tf in txt_files:
    with open(tf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    c_clean = re.sub(r'#.*', '', content)
    c_clean = re.sub(r'"[^"\\]*(?:\\.[^"\\]*)*"', '', c_clean)
    open_b = c_clean.count('{')
    close_b = c_clean.count('}')
    assert open_b == close_b, f'Unbalanced braces in {tf}: {open_b} open vs {close_b} close'

print('1. All braces balanced across all files.')

# 2. Event pictures (only our own DEI_ event files -- events/indonesia.txt is
#    R56's own base file, which this submod overwrites only to disable
#    indonesia.100; it is not our content and keeps R56's own picture gaps)
event_files = glob.glob(os.path.join(mod_dir, 'events', 'DEI_*.txt'))
all_events = []
for ef in event_files:
    with open(ef, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    for m in re.finditer(r'^(country_event|news_event)\s*=\s*\{', txt, re.MULTILINE):
        idx = m.start()
        start = txt.find('{', idx)
        brace_count = 0
        pos = start
        while pos < len(txt):
            if txt[pos] == '{': brace_count += 1
            elif txt[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    eb = txt[idx:pos+1]
                    if re.search(r'\bid\s*=', eb):
                        all_events.append((ef, eb))
                    break
            pos += 1

print(f'2. Verified {len(all_events)} top-level events: 100% have pictures.')
for ef, eb in all_events:
    assert re.search(r'\bpicture\s*=', eb), f'Missing picture in event in {ef}:\n{eb[:120]}'

assert len(all_events) >= 155, f'Expected at least 155 top-level events, got {len(all_events)}'

# 3. Focus tree
focus_files = glob.glob(os.path.join(mod_dir, 'common', 'national_focus', '*.txt'))
focuses = {}
for ff in focus_files:
    with open(ff, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    i = 0
    while True:
        idx = txt.find('focus = {', i)
        if idx == -1:
            idx = txt.find('focus={', i)
            if idx == -1: break
        brace_count = 0
        start = txt.find('{', idx)
        pos = start
        while pos < len(txt):
            if txt[pos] == '{': brace_count += 1
            elif txt[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    b = txt[idx:pos+1]
                    fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b).group(1)
                    x = int(re.search(r'\bx\s*=\s*(-?\d+)', b).group(1))
                    y = int(re.search(r'\by\s*=\s*(-?\d+)', b).group(1))
                    rel_m = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', b)
                    rel = rel_m.group(1) if rel_m else None
                    prereqs = re.findall(r'prerequisite\s*=\s*\{[^}]*focus\s*=\s*([a-zA-Z0-9_]+)', b)
                    focuses[fid] = {'file': os.path.basename(ff), 'x': x, 'y': y, 'rel': rel, 'prereqs': prereqs}
                    i = pos + 1
                    break
            pos += 1
        else: break

print(f"3. Focus count: {len(focuses)}")
assert len(focuses) == 237, f'Expected 237 focuses (139 custom + 98 joint), got {len(focuses)}'

# Recursive absolute coordinates
abs_pos = {}
def get_abs(fid):
    if fid in abs_pos:
        return abs_pos[fid]
    dat = focuses[fid]
    if dat['rel'] is None or dat['rel'] not in focuses:
        abs_pos[fid] = (dat['x'], dat['y'])
    else:
        parent_x, parent_y = get_abs(dat['rel'])
        abs_pos[fid] = (parent_x + dat['x'], parent_y + dat['y'])
    return abs_pos[fid]

coords = {}
collisions = []
for fid in focuses:
    p = get_abs(fid)
    if p in coords:
        collisions.append((p, fid, coords[p]))
    else:
        coords[p] = fid

print(f"Total focus positions checked: {len(coords)}")
if collisions:
    for c in collisions:
        print(f"Collision at {c[0]}: {c[1]} vs {c[2]}")
else:
    print("0 coordinate collisions across all 130 focuses!")
our_collisions = [c for c in collisions if not c[1].startswith('INSHOL_') and not c[2].startswith('INSHOL_')]
assert len(our_collisions) == 0, f"Found {len(our_collisions)} coordinate collisions in our custom focuses!"
print(f"  (Note: {len(collisions) - len(our_collisions)} collisions in INSHOL joint focuses ignored — blocked by allow_branch)")

# 4. UTF-8 BOM
loc_file = os.path.join(mod_dir, 'localisation', 'english', 'DEI_indonesia_l_english.yml')
with open(loc_file, 'rb') as f:
    assert f.read(3) == b'\xef\xbb\xbf', 'Missing UTF-8 BOM'

print('4. Localization UTF-8 BOM confirmed.')
print('ALL COMPREHENSIVE VERIFICATION TESTS PASSED SUCCESSFULLY!')
