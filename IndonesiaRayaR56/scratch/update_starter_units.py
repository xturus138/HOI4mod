with open(r'common\national_focus\DEI_indonesia_focus_tree.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Path B units
old_b = '''			load_oob = DEI_navy_starter_b
			335 = {
				create_unit = {
					division_template = "Divisi Infanteri Siliwangi"
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
					division_template = "Divisi Infanteri Diponegoro"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Korps Komando Operasi"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
			}
			672 = {
				create_unit = {
					division_template = "Resimen Komando Angkatan Darat"
					start_experience_factor = 0.4
					start_equipment_factor = 0.9
				}
			}'''

new_b = '''			load_oob = DEI_navy_starter_b
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
			672 = {
				create_unit = {
					division_template = "KNIL Infanterie Divisie"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
			}'''

# Path C units
old_c = '''			load_oob = DEI_navy_starter_c
			335 = {
				create_unit = {
					division_template = "Divisi Infanteri Siliwangi"
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
					division_template = "Divisi Infanteri Diponegoro"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Korps Komando Operasi"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
			}
			672 = {
				create_unit = {
					division_template = "Resimen Komando Angkatan Darat"
					start_experience_factor = 0.4
					start_equipment_factor = 0.9
				}
			}'''

new_c = '''			load_oob = DEI_navy_starter_c
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
			672 = {
				create_unit = {
					division_template = "Brigade Barisan Buruh Merah"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
			}'''

# Path D units
old_d = '''			load_oob = DEI_navy_starter_d
			335 = {
				create_unit = {
					division_template = "Divisi Infanteri Siliwangi"
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
					division_template = "Divisi Infanteri Diponegoro"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Korps Komando Operasi"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
			}
			672 = {
				create_unit = {
					division_template = "Resimen Komando Angkatan Darat"
					start_experience_factor = 0.4
					start_equipment_factor = 0.9
				}
			}'''

new_d = '''			load_oob = DEI_navy_starter_d
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
			672 = {
				create_unit = {
					division_template = "Resimen Pengawal Dewan Revolusi"
					start_experience_factor = 0.4
					start_equipment_factor = 0.9
				}
			}'''

# Path E units
old_e = '''			load_oob = DEI_navy_starter_e
			335 = {
				create_unit = {
					division_template = "Divisi Infanteri Siliwangi"
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
					division_template = "Divisi Infanteri Diponegoro"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Korps Komando Operasi"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
			}
			672 = {
				create_unit = {
					division_template = "Resimen Komando Angkatan Darat"
					start_experience_factor = 0.4
					start_equipment_factor = 0.9
				}
			}'''

new_e = '''			load_oob = DEI_navy_starter_e
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
			672 = {
				create_unit = {
					division_template = "Resimen Mujahidin TII"
					start_experience_factor = 0.4
					start_equipment_factor = 0.9
				}
			}'''

# Path F units
old_f = '''			load_oob = DEI_navy_starter_f
			335 = {
				create_unit = {
					division_template = "Divisi Infanteri Siliwangi"
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
					division_template = "Divisi Infanteri Diponegoro"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
				create_unit = {
					division_template = "Korps Komando Operasi"
					start_experience_factor = 0.3
					start_equipment_factor = 0.8
				}
			}
			672 = {
				create_unit = {
					division_template = "Resimen Komando Angkatan Darat"
					start_experience_factor = 0.4
					start_equipment_factor = 0.9
				}
			}'''

new_f = '''			load_oob = DEI_navy_starter_f
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
			672 = {
				create_unit = {
					division_template = "Prajurit Utama Bhayangkara"
					start_experience_factor = 0.4
					start_equipment_factor = 0.9
				}
			}'''

assert old_b in text, 'old_b not found'
assert old_c in text, 'old_c not found'
assert old_d in text, 'old_d not found'
assert old_e in text, 'old_e not found'
assert old_f in text, 'old_f not found'

text = text.replace(old_b, new_b)
text = text.replace(old_c, new_c)
text = text.replace(old_d, new_d)
text = text.replace(old_e, new_e)
text = text.replace(old_f, new_f)

with open(r'common\national_focus\DEI_indonesia_focus_tree.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated all 5 paths with thematic starter units successfully!')
