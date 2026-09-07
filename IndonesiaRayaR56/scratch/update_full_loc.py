import re

loc_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"

with open(loc_path, "r", encoding="utf-8-sig") as f:
    text = f.read()

# 1. Update Focus Titles in shared trunk & Path A
replacements = {
    ' dei_focus_root: "Retaknya Pax Neerlandica"': ' dei_focus_root: "Fracture of the Pax Neerlandica"',
    ' dei_focus_pembangkangan: "Pembangkangan Militer & Rakyat"': ' dei_focus_pembangkangan: "Military and Popular Defiance"',
    ' dei_focus_momentum_kemerdekaan: "Momentum Revolusi Nasional 1936"': ' dei_focus_momentum_kemerdekaan: "Momentum of the 1936 National Revolution"',
    ' dei_focus_a_proklamasi: "Proklamasi Kemerdekaan"': ' dei_focus_a_proklamasi: "Proclamation of Independence"',
    ' dei_focus_a_agresi_1: "Confront Agresi Militer Belanda I"': ' dei_focus_a_agresi_1: "Confront First Dutch Military Aggression"',
    ' dei_focus_a_agresi_2: "Confront Agresi Militer Belanda II"': ' dei_focus_a_agresi_2: "Confront Second Dutch Military Aggression"',
    ' dei_focus_a_kmb: "Perundingan Meja Bundar (KMB)"': ' dei_focus_a_kmb: "The Round Table Conference (KMB)"',
    ' dei_decisions_nusantara: "Kedaulatan & Diplomasi Wilayah Nusantara"': ' dei_decisions_nusantara: "Nusantara Sovereignty & Territorial Diplomacy"',
    ' dei_decisions_governance: "Tata Kelola Kepulauan & Ekonomi Nasional"': ' dei_decisions_governance: "Archipelagic Governance & National Economy"',
    ' dei_focus_b_sidang_bfo: "Sidang Raya BFO"': ' dei_focus_b_sidang_bfo: "The Grand BFO Summit"',
}

for old_str, new_str in replacements.items():
    if old_str in text:
        text = text.replace(old_str, new_str)
        print(f"Replaced: {old_str.strip()} -> {new_str.strip()}")
    else:
        print(f"NOT FOUND: {old_str.strip()}")

# 2. Update Proclamations Decisions (lines 990-1042)
old_proc_block = """ dei_decisions_proclamations: "Tata Kelola & Penamaan Resmi Negara"
 dei_decisions_proclamations_desc: "Sebagai pemegang mandat kepemimpinan bangsa, kita berhak menentukan tata kelola, struktur ketatanegaraan, serta nama proklamasi resmi yang merepresentasikan kedaulatan Indonesia di panggung internasional."

 # Keputusan Proklamasi Jalur A: Republik
 dei_proclaim_nkri: "Proklamasikan Negara Kesatuan Republik Indonesia (NKRI)"
 dei_proclaim_nkri_desc: "Tegakkan bentuk negara kesatuan yang berdaulat dan tidak terbagi, berlandaskan amanat Proklamasi Kemerdekaan 17 Agustus 1945 dan falsafah Pancasila."
 dei_proclaim_ris: "Bentuk Republik Indonesia Serikat (RIS)"
 dei_proclaim_ris_desc: "Adopsi struktur federal yang mengakomodasi kedaulatan negara-negara bagian dan swapraja di seluruh kepulauan Nusantara."
 dei_proclaim_sosialis: "Proklamasikan Republik Sosialis Demokratis Indonesia"
 dei_proclaim_sosialis_desc: "Deklarasikan republik sosialis demokratis yang berorientasi pada kemakmuran rakyat, kepemilikan komunal atas alat produksi, dan koperasi gotong royong."

 # Keputusan Proklamasi Jalur B: Kolonial / Federalis
 dei_proclaim_dei: "Pertahankan Hindia Belanda (Nederlandsch-IndiÃ«)"
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
 dei_proclaim_nusantara_desc: "Tuntaskan Sumpah Palapa Patih Gadjah Mada dengan menyatukan seluruh dwipantara di bawah naungan takhta suci Kemaharajaan." """

new_proc_block = """ dei_decisions_proclamations: "State Governance & Official Nomenclature"
 dei_decisions_proclamations_desc: "Holding the sovereign mandate of national leadership, we possess the constitutional authority to establish state structures and determine the official proclamation that represents Indonesia on the world stage."

 # Proclamation Decisions - Path A: Republic
 dei_proclaim_nkri: "Proclaim the Unitary Republic of Indonesia (NKRI)"
 dei_proclaim_nkri_desc: "Establish a sovereign, indivisible unitary republic founded upon the historic Proclamation of Independence and the guiding philosophy of Pancasila."
 dei_proclaim_ris: "Form the Republic of the United States of Indonesia (RIS)"
 dei_proclaim_ris_desc: "Adopt a federal constitutional structure accommodating the regional sovereignty of member states and traditional realms across the archipelago."
 dei_proclaim_sosialis: "Proclaim the Democratic Socialist Republic of Indonesia"
 dei_proclaim_sosialis_desc: "Declare a democratic socialist republic dedicated to people's welfare, cooperative production, and the spirit of Gotong Royong."

 # Proclamation Decisions - Path B: Colonial / Federalist
 dei_proclaim_dei: "Reassert the Netherlands East Indies (Nederlandsch-Indie)"
 dei_proclaim_dei_desc: "Reaffirm the continuity of colonial administration under the protection of the Crown of the Netherlands and the Governor-General."
 dei_proclaim_bfo: "Proclaim the United States of Indonesia (BFO)"
 dei_proclaim_bfo_desc: "Unite all traditional autonomous realms and federal states into a sovereign, orderly federal commonwealth."
 dei_proclaim_dominion: "Establish the Crown Dominion of the Indies"
 dei_proclaim_dominion_desc: "Integrate the archipelago as an autonomous, equal Dominion within the Netherlands-Indonesia Union."

 # Proclamation Decisions - Path C: Communist
 dei_proclaim_rri: "Proclaim the People's Republic of Indonesia (RRI)"
 dei_proclaim_rri_desc: "Raise the red banner and establish the vanguard rule of workers and peasants, sweeping away all vestiges of feudalism and foreign imperialism."
 dei_proclaim_soviet: "Found the Union of Soviet Socialist Republics of Indonesia (URSSI)"
 dei_proclaim_soviet_desc: "Transform Indonesia into a workers' soviet democracy closely linked in fraternal alliance with the international socialist revolution."
 dei_proclaim_front: "Consolidate the People's Democratic Front of Nusantara"
 dei_proclaim_front_desc: "Unite all trade unions, agrarian leagues, and revolutionary mass organizations under the unified leadership of the Front Rakyat."

 # Proclamation Decisions - Path D: Authoritarian Military
 dei_proclaim_otoriter_nkri: "Proclaim the Revolutionary Unitary State of Indonesia"
 dei_proclaim_otoriter_nkri_desc: "Establish a centralized revolutionary regime under the unbending command of the armed forces to preserve national unity."
 dei_proclaim_junta: "Form the Supreme Military Revolutionary Command"
 dei_proclaim_junta_desc: "Vest supreme executive and legislative authority in the Presidium of the Armed Forces Supreme War Council."
 dei_proclaim_raya: "Proclaim the Military Imperium of Indonesia Raya"
 dei_proclaim_raya_desc: "Proclaim the geopolitical doctrine of Indonesia Raya, forging supreme military hegemony across the Indian and Pacific Oceans."

 # Proclamation Decisions - Path E: Islamist / NII
 dei_proclaim_nii: "Proclaim the Negara Islam Indonesia (NII)"
 dei_proclaim_nii_desc: "Implement Islamic Sharia as the supreme law of the state under the sacred leadership of the Imam of Negara Islam Indonesia."
 dei_proclaim_daulah: "Establish the Daulah Islamiyah Nusantara"
 dei_proclaim_daulah_desc: "Unite all Islamic domains and sultanates of the Malay archipelago under the supreme banner of Tawhid."
 dei_proclaim_khilafah: "Proclaim the Khilafah Islamiyah Nusantara"
 dei_proclaim_khilafah_desc: "Revive the glory of the Islamic Caliphate, uniting the Ummah from the shores of Sumatra to the islands of the Moluccas."

 # Proclamation Decisions - Path F: Majapahit Empire
 dei_proclaim_majapahit_empire: "Crown the Kemaharajaan Majapahit"
 dei_proclaim_majapahit_empire_desc: "Restore the throne of the Rajasa dynasty in Wilwatikta and resurrect the golden age of maritime Nusantara."
 dei_proclaim_surya: "Establish the Surya Wilwatikta Imperium"
 dei_proclaim_surya_desc: "Unfurl the sacred Sang Saka banner and the radiant Sun of Majapahit as the eternal symbols of imperial suzerainty."
 dei_proclaim_nusantara: "Unfurl the Standard of the Greater Nusantara Empire"
 dei_proclaim_nusantara_desc: "Fulfill the sacred Sumpah Palapa of Mahapatih Gadjah Mada by uniting all islands under the imperial throne." """

# Normalize whitespace in old block search
old_start = ' dei_decisions_proclamations: "Tata Kelola & Penamaan Resmi Negara"'
old_end = ' dei_proclaim_nusantara_desc: "Tuntaskan Sumpah Palapa Patih Gadjah Mada dengan menyatukan seluruh dwipantara di bawah naungan takhta suci Kemaharajaan."'

idx1 = text.find(old_start)
idx2 = text.find(old_end)
if idx1 != -1 and idx2 != -1:
    end_of_block = idx2 + len(old_end)
    text = text[:idx1] + new_proc_block.strip() + text[end_of_block:]
    print("Replaced Proclamation Decisions block successfully!")
else:
    print(f"Warning: Could not match exact proclamation block: idx1={idx1}, idx2={idx2}")

# 3. Add dei_trunk.6 narrative expansion and sub-events
old_trunk6_block = """ dei_trunk.6.t: "Momentum of Independence: 1936 National Proclamation"
 dei_trunk.6.d: "The old colonial order has fallen. Across the immense archipelago, millions stand vigilant. As emergency units assemble and warships raise new ensigns, what ideological path shall guide the destiny of Indonesia?"
 dei_trunk.6.a: "Path A: Democratic-Nationalist Republic (Sukarno)"
 dei_trunk.6.b: "Path B: Colonial / Federalist Commonwealth (Van Mook)"
 dei_trunk.6.c: "Path C: Communist People's Vanguard (Musso)"
 dei_trunk.6.d: "Path D: Authoritarian Military Regime (Soedirman)"
 dei_trunk.6.e: "Path E: Islamic State of Indonesia (Kartosoewirjo)"
 dei_trunk.6.f: "Path F: Imperial Resurgence of Majapahit (Wuryaningrat)\""""

new_trunk6_block = """ dei_trunk.6.t: "Momentum of Independence: The 1936 National Revolution"
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
 dei_trunk.603.d: "Rejecting secular modernity and colonial compromises, deep spiritual currents surge across the islands. Shall we establish an Islamic State guided by the Ulama and Sharia law under Kartosoewirjo, or awaken the ancient majesty of the Kemaharajaan Majapahit to fulfill the sacred Sumpah Palapa?"

 # Custom Tooltips for Clean Starter Army & Navy
 dei_trunk_path_a_tt: "§YProclaim the Democratic Republic under Sukarno:§!\\n • Transfers political power to Democratic nationalists\\n • Unlocks the Path A National Focus Tree\\n • Deploys 6 Republican divisions in West and Central Java\\n • Commissions Republican starter naval flotilla in Surabaya"
 dei_trunk_path_b_tt: "§YEstablish the Federalist Commonwealth under Van Mook:§!\\n • Transfers political power to Federalist moderates\\n • Unlocks the Path B National Focus Tree\\n • Deploys 5 KNIL Federal divisions in Java\\n • Commissions Royal colonial starter naval flotilla in Surabaya"
 dei_trunk_path_c_tt: "§YProclaim the People's Republic under Musso:§!\\n • Transfers political power to Communist Vanguard\\n • Unlocks the Path C National Focus Tree\\n • Deploys 5 Red People's Army brigades in Java\\n • Commissions Socialist starter naval flotilla in Surabaya"
 dei_trunk_path_d_tt: "§YEstablish the Military Revolutionary Council under General Soedirman:§!\\n • Transfers political power to Military Junta\\n • Unlocks the Path D National Focus Tree\\n • Deploys 5 Revolutionary Guard & Armored divisions in Java\\n • Commissions Armed Forces starter naval flotilla in Surabaya"
 dei_trunk_path_e_tt: "§YProclaim the Negara Islam Indonesia under Kartosoewirjo:§!\\n • Transfers political power to Islamist leadership\\n • Unlocks the Path E National Focus Tree\\n • Deploys 5 Mujahidin TII regiments in Java\\n • Commissions Islamic starter naval flotilla in Surabaya"
 dei_trunk_path_f_tt: "§YRestore the Kemaharajaan Majapahit under Wuryaningrat:§!\\n • Transfers political power to Traditional Imperial House\\n • Unlocks the Path F National Focus Tree\\n • Deploys 5 Bhayangkara & Guard divisions in Java\\n • Commissions Imperial Grand Fleet starter flotilla in Surabaya\""""

if old_trunk6_block in text:
    text = text.replace(old_trunk6_block, new_trunk6_block.strip())
    print("Replaced dei_trunk.6 block successfully!")
else:
    print("Warning: Could not match exact old_trunk6_block!")

# Always ensure UTF-8 BOM
with open(loc_path, "wb") as f:
    f.write(b"\xef\xbb\xbf" + text.encode("utf-8"))

print("SUCCESS: Updated localization file and preserved UTF-8 BOM!")
