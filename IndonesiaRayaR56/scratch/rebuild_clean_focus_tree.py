import re
import os

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"

# Exact coordinates for all 134 focuses
coords = {
    # Prologue (Center X=19, Y=0..2)
    'dei_focus_root': (19, 0),
    'dei_focus_pembangkangan': (19, 1),
    'dei_focus_momentum_kemerdekaan': (19, 2),

    # Path A: Republik Demokratis (Center X=7, Y=3..14)
    'dei_focus_a_proklamasi': (7, 3),
    'dei_focus_a_tkr': (7, 4),
    'dei_focus_a_diplomasi': (6, 5),
    'dei_focus_a_agresi_1': (8, 5),
    'dei_focus_a_gerilya': (8, 6),
    'dei_focus_a_agresi_2': (8, 7),
    'dei_focus_a_kmb': (7, 8),
    'dei_focus_a_parlementer': (7, 9),
    'dei_focus_a_demokrasi_liberal': (6, 10),
    'dei_focus_a_irian_barat': (8, 10),
    'dei_focus_a_demokrasi_terpimpin': (7, 11),
    'dei_focus_a_kaa_bandung': (6, 12),
    'dei_focus_a_trikora': (8, 12),
    'dei_focus_a_dekrit_presiden': (7, 13),
    'dei_focus_a_pancasila': (7, 14),
    'dei_focus_a_dwikora': (8, 14),

    # Path B: Kolonial / Federalis (Center X=12, Y=3..12)
    'dei_focus_b_root': (12, 3),
    'dei_focus_b_tekan_gerilyawan': (11, 4),
    'dei_focus_b_reformasi_terbatas': (13, 4),
    'dei_focus_b_negara_federal': (13, 5),
    'dei_focus_b_nit': (13, 6),
    'dei_focus_b_uni_belanda': (12, 7),
    'dei_focus_b_dominion': (12, 8),
    'dei_focus_b_persemakmuran': (11, 9),
    'dei_focus_b_pasifikasi': (13, 9),
    'dei_focus_b_sidang_bfo': (11, 10),
    'dei_focus_b_angkatan_federal': (13, 10),
    'dei_focus_b_pakta_anzac': (12, 11),
    'dei_focus_b_perkebunan_deli': (11, 12),
    'dei_focus_b_kraton_swapraja': (13, 12),

    # Path C: Komunis (Center X=17, Y=3..13)
    'dei_focus_c_root': (17, 3),
    'dei_focus_c_land_reform': (16, 4),
    'dei_focus_c_pembersihan_reaksioner': (18, 4),
    'dei_focus_c_tentara_rakyat': (17, 5),
    'dei_focus_c_aliansi_soviet': (16, 6),
    'dei_focus_c_aliansi_china': (18, 6),
    'dei_focus_c_industrialisasi_sosialis': (17, 7),
    'dei_focus_c_ekspor_revolusi': (17, 8),
    'dei_focus_c_komune_tani': (16, 9),
    'dei_focus_c_sita_aset_asing': (18, 9),
    'dei_focus_c_angkatan_kelima': (17, 10),
    'dei_focus_c_lekra': (16, 11),
    'dei_focus_c_pakta_asia_merah': (18, 12),
    'dei_focus_c_rencana_semesta': (17, 13),

    # Path D: Otoriter Militer (Center X=22, Y=3..13)
    'dei_focus_d_root': (22, 3),
    'dei_focus_d_darurat_militer': (21, 4),
    'dei_focus_d_bubarkan_partai': (23, 4),
    'dei_focus_d_industri_militer': (22, 5),
    'dei_focus_d_pemuda_militan': (21, 6),
    'dei_focus_d_klaim_wilayah': (23, 7),
    'dei_focus_d_ambisi_regional': (22, 8),
    'dei_focus_d_dewan_revolusi': (21, 9),
    'dei_focus_d_dwifungsi_abri': (23, 9),
    'dei_focus_d_benteng_samudra': (22, 10),
    'dei_focus_d_bela_negara': (21, 11),
    'dei_focus_d_selat_malaka': (23, 11),
    'dei_focus_d_hegemoni_selatan': (22, 12),
    'dei_focus_d_indonesia_raya': (22, 13),

    # Path E: Islamis / NII (Center X=27, Y=3..12)
    'dei_focus_e_root': (27, 3),
    'dei_focus_e_dewan_ulama': (26, 4),
    'dei_focus_e_syariat': (28, 4),
    'dei_focus_e_tii': (27, 5),
    'dei_focus_e_hubungan_arab': (26, 6),
    'dei_focus_e_konflik_sekuler': (28, 6),
    'dei_focus_e_pendidikan_agama': (27, 7),
    'dei_focus_e_persatuan_nusantara': (27, 8),
    'dei_focus_e_baitul_mal': (26, 9),
    'dei_focus_e_mahkamah_syariah': (28, 9),
    'dei_focus_e_akademi_mujahidin': (26, 10),
    'dei_focus_e_hapus_riba': (28, 10),
    'dei_focus_e_liga_muslim': (27, 11),
    'dei_focus_e_khilafah_nusantara': (27, 12),

    # Path F: Majapahit (Center X=32, Y=3..11)
    'dei_focus_f_root': (32, 3),
    'dei_focus_f_pusaka': (31, 4),
    'dei_focus_f_dewan_adat': (33, 4),
    'dei_focus_f_angkatan_laut': (31, 5),
    'dei_focus_f_klaim_nusantara': (33, 5),
    'dei_focus_f_persatuan_kerajaan': (32, 6),
    'dei_focus_f_kekaisaran_baru': (32, 7),
    'dei_focus_f_sumpah_palapa_baru': (31, 8),
    'dei_focus_f_restorasi_trowulan': (33, 8),
    'dei_focus_f_dharmaputra': (31, 9),
    'dei_focus_f_jung_raksasa': (33, 9),
    'dei_focus_f_kitab_kutaramanawa': (32, 10),
    'dei_focus_f_penobatan_maharaja': (32, 11),

    # Industry & Advanced Technology (Center X=41, Y=0..8)
    'INS_industrial_centralisation': (41, 0),
    'INS_continue_the_modernisation': (39, 1),
    'INS_colonial_infrastructure': (41, 1),
    'INS_restore_the_arms_factories': (43, 1),
    'INS_civilian_works': (39, 2),
    'INS_connect_the_islands': (41, 2),
    'INS_earthworks': (43, 2),
    'INS_phillips_radio': (40, 3),
    'INS_the_royal_batavian_society': (42, 3),
    'INS_economic_independence': (41, 4),
    'INS_royal_scientific_cooperation': (43, 4),
    'INS_scientific_exceptionalism': (40, 5),
    'INS_invite_foreign_investors': (42, 5),
    'INS_koninklijk_paketvaart_maatschappij': (41, 6),
    'INS_advanced_telecommunications': (39, 7),
    'INS_institut_teknologi_bandung': (41, 7),
    'INS_pusat_metalurgi_sintesis': (43, 7),
    'INS_proyek_riset_atom_dirgantara': (41, 8),

    # Armed Forces (Army, Air, Navy) (X=48..61, Y=0..6)
    'INS_koninklijk_nederlands_indisch_leger': (50, 0),
    'INS_modernize_the_military': (49, 1),
    'INS_form_the_home_guard': (51, 1),
    'INS_braat_overvalwagen': (48, 2),
    'INS_ambonese_auxilaries': (50, 2),
    'INS_interventionism': (52, 2),
    'INS_city_fortifications': (49, 3),
    'INS_expand_the_officers_corps': (51, 3),
    'INS_non_discriminatory_conscription': (50, 4),
    'INS_preemptive_defense': (49, 5),
    'INS_guerilla_tactics': (51, 5),
    'INS_reform_the_knil': (50, 6),

    'INS_the_test_flight_service': (55, 0),
    'INS_raaf_assistance': (55, 1),
    'INS_knil_integration': (54, 2),
    'INS_indonesian_fighter_schools': (56, 2),
    'INS_the_flying_dutchmen': (55, 3),

    'INS_naval_autonomy': (60, 0),
    'INS_coastal_entrenchment': (59, 1),
    'INS_java_shipyards': (61, 1),
    'INS_naval_warfare': (59, 2),
    'INS_increase_convoy_production': (61, 2),
    'INS_british_ship_designs': (58, 3),
    'INS_KNIL_marines': (60, 3),
    'INS_air_by_sea': (58, 4),
    'INS_joint_wargames': (60, 4),
    'INS_convoy_protection': (59, 5),
    'INS_ship_a_day_tactics': (61, 5),
}

# Path root allow_branch definitions
allow_branch_map = {
    'dei_focus_a_proklamasi': 'allow_branch = { OR = { NOT = { has_country_flag = dei_jalur_dipilih } has_country_flag = dei_path_a_chosen } }',
    'dei_focus_b_root': 'allow_branch = { OR = { NOT = { has_country_flag = dei_jalur_dipilih } has_country_flag = dei_path_b_chosen } }',
    'dei_focus_c_root': 'allow_branch = { OR = { NOT = { has_country_flag = dei_jalur_dipilih } has_country_flag = dei_path_c_chosen } }',
    'dei_focus_d_root': 'allow_branch = { OR = { NOT = { has_country_flag = dei_jalur_dipilih } has_country_flag = dei_path_d_chosen } }',
    'dei_focus_e_root': 'allow_branch = { OR = { NOT = { has_country_flag = dei_jalur_dipilih } has_country_flag = dei_path_e_chosen } }',
    'dei_focus_f_root': 'allow_branch = { OR = { NOT = { has_country_flag = dei_jalur_dipilih } has_country_flag = dei_path_f_chosen } }',
}

with open(tree_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace each focus block's x, y, and remove relative_position_id
# Also add allow_branch to path roots

def clean_focus_block(match):
    b = match.group(0)
    fid_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b)
    if not fid_m: return b
    fid = fid_m.group(1)
    if fid not in coords: return b
    
    nx, ny = coords[fid]
    
    # Remove old x, y, relative_position_id
    b_new = re.sub(r'\bx\s*=\s*-?\d+', f'x = {nx}', b)
    b_new = re.sub(r'\by\s*=\s*-?\d+', f'y = {ny}', b_new)
    b_new = re.sub(r'[ \t]*relative_position_id\s*=\s*[a-zA-Z0-9_]+\n?', '', b_new)
    
    # If this is a path root, inject allow_branch right after cost
    if fid in allow_branch_map:
        # Check if already has allow_branch
        if 'allow_branch' not in b_new:
            ab_line = f"\t\t{allow_branch_map[fid]}\n"
            b_new = re.sub(r'(\bcost\s*=\s*\d+\n)', r'\1' + ab_line, b_new)
            
    return b_new

# Process all focus = { ... }
# Regex matching complete focus = { ... } blocks
pattern = r'focus\s*=\s*\{[^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*\}'
updated_text = re.sub(pattern, clean_focus_block, text)

with open(tree_path, "w", encoding="utf-8") as f:
    f.write(updated_text)

print(f"SUCCESS: Rewrote {tree_path} with pristine absolute layout coordinates!")
