# =====================================================================
# update_focus_politics.py
# Standardizes ruling party, popularities, and party names across focuses, events, debug decisions
# =====================================================================

focus_file = 'common/national_focus/DEI_indonesia_focus_tree.txt'
with open(focus_file, 'r', encoding='utf-8') as f:
    fc = f.read()

# 1. dei_focus_momentum_kemerdekaan
old_m = '''			set_politics = {
				ruling_party = democratic
				elections_allowed = yes
			}
			promote_character = DEI_sukarno'''

new_m = '''			set_politics = {
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
			promote_character = DEI_sukarno'''

assert old_m in fc, "old_m not found in focus tree"
fc = fc.replace(old_m, new_m, 1)

# 2. Path A (Republik)
old_a = '''		set_politics = {
			ruling_party = democratic
			elections_allowed = yes
		}
		promote_character = DEI_sukarno'''

new_a = '''		set_politics = {
			ruling_party = democratic
			elections_allowed = yes
		}
		set_popularities = {
			democratic = 70.0
			neutrality = 10.0
			fascism = 10.0
			communism = 10.0
		}
		set_party_name = {
			ideology = democratic
			name = INS_PNI_party
			long_name = INS_PNI_party_long
		}
		promote_character = DEI_sukarno'''

assert old_a in fc, "old_a not found in focus tree"
fc = fc.replace(old_a, new_a, 1)

# 3. Path B (Federalis)
old_b = '''		set_politics = {
			ruling_party = federalist
			elections_allowed = no
		}
		promote_character = DEI_hubertus_van_mook'''

new_b = '''		set_politics = {
			ruling_party = democratic
			elections_allowed = yes
		}
		set_popularities = {
			democratic = 65.0
			neutrality = 15.0
			fascism = 10.0
			communism = 10.0
		}
		set_party_name = {
			ideology = democratic
			name = INS_BFO_party
			long_name = INS_BFO_party_long
		}
		promote_character = DEI_hubertus_van_mook'''

assert old_b in fc, "old_b not found in focus tree"
fc = fc.replace(old_b, new_b, 1)

# 4. Path C (Komunis)
old_c = '''		set_politics = {
			ruling_party = communism
			elections_allowed = no
		}
		promote_character = DEI_musso'''

new_c = '''		set_politics = {
			ruling_party = communism
			elections_allowed = no
		}
		set_popularities = {
			communism = 70.0
			democratic = 10.0
			fascism = 10.0
			neutrality = 10.0
		}
		set_party_name = {
			ideology = communism
			name = INS_PKI_party
			long_name = INS_PKI_party_long
		}
		promote_character = DEI_musso'''

assert old_c in fc, "old_c not found in focus tree"
fc = fc.replace(old_c, new_c, 1)

# 5. Path D (Otoriter Militer)
old_d = '''		set_politics = {
			ruling_party = fascism
			elections_allowed = no
		}
		promote_character = DEI_sudirman'''

new_d = '''		set_politics = {
			ruling_party = fascism
			elections_allowed = no
		}
		set_popularities = {
			fascism = 75.0
			democratic = 10.0
			communism = 10.0
			neutrality = 5.0
		}
		set_party_name = {
			ideology = fascism
			name = INS_DEWAN_REVOLUSI_party
			long_name = INS_DEWAN_REVOLUSI_party_long
		}
		promote_character = DEI_sudirman'''

assert old_d in fc, "old_d not found in focus tree"
fc = fc.replace(old_d, new_d, 1)

# 6. Path E (Islamis / NII)
old_e = '''		set_politics = {
			ruling_party = islamist
			elections_allowed = no
		}
		promote_character = DEI_kartosuwiryo'''

new_e = '''		set_politics = {
			ruling_party = neutrality
			elections_allowed = no
		}
		set_popularities = {
			neutrality = 70.0
			democratic = 10.0
			fascism = 10.0
			communism = 10.0
		}
		set_party_name = {
			ideology = neutrality
			name = INS_NII_party
			long_name = INS_NII_party_long
		}
		promote_character = DEI_kartosuwiryo'''

assert old_e in fc, "old_e not found in focus tree"
fc = fc.replace(old_e, new_e, 1)

# 7. Path F (Majapahit)
old_f = '''		set_politics = {
			ruling_party = majapahit
			elections_allowed = no
		}
		promote_character = DEI_wuryaningrat'''

new_f = '''		set_politics = {
			ruling_party = neutrality
			elections_allowed = no
		}
		set_popularities = {
			neutrality = 75.0
			democratic = 10.0
			fascism = 10.0
			communism = 5.0
		}
		set_party_name = {
			ideology = neutrality
			name = INS_MAJAPAHIT_party
			long_name = INS_MAJAPAHIT_party_long
		}
		promote_character = DEI_wuryaningrat'''

assert old_f in fc, "old_f not found in focus tree"
fc = fc.replace(old_f, new_f, 1)

with open(focus_file, 'w', encoding='utf-8') as f:
    f.write(fc)
print("Updated DEI_indonesia_focus_tree.txt politics successfully!")

# ---------------------------------------------------------------------
# Update events/DEI_00_shared_trunk_events.txt (dei_trunk.6)
# ---------------------------------------------------------------------
trunk_file = 'events/DEI_00_shared_trunk_events.txt'
with open(trunk_file, 'r', encoding='utf-8') as f:
    tc = f.read()

old_t = '''				set_politics = {
					ruling_party = democratic
					elections_allowed = yes
				}
				promote_character = DEI_sukarno'''

new_t = '''				set_politics = {
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
				promote_character = DEI_sukarno'''

assert old_t in tc, "old_t not found in trunk events"
tc = tc.replace(old_t, new_t, 1)

with open(trunk_file, 'w', encoding='utf-8') as f:
    f.write(tc)
print("Updated DEI_00_shared_trunk_events.txt politics successfully!")
