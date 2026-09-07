import os, glob, re, json

mod_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'
app_dir = os.path.join(mod_dir, 'preview_app')

# 1. Load Localisation
loc = {}
with open(os.path.join(mod_dir, 'localisation', 'english', 'DEI_indonesia_l_english.yml'), 'r', encoding='utf-8-sig', errors='ignore') as f:
    for line in f:
        m = re.match(r'^\s*([a-zA-Z0-9_\.]+):\s*\"(.*)\"\s*$', line)
        if m:
            # unescape \n
            k = m.group(1)
            v = m.group(2).replace('\\n', '\n').replace('\\"', '"')
            loc[k] = v

print(f'Loaded {len(loc)} localization strings.')

# 2. Map sprite names to converted PNG paths
sprites = {}
for gfx_f in glob.glob(os.path.join(mod_dir, 'interface', '*.gfx')):
    with open(gfx_f, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    for m in re.finditer(r'name\s*=\s*\"([^\"]+)\"\s*texturefile\s*=\s*\"([^\"]+)\"', txt):
        s_name = m.group(1)
        tex = m.group(2).replace('\\', '/')
        if tex.startswith('gfx/'):
            tex = tex[4:]
        png_path = 'assets/' + os.path.splitext(tex)[0] + '.png'
        sprites[s_name] = png_path

print(f'Mapped {len(sprites)} sprites.')

# 3. Parse Focus Tree
with open(os.path.join(mod_dir, 'common', 'national_focus', 'DEI_indonesia_focus_tree.txt'), 'r', encoding='utf-8', errors='ignore') as f:
    tree_txt = f.read()

focus_blocks = []
i = 0
while True:
    idx = tree_txt.find('focus = {', i)
    if idx == -1: break
    start = tree_txt.find('{', idx)
    brace = 0
    pos = start
    while pos < len(tree_txt):
        if tree_txt[pos] == '{': brace += 1
        elif tree_txt[pos] == '}':
            brace -= 1
            if brace == 0:
                focus_blocks.append(tree_txt[idx:pos+1])
                i = pos + 1
                break
        pos += 1
    else: break

print(f'Found {len(focus_blocks)} focus blocks in tree.')

focuses = []
for b in focus_blocks:
    f_id = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b).group(1)
    icon = re.search(r'\bicon\s*=\s*([a-zA-Z0-9_]+)', b)
    icon = icon.group(1) if icon else 'GFX_goal_unknown'
    cost = re.search(r'\bcost\s*=\s*([0-9\.]+)', b)
    cost = float(cost.group(1)) if cost else 10.0
    x = re.search(r'\bx\s*=\s*(-?[0-9]+)', b)
    x = int(x.group(1)) if x else 0
    y = re.search(r'\by\s*=\s*(-?[0-9]+)', b)
    y = int(y.group(1)) if y else 0
    rel = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', b)
    rel = rel.group(1) if rel else None
    
    prereqs = re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', b)
    prereq_list = []
    for p in prereqs:
        f_refs = re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', p)
        prereq_list.append(f_refs)
        
    mut_ex = re.findall(r'mutually_exclusive\s*=\s*\{([^}]+)\}', b)
    mut_list = []
    for m in mut_ex:
        f_refs = re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', m)
        mut_list.extend(f_refs)

    # Determine Branch
    branch = 'Armed Forces & Industry'
    if any(k in f_id for k in ['_prolog', 'momentum', 'pembangkangan', 'fraktur']):
        branch = 'Prologue (1936)'
    elif '_a_' in f_id: branch = 'Path A: Republic (Democratic)'
    elif '_b_' in f_id: branch = 'Path B: Federalist (Commonwealth)'
    elif '_c_' in f_id: branch = 'Path C: Communist (Front Rakyat)'
    elif '_d_' in f_id: branch = 'Path D: Military Junta (Dewan Revolusi)'
    elif '_e_' in f_id: branch = 'Path E: Islamic State (NII)'
    elif '_f_' in f_id: branch = 'Path F: Majapahit Empire'
    elif 'INS_' in f_id:
        if any(w in f_id for w in ['navy', 'naval', 'ship', 'fleet', 'marines', 'sea', 'cruiser', 'destroyer']):
            branch = 'Navy & Maritime'
        elif any(w in f_id for w in ['air', 'pilot', 'plane', 'bomber', 'fighter']):
            branch = 'Air Force'
        elif any(w in f_id for w in ['knil', 'army', 'corps', 'division', 'infantry', 'artillery']):
            branch = 'Army & Defense'
        else:
            branch = 'Industry & Science'

    title = loc.get(f_id, f_id)
    desc = loc.get(f'{f_id}_desc', 'No description available.')
    icon_src = sprites.get(icon, 'assets/interface/goals/GFX_goal_generic_positive_trade_relations.png')

    focuses.append({
        'id': f_id,
        'title': title,
        'desc': desc,
        'icon': icon,
        'icon_src': icon_src,
        'cost': cost,
        'days': int(cost * 7),
        'x': x,
        'y': y,
        'relative_to': rel,
        'prerequisites': prereq_list,
        'mutually_exclusive': mut_list,
        'branch': branch
    })

# Compute absolute coordinates
focus_dict = {f['id']: f for f in focuses}
for f in focuses:
    abs_x = f['x']
    abs_y = f['y']
    curr = f
    visited = set()
    while curr.get('relative_to') and curr['relative_to'] in focus_dict:
        parent = focus_dict[curr['relative_to']]
        if parent['id'] in visited: break
        visited.add(parent['id'])
        abs_x += parent['x']
        abs_y += parent['y']
        curr = parent
    f['abs_x'] = abs_x
    f['abs_y'] = abs_y

# 4. Parse Events
events = []
event_files = sorted(glob.glob(os.path.join(mod_dir, 'events', '*.txt')))
for ef in event_files:
    with open(ef, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    for m in re.finditer(r'^(country_event|news_event)\s*=\s*\{', txt, re.MULTILINE):
        idx = m.start()
        ev_type = m.group(1)
        start = txt.find('{', idx)
        brace = 0
        pos = start
        while pos < len(txt):
            if txt[pos] == '{': brace += 1
            elif txt[pos] == '}':
                brace -= 1
                if brace == 0:
                    eb = txt[idx:pos+1]
                    id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\.]+)', eb)
                    if id_m:
                        e_id = id_m.group(1)
                        pic_m = re.search(r'\bpicture\s*=\s*([a-zA-Z0-9_]+)', eb)
                        pic = pic_m.group(1) if pic_m else 'GFX_report_event_generic'
                        title_k = re.search(r'\btitle\s*=\s*([a-zA-Z0-9_\.]+)', eb)
                        title_k = title_k.group(1) if title_k else e_id
                        desc_k = re.search(r'\bdesc\s*=\s*([a-zA-Z0-9_\.]+)', eb)
                        desc_k = desc_k.group(1) if desc_k else f'{e_id}.d'
                        
                        # Options
                        opts = []
                        for opt_m in re.finditer(r'\boption\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', eb):
                            ob = opt_m.group(1)
                            n_m = re.search(r'\bname\s*=\s*([a-zA-Z0-9_\.]+)', ob)
                            n_k = n_m.group(1) if n_m else 'OK'
                            opts.append({
                                'key': n_k,
                                'text': loc.get(n_k, n_k)
                            })
                            
                        # Category
                        cat = 'Trunk & Crisis'
                        if 'path_a' in e_id: cat = 'Path A: Republic'
                        elif 'path_b' in e_id: cat = 'Path B: Federalist'
                        elif 'path_c' in e_id: cat = 'Path C: Communist'
                        elif 'path_d' in e_id: cat = 'Path D: Military'
                        elif 'path_e' in e_id: cat = 'Path E: Islamist'
                        elif 'path_f' in e_id: cat = 'Path F: Majapahit'
                        elif 'flavor' in ef.lower(): cat = 'Archipelago Flavor'
                        elif 'leadership' in ef.lower(): cat = 'National Leadership'
                        
                        events.append({
                            'id': e_id,
                            'type': ev_type,
                            'category': cat,
                            'title': loc.get(title_k, title_k),
                            'desc': loc.get(desc_k, desc_k),
                            'picture': pic,
                            'pic_src': sprites.get(pic, 'assets/event_pictures/DEI_event_ikada.png'),
                            'options': opts,
                            'source_file': os.path.basename(ef)
                        })
                    break
            pos += 1

print(f'Parsed {len(events)} events.')

# 5. Parse Decisions
decisions = []
with open(os.path.join(mod_dir, 'common', 'decisions', 'DEI_decisions.txt'), 'r', encoding='utf-8', errors='ignore') as f:
    dec_txt = f.read()

# Categories
cats = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', dec_txt)
for c_id, c_body in cats:
    cat_title = loc.get(c_id, c_id)
    cat_desc = loc.get(f'{c_id}_desc', '')
    # extract inner decisions
    inner = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', c_body)
    for d_id, d_body in inner:
        if d_id in ['icon', 'picture', 'visible', 'available', 'modifier', 'highlight_states']: continue
        cost_m = re.search(r'cost\s*=\s*(\d+)', d_body)
        cost = int(cost_m.group(1)) if cost_m else 25
        d_title = loc.get(d_id, d_id)
        d_desc = loc.get(f'{d_id}_desc', '')
        decisions.append({
            'id': d_id,
            'category_id': c_id,
            'category_title': cat_title,
            'title': d_title,
            'desc': d_desc,
            'cost': cost
        })

print(f'Parsed {len(decisions)} decisions.')

# 6. Parse Characters & Commanders
chars = []
with open(os.path.join(mod_dir, 'common', 'characters', 'DEI_characters.txt'), 'r', encoding='utf-8', errors='ignore') as f:
    char_txt = f.read()

for m in re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', char_txt):
    c_id = m.group(1)
    c_body = m.group(2)
    name_m = re.search(r'name\s*=\s*\"?([a-zA-Z0-9_\. ]+)\"?', c_body)
    name_k = name_m.group(1).strip() if name_m else c_id
    name = loc.get(name_k, name_k)
    
    port_m = re.search(r'large\s*=\s*\"?([a-zA-Z0-9_]+)\"?', c_body)
    port = port_m.group(1) if port_m else 'GFX_portrait_unknown'
    port_src = sprites.get(port, 'assets/leaders/DEI/DEI_sudirman.png')
    
    traits = re.findall(r'traits\s*=\s*\{([^}]+)\}', c_body)
    trait_list = []
    for t in traits:
        for single in t.split():
            trait_list.append({
                'id': single,
                'name': loc.get(single, single.replace('trait_', '').replace('_', ' ').title())
            })
            
    role = 'Army Commander'
    if 'navy_leader' in c_body: role = 'Admiral (Naval Commander)'
    elif 'country_leader' in c_body: role = 'Political Leader / Head of State'
    elif 'air_chief' in c_body or 'air_commander' in c_body: role = 'Air Chief / Aviator'

    chars.append({
        'id': c_id,
        'name': name,
        'role': role,
        'portrait': port,
        'portrait_src': port_src,
        'traits': trait_list
    })

print(f'Parsed {len(chars)} characters.')

# 7. Doctrinal Templates
templates = []
with open(os.path.join(mod_dir, 'history', 'units', 'DEI_templates.txt'), 'r', encoding='utf-8', errors='ignore') as f:
    tpl_txt = f.read()

for m in re.finditer(r'division_template\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', tpl_txt):
    tb = m.group(1)
    name_m = re.search(r'name\s*=\s*\"([^\"]+)\"', tb)
    if name_m:
        t_name = name_m.group(1)
        regiments = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{\s*x\s*=\s*\d+\s*y\s*=\s*\d+\s*\}', tb)
        templates.append({
            'name': t_name,
            'regiments': regiments,
            'count': len(regiments)
        })

print(f'Parsed {len(templates)} division templates.')

# Save to preview_app/mod_data.js
output_js = os.path.join(app_dir, 'mod_data.js')
data_obj = {
    'stats': {
        'focus_count': len(focuses),
        'event_count': len(events),
        'decision_count': len(decisions),
        'character_count': len(chars),
        'template_count': len(templates),
        'loc_count': len(loc)
    },
    'focuses': focuses,
    'events': events,
    'decisions': decisions,
    'characters': chars,
    'templates': templates
}

with open(output_js, 'w', encoding='utf-8') as f:
    f.write('const MOD_DATA = ' + json.dumps(data_obj, indent=2, ensure_ascii=False) + ';\n')

print(f'Exported master mod dataset to {output_js}!')
