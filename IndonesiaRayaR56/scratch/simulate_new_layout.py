import re

# Let's map each focus in our 134 focus tree to its exact new coordinate (x, y)

new_coords = {}

# --- PROLOGUE (x=19, y=0..2) ---
new_coords['dei_focus_root'] = (19, 0)
new_coords['dei_focus_pembangkangan'] = (19, 1)
new_coords['dei_focus_momentum_kemerdekaan'] = (19, 2)

# --- PATH A: REPUBLIK (Base X=7, Y starts at 3) ---
# Original rels was dei_focus_momentum_kemerdekaan:
# proklamasi: (-8, 9) -> new (7, 3)
# tkr: (-8, 10) -> new (7, 4)
# diplomasi: (-10, 11) -> new (6, 5)
# agresi_1: (-6, 11) -> new (8, 5)
# gerilya: (-6, 12) -> new (8, 6)
# agresi_2: (-6, 13) -> new (8, 7)
# kmb: (-8, 14) -> new (7, 8)
# parlementer: (-8, 15) -> new (7, 9)
# demokrasi_liberal: (-10, 16) -> new (6, 10)
# irian_barat: (-6, 16) -> new (8, 10)
# demokrasi_terpimpin: (-8, 16) -> new (7, 10)
# kaa_bandung: (-10, 17) -> new (6, 11)
# trikora: (-6, 17) -> new (8, 11)
# dekrit_presiden: (-8, 17) -> new (7, 11)
# dwikora: (-6, 18) -> new (8, 12)
# pancasila: (-8, 18) -> new (7, 12)
new_coords['dei_focus_a_proklamasi'] = (7, 3)
new_coords['dei_focus_a_tkr'] = (7, 4)
new_coords['dei_focus_a_diplomasi'] = (6, 5)
new_coords['dei_focus_a_agresi_1'] = (8, 5)
new_coords['dei_focus_a_gerilya'] = (8, 6)
new_coords['dei_focus_a_agresi_2'] = (8, 7)
new_coords['dei_focus_a_kmb'] = (7, 8)
new_coords['dei_focus_a_parlementer'] = (7, 9)
new_coords['dei_focus_a_demokrasi_liberal'] = (6, 10)
new_coords['dei_focus_a_demokrasi_terpimpin'] = (7, 10)
new_coords['dei_focus_a_irian_barat'] = (8, 10)
new_coords['dei_focus_a_kaa_bandung'] = (6, 11)
new_coords['dei_focus_a_dekrit_presiden'] = (7, 11)
new_coords['dei_focus_a_trikora'] = (8, 11)
new_coords['dei_focus_a_pancasila'] = (7, 12)
new_coords['dei_focus_a_dwikora'] = (8, 12)

# --- PATH B: KOLONIAL / FEDERALIS (Base X=12, Y starts at 3) ---
new_coords['dei_focus_b_root'] = (12, 3)
new_coords['dei_focus_b_tekan_gerilyawan'] = (11, 4)
new_coords['dei_focus_b_reformasi_terbatas'] = (13, 4)
new_coords['dei_focus_b_negara_federal'] = (13, 5)
new_coords['dei_focus_b_nit'] = (13, 6)
new_coords['dei_focus_b_uni_belanda'] = (12, 7)
new_coords['dei_focus_b_dominion'] = (12, 8)
new_coords['dei_focus_b_persemakmuran'] = (11, 9)
new_coords['dei_focus_b_pasifikasi'] = (13, 9)
new_coords['dei_focus_b_sidang_bfo'] = (11, 10)
new_coords['dei_focus_b_angkatan_federal'] = (13, 10)
new_coords['dei_focus_b_pakta_anzac'] = (12, 11)
new_coords['dei_focus_b_perkebunan_deli'] = (11, 12)
new_coords['dei_focus_b_kraton_swapraja'] = (13, 12)

# --- PATH C: KOMUNIS (Base X=17, Y starts at 3) ---
new_coords['dei_focus_c_root'] = (17, 3)
new_coords['dei_focus_c_land_reform'] = (16, 4)
new_coords['dei_focus_c_pembersihan_reaksioner'] = (18, 4)
new_coords['dei_focus_c_tentara_rakyat'] = (17, 5)
new_coords['dei_focus_c_aliansi_soviet'] = (16, 6)
new_coords['dei_focus_c_aliansi_china'] = (18, 6)
new_coords['dei_focus_c_industrialisasi_sosialis'] = (17, 7)
new_coords['dei_focus_c_ekspor_revolusi'] = (17, 8)
new_coords['dei_focus_c_komune_tani'] = (16, 9)
new_coords['dei_focus_c_sita_aset_asing'] = (18, 9)
new_coords['dei_focus_c_angkatan_kelima'] = (17, 10)
new_coords['dei_focus_c_lekra'] = (16, 11)
new_coords['dei_focus_c_pakta_asia_merah'] = (18, 11)
new_coords['dei_focus_c_rencana_semesta'] = (17, 12)

# --- PATH D: OTORITER MILITER (Base X=22, Y starts at 3) ---
new_coords['dei_focus_d_root'] = (22, 3)
new_coords['dei_focus_d_darurat_militer'] = (21, 4)
new_coords['dei_focus_d_bubarkan_partai'] = (23, 4)
new_coords['dei_focus_d_industri_militer'] = (22, 5)
new_coords['dei_focus_d_pemuda_militan'] = (21, 6)
new_coords['dei_focus_d_klaim_wilayah'] = (23, 6)
new_coords['dei_focus_d_ambisi_regional'] = (22, 7)
new_coords['dei_focus_d_dewan_revolusi'] = (21, 8)
new_coords['dei_focus_d_dwifungsi_abri'] = (23, 8)
new_coords['dei_focus_d_benteng_samudra'] = (22, 9)
new_coords['dei_focus_d_bela_negara'] = (21, 10)
new_coords['dei_focus_d_selat_malaka'] = (23, 10)
new_coords['dei_focus_d_hegemoni_selatan'] = (22, 11)
new_coords['dei_focus_d_indonesia_raya'] = (22, 12)

# --- PATH E: ISLAMIS / NII (Base X=27, Y starts at 3) ---
new_coords['dei_focus_e_root'] = (27, 3)
new_coords['dei_focus_e_dewan_ulama'] = (26, 4)
new_coords['dei_focus_e_syariat'] = (28, 4)
new_coords['dei_focus_e_tii'] = (27, 5)
new_coords['dei_focus_e_hubungan_arab'] = (26, 6)
new_coords['dei_focus_e_konflik_sekuler'] = (28, 6)
new_coords['dei_focus_e_pendidikan_agama'] = (27, 7)
new_coords['dei_focus_e_persatuan_nusantara'] = (27, 8)
new_coords['dei_focus_e_baitul_mal'] = (26, 9)
new_coords['dei_focus_e_mahkamah_syariah'] = (28, 9)
new_coords['dei_focus_e_akademi_mujahidin'] = (26, 10)
new_coords['dei_focus_e_hapus_riba'] = (28, 10)
new_coords['dei_focus_e_liga_muslim'] = (27, 11)
new_coords['dei_focus_e_khilafah_nusantara'] = (27, 12)

# --- PATH F: MAJAPAHIT (Base X=32, Y starts at 3) ---
new_coords['dei_focus_f_root'] = (32, 3)
new_coords['dei_focus_f_pusaka'] = (31, 4)
new_coords['dei_focus_f_dewan_adat'] = (33, 4)
new_coords['dei_focus_f_angkatan_laut'] = (31, 5)
new_coords['dei_focus_f_klaim_nusantara'] = (33, 5)
new_coords['dei_focus_f_persatuan_kerajaan'] = (32, 6)
new_coords['dei_focus_f_kekaisaran_baru'] = (32, 7)
new_coords['dei_focus_f_sumpah_palapa_baru'] = (31, 8)
new_coords['dei_focus_f_restorasi_trowulan'] = (33, 8)
new_coords['dei_focus_f_dharmaputra'] = (31, 9)
new_coords['dei_focus_f_jung_raksasa'] = (33, 9)
new_coords['dei_focus_f_kitab_kutaramanawa'] = (32, 10)
new_coords['dei_focus_f_penobatan_maharaja'] = (32, 11)

# --- INDUSTRY & ADVANCED TECH (Base X=41, Y=0..8) ---
new_coords['INS_industrial_centralisation'] = (41, 0)
new_coords['INS_continue_the_modernisation'] = (39, 1)
new_coords['INS_colonial_infrastructure'] = (41, 1)
new_coords['INS_restore_the_arms_factories'] = (43, 1)
new_coords['INS_civilian_works'] = (39, 2)
new_coords['INS_connect_the_islands'] = (41, 2)
new_coords['INS_earthworks'] = (43, 2)
new_coords['INS_phillips_radio'] = (40, 3)
new_coords['INS_the_royal_batavian_society'] = (42, 3)
new_coords['INS_economic_independence'] = (41, 4)
new_coords['INS_royal_scientific_cooperation'] = (43, 4)
new_coords['INS_scientific_exceptionalism'] = (40, 5)
new_coords['INS_invite_foreign_investors'] = (42, 5)
new_coords['INS_koninklijk_paketvaart_maatschappij'] = (41, 6)
new_coords['INS_advanced_telecommunications'] = (39, 7)
new_coords['INS_institut_teknologi_bandung'] = (41, 7)
new_coords['INS_pusat_metalurgi_sintesis'] = (43, 7)
new_coords['INS_proyek_riset_atom_dirgantara'] = (41, 8)

# --- ARMED FORCES (Army, Air, Navy) (Base X=48..62, Y=0..6) ---
# Army Head: X=50, Y=0
new_coords['INS_koninklijk_nederlands_indisch_leger'] = (50, 0)
new_coords['INS_modernize_the_military'] = (49, 1)
new_coords['INS_form_the_home_guard'] = (51, 1)
new_coords['INS_braat_overvalwagen'] = (48, 2)
new_coords['INS_ambonese_auxilaries'] = (50, 2)
new_coords['INS_interventionism'] = (52, 2)
new_coords['INS_city_fortifications'] = (49, 3)
new_coords['INS_expand_the_officers_corps'] = (51, 3)
new_coords['INS_non_discriminatory_conscription'] = (50, 4)
new_coords['INS_preemptive_defense'] = (49, 5)
new_coords['INS_guerilla_tactics'] = (51, 5)
new_coords['INS_reform_the_knil'] = (50, 6)

# Air Force Head: X=55, Y=0
new_coords['INS_the_test_flight_service'] = (55, 0)
new_coords['INS_raaf_assistance'] = (55, 1)
new_coords['INS_knil_integration'] = (54, 2)
new_coords['INS_indonesian_fighter_schools'] = (56, 2)
new_coords['INS_the_flying_dutchmen'] = (55, 3)

# Navy Head: X=60, Y=0
new_coords['INS_naval_autonomy'] = (60, 0)
new_coords['INS_coastal_entrenchment'] = (59, 1)
new_coords['INS_java_shipyards'] = (61, 1)
new_coords['INS_naval_warfare'] = (59, 2)
new_coords['INS_increase_convoy_production'] = (61, 2)
new_coords['INS_british_ship_designs'] = (58, 3)
new_coords['INS_KNIL_marines'] = (60, 3)
new_coords['INS_air_by_sea'] = (58, 4)
new_coords['INS_joint_wargames'] = (60, 4)
new_coords['INS_convoy_protection'] = (59, 5)
new_coords['INS_ship_a_day_tactics'] = (61, 5)

print(f"Total coordinates mapped: {len(new_coords)} / 134")

# Check for coordinate collisions!
used = {}
collisions = []
for fid, pos in new_coords.items():
    if pos in used:
        collisions.append((pos, fid, used[pos]))
    used[pos] = fid

if collisions:
    print("COLLISIONS FOUND:")
    for c in collisions:
        print(f"  Pos {c[0]}: {c[1]} vs {c[2]}")
else:
    print("ALL 134 FOCUSES HAVE 100% UNIQUE POSITIONS WITH ZERO COLLISIONS!")
