import os

loc_path = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml'

with open(loc_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

new_loc = '''
 # =====================================================================
 # LEADERSHIP ELECTION CONGRESS EVENTS & UNIQUE TRAITS
 # =====================================================================
 dei_leadership.1.t: "The Grand Congress of the Republic"
 dei_leadership.1.d: "With the proclamation of national independence ringing across the archipelago, revolutionary delegates convene in Yogyakarta. Heated debates erupt over supreme executive authority: the magnetic revolutionary Bung Karno, the sober constitutional economist Bung Hatta, or the sharp democratic socialist Bung Sjahrir."
 dei_leadership.1.a: "Soekarno - President and Great Leader of the Revolution!"
 dei_leadership.1.b: "Mohammad Hatta - Constitutional Architect and Co-operative Pioneer!"
 dei_leadership.1.c: "Sutan Sjahrir - Premier Diplomat and Democratic Socialist!"

 dei_leadership.2.t: "The Federal States Conference (BFO)"
 dei_leadership.2.d: "Representatives from the federal states (*Negara Bagian*) and traditional princely realms gather in Batavia under the BFO banner. They must select the supreme head of the federal commonwealth: royal cavalry general Sultan Hamid II of Pontianak, seasoned Dutch colonial reformer Hubertus van Mook, or Balinese nobleman Tjokorda Gde Raka Sukawati."
 dei_leadership.2.a: "Sultan Hamid II - Head of the Federal Regency!"
 dei_leadership.2.b: "Hubertus van Mook - Governor-General and Reformer!"
 dei_leadership.2.c: "Tjokorda Gde Raka Sukawati - President of East Indonesia!"

 dei_leadership.3.t: "The People's Vanguard Congress"
 dei_leadership.3.d: "Under the crimson banners of the Hammer and Sickle, delegates from the PKI, peasant unions, and red militia battalions convene in Madiun. A decisive choice must be made between the orthodox Comintern line of Musso, the radical sovereign mass-action doctrine of Tan Malaka, and the socialist intellectual leadership of Amir Sjarifuddin."
 dei_leadership.3.a: "Musso - General Secretary of the Proletarian Vanguard!"
 dei_leadership.3.b: "Tan Malaka - Supreme Comrade of the Murba Revolution!"
 dei_leadership.3.c: "Amir Sjarifuddin - Chairman of the People's Defense Council!"

 dei_leadership.4.t: "Session of the Supreme Revolutionary Council"
 dei_leadership.4.d: "Officers of the General Staff and commanders of regional garrisons assemble at supreme war headquarters. Amid escalating national peril, the military junta must declare who wields absolute command: revered Panglima Besar Soedirman, doctrinal strategist Abdul Haris Nasution, or stern operational commander Soeharto."
 dei_leadership.4.a: "Soedirman - Panglima Besar and Commander-in-Chief!"
 dei_leadership.4.b: "Abdul Haris Nasution - Chairman of the Military Presidium!"
 dei_leadership.4.c: "Soeharto - Supreme Commander of National Security!"

 dei_leadership.5.t: "The Grand Majelis Syura of the Islamic Ummah"
 dei_leadership.5.d: "Eminent ulama, mujahidin commanders, and Islamic scholars assemble in Tasikmalaya to establish an Islamic polity (*Daulah Islamiyah*). Delegates deliberate over supreme leadership: unyielding Imam Sekarmaji Marijan Kartosuwiryo, visionary democratic statesman Mohammad Natsir, or esteemed traditionalist cleric K.H. Wahid Hasyim."
 dei_leadership.5.a: "S.M. Kartosuwiryo - Imam of Darul Islam and Commander of TII!"
 dei_leadership.5.b: "Mohammad Natsir - Prime Minister and Masyumi Statesman!"
 dei_leadership.5.c: "K.H. Wahid Hasyim - Rais Aam of the National Ulama!"

 dei_leadership.6.t: "Pisowanan Agung di Keraton Trowulan"
 dei_leadership.6.d: "Amid fragrant sandalwood incense and the echoing chimes of heirloom gamelan, hereditary princes, royal courtiers, and Dharmaputra knights assemble at the restored sanctuary of Trowulan. They seek to anoint the supreme ruler of Nusantara: consecrated descendant Sri Maharaja Suryawikrama, revered reformist monarch Sri Sultan Hamengkubuwono IX, or senior aristocratic regent K.R.M.T. Wuryaningrat."
 dei_leadership.6.a: "Sri Maharaja Suryawikrama - Divine Sovereign of Wilwatikta!"
 dei_leadership.6.b: "Sri Sultan Hamengkubuwono IX - King of Mataram and Sovereign of Nusantara!"
 dei_leadership.6.c: "K.R.M.T. Wuryaningrat - Grand Regent of the Imperial Court!"

 dei_syahrir_diplomacy_bonus: "Sjahrir Diplomatic Academy"

 # Unique Country Leader Traits
 trait_dei_sukarno: "Bung Karno - Penyambung Lidah Rakyat"
 trait_dei_sukarno_desc: "A fiery and magnetic orator whose revolutionary speeches unite disparate archipelago peoples into an unstoppable anti-imperialist movement."
 trait_dei_hatta: "Bung Hatta - Bapak Koperasi & Rasionalis"
 trait_dei_hatta_desc: "A meticulous economist and statesman dedicated to cooperative economic theory, fiscal stability, and constitutional democracy."
 trait_dei_syahrir: "Bung Sjahrir - Diplomat Ulung"
 trait_dei_syahrir_desc: "An internationally respected democratic socialist and sharp intellectual capable of navigating delicate geopolitical negotiations."

 trait_dei_van_mook: "Arsitek Federasi Hindia"
 trait_dei_van_mook_desc: "A seasoned colonial administrator focused on progressive technocratic governance, modern enterprise, and regional decentralization."
 trait_dei_sultan_hamid: "Sultan Pontianak & Jenderal Federal"
 trait_dei_sultan_hamid_desc: "Royal monarch of Pontianak and KNIL major-general, skilled at balancing regional aristocratic autonomy with modern armed force."
 trait_dei_sukawati: "Presiden Indonesia Timur"
 trait_dei_sukawati_desc: "A high-ranking Balinese aristocrat with deep connections across the maritime east, prioritizing inter-island trade and local sovereignty."

 trait_dei_musso: "Kader Komintern Moskow"
 trait_dei_musso_desc: "A veteran of the Moscow International, championing unbending class struggle, rapid war industrialization, and proletarian mobilization."
 trait_dei_tan_malaka: "Bapak Republik & Gerilya Murba"
 trait_dei_tan_malaka_desc: "Legendary revolutionary and author of Madilog, preaching total popular mass-action (*Aksi Massa*) and unwavering anti-colonial guerrilla warfare."
 trait_dei_amir_sjarifuddin: "Intelektual Marxis & Sayap Kiri"
 trait_dei_amir_sjarifuddin_desc: "A passionate anti-fascist resistance leader and defense organizer skilled at rallying urban labor unions and socialist cadres."

 trait_dei_sudirman_leader: "Panglima Besar Revolusi"
 trait_dei_sudirman_leader_desc: "The revered commander-in-chief whose indomitable spirit and personal moral authority inspire devotion among soldiers and guerrillas."
 trait_dei_nasution_leader: "Konseptor Sishanrata"
 trait_dei_nasution_leader_desc: "The mastermind of total territorial defense and modern staff organization, subordinating civil administration to strategic military planning."
 trait_dei_soeharto_leader: "Jenderal Pembangunan & Ketertiban"
 trait_dei_soeharto_leader_desc: "A stern pragmatist focused on ruthless anti-subversion measures, iron law and order, and rapid infrastructural development."

 trait_dei_kartosuwiryo: "Imam Darul Islam / TII"
 trait_dei_kartosuwiryo_desc: "Charismatic religious leader who proclaimed the Islamic State of Indonesia, mobilizing fanatical mujahidin under the banner of jihad."
 trait_dei_natsir: "Negarawan Masyumi & Pelopor Mosi Integral"
 trait_dei_natsir_desc: "Visionary Islamic intellectual and parliamentarian whose integrity fosters national cohesion and robust ethical institutions."
 trait_dei_wahid_hasyim: "Tokoh Ulama Nahdlatul Ulama"
 trait_dei_wahid_hasyim_desc: "Distinguished traditionalist scholar bridging religious education with modern statecraft, ensuring societal balance and harmony."

 trait_dei_maharaja: "Trah Surya Majapahit"
 trait_dei_maharaja_desc: "A sacred emperor wielding the divine Wahyu Keprabon, commanding timeless veneration across the outer Mandala of Nusantara."
 trait_dei_hamengkubuwono: "Sultan Mataram Yogyakarta"
 trait_dei_hamengkubuwono_desc: "A beloved reformist monarch whose moral prestige and commitment to his people guarantee unshakeable public loyalty."
 trait_dei_wuryaningrat: "Sesepuh Bangsawan Surakarta"
 trait_dei_wuryaningrat_desc: "Senior aristocrat and cultural custodian versed in classic Javanese statecraft, patronizing ancient arts and courtly diplomacy."

 # Additional character names
 DEI_sukarno: "Sukarno"
 DEI_hubertus_van_mook: "Hubertus van Mook"
 DEI_sukawati: "Tjokorda Gde Raka Sukawati"
 DEI_musso: "Musso"
 DEI_amir_sjarifuddin: "Amir Sjarifuddin"
 DEI_kartosuwiryo: "Sekarmaji Marijan Kartosuwiryo"
 DEI_wuryaningrat: "K.R.M.T. Wuryaningrat"
 DEI_sudirman: "Soedirman"
'''

content = ''.join(lines) + new_loc
with open(loc_path, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + content.encode('utf-8'))
print('Successfully appended and wrote UTF-8 with BOM!')
