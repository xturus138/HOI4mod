with open(r'common\national_focus\DEI_indonesia_focus_tree.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update dei_focus_fraktur
old_f1 = '''			add_political_power = 40
			add_stability = -0.05
			country_event = { id = dei_trunk.1 hours = 6 }'''
new_f1 = '''			add_political_power = 40
			add_stability = -0.05
			news_event = { id = dei_trunk.1 hours = 6 }'''
assert old_f1 in text, 'old_f1 not found'
text = text.replace(old_f1, new_f1)

# 2. Update dei_focus_pembangkangan
old_f2 = '''			add_war_support = 0.10
			add_stability = -0.05
			country_event = { id = dei_trunk.2 hours = 6 }'''
new_f2 = '''			add_war_support = 0.10
			add_stability = -0.05
			news_event = { id = dei_trunk.2 hours = 6 }'''
assert old_f2 in text, 'old_f2 not found'
text = text.replace(old_f2, new_f2)

# 3. Update dei_focus_momentum_kemerdekaan
old_f3 = '''		completion_reward = {
			load_oob = DEI_templates
			load_oob = DEI_air_starter
			add_equipment_to_stockpile = { type = infantry_equipment amount = 3000 }
			add_equipment_to_stockpile = { type = artillery_equipment amount = 150 }
			add_equipment_to_stockpile = { type = support_equipment amount = 200 }
			recruit_character = DEI_sudirman
			recruit_character = DEI_urip_sumoharjo
			recruit_character = DEI_nasution
			recruit_character = DEI_kawilarang
			recruit_character = DEI_yos_sudarso
			recruit_character = DEI_re_martadinata
			recruit_character = DEI_suryadi_suryadarma
			recruit_character = DEI_halim_perdanakusuma
			recruit_character = DEI_moestopo
			recruit_character = DEI_gatot_soebroto
			recruit_character = DEI_ahmad_yani
			recruit_character = DEI_ngurah_rai
			recruit_character = DEI_soeharto
			recruit_character = DEI_tb_simatupang
			recruit_character = DEI_bung_tomo
			recruit_character = DEI_slamet_rijadi
			recruit_character = DEI_djatikoesoemo
			recruit_character = DEI_soengkono
			recruit_character = DEI_djamin_ginting
			recruit_character = DEI_john_lie
			news_event = { id = dei_trunk.6 hours = 6 }
		}'''

new_f3 = '''		completion_reward = {
			end_puppet = yes
			set_cosmetic_tag = INS_REPUBLIK_NKRI
			add_ideas = dei_idea_revolusi_dini_spirit
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
			add_equipment_to_stockpile = { type = infantry_equipment amount = 3000 }
			add_equipment_to_stockpile = { type = artillery_equipment amount = 150 }
			add_equipment_to_stockpile = { type = support_equipment amount = 200 }
			recruit_character = DEI_urip_sumoharjo
			recruit_character = DEI_nasution
			recruit_character = DEI_kawilarang
			recruit_character = DEI_yos_sudarso
			recruit_character = DEI_re_martadinata
			recruit_character = DEI_suryadi_suryadarma
			recruit_character = DEI_halim_perdanakusuma
			recruit_character = DEI_moestopo
			recruit_character = DEI_gatot_soebroto
			recruit_character = DEI_ahmad_yani
			recruit_character = DEI_ngurah_rai
			recruit_character = DEI_soeharto
			recruit_character = DEI_tb_simatupang
			recruit_character = DEI_bung_tomo
			recruit_character = DEI_slamet_rijadi
			recruit_character = DEI_djatikoesoemo
			recruit_character = DEI_soengkono
			recruit_character = DEI_djamin_ginting
			recruit_character = DEI_john_lie
			news_event = { id = dei_trunk.6 hours = 6 }
		}'''
assert old_f3 in text, 'old_f3 not found'
text = text.replace(old_f3, new_f3)

# 4. Update Path A root
old_pa = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_a_chosen
		set_cosmetic_tag = INS_REPUBLIK_NKRI
		set_politics = {
			ruling_party = democratic
			elections_allowed = yes
		}
		add_ideas = dei_idea_republik_diproklamasikan
		country_event = { id = dei_leadership.1 days = 1 }'''
new_pa = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_a_chosen
		set_cosmetic_tag = INS_REPUBLIK_NKRI
		recruit_character = DEI_sukarno
		recruit_character = DEI_mohammad_hatta
		set_politics = {
			ruling_party = democratic
			elections_allowed = yes
		}
		promote_character = DEI_sukarno
		add_ideas = dei_idea_republik_diproklamasikan
		country_event = { id = dei_leadership.1 days = 1 }'''
assert old_pa in text, 'old_pa not found'
text = text.replace(old_pa, new_pa)

# 5. Update Path B root
old_pb = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_b_chosen
		set_cosmetic_tag = INS_KOLONIAL_BFO
		set_politics = {
			ruling_party = federalist
			elections_allowed = no
		}
		country_event = { id = dei_leadership.2 days = 1 }'''
new_pb = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_b_chosen
		set_cosmetic_tag = INS_KOLONIAL_BFO
		recruit_character = DEI_hubertus_van_mook
		recruit_character = DEI_sukawati
		set_politics = {
			ruling_party = federalist
			elections_allowed = no
		}
		promote_character = DEI_hubertus_van_mook
		country_event = { id = dei_leadership.2 days = 1 }'''
assert old_pb in text, 'old_pb not found'
text = text.replace(old_pb, new_pb)

# 6. Update Path C root
old_pc = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_c_chosen
		set_cosmetic_tag = INS_KOMUNIS_RRI
		set_politics = {
			ruling_party = communism
			elections_allowed = no
		}
		country_event = { id = dei_leadership.3 days = 1 }'''
new_pc = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_c_chosen
		set_cosmetic_tag = INS_KOMUNIS_RRI
		recruit_character = DEI_musso
		recruit_character = DEI_tan_malaka
		recruit_character = DEI_amir_sjarifuddin
		set_politics = {
			ruling_party = communism
			elections_allowed = no
		}
		promote_character = DEI_musso
		country_event = { id = dei_leadership.3 days = 1 }'''
assert old_pc in text, 'old_pc not found'
text = text.replace(old_pc, new_pc)

# 7. Update Path D root
old_pd = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_d_chosen
		set_cosmetic_tag = INS_OTORITER_NKRI
		set_politics = {
			ruling_party = fascism
			elections_allowed = no
		}
		country_event = { id = dei_leadership.4 days = 1 }'''
new_pd = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_d_chosen
		set_cosmetic_tag = INS_OTORITER_NKRI
		recruit_character = DEI_sudirman
		recruit_character = DEI_nasution
		recruit_character = DEI_kawilarang
		set_politics = {
			ruling_party = fascism
			elections_allowed = no
		}
		promote_character = DEI_sudirman
		country_event = { id = dei_leadership.4 days = 1 }'''
assert old_pd in text, 'old_pd not found'
text = text.replace(old_pd, new_pd)

# 8. Update Path E root
old_pe = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_e_chosen
		set_cosmetic_tag = INS_ISLAMIS_NII
		set_politics = {
			ruling_party = islamist
			elections_allowed = no
		}
		country_event = { id = dei_leadership.5 days = 1 }'''
new_pe = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_e_chosen
		set_cosmetic_tag = INS_ISLAMIS_NII
		recruit_character = DEI_kartosuwiryo
		recruit_character = DEI_wahid_hasyim
		recruit_character = DEI_mohammad_natsir
		set_politics = {
			ruling_party = islamist
			elections_allowed = no
		}
		promote_character = DEI_kartosuwiryo
		country_event = { id = dei_leadership.5 days = 1 }'''
assert old_pe in text, 'old_pe not found'
text = text.replace(old_pe, new_pe)

# 9. Update Path F root
old_pf = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_f_chosen
		set_cosmetic_tag = INS_MAJAPAHIT_EMPIRE
		set_politics = {
			ruling_party = majapahit
			elections_allowed = no
		}
		country_event = { id = dei_leadership.6 days = 1 }'''
new_pf = '''		set_country_flag = dei_jalur_dipilih
		set_country_flag = dei_path_f_chosen
		set_cosmetic_tag = INS_MAJAPAHIT_EMPIRE
		recruit_character = DEI_wuryaningrat
		recruit_character = DEI_hamengkubuwono_ix
		recruit_character = DEI_maharaja_suryawikrama
		set_politics = {
			ruling_party = majapahit
			elections_allowed = no
		}
		promote_character = DEI_wuryaningrat
		country_event = { id = dei_leadership.6 days = 1 }'''
assert old_pf in text, 'old_pf not found'
text = text.replace(old_pf, new_pf)

with open(r'common\national_focus\DEI_indonesia_focus_tree.txt', 'w', encoding='utf-8') as f:
    f.write(text)

diff = text.count('{') - text.count('}')
print(f'Focus tree updated successfully! Brace diff: {diff}')
