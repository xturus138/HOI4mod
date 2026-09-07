# State transfer block: Java & Bali to INS, Outer Islands to HOL (with INS cores on all)
outer_islands_to_hol = '''				# Outer Islands under colonial garrison / loyalist control
				672 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				1135 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				974 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				1128 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				909 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				334 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				977 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				978 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				673 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				975 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				668 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				738 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				1142 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				667 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				669 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				1137 = { set_state_owner_to = HOL set_state_controller_to = HOL }
				# INS Bastion: Java & Bali
				1126 = { set_state_owner_to = INS set_state_controller_to = INS }
				335 = { set_state_owner_to = INS set_state_controller_to = INS }
				976 = { set_state_owner_to = INS set_state_controller_to = INS }
				1143 = { set_state_owner_to = INS set_state_controller_to = INS }
				446 = { set_state_owner_to = INS set_state_controller_to = INS }
				1127 = { set_state_owner_to = INS set_state_controller_to = INS }
				# Core territory of Indonesia across all 22 states
				every_state = {
					limit = {
						OR = {
							state = 1126 state = 335 state = 976 state = 1143 state = 446 state = 1127
							state = 672 state = 1135 state = 974 state = 1128 state = 909
							state = 334 state = 977 state = 978
							state = 673 state = 975
							state = 668 state = 738 state = 1142 state = 667
							state = 669 state = 1137
						}
					}
					add_core_of = INS
				}'''

# 1. Update events/DEI_00_shared_trunk_events.txt
with open('events/DEI_00_shared_trunk_events.txt', 'r', encoding='utf-8') as f:
    trunk_text = f.read()

target = 'set_cosmetic_tag = INS_REPUBLIK_NKRI\n\t\t\t\tadd_ideas = dei_idea_revolusi_dini_spirit'
assert target in trunk_text, "target not found in trunk events!"
trunk_text = trunk_text.replace(target, f'{target}\n{outer_islands_to_hol}')

with open('events/DEI_00_shared_trunk_events.txt', 'w', encoding='utf-8') as f:
    f.write(trunk_text)
print('Updated DEI_00_shared_trunk_events.txt with outer islands garrison transfer!')

# 2. Update common/national_focus/DEI_indonesia_focus_tree.txt (dei_focus_momentum_kemerdekaan)
with open('common/national_focus/DEI_indonesia_focus_tree.txt', 'r', encoding='utf-8') as f:
    focus_text = f.read()

target_focus = 'set_cosmetic_tag = INS_REPUBLIK_NKRI\n\t\t\tadd_ideas = dei_idea_revolusi_dini_spirit'
assert target_focus in focus_text, "target_focus not found in focus tree!"
focus_text = focus_text.replace(target_focus, f'{target_focus}\n{outer_islands_to_hol}')

with open('common/national_focus/DEI_indonesia_focus_tree.txt', 'w', encoding='utf-8') as f:
    f.write(focus_text)
print('Updated DEI_indonesia_focus_tree.txt with outer islands garrison transfer!')

# 3. Update history/units/DEI_templates.txt with units block
units_block = '''
# =====================================================================
# STARTER DIVISIONS OOB: JAVA REVOLUTIONARY BASTION
# Placed precisely across Java: Batavia, Bandung, Semarang, Yogya, Surabaya, Malang
# =====================================================================
units = {
	division = {
		name = "Resimen Garnisun Batavia"
		location = 7381
		division_template = "Divisi Garnisun Pantai"
		start_experience_factor = 0.3
	}
	division = {
		name = "1. Divisi Siliwangi"
		location = 7421
		division_template = "Divisi Infanteri Siliwangi"
		start_experience_factor = 0.4
	}
	division = {
		name = "2. Divisi Diponegoro"
		location = 13522
		division_template = "Divisi Infanteri Diponegoro"
		start_experience_factor = 0.3
	}
	division = {
		name = "Resimen Pelopor Yogyakarta"
		location = 10135
		division_template = "Resimen Pelopor Rakyat"
		start_experience_factor = 0.4
	}
	division = {
		name = "Resimen Marinir KKO Surabaya"
		location = 13520
		division_template = "Divisi Marinir KKO"
		start_experience_factor = 0.4
	}
	division = {
		name = "Resimen Komando Darat Malang"
		location = 10479
		division_template = "Resimen Komando Angkatan Darat"
		start_experience_factor = 0.5
	}
}
'''

with open('history/units/DEI_templates.txt', 'r', encoding='utf-8') as f:
    t_text = f.read()

if 'units = {' not in t_text:
    t_text += units_block
    with open('history/units/DEI_templates.txt', 'w', encoding='utf-8') as f:
        f.write(t_text)
    print('Added Java starter units to history/units/DEI_templates.txt!')
else:
    print('units already present in DEI_templates.txt!')
