import codecs

path = 'localisation/english/DEI_indonesia_l_english.yml'

with open(path, 'rb') as f:
    raw = f.read()

assert raw.startswith(codecs.BOM_UTF8), "Missing BOM!"
text = raw.decode('utf-8-sig')

new_loc = '''
 # =====================================================================
 # LIBERATION OF OUTER ISLANDS DECISIONS
 # =====================================================================
 dei_decision_liberate_sumatra: "Ekspedisi Pembebasan Sumatera"
 dei_decision_liberate_sumatra_desc: "Launch revolutionary infiltrations across the Sunda Strait to rally local youth leagues and liberate Palembang, Padang, Medan, and Aceh from colonial garrisons."

 dei_decision_liberate_kalimantan: "Ekspedisi Gerilya Rimba Kalimantan"
 dei_decision_liberate_kalimantan_desc: "Organize Dayak tribes and coastal labor unions into active insurgent vanguards, seizing Banjarmasin and Pontianak."

 dei_decision_liberate_east_indies: "Operasi Lintas Laut Sulawesi & Kepulauan Timur"
 dei_decision_liberate_east_indies_desc: "Mobilize Bugis pinisi fleets and maritime commandos to secure the Makassar Strait, liberating Sulawesi, Maluku, and the Lesser Sunda Islands."

 dei_decision_liberate_papua: "Operasi Pembebasan Papua Barat"
 dei_decision_liberate_papua_desc: "Deploy airborne vanguards and naval infiltrators to establish sovereign control over Hollandia and Merauke."

 dei_debug_liberate_all_islands: "🚀 [DEBUG] Instantly Liberate All Outer Islands"
 dei_debug_liberate_all_islands_desc: "Developer cheat to instantly transfer all 16 outer island states to Indonesia for full-map testing."
'''

if 'dei_decision_liberate_sumatra:' not in text:
    text += new_loc
    new_raw = codecs.BOM_UTF8 + text.encode('utf-8')
    with open(path, 'wb') as f:
        f.write(new_raw)
    print('Added liberation localization keys successfully!')
else:
    print('Liberation keys already present!')
