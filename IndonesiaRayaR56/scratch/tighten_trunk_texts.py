import codecs

path = 'localisation/english/DEI_indonesia_l_english.yml'

with open(path, 'rb') as f:
    raw = f.read()

assert raw.startswith(codecs.BOM_UTF8), "Missing BOM!"
text = raw.decode('utf-8-sig')

# Tightened descriptions for dei_trunk 1-6 (perfect fit in EventWindow_News)
replacements = {
    'dei_trunk.1.d': 'Spurred by severe economic depression and plummeting wages, dockers at Tanjung Priok and Tanjung Perak have laid down tools, joined by Staatsspoorwegen railway crews. Transport across Java has ground to a sudden halt.\\n\\nDefiant crowds flood public squares from Batavia to Surabaya, hopelessly outnumbering municipal police. Colonial factories stand silent as panic spreads across the archipelago.',
    'dei_trunk.2.d': 'In the highland garrisons of Cimahi and Magelang, native KNIL soldiers have openly broken discipline. Refusing orders to march against civilian strikers, indigenous troops have detained colonial officers and thrown open the armories.\\n\\nThousands of rifles, machine guns, and ammunition crates are distributed to youth militias, transforming civil disobedience into an organized armed uprising.',
    'dei_trunk.3.d': 'Colonial administration in Batavia has plunged into total chaos. Emergency decrees from the Governor-General are torn down in the streets as civil servants walk out in sweeping solidarity.\\n\\nInside the Volksraad, Indonesian delegates walk out en masse, declaring the colonial constitution defunct as colonial moral authority entirely evaporates.',
    'dei_trunk.4.d': 'Meeting in clandestine safehouses in Bandung, Yogyakarta, and Surakarta, nationalist leaders and labor commanders have forged an emergency united front to coordinate the uprising under a central revolutionary council.\\n\\nCouriers on steam trains and motorbikes crisscross the island, securing communications and uniting all factions for this historic opportunity.',
    'dei_trunk.5.d': 'The final vestiges of Dutch colonial authority are dissolving. Clandestine radio stations overpower colonial airwaves, broadcasting revolutionary marches across the straits of Nusantara.\\n\\nSang Saka Merah-Putih unfurls over government buildings and railway terminals as revolutionary vanguards assemble to proclaim the birth of a sovereign nation.',
    'dei_trunk.6.d': 'Across Java and Sumatra, the general strike wave has paralyzed the colonial apparatus. Docks and railways stand silent as civil servants and native KNIL soldiers join the national defiance.\\n\\nFrom clandestine radio stations in Bandung and Yogyakarta, the Proclamation of Independence is broadcast to the world. As the Merah-Putih unfurls from Sabang to Merauke, colonial rule has collapsed, ushering Nusantara into a sovereign new era.'
}

for k, v in replacements.items():
    import re
    pat = re.compile(rf'({re.escape(k)}:\s*")[^"]*(")')
    match = pat.search(text)
    if match:
        text = text[:match.start(1)] + f'{k}: "{v}"' + text[match.end(2):]
        print(f'Replaced {k}')
    else:
        print(f'Pattern for {k} not found!')

new_raw = codecs.BOM_UTF8 + text.encode('utf-8')
with open(path, 'wb') as f:
    f.write(new_raw)

print('Updated all dei_trunk 1-6 descriptions with clean concise lengths and UTF-8 BOM!')
