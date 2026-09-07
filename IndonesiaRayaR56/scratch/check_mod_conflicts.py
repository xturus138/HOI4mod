import os

workshop_dir = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360"
interesting_mods = {
    "3523920876": "Formable Nations for Road to 56",
    "3766377228": "FPS BOOSTER - CPU & AI LITE",
    "3369706283": "Better AI | 1.15"
}

for mod_id, mod_name in interesting_mods.items():
    print(f"\n=== Inspecting {mod_name} (ID: {mod_id}) ===")
    m_path = os.path.join(workshop_dir, mod_id)
    if not os.path.exists(m_path):
        print("  Not found!")
        continue
    
    ins_files = []
    dei_files = []
    focus_files = []
    for root, dirs, files in os.walk(m_path):
        for f in files:
            fl = f.lower()
            rel = os.path.relpath(os.path.join(root, f), m_path)
            if 'ins' in fl:
                ins_files.append(rel)
            if 'dei' in fl or 'indonesia' in fl:
                dei_files.append(rel)
            if 'focus' in fl:
                focus_files.append(rel)
    
    print(f"  INS related files: {ins_files}")
    print(f"  DEI/Indonesia related files: {dei_files}")
    print(f"  Focus files: {focus_files}")
