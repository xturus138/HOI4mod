import os

loc_file = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml'

with open(loc_file, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Replace focus section
old_focus_sec = ''' #### FOCUS TREE: Shared Trunk ####
 dei_focus_root: "The Dutch East Indies at the Crossroads"
 dei_focus_root_desc: "The year is 1936. The Great Depression still casts its long shadow, while nationalist voices grow bolder within the Volksraad. The colonial administration must chart its course."
 dei_focus_volksraad: "Empower the Volksraad"
 dei_focus_volksraad_desc: "Granting the Volksraad (People's Council) genuine legislative authority, rather than serving as a mere symbolic advisory body."
 dei_focus_econ_liberal: "Economic Liberalization"
 dei_focus_econ_liberal_desc: "Opening key sectors of the Indies economy to indigenous entrepreneurs and foreign investment beyond the Netherlands."
 dei_focus_econ_conservative: "Maintain Colonial Monopolies"
 dei_focus_econ_conservative_desc: "Upholding modern plantation concessions and state trade monopolies to ensure maximum revenue flows to the Dutch Crown."
 dei_focus_native_education: "Expand Native Education"
 dei_focus_native_education_desc: "Establishing new public schools for the native population — inadvertently sowing the seeds of modern national consciousness."
 dei_focus_nationalist_watch: "Address the Nationalist Movement"
 dei_focus_nationalist_watch_desc: "Prominent leaders like Mohammad Hoesni Thamrin speak with growing fervor in the Volksraad. How shall the administration respond?"
 dei_focus_knil_reform: "Reform the KNIL"
 dei_focus_knil_reform_desc: "Modernizing the Koninklijk Nederlandsch-Indisch Leger (KNIL) to prepare for gathering storm clouds across the Pacific."
 dei_focus_defense_plan: "Indies Defense Plan"
 dei_focus_defense_plan_desc: "Formulating a comprehensive territorial defense strategy for an immense and fragmented archipelago."
 dei_focus_foreign_support: "Seek Foreign Backing"
 dei_focus_foreign_support_desc: "Approaching the United States and the British Empire for diplomatic recognition, arms shipments, and naval support."
 dei_focus_japan_threat: "Waspada Ancaman Jepang"
 dei_focus_japan_threat_desc: "Japanese expansionism in East Asia accelerates. The East Indies, rich in vital oil and rubber, is their prime southern target."
 dei_focus_momentum_kemerdekaan: "Momentum Kemerdekaan"
 dei_focus_momentum_kemerdekaan_desc: "History reaches its decisive turning point. What path shall the peoples of Nusantara forge from here?"'''

new_focus_sec = ''' #### FOCUS TREE: Shared Trunk - Prolog Revolusi 1936 ####
 dei_focus_root: "Retaknya Pax Neerlandica"
 dei_focus_root_desc: "The devastating toll of the Great Depression has shattered the export economy of the East Indies. Mass layoffs and wage cuts among railroad and harbor workers ignite an explosive wave of general strikes across Java."
 dei_focus_pembangkangan: "Pembangkangan Militer & Rakyat"
 dei_focus_pembangkangan_desc: "The mutinous spirit of the cruiser De Zeven Provinciën echoes into native KNIL garrisons in Cimahi and Magelang. Soldiers refuse orders to fire upon striking workers, distributing rifles and ammunition to underground youth leagues."
 dei_focus_momentum_kemerdekaan: "Momentum Revolusi Nasional 1936"
 dei_focus_momentum_kemerdekaan_desc: "With colonial communications paralyzed, garrisons in revolt, and the red-and-white flag raised over public squares, the hour of national destiny has arrived. What ideological banner shall guide the revolution?"'''

assert old_focus_sec in content, "old_focus_sec not found"
content = content.replace(old_focus_sec, new_focus_sec)

# Replace events section
old_events_sec = ''' #### EVENTS: Shared Trunk ####
 dei_trunk.1.t: "The Dutch East Indies Enters a New Era"
 dei_trunk.1.d: "The colonial administration reasserts its authority over the immense archipelago, as mounting international rivalries cast a shadow over Asia."
 dei_trunk.1.a: "Proceed"

 dei_trunk.2.t: "New Schools, New Ideas"
 dei_trunk.2.d: "Graduates of vernacular and colonial schools read newspapers and debate the future of their people. Conservative officials warn that broad education nurtures dangerous nationalist sentiment."
 dei_trunk.2.a: "Allow native education to expand freely"
 dei_trunk.2.b: "Restrict curricula deemed subversive"

 dei_trunk.3.t: "Voices in the Volksraad"
 dei_trunk.3.d: "Nationalist delegates speak with increasing defiance, demanding meaningful home rule. The administration must decide: accommodate reformist demands or tighten control."
 dei_trunk.3.a: "Repress radical agitators"
 dei_trunk.3.b: "Open room for dialogue and reform"

 dei_trunk.4.t: "Reforming the KNIL"
 dei_trunk.4.d: "The Koninklijk Nederlandsch-Indisch Leger requires extensive modernization and expanded native recruitment if it is to defend these far-flung islands."
 dei_trunk.4.a: "Modernize equipment and expand local recruitment"
 dei_trunk.4.b: "Rely primarily on traditional European officer corps"

 dei_trunk.5.t: "The Rising Sun in the South"
 dei_trunk.5.d: "Imperial Japan's advance into China and French Indochina signals an imminent threat to the oil fields of Sumatra and Borneo. The Indies must stand ready."
 dei_trunk.5.a: "Prepare total archipelago defense"

 dei_trunk.6.t: "Momentum Kemerdekaan: A Crossroads of History"
 dei_trunk.6.d: "The old colonial equilibrium has shattered. In the crucible of global war and rising national awakening, the destiny of Nusantara hangs in the balance. What path will we forge?"
 dei_trunk.6.a: "Path A: Democratic-Nationalist Republic (Sukarno)"
 dei_trunk.6.b: "Path B: Colonial / Federalist Commonwealth (Van Mook)"
 dei_trunk.6.c: "Path C: Communist People's Vanguard (Musso)"
 dei_trunk.6.d: "Path D: Authoritarian Military Regime (Soedirman)"
 dei_trunk.6.e: "Path E: Islamic State of Indonesia (Kartosoewirjo)"
 dei_trunk.6.f: "Path F: Imperial Resurgence of Majapahit (Wuryaningrat)"

 #### EVENTS: Revolusi Dini ####
 dei_revolusi_dini.1.t: "Gelora Revolusi Dini"
 dei_revolusi_dini.1.d: "[OPTIONAL / AHISTORICAL] Rejecting the slow pace of colonial reform, patriotic factions take up arms years ahead of schedule. The colonial administration collapses into nationwide revolt."
 dei_revolusi_dini.1.a: "Advance immediately to ideological alignment"'''

new_events_sec = ''' #### EVENTS: Shared Trunk - Prolog Revolusi 1936 ####
 dei_trunk.1.t: "Gelombang Pemogokan Umum 1936"
 dei_trunk.1.d: "Spurred by catastrophic economic ruin, dockers at Tanjung Priok and Tanjung Perak join railway workers in an unprecedented coordinated strike. The colonial apparatus is paralyzed as defiant crowds flood the public squares."
 dei_trunk.1.a: "Deploy field constabulary and police batons"
 dei_trunk.1.b: "Offer a Volksraad wage commission inquiry"

 dei_trunk.2.t: "Pembangkangan di Barak KNIL"
 dei_trunk.2.d: "Indigenous soldiers in Cimahi and Magelang refuse orders to suppress the strikes. Officers are detained, armories breached, and thousands of rifles distributed to underground youth militias."
 dei_trunk.2.a: "Distribute armaments to the fledgling Laskar Rakyat"
 dei_trunk.2.b: "Coordinate with youth leagues to secure ammunition depots"

 dei_trunk.3.t: "Krisis Politik Batavia"
 dei_trunk.3.d: "Repressive decrees issued by the Governor-General in Batavia are ignored by the populace. The colonial civil service dissolves as indigenous staff walk out in open solidarity with the movement."
 dei_trunk.3.a: "The moral authority of the colonial state has collapsed"

 dei_trunk.4.t: "Konsolidasi Komite Perjuangan Bawah Tanah"
 dei_trunk.4.d: "Patriotic leaders, veteran dissidents, and labor organizers convene secretly across Java and Sumatra, unifying disparate militias and youth leagues under a single revolutionary command."
 dei_trunk.4.a: "Prepare the proclamation of national sovereignty"

 dei_trunk.5.t: "Ambang Revolusi Nasional"
 dei_trunk.5.d: "Radio stations in Bandung and Surabaya broadcast patriotic marches. Dutch administrative garrisons are cut off as red-and-white banners unfurl across city halls and village squares."
 dei_trunk.5.a: "The decisive hour has struck for all of Nusantara!"

 dei_trunk.6.t: "Momentum Kemerdekaan: Proklamasi Revolusi Nasional 1936"
 dei_trunk.6.d: "The old colonial order has fallen. Across the immense archipelago, millions stand vigilant. As emergency units assemble and warships raise new ensigns, what ideological path shall guide the destiny of Indonesia?"
 dei_trunk.6.a: "Path A: Democratic-Nationalist Republic (Sukarno)"
 dei_trunk.6.b: "Path B: Colonial / Federalist Commonwealth (Van Mook)"
 dei_trunk.6.c: "Path C: Communist People's Vanguard (Musso)"
 dei_trunk.6.d: "Path D: Authoritarian Military Regime (Soedirman)"
 dei_trunk.6.e: "Path E: Islamic State of Indonesia (Kartosoewirjo)"
 dei_trunk.6.f: "Path F: Imperial Resurgence of Majapahit (Wuryaningrat)"'''

assert old_events_sec in content, "old_events_sec not found"
content = content.replace(old_events_sec, new_events_sec)

with open(loc_file, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + content.encode('utf-8'))

print("Updated localisation successfully with UTF-8 BOM!")
