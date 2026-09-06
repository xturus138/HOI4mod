import os, re

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
focus_dir = os.path.join(mod_dir, "common", "national_focus")

replacements = {
    "DEI_00_shared_trunk.txt": {
        "dei_focus_root": "GFX_focus_dei_pax_neerlandica",
        "dei_focus_pembangkangan": "GFX_focus_dei_pembangkangan",
        "dei_focus_momentum_kemerdekaan": "GFX_focus_dei_momentum_kemerdekaan",
    },
    "DEI_01_path_a_republik.txt": {
        "dei_focus_a_proklamasi": "GFX_focus_dei_proklamasi",
        "dei_focus_a_tkr": "GFX_focus_dei_tkr",
        "dei_focus_a_kaa_bandung": "GFX_focus_dei_kaa_bandung",
        "dei_focus_a_trikora": "GFX_focus_dei_trikora",
        "dei_focus_a_dekrit_presiden": "GFX_focus_dei_dekrit_presiden",
        "dei_focus_a_dwikora": "GFX_focus_dei_dwikora",
        "dei_focus_a_pancasila": "GFX_focus_dei_pancasila",
        "dei_focus_a_trisakti": "GFX_focus_dei_trisakti",
    },
    "DEI_02_path_b_kolonial.txt": {
        "dei_focus_b_sidang_bfo": "GFX_focus_dei_sidang_bfo",
        "dei_focus_b_angkatan_federal": "GFX_focus_dei_angkatan_federal",
        "dei_focus_b_perkebunan_deli": "GFX_focus_dei_perkebunan_deli",
        "dei_focus_b_otonomi_kerajaan": "GFX_focus_dei_swapraja",
    },
    "DEI_03_path_c_komunis.txt": {
        "dei_focus_c_komune_tani": "GFX_focus_dei_komune_tani",
        "dei_focus_c_angkatan_kelima": "GFX_focus_dei_angkatan_kelima",
        "dei_focus_c_lekra": "GFX_focus_dei_lekra",
        "dei_focus_c_pakta_asia_merah": "GFX_focus_dei_pakta_asia_merah",
    },
    "DEI_04_path_d_otoriter.txt": {
        "dei_focus_d_pemuda_militan": "GFX_focus_dei_bela_negara",
        "dei_focus_d_dewan_revolusi": "GFX_focus_dei_dewan_revolusi",
        "dei_focus_d_karyawan_abri": "GFX_focus_dei_dwifungsi",
        "dei_focus_d_benteng_samudra": "GFX_focus_dei_benteng_samudra",
    },
    "DEI_05_path_e_islamis.txt": {
        "dei_focus_e_baitul_mal": "GFX_focus_dei_baitul_mal",
        "dei_focus_e_mahkamah_syariah": "GFX_focus_dei_mahkamah_syariah",
        "dei_focus_e_akademi_mujahidin": "GFX_focus_dei_akademi_mujahidin",
        "dei_focus_e_khilafah_nusantara": "GFX_focus_dei_khilafah_nusantara",
    },
    "DEI_06_path_f_majapahit.txt": {
        "dei_focus_f_sumpah_palapa_baru": "GFX_focus_dei_sumpah_palapa",
        "dei_focus_f_restorasi_trowulan": "GFX_focus_dei_restorasi_trowulan",
        "dei_focus_f_dharmaputra": "GFX_focus_dei_dharmaputra",
        "dei_focus_f_jung_raksasa": "GFX_focus_dei_jung_raksasa",
        "dei_focus_f_penobatan_maharaja": "GFX_focus_dei_penobatan_maharaja",
    }
}

for fname, mapping in replacements.items():
    fpath = os.path.join(focus_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    for fid, new_icon in mapping.items():
        # Match focus block: id = fid ... icon = OLD_ICON
        pattern = rf"(focus\s*=\s*\{{\s*id\s*=\s*{fid}\s+icon\s*=\s*)[a-zA-Z0-9_]+"
        new_content, count = re.subn(pattern, rf"\g<1>{new_icon}", content)
        if count == 0:
            # Try alternate spacing
            pattern2 = rf"(id\s*=\s*{fid}[\s\S]*?icon\s*=\s*)[a-zA-Z0-9_]+"
            new_content, count = re.subn(pattern2, rf"\g<1>{new_icon}", content, count=1)
        if count > 0:
            print(f"[{fname}] Updated {fid} -> {new_icon}")
            content = new_content
        else:
            print(f"[{fname}] FAILED to update {fid}")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Focus trees updated.")
