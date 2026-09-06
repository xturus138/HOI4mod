import os

file_path = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\units\names_divisions\INS_names_divisions.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

otoriter_block = '''
DEI_OTORITER = {
	name = "Resimen Pengawal Dewan Revolusi & Pelopor Bela Negara"
	for_countries = { INS }
	can_use = { always = yes }
	division_types = { "infantry" "motorized" "mechanized" }
	fallback_name = "Resimen Pengawal %d"
	ordered = {
		1 = { "Resimen I Pengawal Dewan Revolusi" }
		2 = { "Resimen II Pengawal Dewan Revolusi" }
		3 = { "Brigade Khusus Mandala Perkasa" }
		4 = { "Resimen Pelopor Bela Negara I" }
		5 = { "Resimen Pelopor Bela Negara II" }
		6 = { "Divisi Garda Kehormatan Revolusi" }
		7 = { "Resimen Tempur Selat Sunda" }
		8 = { "Resimen Tempur Selat Malaka" }
		9 = { "Brigade Serbu Khatulistiwa" }
		10 = { "Detasemen Siaga Puncak Revolusi" }
	}
}
'''

if 'DEI_OTORITER' not in text:
    text = text.rstrip() + '\n\n' + otoriter_block.strip() + '\n'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('Added DEI_OTORITER to INS_names_divisions.txt')
else:
    print('DEI_OTORITER already present')
