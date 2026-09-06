import os

loc_file = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml'

with open(loc_file, 'r', encoding='utf-8-sig') as f:
    content = f.read()

r56_override_keys = '''
 #### OVERRIDES: R56 Armed Forces & Industry Harmonization ####
 INS_koninklijk_nederlands_indisch_leger: "Modernisasi Angkatan Bersenjata"
 INS_koninklijk_nederlands_indisch_leger_desc: "Reorganizing the armed forces into a unified, disciplined military command capable of defending the territorial integrity of Nusantara."
 INS_naval_autonomy: "Komando Pertahanan Maritim"
 INS_naval_autonomy_desc: "Establishing autonomous naval defense squadrons and modernizing maritime dockyards to patrol key strategic straits."
 INS_KNIL_marines: "Korps Komando Marinir"
 INS_KNIL_marines_desc: "Training elite amphibious assault commandos capable of rapid island-hopping and coastal defense across the Indonesian archipelago."
 INS_the_flying_dutchmen: "Resimen Pasukan Payung Nusantara"
 INS_the_flying_dutchmen_desc: "Establishing an elite paratrooper regiment to deploy swiftly across distant islands and mountain strongholds."
 INS_ambonese_auxilaries: "Resimen Milisi Daerah Nusantara"
 INS_ambonese_auxilaries_desc: "Mobilizing disciplined local auxiliary regiments from across the archipelago to fortify territorial defense."
 INS_reform_the_knil: "Konsolidasi Komando Wilayah"
 INS_reform_the_knil_desc: "Restructuring regional military commands into unified fighting forces under central operational leadership."
 INS_koninklijk_paketvaart_maatschappij: "Pelayaran Nasional Indonesia (PELNI)"
 INS_koninklijk_paketvaart_maatschappij_desc: "Consolidating state-directed merchant shipping networks to guarantee domestic maritime supply routes."
 INS_the_royal_batavian_society: "Lembaga Ilmu Pengetahuan & Riset"
 INS_the_royal_batavian_society_desc: "Fostering indigenous scientific research, mapping geological wealth, and expanding technological academies."
 INS_royal_scientific_cooperation: "Kerjasama Riset & Teknologi"
 INS_royal_scientific_cooperation_desc: "Establishing international research exchanges to advance domestic radio communications, radar, and heavy industries."
'''

# Append before the end if not already present
if 'INS_koninklijk_nederlands_indisch_leger:' not in content:
    content = content.rstrip() + '\n' + r56_override_keys.lstrip()

with open(loc_file, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + content.encode('utf-8'))

print("Updated localisation with R56 overrides and confirmed UTF-8 BOM!")
