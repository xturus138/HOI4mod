file_path = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\events\DEI_00_shared_trunk_events.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove load_oob = DEI_navy_starter from immediate
text = text.replace('load_oob = DEI_navy_starter\n', '')

# 2. Update option A
old_opt_a = '''	option = {
		name = dei_trunk.6.a # Jalur A: Republik Nasionalis-Demokratis
		set_country_flag = dei_path_a_chosen
		add_ideas = dei_idea_republik_diproklamasikan'''

new_opt_a = '''	option = {
		name = dei_trunk.6.a # Jalur A: Republik Nasionalis-Demokratis
		set_country_flag = dei_path_a_chosen
		set_cosmetic_tag = INS_REPUBLIK_NKRI
		load_oob = DEI_navy_starter_a
		add_ideas = dei_idea_republik_diproklamasikan'''

text = text.replace(old_opt_a, new_opt_a)

# 3. Update option B
old_opt_b = '''	option = {
		name = dei_trunk.6.b # Jalur B: Kolonial/Federalis (Belanda tetap berkuasa)
		set_country_flag = dei_path_b_chosen'''

new_opt_b = '''	option = {
		name = dei_trunk.6.b # Jalur B: Kolonial/Federalis (Belanda tetap berkuasa)
		set_country_flag = dei_path_b_chosen
		set_cosmetic_tag = INS_KOLONIAL_BFO
		load_oob = DEI_navy_starter_b'''

text = text.replace(old_opt_b, new_opt_b)

# 4. Update option C
old_opt_c = '''	option = {
		name = dei_trunk.6.c # Jalur C: Komunis
		set_country_flag = dei_path_c_chosen'''

new_opt_c = '''	option = {
		name = dei_trunk.6.c # Jalur C: Komunis
		set_country_flag = dei_path_c_chosen
		set_cosmetic_tag = INS_KOMUNIS_RRI
		load_oob = DEI_navy_starter_c'''

text = text.replace(old_opt_c, new_opt_c)

# 5. Update option D
old_opt_d = '''	option = {
		name = dei_trunk.6.d # Jalur D: Otoriter Militeristik/Nasionalis Radikal
		set_country_flag = dei_path_d_chosen'''

new_opt_d = '''	option = {
		name = dei_trunk.6.d # Jalur D: Otoriter Militeristik/Nasionalis Radikal
		set_country_flag = dei_path_d_chosen
		set_cosmetic_tag = INS_OTORITER_NKRI
		load_oob = DEI_navy_starter_d'''

text = text.replace(old_opt_d, new_opt_d)

# 6. Update option E
old_opt_e = '''	option = {
		name = dei_trunk.6.e # Jalur E: Islamis (Negara Islam Indonesia)
		set_country_flag = dei_path_e_chosen'''

new_opt_e = '''	option = {
		name = dei_trunk.6.e # Jalur E: Islamis (Negara Islam Indonesia)
		set_country_flag = dei_path_e_chosen
		set_cosmetic_tag = INS_ISLAMIS_NII
		load_oob = DEI_navy_starter_e'''

text = text.replace(old_opt_e, new_opt_e)

# 7. Update option F
old_opt_f = '''	option = {
		name = dei_trunk.6.f # Jalur F: Kebangkitan Majapahit (ahistoris, selalu tersedia)
		set_country_flag = dei_path_f_chosen'''

new_opt_f = '''	option = {
		name = dei_trunk.6.f # Jalur F: Kebangkitan Majapahit (ahistoris, selalu tersedia)
		set_country_flag = dei_path_f_chosen
		set_cosmetic_tag = INS_MAJAPAHIT_EMPIRE
		load_oob = DEI_navy_starter_f'''

text = text.replace(old_opt_f, new_opt_f)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated events/DEI_00_shared_trunk_events.txt successfully.')
