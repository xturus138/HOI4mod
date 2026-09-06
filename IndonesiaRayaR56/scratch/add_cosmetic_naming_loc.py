import os

loc_file = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml'

with open(loc_file, 'r', encoding='utf-8-sig') as f:
    existing_content = f.read()

new_loc_entries = '''
 # =====================================================================
 # TATA KELOLA & PENAMAAN RESMI NEGARA (DECISIONS & COSMETIC TAGS)
 # =====================================================================
 dei_decisions_proclamations: "Tata Kelola & Penamaan Resmi Negara"
 dei_decisions_proclamations_desc: "Sebagai pemegang mandat kepemimpinan bangsa, kita berhak menentukan tata kelola, struktur ketatanegaraan, serta nama proklamasi resmi yang merepresentasikan kedaulatan Indonesia di panggung internasional."

 # Keputusan Proklamasi Jalur A: Republik
 dei_proclaim_nkri: "Proklamasikan Negara Kesatuan Republik Indonesia (NKRI)"
 dei_proclaim_nkri_desc: "Tegakkan bentuk negara kesatuan yang berdaulat dan tidak terbagi, berlandaskan amanat Proklamasi Kemerdekaan 17 Agustus 1945 dan falsafah Pancasila."
 dei_proclaim_ris: "Bentuk Republik Indonesia Serikat (RIS)"
 dei_proclaim_ris_desc: "Adopsi struktur federal yang mengakomodasi kedaulatan negara-negara bagian dan swapraja di seluruh kepulauan Nusantara."
 dei_proclaim_sosialis: "Proklamasikan Republik Sosialis Demokratis Indonesia"
 dei_proclaim_sosialis_desc: "Deklarasikan republik sosialis demokratis yang berorientasi pada kemakmuran rakyat, kepemilikan komunal atas alat produksi, dan koperasi gotong royong."

 # Keputusan Proklamasi Jalur B: Kolonial / Federalis
 dei_proclaim_dei: "Pertahankan Hindia Belanda (Nederlandsch-Indi\\xc3\\xab)"
 dei_proclaim_dei_desc: "Tegakkan kembali kelanjutan administrasi kolonial Hindia Belanda di bawah perlindungan Mahkota Kerajaan Belanda dan Gubernur Jenderal."
 dei_proclaim_bfo: "Deklarasikan Uni Negara-Negara Indonesia (BFO)"
 dei_proclaim_bfo_desc: "Satukan seluruh swapraja dan negara bagian dalam sebuah uni persemakmuran federal yang mandiri, tertib, dan berdaulat."
 dei_proclaim_dominion: "Bentuk Persemakmuran Mahkota Hindia"
 dei_proclaim_dominion_desc: "Integrasikan kepulauan Nusantara sebagai wilayah persemakmuran (Dominion) otonom yang setara di bawah Uni Belanda-Indonesia."

 # Keputusan Proklamasi Jalur C: Komunis
 dei_proclaim_rri: "Proklamasikan Republik Rakyat Indonesia (RRI)"
 dei_proclaim_rri_desc: "Kibarkan panji merah dan tegakkan kekuasaan kaum buruh dan tani, menghapus sisa-sisa feodalisme dan kapitalisme imperialis."
 dei_proclaim_soviet: "Dirikan Uni Republik Sosialis Soviet Indonesia (URSSI)"
 dei_proclaim_soviet_desc: "Transformasikan Indonesia menjadi dewan-dewan soviet proletariat yang tergabung erat dalam persaudaraan revolusi sosialis internasional."
 dei_proclaim_front: "Konsolidasikan Front Demokrasi Rakyat Nusantara"
 dei_proclaim_front_desc: "Satukan seluruh elemen massa revolusioner dan perserikatan buruh dalam kepemimpinan Front Demokrasi Rakyat."

 # Keputusan Proklamasi Jalur D: Otoriter Militer
 dei_proclaim_otoriter_nkri: "Tegakkan Negara Kesatuan Revolusioner Indonesia"
 dei_proclaim_otoriter_nkri_desc: "Kukuhkan kepemimpinan revolusi terpusat di bawah komando baja tentara demi menyelamatkan persatuan tanah air dari anarki."
 dei_proclaim_junta: "Bentuk Komando Markas Besar Revolusi Militer"
 dei_proclaim_junta_desc: "Serahkan seluruh tampuk kekuasaan eksekutif dan legislatif kepada Presidium Dewan Panglima Perang Angkatan Bersenjata."
 dei_proclaim_raya: "Deklarasikan Imperium Militer Indonesia Raya"
 dei_proclaim_raya_desc: "Kobarkan doktrin geopolitik Indonesia Raya dengan supremasi militer terkuat di lingkar samudra Pasifik dan Hindia."

 # Keputusan Proklamasi Jalur E: Islamis / NII
 dei_proclaim_nii: "Proklamasikan Negara Islam Indonesia (NII)"
 dei_proclaim_nii_desc: "Kukuhkan Syariat Islam secara kaffah sebagai hukum dasar tertinggi negara di bawah pimpinan Imam Negara Islam Indonesia."
 dei_proclaim_daulah: "Kukuhkan Daulah Islamiyah Nusantara"
 dei_proclaim_daulah_desc: "Tegakkan kedaulatan daulah Islamiah yang menyatukan seluruh bumi kepulauan Melayu dan Nusantara di bawah naungan kalimat Tauhid."
 dei_proclaim_khilafah: "Dirikan Khilafah Islamiyah Nusantara"
 dei_proclaim_khilafah_desc: "Bangkitkan kembali kemuliaan Khilafah Islamiyah yang mempersatukan umat dari ujung barat Sumatra hingga tanah timur Maluku."

 # Keputusan Proklamasi Jalur F: Majapahit
 dei_proclaim_majapahit_empire: "Nobatkan Kemaharajaan Majapahit"
 dei_proclaim_majapahit_empire_desc: "Kembalikan takhta wangsa Rajasa di Wilwatikta dan hidupkan kembali kejayaan keemasan Nusantara."
 dei_proclaim_surya: "Tegakkan Imperium Surya Wilwatikta"
 dei_proclaim_surya_desc: "Kibarkan bendera Sang Saka Gula Kelapa dan panji Surya Majapahit sebagai simbol kedaulatan abadi kaisar diraja."
 dei_proclaim_nusantara: "Kibarkan Panji Maha-Imperium Nusantara Raya"
 dei_proclaim_nusantara_desc: "Tuntaskan Sumpah Palapa Patih Gadjah Mada dengan menyatukan seluruh dwipantara di bawah naungan takhta suci Kemaharajaan."

 # =====================================================================
 # DYNAMIC COUNTRY NAMES & ADJECTIVES (BASE TAG INS)
 # =====================================================================
 INS_democratic: "Republic of Indonesia"
 INS_democratic_DEF: "the Republic of Indonesia"
 INS_democratic_ADJ: "Indonesian"

 INS_federalist: "Union of Indonesian States"
 INS_federalist_DEF: "the Union of Indonesian States"
 INS_federalist_ADJ: "Indonesian"

 INS_communism: "People's Republic of Indonesia"
 INS_communism_DEF: "the People's Republic of Indonesia"
 INS_communism_ADJ: "Indonesian"

 INS_fascism: "Revolutionary State of Indonesia"
 INS_fascism_DEF: "the Revolutionary State of Indonesia"
 INS_fascism_ADJ: "Indonesian"

 INS_islamist: "Islamic State of Indonesia"
 INS_islamist_DEF: "the Islamic State of Indonesia"
 INS_islamist_ADJ: "Indonesian"

 INS_majapahit: "Majapahit Empire"
 INS_majapahit_DEF: "the Majapahit Empire"
 INS_majapahit_ADJ: "Majapahit"

 INS_neutrality: "Dutch East Indies"
 INS_neutrality_DEF: "the Dutch East Indies"
 INS_neutrality_ADJ: "Indies"

 # Base Parties
 INS_democratic_party: "PNI"
 INS_democratic_party_long: "Partai Nasional Indonesia"
 INS_federalist_party: "BFO"
 INS_federalist_party_long: "Bijeenkomst voor Federaal Overleg"
 INS_communism_party: "PKI"
 INS_communism_party_long: "Partai Komunis Indonesia"
 INS_fascism_party: "Dewan Revolusi"
 INS_fascism_party_long: "Dewan Pimpinan Tertinggi Revolusi"
 INS_islamist_party: "Majelis Syuro NII"
 INS_islamist_party_long: "Dewan Imam & Majelis Syuro NII"
 INS_majapahit_party: "Wilwatikta"
 INS_majapahit_party_long: "Keluarga Diraja & Rakryan Majapahit"
 INS_neutrality_party: "Volksraad"
 INS_neutrality_party_long: "Volksraad van Nederlandsch-Indi\\xc3\\xab"

 # =====================================================================
 # 18 COSMETIC TAGS LOCALISATION (NAMES & PARTIES)
 # =====================================================================
 # Jalur A
 INS_REPUBLIK_NKRI: "Negara Kesatuan Republik Indonesia"
 INS_REPUBLIK_NKRI_DEF: "the Unitary State of the Republic of Indonesia"
 INS_REPUBLIK_NKRI_ADJ: "Indonesian"
 INS_REPUBLIK_NKRI_party: "PNI"
 INS_REPUBLIK_NKRI_party_long: "Partai Nasional Indonesia"

 INS_REPUBLIK_RIS: "Republik Indonesia Serikat"
 INS_REPUBLIK_RIS_DEF: "the United States of Indonesia"
 INS_REPUBLIK_RIS_ADJ: "Indonesian"
 INS_REPUBLIK_RIS_party: "RIS-Koalisi"
 INS_REPUBLIK_RIS_party_long: "Koalisi Federal Republik Indonesia Serikat"

 INS_REPUBLIK_SOSIALIS: "Republik Sosialis Demokratis Indonesia"
 INS_REPUBLIK_SOSIALIS_DEF: "the Democratic Socialist Republic of Indonesia"
 INS_REPUBLIK_SOSIALIS_ADJ: "Indonesian"
 INS_REPUBLIK_SOSIALIS_party: "PSI"
 INS_REPUBLIK_SOSIALIS_party_long: "Partai Sosialis Indonesia"

 # Jalur B
 INS_KOLONIAL_DEI: "Hindia Belanda"
 INS_KOLONIAL_DEI_DEF: "the Dutch East Indies"
 INS_KOLONIAL_DEI_ADJ: "Indies"
 INS_KOLONIAL_DEI_party: "Gouvernement"
 INS_KOLONIAL_DEI_party_long: "Koloniaal Gouvernement van Nederlandsch-Indi\\xc3\\xab"

 INS_KOLONIAL_BFO: "Uni Negara-Negara Indonesia"
 INS_KOLONIAL_BFO_DEF: "the Union of Indonesian States"
 INS_KOLONIAL_BFO_ADJ: "Indonesian"
 INS_KOLONIAL_BFO_party: "BFO"
 INS_KOLONIAL_BFO_party_long: "Bijeenkomst voor Federaal Overleg"

 INS_KOLONIAL_DOMINION: "Persemakmuran Mahkota Hindia"
 INS_KOLONIAL_DOMINION_DEF: "the Commonwealth of the Netherlands Indies"
 INS_KOLONIAL_DOMINION_ADJ: "Indies"
 INS_KOLONIAL_DOMINION_party: "Kroonraad"
 INS_KOLONIAL_DOMINION_party_long: "Raad van State Nederlandsch-Indi\\xc3\\xab"

 # Jalur C
 INS_KOMUNIS_RRI: "Republik Rakyat Indonesia"
 INS_KOMUNIS_RRI_DEF: "the People's Republic of Indonesia"
 INS_KOMUNIS_RRI_ADJ: "Indonesian"
 INS_KOMUNIS_RRI_party: "PKI"
 INS_KOMUNIS_RRI_party_long: "Partai Komunis Indonesia"

 INS_KOMUNIS_SOVIET: "Uni Republik Sosialis Soviet Indonesia"
 INS_KOMUNIS_SOVIET_DEF: "the Union of Indonesian Soviet Socialist Republics"
 INS_KOMUNIS_SOVIET_ADJ: "Soviet Indonesian"
 INS_KOMUNIS_SOVIET_party: "Komintern-PKI"
 INS_KOMUNIS_SOVIET_party_long: "Partai Komunis Indonesia - Seksi Komintern"

 INS_KOMUNIS_FRONT: "Front Demokrasi Rakyat Nusantara"
 INS_KOMUNIS_FRONT_DEF: "the Nusantara People's Democratic Front"
 INS_KOMUNIS_FRONT_ADJ: "Indonesian"
 INS_KOMUNIS_FRONT_party: "FDR"
 INS_KOMUNIS_FRONT_party_long: "Front Demokrasi Rakyat"

 # Jalur D
 INS_OTORITER_NKRI: "Negara Kesatuan Revolusioner Indonesia"
 INS_OTORITER_NKRI_DEF: "the Revolutionary Unitary State of Indonesia"
 INS_OTORITER_NKRI_ADJ: "Indonesian"
 INS_OTORITER_NKRI_party: "Dewan Revolusi"
 INS_OTORITER_NKRI_party_long: "Dewan Pimpinan Tertinggi Revolusi"

 INS_OTORITER_JUNTA: "Komando Militer Revolusi Indonesia"
 INS_OTORITER_JUNTA_DEF: "the Indonesian Revolutionary Military Command"
 INS_OTORITER_JUNTA_ADJ: "Indonesian"
 INS_OTORITER_JUNTA_party: "Junta ABRI"
 INS_OTORITER_JUNTA_party_long: "Presidium Markas Besar Revolusi Militer"

 INS_OTORITER_RAYA: "Imperium Militer Indonesia Raya"
 INS_OTORITER_RAYA_DEF: "the Greater Indonesian Military Empire"
 INS_OTORITER_RAYA_ADJ: "Indonesian"
 INS_OTORITER_RAYA_party: "Bela Negara"
 INS_OTORITER_RAYA_party_long: "Front Pemuda Bela Negara Indonesia Raya"

 # Jalur E
 INS_ISLAMIS_NII: "Negara Islam Indonesia"
 INS_ISLAMIS_NII_DEF: "the Islamic State of Indonesia"
 INS_ISLAMIS_NII_ADJ: "Indonesian"
 INS_ISLAMIS_NII_party: "Majelis Syuro"
 INS_ISLAMIS_NII_party_long: "Majelis Syuro Negara Islam Indonesia"

 INS_ISLAMIS_DAULAH: "Daulah Islamiyah Nusantara"
 INS_ISLAMIS_DAULAH_DEF: "the Islamic State of the Archipelago"
 INS_ISLAMIS_DAULAH_ADJ: "Nusantara"
 INS_ISLAMIS_DAULAH_party: "Diwan Imam"
 INS_ISLAMIS_DAULAH_party_long: "Diwan Al-Imam Darul Islam"

 INS_ISLAMIS_KHILAFAH: "Khilafah Islamiyah Nusantara"
 INS_ISLAMIS_KHILAFAH_DEF: "the Islamic Caliphate of Nusantara"
 INS_ISLAMIS_KHILAFAH_ADJ: "Islamic"
 INS_ISLAMIS_KHILAFAH_party: "Baitul Mal & Syuro"
 INS_ISLAMIS_KHILAFAH_party_long: "Majelis Khilafah Islamiyah Nusantara"

 # Jalur F
 INS_MAJAPAHIT_EMPIRE: "Kemaharajaan Majapahit"
 INS_MAJAPAHIT_EMPIRE_DEF: "the Majapahit Empire"
 INS_MAJAPAHIT_EMPIRE_ADJ: "Majapahit"
 INS_MAJAPAHIT_EMPIRE_party: "Kraton Wilwatikta"
 INS_MAJAPAHIT_EMPIRE_party_long: "Keluarga Diraja & Rakryan Majapahit"

 INS_MAJAPAHIT_SURYA: "Imperium Surya Wilwatikta"
 INS_MAJAPAHIT_SURYA_DEF: "the Solar Empire of Wilwatikta"
 INS_MAJAPAHIT_SURYA_ADJ: "Wilwatikta"
 INS_MAJAPAHIT_SURYA_party: "Surya Kencana"
 INS_MAJAPAHIT_SURYA_party_long: "Dewan Saptaprabu Surya Wilwatikta"

 INS_MAJAPAHIT_NUSANTARA: "Maha-Imperium Nusantara Raya"
 INS_MAJAPAHIT_NUSANTARA_DEF: "the Grand Empire of Greater Nusantara"
 INS_MAJAPAHIT_NUSANTARA_ADJ: "Nusantara"
 INS_MAJAPAHIT_NUSANTARA_party: "Bhayangkara Raya"
 INS_MAJAPAHIT_NUSANTARA_party_long: "Dewan Mahamenteri Nusantara Raya"

 # =====================================================================
 # SHIP & DIVISION NAMELISTS
 # =====================================================================
 INS_CAPITAL_SHIPS_REPUBLIK: "KRI: Kapal Tempur & Penjelajah Republik"
 INS_DESTROYERS_REPUBLIK: "KRI: Perusak & Korvet Republik"
 INS_SUBMARINES_REPUBLIK: "KRI: Kapal Selam Senjata Pusaka"
 INS_ESCORT_REPUBLIK: "KRI: Armada Ronda & Angkut Selat"
 INS_CAPITAL_SHIPS_KOLONIAL: "Hr.Ms.: Slagschepen en Kruisers van de Oost"
 INS_DESTROYERS_KOLONIAL: "Hr.Ms.: Torpedobootjagers Nederlandsch-Indi\\xc3\\xab"
 INS_SUBMARINES_KOLONIAL: "Hr.Ms.: Onderzeeboten Indische Oceaan"
 INS_ESCORT_KOLONIAL: "Hr.Ms.: Mijnenvegers en Escorteurs"
 INS_CAPITAL_SHIPS_KOMUNIS: "KPR: Kapal Tempur Proletar & Front Merah"
 INS_DESTROYERS_KOMUNIS: "KPR: Perusak & Korvet Martir Revolusi"
 INS_SUBMARINES_KOMUNIS: "KPR: Kapal Selam Hiu Merah"
 INS_ESCORT_KOMUNIS: "KPR: Ronda & Logistik Rakyat"
 INS_CAPITAL_SHIPS_OTORITER: "KRI: Kapal Tempur Komando Dewan Revolusi"
 INS_DESTROYERS_OTORITER: "KRI: Perusak & Pemburu Bela Negara"
 INS_SUBMARINES_OTORITER: "KRI: Kapal Selam Pasukan Khusus Bawah Air"
 INS_ESCORT_OTORITER: "KRI: Pengawal Garis Depan Samudra"
 INS_CAPITAL_SHIPS_ISLAMIS: "KNI: Kapal Tempur Mujahidin & Benteng Tauhid"
 INS_DESTROYERS_ISLAMIS: "KNI: Perusak & Korvet Pedang Tauhid"
 INS_SUBMARINES_ISLAMIS: "KNI: Kapal Selam Panah & Pusaka Islam"
 INS_ESCORT_ISLAMIS: "KNI: Ronda Syariat & Angkut Baitul Mal"
 INS_CAPITAL_SHIPS_MAJAPAHIT: "JPS: Jung Tempur Segara Wilwatikta"
 INS_DESTROYERS_MAJAPAHIT: "JPS: Jung Pasukan & Warastra Jalayanapati"
 INS_SUBMARINES_MAJAPAHIT: "KMN: Kapal Pusaka Siluman Segara"
 INS_ESCORT_MAJAPAHIT: "JPS: Jung Layar & Niaga Upacara"
 DEI_OTORITER: "Resimen Pengawal Dewan Revolusi & Pelopor Bela Negara"
'''

# Decode any raw byte escapes properly
processed_loc = new_loc_entries.encode('utf-8').decode('unicode_escape')

updated_content = existing_content.rstrip() + '\n' + processed_loc.strip() + '\n'

with open(loc_file, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + updated_content.encode('utf-8'))

print('Successfully updated DEI_indonesia_l_english.yml with UTF-8 BOM.')
