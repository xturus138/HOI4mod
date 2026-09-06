loc_file = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"

with open(loc_file, "r", encoding="utf-8-sig") as f:
    content = f.read()

new_keys = """
 # --- COUNTRY LEADERS FOR ALL 6 IDEOLOGIES ---
 DEI_sultan_hamid_ii:0 "Sultan Hamid II"
 DEI_hamengkubuwono_ix:0 "Sri Sultan Hamengkubuwono IX"
 DEI_wahid_hasyim:0 "K.H. Wahid Hasyim"
 DEI_soeharto:0 "Soeharto"
 DEI_maharaja_suryawikrama:0 "Sri Maharaja Suryawikrama"
 DEI_tan_malaka:0 "Tan Malaka"
 DEI_mohammad_hatta:0 "Mohammad Hatta"
 DEI_sutan_syahrir:0 "Sutan Sjahrir"
 DEI_mohammad_natsir:0 "Mohammad Natsir"
"""

full_content = content.rstrip() + "\n" + new_keys

with open(loc_file, "wb") as f:
    f.write(b'\xef\xbb\xbf')
    f.write(full_content.encode("utf-8"))

print("Added country leaders loc keys successfully with UTF-8 BOM.")
