import os

loc_path = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml'

with open(loc_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

new_entries = """
 # =====================================================================
 # EXPANDED MILITARY COMMANDERS (AD & AL)
 # =====================================================================
 DEI_ahmad_yani: "Ahmad Yani"
 DEI_ngurah_rai: "I Gusti Ngurah Rai"
 DEI_tb_simatupang: "T.B. Simatupang"
 DEI_bung_tomo: "Sutomo (Bung Tomo)"
 DEI_slamet_rijadi: "Ignatius Slamet Rijadi"
 DEI_djatikoesoemo: "G.P.H. Djatikusumo"
 DEI_soengkono: "Soengkono"
 DEI_djamin_ginting: "Djamin Ginting"
 DEI_john_lie: "John Lie (Jahja Daniel Dharma)"

 trait_dei_ahmad_yani: "Pahlawan Palagan Ambarawa"
 trait_dei_ahmad_yani_desc: "Hero of the Battle of Ambarawa, renowned for aggressive tactical assaults and inspiring frontline infantry resilience."
 trait_dei_ngurah_rai: "Panglima Ciung Wanara"
 trait_dei_ngurah_rai_desc: "Heroic commander of the Balinese resistance, inspiring unflinching valor in rugged mountain terrain even when isolated from supply lines."
 trait_dei_simatupang: "Kepala Staf Angkatan Perang"
 trait_dei_simatupang_desc: "Brilliant military intellectual and supreme staff organizer, mastering rapid operational planning and frugal logistics."
 trait_dei_bung_tomo: "Pengobar Semangat BPRI"
 trait_dei_bung_tomo_desc: "Electrifying orator of the Surabaya resistance, driving volunteer battalions and youth militias into fearless combat."
 trait_dei_john_lie: "Macan Selat Malaka"
 trait_dei_john_lie_desc: "Audacious naval captain known as 'The Outlaw', legendary for daringly breaching hostile blockades across the Malacca Straits."
"""

new_content = content + new_entries
with open(loc_path, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + new_content.encode('utf-8'))
print('Successfully appended expanded military commander loc keys with UTF-8 BOM!')
