with open(r'localisation\english\DEI_indonesia_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

start_idx = None
end_idx = None
for i, l in enumerate(lines):
    if 'dei_trunk.1.t:' in l:
        start_idx = i
    if 'dei_trunk.603.d:' in l:
        end_idx = i + 1

print('Found range:', start_idx, end_idx)

new_lines = [
    ' dei_trunk.1.t: "The 1936 General Strike Wave"\n',
    ' dei_trunk.1.d: "Spurred by years of severe economic depression and plummeting wages, dockers at Tanjung Priok and Tanjung Perak have laid down their tools, joined by railway engineers across the entire Staatsspoorwegen network. Transport and commerce throughout Java have ground to a sudden, screeching halt.\\n\\nAs defiant crowds flood the public squares from Batavia to Surabaya, municipal police find themselves hopelessly outnumbered. Colonial factories stand silent, and telegraph wires buzz frantically with appeals from panicked plantation owners demanding armed intervention."\n',
    ' dei_trunk.1.a: "Deploy field constabulary and police batons"\n',
    ' dei_trunk.1.b: "Offer a Volksraad wage commission inquiry"\n',
    '\n',
    ' dei_trunk.2.t: "Mutiny in the KNIL Barracks"\n',
    ' dei_trunk.2.d: "In the highland garrisons of Cimahi and Magelang, native KNIL soldiers have openly broken discipline. Refusing orders to march against striking civilian workers, indigenous sergeants and riflemen have detained their Dutch officers and thrown open the heavy gates of the colonial armories.\\n\\nThousands of modern Mannlicher rifles, machine guns, and crates of ammunition are rapidly distributed into the eager hands of underground youth militias. Across Java, what began as civil disobedience has swiftly transformed into an armed and organized popular uprising."\n',
    ' dei_trunk.2.a: "Distribute armaments to the fledgling Laskar Rakyat"\n',
    ' dei_trunk.2.b: "Coordinate with youth leagues to secure ammunition depots"\n',
    '\n',
    ' dei_trunk.3.t: "Political Crisis in Batavia"\n',
    ' dei_trunk.3.d: "The colonial seat of government in Batavia has plunged into total chaos. Draconian decrees and curfew orders issued by the Governor-General are openly torn down and mocked in the streets, as indigenous civil servants and postal clerks walk out in sweeping solidarity.\\n\\nInside the Volksraad, Indonesian delegates denounce colonial rule and walk out en masse, declaring the colonial constitution defunct. With administrative authority evaporating hour by hour, the colonial state possesses no remaining moral authority to govern the archipelago."\n',
    ' dei_trunk.3.a: "The moral authority of the colonial state has collapsed"\n',
    '\n',
    ' dei_trunk.4.t: "Consolidation of Underground Resistance"\n',
    ' dei_trunk.4.d: "Meeting in clandestine safehouses throughout Bandung, Yogyakarta, and Surakarta, prominent nationalist leaders, veteran dissidents, and labor commanders have forged an emergency united front to coordinate the uprising. Disparate regional militias and student leagues are unified under a central revolutionary council.\\n\\nCouriers on steam trains and motorbikes crisscross the countryside, establishing secure communications and supply lines. The disparate factions of the independence movement have buried their tactical differences, recognizing that this historic opportunity will never come again."\n',
    ' dei_trunk.4.a: "Prepare the proclamation of national sovereignty"\n',
    '\n',
    ' dei_trunk.5.t: "Threshold of National Revolution"\n',
    ' dei_trunk.5.d: "Across the archipelago, the final vestiges of Dutch control are dissolving. Clandestine radio stations in Bandung and Surabaya overpower colonial airwaves, broadcasting revolutionary marches and fiery appeals that echo across the mountains and straits of Nusantara.\\n\\nRed-and-white banners unfurl defiantly over government buildings, postal offices, and railway terminals. As revolutionary vanguards assemble in city squares under torchlight, the decisive hour has arrived to proclaim the birth of a sovereign nation."\n',
    ' dei_trunk.5.a: "The decisive hour has struck for all of Nusantara!"\n',
    '\n',
    ' dei_trunk.6.t: "The 1936 Indonesian National Revolution"\n',
    ' dei_trunk.6.d: "Across the bustling port cities and interior highlands of Java and Sumatra, the general strike wave has paralyzed the colonial apparatus. Docks at Tanjung Priok and Tanjung Perak stand silent, railways have ceased operations, and municipal administrative offices have been emptied as civil servants walk out in sweeping defiance.\\n\\nIn the military garrisons of Cimahi and Magelang, native KNIL soldiers have refused orders to suppress the strikes, detaining colonial officers and opening the armories to revolutionary youth leagues. What began as labor resistance has escalated into a nationwide, coordinated uprising across the entire archipelago.\\n\\nFrom clandestine radio stations in Bandung and Yogyakarta, the momentous Proclamation of Independence is broadcast to the world. As the red-and-white banner unfurls over public squares from Sabang to Merauke, the colonial authority of the Dutch East Indies has collapsed, ushering Nusantara into an unprecedented new era."\n',
    ' dei_trunk.6.a: "Merdeka! The destiny of Nusantara is in our hands."\n',
    ' dei_trunk.6.world: "A momentous revolution in Southeast Asia."\n',
]

lines[start_idx:end_idx] = new_lines

full_text = ''.join(lines)
# Save as UTF-8 with BOM
raw = b'\xef\xbb\xbf' + full_text.encode('utf-8')
with open(r'localisation\english\DEI_indonesia_l_english.yml', 'wb') as f:
    f.write(raw)

print('Updated localization file successfully with UTF-8 BOM!')
