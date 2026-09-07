# Script to update dei_trunk localization cleanly with UTF-8 BOM
with open(r'localisation\english\DEI_indonesia_l_english.yml', 'r', encoding='utf-8-sig') as f:
    text = f.read()

old_block = ''' dei_trunk.1.t: "The 1936 General Strike Wave"
 dei_trunk.1.d: "Spurred by catastrophic economic ruin, dockers at Tanjung Priok and Tanjung Perak join railway workers in an unprecedented coordinated strike. The colonial apparatus is paralyzed as defiant crowds flood the public squares."
 dei_trunk.1.a: "Deploy field constabulary and police batons"
 dei_trunk.1.b: "Offer a Volksraad wage commission inquiry"

 dei_trunk.2.t: "Mutiny in the KNIL Barracks"
 dei_trunk.2.d: "Indigenous soldiers in Cimahi and Magelang refuse orders to suppress the strikes. Officers are detained, armories breached, and thousands of rifles distributed to underground youth militias."
 dei_trunk.2.a: "Distribute armaments to the fledgling Laskar Rakyat"
 dei_trunk.2.b: "Coordinate with youth leagues to secure ammunition depots"

 dei_trunk.3.t: "Political Crisis in Batavia"
 dei_trunk.3.d: "Repressive decrees issued by the Governor-General in Batavia are ignored by the populace. The colonial civil service dissolves as indigenous staff walk out in open solidarity with the movement."
 dei_trunk.3.a: "The moral authority of the colonial state has collapsed"

 dei_trunk.4.t: "Consolidation of Underground Resistance"
 dei_trunk.4.d: "Patriotic leaders, veteran dissidents, and labor organizers convene secretly across Java and Sumatra, unifying disparate militias and youth leagues under a single revolutionary command."
 dei_trunk.4.a: "Prepare the proclamation of national sovereignty"

 dei_trunk.5.t: "Threshold of National Revolution"
 dei_trunk.5.d: "Radio stations in Bandung and Surabaya broadcast patriotic marches. Dutch administrative garrisons are cut off as red-and-white banners unfurl across city halls and village squares."
 dei_trunk.5.a: "The decisive hour has struck for all of Nusantara!"

 dei_trunk.6.t: "Momentum of Independence: The 1936 National Revolution"
 dei_trunk.6.d: "The decisive hour of national revolution has struck. Across Batavia, Bandung, and Surabaya, general strikes have brought colonial transportation and commerce to a standstill. In military garrisons, native KNIL soldiers have mutinied, joining arm-in-arm with revolutionary youth to open the armories.\\n\\nFrom the shortwave transmitters of Andir and Maguwo, bold broadcasts proclaim the dawn of a sovereign Indonesia to a stunned world. The colonial authority of the Dutch East Indies has collapsed, creating a historical vacuum across the archipelago. In this fateful moment, three distinct ideological currents vie to guide the destiny of our nation. Which path shall we take?"
 dei_trunk.6.opt_republic: "The Republican & Constitutional Paths (Democratic or Federalist)"
 dei_trunk.6.opt_radical: "The Revolutionary & Military Paths (Communist or Military Junta)"
 dei_trunk.6.opt_traditional: "The Faith & Imperial Heritage Paths (Islamic State or Majapahit Empire)"
 dei_trunk.6.back: "Return to consider other ideological paths"
 dei_trunk.6.a: "Path A: Democratic-Nationalist Republic (Sukarno)"
 dei_trunk.6.b: "Path B: Colonial / Federalist Commonwealth (Van Mook)"
 dei_trunk.6.c: "Path C: Communist People's Vanguard (Musso)"
 dei_trunk.6.d: "Path D: Authoritarian Military Regime (Soedirman)"
 dei_trunk.6.e: "Path E: Islamic State of Indonesia (Kartosoewirjo)"
 dei_trunk.6.f: "Path F: Imperial Resurgence of Majapahit (Wuryaningrat)"

 dei_trunk.601.t: "The Destiny of the Nation: Republic or Commonwealth"
 dei_trunk.601.d: "With the colonial administrative machinery paralyzed, two distinct visions emerge to secure our sovereignty: Sukarno and Hatta's vision of an independent, democratic republic standing proudly on its own feet, or Hubertus van Mook's vision of an autonomous federal commonwealth that preserves stability, commerce, and international ties. Which direction shall we embrace?"

 dei_trunk.602.t: "The Destiny of the Nation: Vanguard or Military Rule"
 dei_trunk.602.d: "The old order has fallen, but foreign imperialists and internal enemies threaten to extinguish the revolution. To safeguard our independence, shall we mobilize the workers and peasants into a socialist vanguard state under Musso, or place executive command under a patriotic Military Revolutionary Council led by General Soedirman?"

 dei_trunk.603.t: "The Destiny of the Nation: Faith or Empire"
 dei_trunk.603.d: "Rejecting secular modernity and colonial compromises, deep spiritual currents surge across the islands. Shall we establish an Islamic State guided by the Ulama and Sharia law under Kartosoewirjo, or awaken the ancient majesty of the Kemaharajaan Majapahit to fulfill the sacred Sumpah Palapa?"'''

new_block = ''' dei_trunk.1.t: "The 1936 General Strike Wave"
 dei_trunk.1.d: "Spurred by years of severe economic depression and plummeting wages, dockers at Tanjung Priok and Tanjung Perak have laid down their tools, joined by railway engineers across the entire Staatsspoorwegen network. Transport and commerce throughout Java have ground to a sudden, screeching halt.\\n\\nAs defiant crowds flood the public squares from Batavia to Surabaya, municipal police find themselves hopelessly outnumbered. Colonial factories stand silent, and telegraph wires buzz frantically with appeals from panicked plantation owners demanding armed intervention."
 dei_trunk.1.a: "Deploy field constabulary and police batons"
 dei_trunk.1.b: "Offer a Volksraad wage commission inquiry"

 dei_trunk.2.t: "Mutiny in the KNIL Barracks"
 dei_trunk.2.d: "In the highland garrisons of Cimahi and Magelang, native KNIL soldiers have openly broken discipline. Refusing orders to march against striking civilian workers, indigenous sergeants and riflemen have detained their Dutch officers and thrown open the heavy gates of the colonial armories.\\n\\nThousands of modern Mannlicher rifles, machine guns, and crates of ammunition are rapidly distributed into the eager hands of underground youth militias. Across Java, what began as civil disobedience has swiftly transformed into an armed and organized popular uprising."
 dei_trunk.2.a: "Distribute armaments to the fledgling Laskar Rakyat"
 dei_trunk.2.b: "Coordinate with youth leagues to secure ammunition depots"

 dei_trunk.3.t: "Political Crisis in Batavia"
 dei_trunk.3.d: "The colonial seat of government in Batavia has plunged into total chaos. Draconian decrees and curfew orders issued by the Governor-General are openly torn down and mocked in the streets, as indigenous civil servants and postal clerks walk out in sweeping solidarity.\\n\\nInside the Volksraad, Indonesian delegates denounce colonial rule and walk out en masse, declaring the colonial constitution defunct. With administrative authority evaporating hour by hour, the colonial state possesses no remaining moral authority to govern the archipelago."
 dei_trunk.3.a: "The moral authority of the colonial state has collapsed"

 dei_trunk.4.t: "Consolidation of Underground Resistance"
 dei_trunk.4.d: "Meeting in clandestine safehouses throughout Bandung, Yogyakarta, and Surakarta, prominent nationalist leaders, veteran dissidents, and labor commanders have forged an emergency united front to coordinate the uprising. Disparate regional militias and student leagues are unified under a central revolutionary council.\\n\\nCouriers on steam trains and motorbikes crisscross the countryside, establishing secure communications and supply lines. The disparate factions of the independence movement have buried their tactical differences, recognizing that this historic opportunity will never come again."
 dei_trunk.4.a: "Prepare the proclamation of national sovereignty"

 dei_trunk.5.t: "Threshold of National Revolution"
 dei_trunk.5.d: "Across the archipelago, the final vestiges of Dutch control are dissolving. Clandestine radio stations in Bandung and Surabaya overpower colonial airwaves, broadcasting revolutionary marches and fiery appeals that echo across the mountains and straits of Nusantara.\\n\\nRed-and-white banners unfurl defiantly over government buildings, postal offices, and railway terminals. As revolutionary vanguards assemble in city squares under torchlight, the decisive hour has arrived to proclaim the birth of a sovereign nation."
 dei_trunk.5.a: "The decisive hour has struck for all of Nusantara!"

 dei_trunk.6.t: "The 1936 Indonesian National Revolution"
 dei_trunk.6.d: "Across the bustling port cities and interior highlands of Java and Sumatra, the general strike wave has paralyzed the colonial apparatus. Docks at Tanjung Priok and Tanjung Perak stand silent, railways have ceased operations, and municipal administrative offices have been emptied as civil servants walk out in sweeping defiance.\\n\\nIn the military garrisons of Cimahi and Magelang, native KNIL soldiers have refused orders to suppress the strikes, detaining colonial officers and opening the armories to revolutionary youth leagues. What began as labor resistance has escalated into a nationwide, coordinated uprising across the entire archipelago.\\n\\nFrom clandestine radio stations in Bandung and Yogyakarta, the momentous Proclamation of Independence is broadcast to the world. As the red-and-white banner unfurls over public squares from Sabang to Merauke, the colonial authority of the Dutch East Indies has collapsed, ushering Nusantara into an unprecedented new era."
 dei_trunk.6.a: "Merdeka! The destiny of Nusantara is in our hands."
 dei_trunk.6.world: "A momentous revolution in Southeast Asia."'''

assert old_block in text, 'old_block not found in localization file!'
text = text.replace(old_block, new_block)

# Ensure UTF-8 with BOM
raw = b'\xef\xbb\xbf' + text.encode('utf-8')
with open(r'localisation\english\DEI_indonesia_l_english.yml', 'wb') as f:
    f.write(raw)

print('Updated DEI_indonesia_l_english.yml with rich evenly-formatted text & UTF-8 BOM!')
