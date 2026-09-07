# Category definition
cat_content = '''# =====================================================================
# INDONESIA RAYA (R56 SUBMOD) - Developer Debugging Tools Category
# Pinned to the top of Decisions tab (priority = 1000)
# =====================================================================

dei_decisions_debug_tools = {
	icon = generic_research
	priority = 1000
	allowed = { tag = INS }
	visible = {
		tag = INS
	}
}
'''

# Decisions definition
dec_content = '''# =====================================================================
# INDONESIA RAYA (R56 SUBMOD) - Developer Debugging Tools
# =====================================================================

dei_decisions_debug_tools = {

	# 1. INSTANT COMPLETE 1936 PROLOGUE
	dei_debug_instant_prologue = {
		icon = generic_crisis
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			complete_national_focus = dei_focus_root
			complete_national_focus = dei_focus_pembangkangan
			complete_national_focus = dei_focus_momentum_kemerdekaan
			end_puppet = yes
			set_cosmetic_tag = INS_REPUBLIK_NKRI
			recruit_character = DEI_sukarno
			recruit_character = DEI_mohammad_hatta
			recruit_character = DEI_sudirman
			set_politics = {
				ruling_party = democratic
				elections_allowed = yes
			}
			promote_character = DEI_sukarno
			load_oob = DEI_templates
			load_oob = DEI_air_starter
			add_equipment_to_stockpile = { type = infantry_equipment amount = 5000 }
			add_equipment_to_stockpile = { type = artillery_equipment amount = 300 }
			add_equipment_to_stockpile = { type = support_equipment amount = 300 }
			news_event = { id = dei_trunk.6 }
		}
	}

	# 2. INSTANT PATH A - REPUBLIK DEMOKRATIS
	dei_debug_path_a = {
		icon = generic_democracy
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			clr_country_flag = dei_path_b_chosen
			clr_country_flag = dei_path_c_chosen
			clr_country_flag = dei_path_d_chosen
			clr_country_flag = dei_path_e_chosen
			clr_country_flag = dei_path_f_chosen
			set_country_flag = dei_jalur_dipilih
			set_country_flag = dei_path_a_chosen
			complete_national_focus = dei_focus_a_proklamasi
			set_cosmetic_tag = INS_REPUBLIK_NKRI
			recruit_character = DEI_sukarno
			recruit_character = DEI_mohammad_hatta
			set_politics = {
				ruling_party = democratic
				elections_allowed = yes
			}
			promote_character = DEI_sukarno
			load_oob = DEI_navy_starter_a
			335 = {
				create_unit = {
					division_template = "Divisi Infanteri TKR"
					start_experience_factor = 0.3
				}
				create_unit = {
					division_template = "Divisi Infanteri TKR"
					start_experience_factor = 0.3
				}
			}
		}
	}

	# 3. INSTANT PATH B - FEDERALIS BFO / VAN MOOK
	dei_debug_path_b = {
		icon = generic_national_unity
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			clr_country_flag = dei_path_a_chosen
			clr_country_flag = dei_path_c_chosen
			clr_country_flag = dei_path_d_chosen
			clr_country_flag = dei_path_e_chosen
			clr_country_flag = dei_path_f_chosen
			set_country_flag = dei_jalur_dipilih
			set_country_flag = dei_path_b_chosen
			complete_national_focus = dei_focus_b_root
			set_cosmetic_tag = INS_KOLONIAL_BFO
			recruit_character = DEI_hubertus_van_mook
			recruit_character = DEI_sukawati
			set_politics = {
				ruling_party = federalist
				elections_allowed = no
			}
			promote_character = DEI_hubertus_van_mook
			load_oob = DEI_navy_starter_b
			335 = {
				create_unit = {
					division_template = "KNIL Infanterie Divisie"
					start_experience_factor = 0.4
				}
				create_unit = {
					division_template = "KNIL Infanterie Divisie"
					start_experience_factor = 0.4
				}
			}
		}
	}

	# 4. INSTANT PATH C - KOMUNIS / MUSSO
	dei_debug_path_c = {
		icon = generic_communism
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			clr_country_flag = dei_path_a_chosen
			clr_country_flag = dei_path_b_chosen
			clr_country_flag = dei_path_d_chosen
			clr_country_flag = dei_path_e_chosen
			clr_country_flag = dei_path_f_chosen
			set_country_flag = dei_jalur_dipilih
			set_country_flag = dei_path_c_chosen
			complete_national_focus = dei_focus_c_root
			set_cosmetic_tag = INS_KOMUNIS_RRI
			recruit_character = DEI_musso
			recruit_character = DEI_tan_malaka
			recruit_character = DEI_amir_sjarifuddin
			set_politics = {
				ruling_party = communism
				elections_allowed = no
			}
			promote_character = DEI_musso
			load_oob = DEI_navy_starter_c
			335 = {
				create_unit = {
					division_template = "Brigade Barisan Buruh"
					start_experience_factor = 0.3
				}
				create_unit = {
					division_template = "Brigade Barisan Buruh"
					start_experience_factor = 0.3
				}
			}
		}
	}

	# 5. INSTANT PATH D - MILITER / SOEDIRMAN
	dei_debug_path_d = {
		icon = generic_fascism
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			clr_country_flag = dei_path_a_chosen
			clr_country_flag = dei_path_b_chosen
			clr_country_flag = dei_path_c_chosen
			clr_country_flag = dei_path_e_chosen
			clr_country_flag = dei_path_f_chosen
			set_country_flag = dei_jalur_dipilih
			set_country_flag = dei_path_d_chosen
			complete_national_focus = dei_focus_d_root
			set_cosmetic_tag = INS_OTORITER_NKRI
			recruit_character = DEI_sudirman
			recruit_character = DEI_nasution
			recruit_character = DEI_kawilarang
			set_politics = {
				ruling_party = fascism
				elections_allowed = no
			}
			promote_character = DEI_sudirman
			load_oob = DEI_navy_starter_d
			335 = {
				create_unit = {
					division_template = "Resimen Pengawal Revolusi"
					start_experience_factor = 0.4
				}
				create_unit = {
					division_template = "Resimen Pengawal Revolusi"
					start_experience_factor = 0.4
				}
			}
		}
	}

	# 6. INSTANT PATH E - ISLAMIS NII / KARTOSOEWIRJO
	dei_debug_path_e = {
		icon = generic_propaganda
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			clr_country_flag = dei_path_a_chosen
			clr_country_flag = dei_path_b_chosen
			clr_country_flag = dei_path_c_chosen
			clr_country_flag = dei_path_d_chosen
			clr_country_flag = dei_path_f_chosen
			set_country_flag = dei_jalur_dipilih
			set_country_flag = dei_path_e_chosen
			complete_national_focus = dei_focus_e_root
			set_cosmetic_tag = INS_ISLAMIS_NII
			recruit_character = DEI_kartosuwiryo
			recruit_character = DEI_wahid_hasyim
			recruit_character = DEI_mohammad_natsir
			set_politics = {
				ruling_party = islamist
				elections_allowed = no
			}
			promote_character = DEI_kartosuwiryo
			load_oob = DEI_navy_starter_e
			335 = {
				create_unit = {
					division_template = "Resimen Laskar Hizbullah"
					start_experience_factor = 0.3
				}
				create_unit = {
					division_template = "Resimen Laskar Hizbullah"
					start_experience_factor = 0.3
				}
			}
		}
	}

	# 7. INSTANT PATH F - MAJAPAHIT / WURYANINGRAT
	dei_debug_path_f = {
		icon = generic_civilian_economy
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			clr_country_flag = dei_path_a_chosen
			clr_country_flag = dei_path_b_chosen
			clr_country_flag = dei_path_c_chosen
			clr_country_flag = dei_path_d_chosen
			clr_country_flag = dei_path_e_chosen
			set_country_flag = dei_jalur_dipilih
			set_country_flag = dei_path_f_chosen
			complete_national_focus = dei_focus_f_root
			set_cosmetic_tag = INS_MAJAPAHIT_EMPIRE
			recruit_character = DEI_wuryaningrat
			recruit_character = DEI_hamengkubuwono_ix
			recruit_character = DEI_maharaja_suryawikrama
			set_politics = {
				ruling_party = majapahit
				elections_allowed = no
			}
			promote_character = DEI_wuryaningrat
			load_oob = DEI_navy_starter_f
			335 = {
				create_unit = {
					division_template = "Bhayangkara Praja Majapahit"
					start_experience_factor = 0.4
				}
				create_unit = {
					division_template = "Bhayangkara Praja Majapahit"
					start_experience_factor = 0.4
				}
			}
		}
	}

	# 8. SUPER GOD BUFF (PP + STABILITY + WAR SUPPORT + STOCKPILE)
	dei_debug_super_buff = {
		icon = generic_war_support
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			add_political_power = 2000
			add_stability = 0.50
			add_war_support = 0.50
			add_command_power = 100
			add_equipment_to_stockpile = { type = infantry_equipment amount = 20000 }
			add_equipment_to_stockpile = { type = artillery_equipment amount = 2000 }
			add_equipment_to_stockpile = { type = support_equipment amount = 2000 }
			add_equipment_to_stockpile = { type = light_tank_chassis amount = 500 }
			add_equipment_to_stockpile = { type = small_plane_airframe amount = 300 }
		}
	}

	# 9. FIRE PROLOGUE NEWS EVENTS (TESTER)
	dei_debug_fire_events = {
		icon = generic_propaganda
		allowed = { tag = INS }
		visible = { tag = INS }
		available = { always = yes }
		cost = 0
		fire_only_once = no

		complete_effect = {
			news_event = { id = dei_trunk.1 }
			news_event = { id = dei_trunk.2 }
		}
	}
}
'''

with open('common/decisions/categories/DEI_debug_categories.txt', 'w', encoding='utf-8') as f:
    f.write(cat_content)

with open('common/decisions/DEI_debug_decisions.txt', 'w', encoding='utf-8') as f:
    f.write(dec_content)

print('Created DEI_debug_categories.txt and DEI_debug_decisions.txt successfully!')
