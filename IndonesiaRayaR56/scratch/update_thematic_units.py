with open(r'common\national_focus\DEI_indonesia_focus_tree.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def get_block(navy_letter):
    return f'''		hidden_effect = {{
			load_oob = DEI_navy_starter_{navy_letter}
			335 = {{
				create_unit = {{
					division_template = "Divisi Infanteri Siliwangi"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}}
				create_unit = {{
					division_template = "Brigade Laskar Rakyat"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}}
			}}
			446 = {{
				create_unit = {{
					division_template = "Divisi Infanteri Diponegoro"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}}
				create_unit = {{
					division_template = "Brigade Laskar Rakyat"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}}
			}}
			add_equipment_to_stockpile = {{ type = infantry_equipment amount = 3000 }}
		}}'''

new_b = '''		hidden_effect = {
			load_oob = DEI_navy_starter_b
			335 = {
				create_unit = {
					division_template = "KNIL Infanterie Divisie"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Garnizun Stadswacht & Pantai"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			446 = {
				create_unit = {
					division_template = "KNIL Infanterie Divisie"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Garnizun Stadswacht & Pantai"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			add_equipment_to_stockpile = { type = infantry_equipment amount = 3000 }
		}'''

new_c = '''		hidden_effect = {
			load_oob = DEI_navy_starter_c
			335 = {
				create_unit = {
					division_template = "Brigade Barisan Buruh Merah"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Brigade Laskar Rakyat"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			446 = {
				create_unit = {
					division_template = "Brigade Barisan Buruh Merah"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Brigade Laskar Rakyat"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			add_equipment_to_stockpile = { type = infantry_equipment amount = 3000 }
		}'''

new_d = '''		hidden_effect = {
			load_oob = DEI_navy_starter_d
			335 = {
				create_unit = {
					division_template = "Resimen Pengawal Dewan Revolusi"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Barisan Pemuda Bela Negara"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			446 = {
				create_unit = {
					division_template = "Resimen Pengawal Dewan Revolusi"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Barisan Pemuda Bela Negara"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			add_equipment_to_stockpile = { type = infantry_equipment amount = 3000 }
		}'''

new_e = '''		hidden_effect = {
			load_oob = DEI_navy_starter_e
			335 = {
				create_unit = {
					division_template = "Resimen Mujahidin TII"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Brigade Laskar Rakyat"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			446 = {
				create_unit = {
					division_template = "Resimen Mujahidin TII"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Brigade Laskar Rakyat"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			add_equipment_to_stockpile = { type = infantry_equipment amount = 3000 }
		}'''

new_f = '''		hidden_effect = {
			load_oob = DEI_navy_starter_f
			335 = {
				create_unit = {
					division_template = "Prajurit Utama Bhayangkara"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Resimen Ksatria Dharmaputra"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			446 = {
				create_unit = {
					division_template = "Prajurit Utama Bhayangkara"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Resimen Ksatria Dharmaputra"
					start_experience_factor = 0.2
					start_equipment_factor = 0.9
				}
			}
			add_equipment_to_stockpile = { type = infantry_equipment amount = 3000 }
		}'''

for letter, repl in [('b', new_b), ('c', new_c), ('d', new_d), ('e', new_e), ('f', new_f)]:
    target = get_block(letter)
    assert target in text, f'Target for path {letter} not found'
    text = text.replace(target, repl)
    print(f'Replaced target for path {letter}')

with open(r'common\national_focus\DEI_indonesia_focus_tree.txt', 'w', encoding='utf-8') as f:
    f.write(text)

open_b = text.count('{')
close_b = text.count('}')
print(f'Braces check: open={open_b}, close={close_b}, diff={open_b - close_b}')
