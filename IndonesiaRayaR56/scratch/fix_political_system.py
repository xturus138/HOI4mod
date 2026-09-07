import os

loc_file = r'localisation/english/DEI_indonesia_l_english.yml'
with open(loc_file, 'r', encoding='utf-8') as f:
    loc_text = f.read()

# Replace the party keys in loc
# Jalur A: democratic
loc_text = loc_text.replace('INS_REPUBLIK_NKRI_party:', 'INS_REPUBLIK_NKRI_democratic_party:')
loc_text = loc_text.replace('INS_REPUBLIK_NKRI_party_long:', 'INS_REPUBLIK_NKRI_democratic_party_long:')
loc_text = loc_text.replace('INS_REPUBLIK_RIS_party:', 'INS_REPUBLIK_RIS_democratic_party:')
loc_text = loc_text.replace('INS_REPUBLIK_RIS_party_long:', 'INS_REPUBLIK_RIS_democratic_party_long:')
loc_text = loc_text.replace('INS_REPUBLIK_SOSIALIS_party:', 'INS_REPUBLIK_SOSIALIS_democratic_party:')
loc_text = loc_text.replace('INS_REPUBLIK_SOSIALIS_party_long:', 'INS_REPUBLIK_SOSIALIS_democratic_party_long:')

# Jalur B: democratic
loc_text = loc_text.replace('INS_KOLONIAL_DEI_party:', 'INS_KOLONIAL_DEI_democratic_party:')
loc_text = loc_text.replace('INS_KOLONIAL_DEI_party_long:', 'INS_KOLONIAL_DEI_democratic_party_long:')
loc_text = loc_text.replace('INS_KOLONIAL_BFO_party:', 'INS_KOLONIAL_BFO_democratic_party:')
loc_text = loc_text.replace('INS_KOLONIAL_BFO_party_long:', 'INS_KOLONIAL_BFO_democratic_party_long:')
loc_text = loc_text.replace('INS_KOLONIAL_DOMINION_party:', 'INS_KOLONIAL_DOMINION_democratic_party:')
loc_text = loc_text.replace('INS_KOLONIAL_DOMINION_party_long:', 'INS_KOLONIAL_DOMINION_democratic_party_long:')

# Jalur C: communism
loc_text = loc_text.replace('INS_KOMUNIS_RRI_party:', 'INS_KOMUNIS_RRI_communism_party:')
loc_text = loc_text.replace('INS_KOMUNIS_RRI_party_long:', 'INS_KOMUNIS_RRI_communism_party_long:')
loc_text = loc_text.replace('INS_KOMUNIS_SOVIET_party:', 'INS_KOMUNIS_SOVIET_communism_party:')
loc_text = loc_text.replace('INS_KOMUNIS_SOVIET_party_long:', 'INS_KOMUNIS_SOVIET_communism_party_long:')
loc_text = loc_text.replace('INS_KOMUNIS_FRONT_party:', 'INS_KOMUNIS_FRONT_communism_party:')
loc_text = loc_text.replace('INS_KOMUNIS_FRONT_party_long:', 'INS_KOMUNIS_FRONT_communism_party_long:')

# Jalur D: fascism
loc_text = loc_text.replace('INS_OTORITER_NKRI_party:', 'INS_OTORITER_NKRI_fascism_party:')
loc_text = loc_text.replace('INS_OTORITER_NKRI_party_long:', 'INS_OTORITER_NKRI_fascism_party_long:')
loc_text = loc_text.replace('INS_OTORITER_JUNTA_party:', 'INS_OTORITER_JUNTA_fascism_party:')
loc_text = loc_text.replace('INS_OTORITER_JUNTA_party_long:', 'INS_OTORITER_JUNTA_fascism_party_long:')
loc_text = loc_text.replace('INS_OTORITER_RAYA_party:', 'INS_OTORITER_RAYA_fascism_party:')
loc_text = loc_text.replace('INS_OTORITER_RAYA_party_long:', 'INS_OTORITER_RAYA_fascism_party_long:')

# Jalur E: neutrality
loc_text = loc_text.replace('INS_ISLAMIS_NII_party:', 'INS_ISLAMIS_NII_neutrality_party:')
loc_text = loc_text.replace('INS_ISLAMIS_NII_party_long:', 'INS_ISLAMIS_NII_neutrality_party_long:')
loc_text = loc_text.replace('INS_ISLAMIS_DAULAH_party:', 'INS_ISLAMIS_DAULAH_neutrality_party:')
loc_text = loc_text.replace('INS_ISLAMIS_DAULAH_party_long:', 'INS_ISLAMIS_DAULAH_neutrality_party_long:')
loc_text = loc_text.replace('INS_ISLAMIS_KHILAFAH_party:', 'INS_ISLAMIS_KHILAFAH_neutrality_party:')
loc_text = loc_text.replace('INS_ISLAMIS_KHILAFAH_party_long:', 'INS_ISLAMIS_KHILAFAH_neutrality_party_long:')

# Jalur F: neutrality
loc_text = loc_text.replace('INS_MAJAPAHIT_EMPIRE_party:', 'INS_MAJAPAHIT_EMPIRE_neutrality_party:')
loc_text = loc_text.replace('INS_MAJAPAHIT_EMPIRE_party_long:', 'INS_MAJAPAHIT_EMPIRE_neutrality_party_long:')
loc_text = loc_text.replace('INS_MAJAPAHIT_SURYA_party:', 'INS_MAJAPAHIT_SURYA_neutrality_party:')
loc_text = loc_text.replace('INS_MAJAPAHIT_SURYA_party_long:', 'INS_MAJAPAHIT_SURYA_neutrality_party_long:')
loc_text = loc_text.replace('INS_MAJAPAHIT_NUSANTARA_party:', 'INS_MAJAPAHIT_NUSANTARA_neutrality_party:')
loc_text = loc_text.replace('INS_MAJAPAHIT_NUSANTARA_party_long:', 'INS_MAJAPAHIT_NUSANTARA_neutrality_party_long:')

# Extra general party keys and set_party_name keys
extra_parties = '''
 # ---------------------------------------------------------------------
 # PARTIES: STANDARD & SET_PARTY_NAME DIRECT KEYS
 # ---------------------------------------------------------------------
 INS_democratic_party: "PNI"
 INS_democratic_party_long: "Partai Nasional Indonesia"
 INS_communism_party: "PKI"
 INS_communism_party_long: "Partai Komunis Indonesia"
 INS_fascism_party: "Dewan Revolusi"
 INS_fascism_party_long: "Dewan Revolusi Angkatan Bersenjata"
 INS_neutrality_party: "Volksraad"
 INS_neutrality_party_long: "Volksraad Hindia Belanda"

 INS_PNI_party: "PNI"
 INS_PNI_party_long: "Partai Nasional Indonesia"
 INS_BFO_party: "BFO"
 INS_BFO_party_long: "Bijeenkomst voor Federaal Overleg"
 INS_PKI_party: "PKI"
 INS_PKI_party_long: "Partai Komunis Indonesia"
 INS_DEWAN_REVOLUSI_party: "Dewan Revolusi"
 INS_DEWAN_REVOLUSI_party_long: "Dewan Revolusi Angkatan Bersenjata"
 INS_NII_party: "Majelis Syuro"
 INS_NII_party_long: "Majelis Syuro Negara Islam Indonesia"
 INS_MAJAPAHIT_party: "Kraton Wilwatikta"
 INS_MAJAPAHIT_party_long: "Keluarga Diraja & Rakryan Majapahit"
'''

if 'INS_PNI_party:' not in loc_text:
    loc_text += extra_parties

# Write back with BOM
with open(loc_file, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + loc_text.lstrip('\ufeff').encode('utf-8'))

print('Updated localization party keys with BOM successfully!')
