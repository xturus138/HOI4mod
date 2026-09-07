import codecs

loc_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"
with codecs.open(loc_path, "r", encoding="utf-8-sig") as f:
    c = f.read()

new_keys = """
 # Custom Tooltips for Revolution Path Selection
 dei_path_a_chosen_tt:0 "§YProclaimed the Democratic Republic§! in the 1936 National Revolution"
 dei_path_b_chosen_tt:0 "§YRatified the Federal Commonwealth§! in the 1936 National Revolution"
 dei_path_c_chosen_tt:0 "§YEstablished the People's Front (Komunis)§! in the 1936 National Revolution"
 dei_path_d_chosen_tt:0 "§YEstablished the Revolutionary Military Council§! in the 1936 National Revolution"
 dei_path_e_chosen_tt:0 "§YProclaimed the Islamic State (NII)§! in the 1936 National Revolution"
 dei_path_f_chosen_tt:0 "§YRestored the Majapahit Empire§! in the 1936 National Revolution"
"""

if "dei_path_a_chosen_tt" not in c:
    c = c + new_keys
    with codecs.open(loc_path, "w", encoding="utf-8-sig") as f:
        f.write(c)
    print("Appended tooltips successfully with UTF-8 BOM!")
else:
    print("Already present!")

# Verify BOM
raw = open(loc_path, "rb").read()
assert raw.startswith(b"\xef\xbb\xbf")
print("Verified UTF-8 BOM presence!")
