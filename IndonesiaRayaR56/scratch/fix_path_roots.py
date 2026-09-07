import re

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    content = f.read()

# Path root IDs and their flag names
path_roots = {
    "dei_focus_a_proklamasi": {
        "flag": "dei_path_a_chosen",
        "cosmetic": "INS_REPUBLIK_NKRI",
        "politics": "democratic",
        "elections": "yes",
        "idea": "dei_idea_republik_diproklamasikan",
        "navy": "DEI_navy_starter_a",
        "leadership": "dei_leadership.1",
        "event": "dei_path_a.1",
    },
    "dei_focus_b_root": {
        "flag": "dei_path_b_chosen",
        "cosmetic": "INS_KOLONIAL_BFO",
        "politics": "federalist",
        "elections": "no",
        "idea": None,
        "navy": "DEI_navy_starter_b",
        "leadership": "dei_leadership.2",
        "event": "dei_path_b.1",
    },
    "dei_focus_c_root": {
        "flag": "dei_path_c_chosen",
        "cosmetic": "INS_KOMUNIS_RRI",
        "politics": "communism",
        "elections": "no",
        "idea": None,
        "navy": "DEI_navy_starter_c",
        "leadership": "dei_leadership.3",
        "event": "dei_path_c.1",
    },
    "dei_focus_d_root": {
        "flag": "dei_path_d_chosen",
        "cosmetic": "INS_OTORITER_NKRI",
        "politics": "fascism",
        "elections": "no",
        "idea": None,
        "navy": "DEI_navy_starter_d",
        "leadership": "dei_leadership.4",
        "event": "dei_path_d.1",
    },
    "dei_focus_e_root": {
        "flag": "dei_path_e_chosen",
        "cosmetic": "INS_ISLAMIS_NII",
        "politics": "islamist",
        "elections": "no",
        "idea": None,
        "navy": "DEI_navy_starter_e",
        "leadership": "dei_leadership.5",
        "event": "dei_path_e.1",
    },
    "dei_focus_f_root": {
        "flag": "dei_path_f_chosen",
        "cosmetic": "INS_MAJAPAHIT_EMPIRE",
        "politics": "majapahit",
        "elections": "no",
        "idea": None,
        "navy": "DEI_navy_starter_f",
        "leadership": "dei_leadership.6",
        "event": "dei_path_f.1",
    },
}

# For each path root, replace:
# 1. available = { custom_trigger_tooltip... } -> available = { always = yes }
# 2. completion_reward = { set_country_flag... } -> add all path effects

for root_id, data in path_roots.items():
    # Find the focus block
    pattern = f"id = {root_id}"
    pos = content.find(pattern)
    if pos < 0:
        print(f"WARNING: {root_id} not found!")
        continue
    
    # Find end of block
    depth = 0
    in_block = False
    block_start = content.rfind("focus = {", 0, pos)
    i = block_start
    while i < len(content):
        if content[i] == '{':
            depth += 1
            in_block = True
        elif content[i] == '}':
            depth -= 1
            if in_block and depth <= 0:
                block_end = i + 1
                break
        i += 1
    
    old_block = content[block_start:block_end]
    
    # Build new available block
    new_available = "available = { always = yes }"
    
    # Build new completion_reward
    reward = f"""completion_reward = {{
\t\tset_country_flag = dei_jalur_dipilih
\t\tset_country_flag = {data['flag']}
\t\tset_cosmetic_tag = {data['cosmetic']}
\t\tset_politics = {{
\t\t\truling_party = {data['politics']}
\t\t\telections_allowed = {data['elections']}
\t\t}}
\t\tcountry_event = {{ id = {data['leadership']} days = 1 }}
\t\thidden_effect = {{
\t\t\tload_oob = {data['navy']}
\t\t\t335 = {{
\t\t\t\tcreate_unit = {{
\t\t\t\t\tdivision_template = "Divisi Infanteri Siliwangi"
\t\t\t\t\tstart_experience_factor = 0.3
\t\t\t\t\tstart_equipment_factor = 0.8
\t\t\t\t}}
\t\t\t\tcreate_unit = {{
\t\t\t\t\tdivision_template = "Brigade Laskar Rakyat"
\t\t\t\t\tstart_experience_factor = 0.2
\t\t\t\t\tstart_equipment_factor = 0.9
\t\t\t\t}}
\t\t\t}}
\t\t\t446 = {{
\t\t\t\tcreate_unit = {{
\t\t\t\t\tdivision_template = "Divisi Infanteri Diponegoro"
\t\t\t\t\tstart_experience_factor = 0.3
\t\t\t\t\tstart_equipment_factor = 0.8
\t\t\t\t}}
\t\t\t\tcreate_unit = {{
\t\t\t\t\tdivision_template = "Brigade Laskar Rakyat"
\t\t\t\t\tstart_experience_factor = 0.2
\t\t\t\t\tstart_equipment_factor = 0.9
\t\t\t\t}}
\t\t\t}}
\t\t\tadd_equipment_to_stockpile = {{ type = infantry_equipment amount = 3000 }}
\t\t}}
\t\tcountry_event = {{ id = {data['event']} hours = 6 }}
\t}}"""
    
    if data['idea']:
        reward = reward.replace(
            f"\t\tcountry_event = {{ id = {data['leadership']}",
            f"\t\tadd_ideas = {data['idea']}\n\t\tcountry_event = {{ id = {data['leadership']}"
        )
    
    # Replace available block in old_block
    new_block = re.sub(
        r'available\s*=\s*\{[^}]*custom_trigger_tooltip[^}]*\}[^}]*\}',
        new_available,
        old_block,
        flags=re.DOTALL
    )
    
    # Also handle simpler available blocks
    new_block = re.sub(
        r'available\s*=\s*\{\s*custom_trigger_tooltip\s*=\s*\{[^}]*\}[^}]*\}',
        new_available,
        new_block,
        flags=re.DOTALL
    )
    
    # Replace completion_reward
    new_block = re.sub(
        r'completion_reward\s*=\s*\{[^}]*\}',
        reward,
        new_block,
        count=1,
        flags=re.DOTALL
    )
    
    content = content[:block_start] + new_block + content[block_end:]
    print(f"Updated {root_id}")

with open(tree_path, "w", encoding="utf-8") as f:
    f.write(content)

print("All path roots updated with full completion rewards.")
