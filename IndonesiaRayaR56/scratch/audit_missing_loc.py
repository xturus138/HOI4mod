import os, re

base = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
loc_file = os.path.join(base, "localisation", "english", "DEI_indonesia_l_english.yml")
parties_loc = os.path.join(base, "localisation", "english", "replace", "DEI_parties_l_english.yml")

with open(loc_file, "r", encoding="utf-8") as f:
    loc_text = f.read()

if os.path.exists(parties_loc):
    with open(parties_loc, "r", encoding="utf-8") as f:
        loc_text += "\n" + f.read()

# Load all defined keys
defined_keys = set(re.findall(r'^\s*([a-zA-Z0-9_\.\-]+):', loc_text, re.MULTILINE))
print(f"Total defined localization keys: {len(defined_keys)}")

# Check Focuses
ft_file = os.path.join(base, "common", "national_focus", "DEI_indonesia_focus_tree.txt")
with open(ft_file, "r", encoding="utf-8") as f:
    ft = f.read()

focus_ids = re.findall(r'id\s*=\s*(dei_focus_[a-zA-Z0-9_]+)', ft)
missing_focus_name = [fid for fid in focus_ids if fid not in defined_keys]
missing_focus_desc = [fid for fid in focus_ids if f"{fid}_desc" not in defined_keys]

print(f"Focuses checked: {len(focus_ids)}")
print(f"Missing focus titles: {len(missing_focus_name)}", missing_focus_name)
print(f"Missing focus descs: {len(missing_focus_desc)}", missing_focus_desc)

# Check Events
events_dir = os.path.join(base, "events")
missing_event_loc = []
for f in os.listdir(events_dir):
    if f.startswith("DEI_") and f.endswith(".txt"):
        with open(os.path.join(events_dir, f), "r", encoding="utf-8") as fl:
            ev_content = fl.read()
        # find event ids
        ev_ids = re.findall(r'id\s*=\s*([a-zA-Z0-9_\.]+)', ev_content)
        for eid in ev_ids:
            if f"{eid}.t" not in defined_keys:
                missing_event_loc.append(f"{eid}.t")
            if f"{eid}.d" not in defined_keys and f"{eid}.desc" not in defined_keys:
                missing_event_loc.append(f"{eid}.d")

print(f"Missing event titles/descs: {len(missing_event_loc)}", missing_event_loc[:15])

# Check Ideas
ideas_dir = os.path.join(base, "common", "ideas")
missing_ideas = []
if os.path.exists(ideas_dir):
    for f in os.listdir(ideas_dir):
        if f.startswith("DEI_") and f.endswith(".txt"):
            with open(os.path.join(ideas_dir, f), "r", encoding="utf-8") as fl:
                id_content = fl.read()
            ids = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{\s*picture', id_content)
            for iid in ids:
                if iid not in defined_keys:
                    missing_ideas.append(iid)

print(f"Missing idea names: {len(missing_ideas)}", missing_ideas)
