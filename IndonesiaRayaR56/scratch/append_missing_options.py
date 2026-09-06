import os

loc_path = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml'

with open(loc_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

missing_entries = """
 # Missing event option keys
 dei_path_b.4.b: "Form fewer, larger federal states for greater stability."
 dei_path_b.5.b: "A loose union with greater domestic autonomy."
 dei_path_c.1.b: "The PKI shall act as the sole vanguard with strict discipline."
 dei_path_c.7.b: "Balance state mobilization with the living needs of the people."
 dei_path_d.1.b: "A surgical coup with minimal disruption."
 dei_path_d.3.b: "Maintain a single disciplined state party."
 dei_path_d.5.b: "Subtle patriotic instruction through national education."
 dei_path_d.7.b: "Advance claims gradually to avoid early war."
 dei_path_e.1.b: "Consolidate regional control before formally proclaiming the state."
 dei_path_e.3.b: "Implement reforms gradually, accommodating local customs."
 dei_path_e.6.b: "Embrace moderate secular factions into a broad coalition."
"""

new_content = content + missing_entries
with open(loc_path, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + new_content.encode('utf-8'))
print('Successfully appended 11 missing event options with UTF-8 BOM!')
