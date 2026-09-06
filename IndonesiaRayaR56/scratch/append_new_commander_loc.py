loc_file = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"

with open(loc_file, "r", encoding="utf-8-sig") as f:
    content = f.read()

new_keys = """
 # --- AUTHENTIC INDONESIAN COMMANDERS & ALUTSISTA ---
 DEI_re_martadinata:0 "Raden Eddy Martadinata"
 DEI_suryadi_suryadarma:0 "Suryadi Suryadarma"
 DEI_halim_perdanakusuma:0 "Halim Perdanakusuma"
 DEI_moestopo:0 "Moestopo"
 DEI_gatot_soebroto:0 "Gatot Soebroto"
 INS_marmon_herrington_ctls:0 "Marmon-Herrington CTLS-4TA"
 INS_marmon_herrington_ctls_desc:0 "Light tank acquired during the early 1940s, providing essential mobile direct fire support in open terrain."
 INS_cw21_demon:0 "Curtiss-Wright CW-21 Demon"
 INS_cw21_demon_desc:0 "High-climb interceptor fighter deployed for territorial air interception across Java airfields."
 INS_b25_mitchell:0 "B-25 Mitchell 'Si Djimat'"
 INS_b25_mitchell_desc:0 "Twin-engine medium tactical bomber, renowned for tactical ground-support operations throughout the Indonesian archipelago."
"""

full_content = content.rstrip() + "\n" + new_keys

with open(loc_file, "wb") as f:
    f.write(b'\xef\xbb\xbf')
    f.write(full_content.encode("utf-8"))

print("Added new commander and alutsista loc keys successfully with UTF-8 BOM.")
