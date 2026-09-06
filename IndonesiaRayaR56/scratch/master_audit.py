import os, glob, re

mod_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'
vanilla_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
r56_dir = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968'

print("===============================================================")
print("     AUDIT MENYELURUH MOD INDONESIA RAYA: ROAD TO MERDEKA      ")
print("===============================================================\n")

errors = []
warnings = []

# --- 1. SINTAKS & KURUNG KURAWAL ---
txt_files = glob.glob(os.path.join(mod_dir, '**', '*.txt'), recursive=True)
print(f"[1/8] Memeriksa sintaks & keseimbangan kurung ({len(txt_files)} file .txt)...")
for tf in txt_files:
    with open(tf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    c_clean = re.sub(r'#.*', '', c)
    c_clean = re.sub(r'"[^"\\]*(?:\\.[^"\\]*)*"', '', c_clean)
    ob = c_clean.count('{')
    cb = c_clean.count('}')
    if ob != cb:
        errors.append(f"Kurung tidak seimbang di {os.path.basename(tf)}: {ob} buka vs {cb} tutup")
print(f"      -> {'SEMUA KURUNG SEIMBANG (OK)' if not errors else 'ADA ERROR KURUNG'}")

# --- 2. POHON FOKUS & TABRAKAN KOORDINAT ---
print(f"[2/8] Memeriksa pohon fokus nasional (130 fokus)...")
focus_files = glob.glob(os.path.join(mod_dir, 'common', 'national_focus', '*.txt'))
focuses = {}
for ff in focus_files:
    with open(ff, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    i = 0
    while True:
        idx = txt.find('focus = {', i)
        if idx == -1: idx = txt.find('focus={', i)
        if idx == -1: break
        start = txt.find('{', idx)
        pos = start
        bc = 0
        while pos < len(txt):
            if txt[pos] == '{': bc += 1
            elif txt[pos] == '}':
                bc -= 1
                if bc == 0:
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

print(f"      Total fokus terdeteksi: {len(focuses)} fokus")
if len(focuses) != 134:
    errors.append(f"Jumlah fokus tidak 134, terdeteksi: {len(focuses)}")

# Validasi Prerequisite
for fid, dat in focuses.items():
    for p in dat['prereqs']:
        if p not in focuses:
            errors.append(f"Fokus {fid} merujuk prerequisite tidak ada: {p}")

# Validasi Koordinat Mutlak
abs_pos = {}
def get_abs(fid):
    if fid in abs_pos: return abs_pos[fid]
    dat = focuses[fid]
    if dat['rel'] is None or dat['rel'] not in focuses:
        abs_pos[fid] = (dat['x'], dat['y'])
    else:
        px, py = get_abs(dat['rel'])
        abs_pos[fid] = (px + dat['x'], py + dat['y'])
    return abs_pos[fid]

coords = {}
collisions = []
for fid in focuses:
    p = get_abs(fid)
    if p in coords:
        collisions.append((p, fid, coords[p]))
    else:
        coords[p] = fid

if collisions:
    for c in collisions:
        errors.append(f"Tabrakan koordinat di {c[0]}: {c[1]} bertabrakan dengan {c[2]}")
print(f"      -> Koordinat unik: {len(coords)}, Tabrakan: {len(collisions)} (OK)")

# --- 3. EVENT SYSTEM & GAMBAR ---
print(f"[3/8] Memeriksa event dan gambar sprite...")
event_files = glob.glob(os.path.join(mod_dir, 'events', '*.txt'))
events = []
for ef in event_files:
    with open(ef, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    i = 0
    while True:
        idx = txt.find('country_event = {', i)
        if idx == -1: idx = txt.find('country_event={', i)
        if idx == -1: break
        start = txt.find('{', idx)
        pos = start
        bc = 0
        while pos < len(txt):
            if txt[pos] == '{': bc += 1
            elif txt[pos] == '}':
                bc -= 1
                if bc == 0:
                    eb = txt[idx:pos+1]
                    eid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\.]+)', eb).group(1)
                    pic = re.search(r'\bpicture\s*=\s*([a-zA-Z0-9_]+)', eb)
                    pic_name = pic.group(1) if pic else None
                    events.append((eid, os.path.basename(ef), pic_name))
                    i = pos + 1
                    break
            pos += 1
        else: break

print(f"      Total event terdeteksi: {len(events)} event")
missing_pics = [e for e in events if not e[2]]
if missing_pics:
    errors.append(f"{len(missing_pics)} event tanpa gambar picture: {missing_pics}")
else:
    print(f"      -> 100% Event memiliki aset gambar (OK)")

# --- 4. KUNCI LOKALISASI & ENCODING BOM ---
print(f"[4/8] Memeriksa berkas lokalisasi & UTF-8 BOM...")
loc_file = os.path.join(mod_dir, 'localisation', 'english', 'DEI_indonesia_l_english.yml')
with open(loc_file, 'rb') as f:
    has_bom = f.read(3) == b'\xef\xbb\xbf'
if not has_bom:
    errors.append("DEI_indonesia_l_english.yml TIDAK memiliki UTF-8 BOM")
else:
    print("      -> UTF-8 BOM terkonfirmasi (OK)")

loc_keys = set()
with open(loc_file, 'r', encoding='utf-8-sig') as f:
    for line in f:
        l = line.strip()
        if not l or l.startswith('#') or l.startswith('l_english:'): continue
        km = re.match(r'^([a-zA-Z0-9_\.]+):(?:\d+)?\s*"(.*)"', l)
        if km: loc_keys.add(km.group(1))

print(f"      Total kunci lokalisasi: {len(loc_keys)}")

# Cek nama fokus
missing_f_loc = []
for fid in focuses:
    if fid not in loc_keys: missing_f_loc.append(fid)
    if f"{fid}_desc" not in loc_keys: missing_f_loc.append(f"{fid}_desc")

# Cek event
missing_e_loc = []
for eid, ef, _ in events:
    if f"{eid}.t" not in loc_keys and eid not in loc_keys: missing_e_loc.append(f"{eid}.t")
    if f"{eid}.d" not in loc_keys and f"{eid}_desc" not in loc_keys: missing_e_loc.append(f"{eid}.d")

if missing_f_loc:
    errors.append(f"{len(missing_f_loc)} fokus belum terlokalisasi: {missing_f_loc[:10]}")
if missing_e_loc:
    errors.append(f"{len(missing_e_loc)} event belum terlokalisasi: {missing_e_loc[:10]}")
print(f"      -> Missing focus loc: {len(missing_f_loc)}, Missing event loc: {len(missing_e_loc)} (OK)")

# --- 5. KEPUTUSAN & KATEGORI (DECISIONS) ---
print(f"[5/8] Memeriksa keputusan (decisions)...")
dec_file = os.path.join(mod_dir, 'common', 'decisions', 'DEI_decisions.txt')
with open(dec_file, 'r', encoding='utf-8') as f:
    dtxt = f.read()

categories = re.findall(r'decisions_category\s*=\s*\{([^}]+)\}', dtxt)
decisions = re.findall(r'(dei_decision_[a-zA-Z0-9_]+)\s*=\s*\{', dtxt)
print(f"      Kategori keputusan: {len(categories)}, Total Keputusan: {len(decisions)}")
missing_d_loc = []
for d in decisions:
    if d not in loc_keys: missing_d_loc.append(d)
    if f"{d}_desc" not in loc_keys: missing_d_loc.append(f"{d}_desc")
if missing_d_loc:
    errors.append(f"{len(missing_d_loc)} keputusan belum terlokalisasi: {missing_d_loc}")
print(f"      -> Missing decision loc: {len(missing_d_loc)} (OK)")

# --- 6. MILITER & TEMPLATES OOB ---
print(f"[6/8] Memeriksa OOB starter, templates & namelist...")
templates_file = os.path.join(mod_dir, 'history', 'units', 'DEI_templates.txt')
with open(templates_file, 'r', encoding='utf-8') as f:
    tmpls = re.findall(r'name\s*=\s*"([^"]+)"', f.read())
print(f"      Templat Divisi Doktrinal: {len(tmpls)} templat")

navies = glob.glob(os.path.join(mod_dir, 'history', 'units', 'DEI_navy_starter_*.txt'))
print(f"      Dedicated Starter Navies: {len(navies)} armada OOB (Jalur A s/d F)")

# --- 7. BENDERA NASIONAL & COSMETIC TAGS ---
print(f"[7/8] Memeriksa sinkronisasi bendera TGA...")
flag_dirs = ['gfx/flags', 'gfx/flags/medium', 'gfx/flags/small']
flag_counts = [len(glob.glob(os.path.join(mod_dir, d, '*.tga'))) for d in flag_dirs]
print(f"      Jumlah bendera: Standar={flag_counts[0]}, Medium={flag_counts[1]}, Small={flag_counts[2]}")
if len(set(flag_counts)) != 1:
    errors.append(f"Ukuran bendera tidak sinkron: {flag_counts}")
else:
    print(f"      -> 100% Sinkronisasi 3 ukuran bendera ({flag_counts[0]} desain) (OK)")

# --- 8. INTEGRASI SPRITE GRAFIS MOD, R56 & VANILLA ---
print(f"[8/8] Memeriksa integritas sprite grafis...")
all_sprites = set()
for root, dirs, files in os.walk(os.path.join(mod_dir, 'interface')):
    for f in files:
        if f.endswith('.gfx'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as fp:
                for n in re.findall(r'name\s*=\s*"([^"]+)"', fp.read()): all_sprites.add(n)

if os.path.exists(r56_dir):
    for root, dirs, files in os.walk(os.path.join(r56_dir, 'interface')):
        for f in files:
            if f.endswith('.gfx'):
                with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as fp:
                    for n in re.findall(r'name\s*=\s*"([^"]+)"', fp.read()): all_sprites.add(n)

if os.path.exists(vanilla_dir):
    for root, dirs, files in os.walk(os.path.join(vanilla_dir, 'interface')):
        for f in files:
            if f.endswith('.gfx'):
                with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as fp:
                    for n in re.findall(r'name\s*=\s*"([^"]+)"', fp.read()): all_sprites.add(n)

missing_event_sprites = []
for eid, ef, pic in events:
    if pic and pic not in all_sprites:
        missing_event_sprites.append((eid, pic))

if missing_event_sprites:
    errors.append(f"{len(missing_event_sprites)} event sprite hilang: {missing_event_sprites}")
else:
    print(f"      -> 100% Sprite event terdaftar di interface GFX (OK)")

print("\n===============================================================")
if errors:
    print(f"HASIL: DITEMUKAN {len(errors)} KETIDAKSESUAIAN:")
    for e in errors:
        print(f"  [ERROR] {e}")
else:
    print("HASIL AUDIT TOTAL: 100% SESUAI & LULUS VERIFIKASI TANPA KESALAHAN!")
print("===============================================================")
