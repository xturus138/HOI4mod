# Add liberation decisions to DEI_decisions.txt
dec_path = 'common/decisions/DEI_decisions.txt'
with open(dec_path, 'r', encoding='utf-8') as f:
    d_text = f.read()

liberation_decisions = '''
		# Ekspedisi Pembebasan Sumatera
		dei_decision_liberate_sumatra = {
			icon = generic_civil_war
			allowed = { tag = INS }
			visible = {
				has_country_flag = dei_jalur_dipilih
				NOT = { has_country_flag = dei_sumatra_liberated }
			}
			available = {
				has_political_power > 24
			}
			cost = 25
			fire_only_once = yes

			complete_effect = {
				set_country_flag = dei_sumatra_liberated
				672 = { set_state_owner_to = INS set_state_controller_to = INS }
				1135 = { set_state_owner_to = INS set_state_controller_to = INS }
				974 = { set_state_owner_to = INS set_state_controller_to = INS }
				1128 = { set_state_owner_to = INS set_state_controller_to = INS }
				909 = { set_state_owner_to = INS set_state_controller_to = INS }
				add_stability = 0.05
				add_war_support = 0.05
				672 = {
					create_unit = {
						division_template = "Resimen Pelopor Rakyat"
						start_experience_factor = 0.3
					}
				}
				974 = {
					create_unit = {
						division_template = "Resimen Pelopor Rakyat"
						start_experience_factor = 0.3
					}
				}
			}
		}

		# Ekspedisi Pembebasan Kalimantan
		dei_decision_liberate_kalimantan = {
			icon = generic_operation
			allowed = { tag = INS }
			visible = {
				has_country_flag = dei_jalur_dipilih
				NOT = { has_country_flag = dei_kalimantan_liberated }
			}
			available = {
				has_political_power > 24
			}
			cost = 25
			fire_only_once = yes

			complete_effect = {
				set_country_flag = dei_kalimantan_liberated
				334 = { set_state_owner_to = INS set_state_controller_to = INS }
				977 = { set_state_owner_to = INS set_state_controller_to = INS }
				978 = { set_state_owner_to = INS set_state_controller_to = INS }
				add_stability = 0.05
				add_war_support = 0.05
				334 = {
					create_unit = {
						division_template = "Resimen Pelopor Rakyat"
						start_experience_factor = 0.3
					}
				}
			}
		}

		# Operasi Lintas Laut Sulawesi, Maluku & Nusa Tenggara
		dei_decision_liberate_east_indies = {
			icon = generic_naval
			allowed = { tag = INS }
			visible = {
				has_country_flag = dei_jalur_dipilih
				NOT = { has_country_flag = dei_east_indies_liberated }
			}
			available = {
				has_political_power > 24
			}
			cost = 25
			fire_only_once = yes

			complete_effect = {
				set_country_flag = dei_east_indies_liberated
				673 = { set_state_owner_to = INS set_state_controller_to = INS }
				975 = { set_state_owner_to = INS set_state_controller_to = INS }
				668 = { set_state_owner_to = INS set_state_controller_to = INS }
				738 = { set_state_owner_to = INS set_state_controller_to = INS }
				1142 = { set_state_owner_to = INS set_state_controller_to = INS }
				667 = { set_state_owner_to = INS set_state_controller_to = INS }
				add_stability = 0.05
				add_war_support = 0.05
				673 = {
					create_unit = {
						division_template = "Divisi Marinir KKO"
						start_experience_factor = 0.4
					}
				}
			}
		}

		# Pembebasan Papua Barat
		dei_decision_liberate_papua = {
			icon = generic_national_unity
			allowed = { tag = INS }
			visible = {
				has_country_flag = dei_jalur_dipilih
				NOT = { has_country_flag = dei_papua_liberated }
			}
			available = {
				has_political_power > 24
			}
			cost = 25
			fire_only_once = yes

			complete_effect = {
				set_country_flag = dei_papua_liberated
				669 = { set_state_owner_to = INS set_state_controller_to = INS }
				1137 = { set_state_owner_to = INS set_state_controller_to = INS }
				add_stability = 0.05
				add_war_support = 0.05
			}
		}
'''

target_dec = 'dei_decisions_nusantara = {'
assert target_dec in d_text, "target_dec not found!"
d_text = d_text.replace(target_dec, target_dec + liberation_decisions, 1)

with open(dec_path, 'w', encoding='utf-8') as f:
    f.write(d_text)
print('Added liberation decisions to DEI_decisions.txt successfully!')

# Add dei_debug_liberate_all_islands to DEI_debug_decisions.txt
debug_path = 'common/decisions/DEI_debug_decisions.txt'
with open(debug_path, 'r', encoding='utf-8') as f:
    dbg_text = f.read()

debug_liberate_all = '''
	# 10. INSTANT LIBERATE ALL OUTER ISLANDS (TESTER)
	dei_debug_liberate_all_islands = {
		icon = generic_national_unity
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			set_country_flag = dei_sumatra_liberated
			set_country_flag = dei_kalimantan_liberated
			set_country_flag = dei_east_indies_liberated
			set_country_flag = dei_papua_liberated
			672 = { set_state_owner_to = INS set_state_controller_to = INS }
			1135 = { set_state_owner_to = INS set_state_controller_to = INS }
			974 = { set_state_owner_to = INS set_state_controller_to = INS }
			1128 = { set_state_owner_to = INS set_state_controller_to = INS }
			909 = { set_state_owner_to = INS set_state_controller_to = INS }
			334 = { set_state_owner_to = INS set_state_controller_to = INS }
			977 = { set_state_owner_to = INS set_state_controller_to = INS }
			978 = { set_state_owner_to = INS set_state_controller_to = INS }
			673 = { set_state_owner_to = INS set_state_controller_to = INS }
			975 = { set_state_owner_to = INS set_state_controller_to = INS }
			668 = { set_state_owner_to = INS set_state_controller_to = INS }
			738 = { set_state_owner_to = INS set_state_controller_to = INS }
			1142 = { set_state_owner_to = INS set_state_controller_to = INS }
			667 = { set_state_owner_to = INS set_state_controller_to = INS }
			669 = { set_state_owner_to = INS set_state_controller_to = INS }
			1137 = { set_state_owner_to = INS set_state_controller_to = INS }
			add_stability = 0.10
			add_war_support = 0.10
		}
	}
'''

target_dbg = 'dei_decisions_debug_tools = {'
assert target_dbg in dbg_text, "target_dbg not found!"
dbg_text = dbg_text.replace(target_dbg, target_dbg + debug_liberate_all, 1)

with open(debug_path, 'w', encoding='utf-8') as f:
    f.write(dbg_text)
print('Added dei_debug_liberate_all_islands to DEI_debug_decisions.txt successfully!')
