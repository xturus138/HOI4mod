import os, re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =====================================================================
# 1. CREATE localisation/english/replace/DEI_parties_l_english.yml
# =====================================================================
replace_dir = os.path.join(base_dir, 'localisation', 'english', 'replace')
os.makedirs(replace_dir, exist_ok=True)
parties_file = os.path.join(replace_dir, 'DEI_parties_l_english.yml')

parties_content = """l_english:
 # ---------------------------------------------------------------------
 # STANDARD INS PARTIES OVERRIDE (OVERRIDES R56 r56_parties_l_english.yml)
 # ---------------------------------------------------------------------
 INS_democratic_party:0 "PNI"
 INS_democratic_party_long:0 "Partai Nasional Indonesia"
 INS_communism_party:0 "PKI"
 INS_communism_party_long:0 "Partai Komunis Indonesia"
 INS_fascism_party:0 "Dewan Revolusi"
 INS_fascism_party_long:0 "Dewan Revolusi Angkatan Bersenjata"
 INS_neutrality_party:0 "Volksraad"
 INS_neutrality_party_long:0 "Volksraad Hindia Belanda"

 # ---------------------------------------------------------------------
 # DYNAMIC SET_PARTY_NAME DIRECT KEYS
 # ---------------------------------------------------------------------
 INS_PNI_party:0 "PNI"
 INS_PNI_party_long:0 "Partai Nasional Indonesia"
 INS_BFO_party:0 "BFO"
 INS_BFO_party_long:0 "Bijeenkomst voor Federaal Overleg"
 INS_PKI_party:0 "PKI"
 INS_PKI_party_long:0 "Partai Komunis Indonesia"
 INS_DEWAN_REVOLUSI_party:0 "Dewan Revolusi"
 INS_DEWAN_REVOLUSI_party_long:0 "Dewan Revolusi Angkatan Bersenjata"
 INS_NII_party:0 "Majelis Syuro"
 INS_NII_party_long:0 "Majelis Syuro Negara Islam Indonesia"
 INS_MAJAPAHIT_party:0 "Kraton Wilwatikta"
 INS_MAJAPAHIT_party_long:0 "Keluarga Diraja & Rakryan Majapahit"

 # ---------------------------------------------------------------------
 # 18 COSMETIC TAG PARTIES (EXPLICIT IDEOLOGY MAPPINGS)
 # ---------------------------------------------------------------------
 # Jalur A: Republik (Democratic)
 INS_REPUBLIK_NKRI_democratic_party:0 "PNI"
 INS_REPUBLIK_NKRI_democratic_party_long:0 "Partai Nasional Indonesia"
 INS_REPUBLIK_RIS_democratic_party:0 "RIS"
 INS_REPUBLIK_RIS_democratic_party_long:0 "Republik Indonesia Serikat"
 INS_REPUBLIK_SOSIALIS_democratic_party:0 "PSI"
 INS_REPUBLIK_SOSIALIS_democratic_party_long:0 "Partai Sosialis Indonesia"

 # Jalur B: Kolonial / BFO (Democratic)
 INS_KOLONIAL_DEI_democratic_party:0 "Volksraad"
 INS_KOLONIAL_DEI_democratic_party_long:0 "Volksraad Nederlandsch-Indie"
 INS_KOLONIAL_BFO_democratic_party:0 "BFO"
 INS_KOLONIAL_BFO_democratic_party_long:0 "Bijeenkomst voor Federaal Overleg"
 INS_KOLONIAL_DOMINION_democratic_party:0 "VDP"
 INS_KOLONIAL_DOMINION_democratic_party_long:0 "Vaderlandsche Club & IEV"

 # Jalur C: Komunis (Communism)
 INS_KOMUNIS_RRI_communism_party:0 "PKI"
 INS_KOMUNIS_RRI_communism_party_long:0 "Partai Komunis Indonesia"
 INS_KOMUNIS_SOVIET_communism_party:0 "PKI-Internasional"
 INS_KOMUNIS_SOVIET_communism_party_long:0 "Partai Komunis Indonesia (Komintern)"
 INS_KOMUNIS_FRONT_communism_party:0 "Front Rakyat"
 INS_KOMUNIS_FRONT_communism_party_long:0 "Front Persatuan Rakyat Anti-Fasis"

 # Jalur D: Otoriter (Fascism)
 INS_OTORITER_NKRI_fascism_party:0 "Dewan Revolusi"
 INS_OTORITER_NKRI_fascism_party_long:0 "Dewan Revolusi Angkatan Bersenjata"
 INS_OTORITER_JUNTA_fascism_party:0 "Junta Militer"
 INS_OTORITER_JUNTA_fascism_party_long:0 "Junta Pertahanan Keamanan Rakyat"
 INS_OTORITER_RAYA_fascism_party:0 "Parindra Raya"
 INS_OTORITER_RAYA_fascism_party_long:0 "Partai Indonesia Raya Bersatu"

 # Jalur E: Islamis (Neutrality)
 INS_ISLAMIS_NII_neutrality_party:0 "Majelis Syuro"
 INS_ISLAMIS_NII_neutrality_party_long:0 "Majelis Syuro Negara Islam Indonesia"
 INS_ISLAMIS_DAULAH_neutrality_party:0 "Darul Islam"
 INS_ISLAMIS_DAULAH_neutrality_party_long:0 "Dewan Imamah Darul Islam"
 INS_ISLAMIS_KHILAFAH_neutrality_party:0 "Khilafah"
 INS_ISLAMIS_KHILAFAH_neutrality_party_long:0 "Majelis Ulama Khilafah Nusantara"

 # Jalur F: Majapahit (Neutrality)
 INS_MAJAPAHIT_EMPIRE_neutrality_party:0 "Kraton Wilwatikta"
 INS_MAJAPAHIT_EMPIRE_neutrality_party_long:0 "Keluarga Diraja & Rakryan Majapahit"
 INS_MAJAPAHIT_SURYA_neutrality_party:0 "Surya Majapahit"
 INS_MAJAPAHIT_SURYA_neutrality_party_long:0 "Wangsa Surya Wilwatikta"
 INS_MAJAPAHIT_NUSANTARA_neutrality_party:0 "Sapta Prabu"
 INS_MAJAPAHIT_NUSANTARA_neutrality_party_long:0 "Dewan Penasihat Agung Sapta Prabu"
"""

with open(parties_file, 'wb') as f:
    f.write(b'\xef\xbb\xbf')
    f.write(parties_content.encode('utf-8'))
print("[OK] Created replace/DEI_parties_l_english.yml with UTF-8 BOM")

# =====================================================================
# 2. UPDATE DEI_00_shared_trunk_events.txt (dei_trunk.6)
# =====================================================================
trunk_file = os.path.join(base_dir, 'events', 'DEI_00_shared_trunk_events.txt')
with open(trunk_file, 'r', encoding='utf-8') as f:
    trunk_txt = f.read()

# Replace immediate block of dei_trunk.6 to avoid forcing Path A on world/INS
old_immediate_pattern = re.compile(r'news_event\s*=\s*\{\s*id\s*=\s*dei_trunk\.6.*?immediate\s*=\s*\{.*?\}\s*\}\s*\}', re.DOTALL)
m = old_immediate_pattern.search(trunk_txt)
if m:
    # We want immediate to simply set global flag and not overwrite INS politics
    new_immediate = """news_event = {
	id = dei_trunk.6
	title = dei_trunk.6.t
	desc = dei_trunk.6.d
	picture = GFX_dei_news_event_1936_revolution

	is_triggered_only = yes
	major = yes

	immediate = {
		set_global_flag = dei_revolution_1936_happened
	}"""
    trunk_txt = trunk_txt[:m.start()] + new_immediate + trunk_txt[m.end():]
    with open(trunk_file, 'w', encoding='utf-8') as f:
        f.write(trunk_txt)
    print("[OK] Cleaned immediate block in dei_trunk.6")
else:
    print("[WARN] Could not find immediate block in dei_trunk.6")

# =====================================================================
# 3. UPDATE DEI_indonesia_focus_tree.txt
# =====================================================================
focus_file = os.path.join(base_dir, 'common', 'national_focus', 'DEI_indonesia_focus_tree.txt')
with open(focus_file, 'r', encoding='utf-8') as f:
    focus_txt = f.read()

# 3a. Fix dei_focus_momentum_kemerdekaan (Prologue focus 3)
# Remove premature cosmetic tag, premature set_politics, premature promote_character, recruit duplicates
old_prologue_block = """			if = {
				limit = { is_subject = yes }
				OVERLORD = {
					set_autonomy = {
						target = ROOT
						autonomy_state = autonomy_free
					}
				}
			}
			set_autonomy = {
				target = ROOT
				autonomy_state = autonomy_free
			}
			end_puppet = yes
			HOL = {
				set_autonomy = {
					target = INS
					autonomy_state = autonomy_free
				}
				end_puppet = INS
				remove_from_faction = INS
			}
			remove_ideas = INS_political_idea
			remove_ideas = INS_army_idea
			remove_ideas = INS_economy_idea
			remove_ideas = INS_science_idea
			set_cosmetic_tag = INS_REPUBLIK_NKRI
			add_ideas = dei_idea_revolusi_dini_spirit"""

new_prologue_block = """			if = {
				limit = { is_subject = yes }
				OVERLORD = {
					end_puppet = ROOT
				}
			}
			HOL = {
				remove_from_faction = INS
			}
			remove_ideas = INS_political_idea
			remove_ideas = INS_army_idea
			remove_ideas = INS_economy_idea
			remove_ideas = INS_science_idea
			add_ideas = dei_idea_revolusi_dini_spirit"""

assert old_prologue_block in focus_txt, "old_prologue_block not found"
focus_txt = focus_txt.replace(old_prologue_block, new_prologue_block, 1)

old_prologue_politics = """			recruit_character = DEI_sukarno
			recruit_character = DEI_mohammad_hatta
			recruit_character = DEI_sudirman
			set_politics = {
				ruling_party = democratic
				elections_allowed = yes
			}
			set_popularities = {
				democratic = 60.0
				neutrality = 20.0
				communism = 10.0
				fascism = 10.0
			}
			set_party_name = {
				ideology = democratic
				name = INS_PNI_party
				long_name = INS_PNI_party_long
			}
			promote_character = DEI_sukarno
			load_oob = DEI_templates
			load_oob = DEI_air_starter
			add_equipment_to_stockpile = { type = infantry_equipment amount = 3000 }"""

new_prologue_politics = """			load_oob = DEI_templates
			load_oob = DEI_air_starter
			add_equipment_to_stockpile = { type = infantry_equipment_0 amount = 3000 }"""

assert old_prologue_politics in focus_txt, "old_prologue_politics not found"
focus_txt = focus_txt.replace(old_prologue_politics, new_prologue_politics, 1)

# 3b. Fix all path roots autonomy breaks
bad_autonomy = """			if = {
				limit = { is_subject = yes }
				OVERLORD = {
					set_autonomy = {
						target = ROOT
						autonomy_state = autonomy_free
					}
				}
			}
			set_autonomy = {
				target = ROOT
				autonomy_state = autonomy_free
			}
			end_puppet = yes
			HOL = {
				set_autonomy = {
					target = INS
					autonomy_state = autonomy_free
				}
				end_puppet = INS
				remove_from_faction = INS
			}"""

clean_autonomy = """			if = {
				limit = { is_subject = yes }
				OVERLORD = {
					end_puppet = ROOT
				}
			}
			HOL = {
				remove_from_faction = INS
			}"""

count_auto = focus_txt.count(bad_autonomy)
focus_txt = focus_txt.replace(bad_autonomy, clean_autonomy)
print(f"[OK] Replaced {count_auto} instances of bad autonomy in focus tree")

# 3c. Fix create_unit in focus tree - ensure owner = ROOT
# Pattern: create_unit = {\n\t\t\t\t\tdivision_template
focus_txt = re.sub(
    r'(create_unit\s*=\s*\{\s*\n\s*division_template\s*=\s*"[^"]+")(?!\s*\n\s*owner)',
    r'\1\n\t\t\t\t\towner = ROOT',
    focus_txt
)

# Replace generic infantry_equipment stockpile with infantry_equipment_0 in focus tree
focus_txt = focus_txt.replace('type = infantry_equipment amount = 3000', 'type = infantry_equipment_0 amount = 3000')

with open(focus_file, 'w', encoding='utf-8') as f:
    f.write(focus_txt)
print("[OK] Updated DEI_indonesia_focus_tree.txt successfully!")

# =====================================================================
# 4. UPDATE DEI_debug_decisions.txt
# =====================================================================
debug_file = os.path.join(base_dir, 'common', 'decisions', 'DEI_debug_decisions.txt')
with open(debug_file, 'r', encoding='utf-8') as f:
    debug_txt = f.read()

count_auto_dbg = debug_txt.count(bad_autonomy)
debug_txt = debug_txt.replace(bad_autonomy, clean_autonomy)
print(f"[OK] Replaced {count_auto_dbg} instances of bad autonomy in debug decisions")

# Add owner = ROOT to all create_unit in debug decisions
debug_txt = re.sub(
    r'(create_unit\s*=\s*\{\s*\n\s*division_template\s*=\s*"[^"]+")(?!\s*\n\s*owner)',
    r'\1\n\t\t\t\t\towner = ROOT',
    debug_txt
)

# Remove premature cosmetic/politics in dei_debug_instant_prologue
old_dbg_prologue = """			set_cosmetic_tag = INS_REPUBLIK_NKRI
			recruit_character = DEI_sukarno
			recruit_character = DEI_mohammad_hatta
			recruit_character = DEI_sudirman
			set_politics = {
				ruling_party = democratic
				elections_allowed = yes
			}
			set_popularities = {
				democratic = 60.0
				neutrality = 20.0
				communism = 10.0
				fascism = 10.0
			}
			set_party_name = {
				ideology = democratic
				name = INS_PNI_party
				long_name = INS_PNI_party_long
			}
			promote_character = DEI_sukarno
			load_oob = DEI_templates
			load_oob = DEI_air_starter"""

new_dbg_prologue = """			load_oob = DEI_templates
			load_oob = DEI_air_starter"""

if old_dbg_prologue in debug_txt:
    debug_txt = debug_txt.replace(old_dbg_prologue, new_dbg_prologue, 1)
    print("[OK] Cleaned premature politics from dei_debug_instant_prologue")

with open(debug_file, 'w', encoding='utf-8') as f:
    f.write(debug_txt)
print("[OK] Updated DEI_debug_decisions.txt successfully!")

print("\n=== ALL FIXES APPLIED SUCCESSFULLY ===")
