loc_file = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"

with open(loc_file, "r", encoding="utf-8-sig") as f:
    content = f.read()

new_keys = """
 # --- ADVANCED SCIENTIFIC & FIFTH RESEARCH SLOT FOCUSES ---
 INS_advanced_telecommunications:0 "Advanced Radar & Telecommunications"
 INS_advanced_telecommunications_desc:0 "Expanding upon the foundation laid by Bandung radio laboratories and modern telephony, our technicians shall construct a cutting-edge radar and electronic signal surveillance network across the Indonesian archipelago."
 INS_institut_teknologi_bandung:0 "Institut Teknologi Bandung"
 INS_institut_teknologi_bandung_desc:0 "Elevating the Technische Hoogeschool te Bandoeng into a premier polytechnic and scientific powerhouse guarantees a permanent fifth research bureau for our burgeoning industrial and defense sectors."
 INS_pusat_metalurgi_sintesis:0 "National Metallurgy & Synthetic Processing"
 INS_pusat_metalurgi_sintesis_desc:0 "Capitalizing on foreign capital and local raw riches, we build advanced synthetic fuel hydrogenation facilities and high-grade metallurgical smelting to sustain prolonged industrial mobilization."
 INS_proyek_riset_atom_dirgantara:0 "Advanced Aeronautics & Atomic Physics"
 INS_proyek_riset_atom_dirgantara_desc:0 "By gathering our finest physicists, aeronautical minds, and mineral prospectors, we pioneer indigenous rocketry, jet propulsion research, and atomic studies to ensure eternal sovereignty."
"""

full_content = content.rstrip() + "\n" + new_keys

with open(loc_file, "wb") as f:
    f.write(b'\xef\xbb\xbf')
    f.write(full_content.encode("utf-8"))

print("Added advanced research loc keys successfully with UTF-8 BOM.")
