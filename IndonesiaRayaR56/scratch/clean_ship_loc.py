loc_file = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml'

with open(loc_file, 'r', encoding='utf-8-sig') as f:
    text = f.read()

replacements = {
    'INS_CAPITAL_SHIPS_MAJAPAHIT: "JPS: Jung Tempur Segara Wilwatikta"': 'INS_CAPITAL_SHIPS_MAJAPAHIT: "Armada Jung Tempur Segara Wilwatikta"',
    'INS_DESTROYERS_MAJAPAHIT: "JPS: Jung Pasukan & Warastra Jalayanapati"': 'INS_DESTROYERS_MAJAPAHIT: "Armada Pasukan & Warastra Jalayanapati"',
    'INS_SUBMARINES_MAJAPAHIT: "KMN: Kapal Pusaka Siluman Segara"': 'INS_SUBMARINES_MAJAPAHIT: "Armada Kapal Pusaka Siluman Segara"',
    'INS_ESCORT_MAJAPAHIT: "JPS: Jung Layar & Niaga Upacara"': 'INS_ESCORT_MAJAPAHIT: "Armada Jung Layar & Niaga Upacara"',

    'INS_CAPITAL_SHIPS_ISLAMIS: "KNI: Kapal Tempur Mujahidin & Benteng Tauhid"': 'INS_CAPITAL_SHIPS_ISLAMIS: "Kapal Tempur Mujahidin & Benteng Tauhid"',
    'INS_DESTROYERS_ISLAMIS: "KNI: Perusak & Korvet Pedang Tauhid"': 'INS_DESTROYERS_ISLAMIS: "Perusak & Korvet Pedang Tauhid"',
    'INS_SUBMARINES_ISLAMIS: "KNI: Kapal Selam Panah & Pusaka Islam"': 'INS_SUBMARINES_ISLAMIS: "Kapal Selam Panah & Pusaka Islam"',
    'INS_ESCORT_ISLAMIS: "KNI: Ronda Syariat & Angkut Baitul Mal"': 'INS_ESCORT_ISLAMIS: "Ronda Syariat & Angkut Baitul Mal"',

    'INS_CAPITAL_SHIPS_KOMUNIS: "KPR: Kapal Tempur Proletar & Front Merah"': 'INS_CAPITAL_SHIPS_KOMUNIS: "Kapal Tempur Proletar & Front Merah"',
    'INS_DESTROYERS_KOMUNIS: "KPR: Perusak & Korvet Martir Revolusi"': 'INS_DESTROYERS_KOMUNIS: "Perusak & Korvet Martir Revolusi"',
    'INS_SUBMARINES_KOMUNIS: "KPR: Kapal Selam Hiu Merah"': 'INS_SUBMARINES_KOMUNIS: "Kapal Selam Hiu Merah"',
    'INS_ESCORT_KOMUNIS: "KPR: Ronda & Logistik Rakyat"': 'INS_ESCORT_KOMUNIS: "Ronda & Logistik Rakyat"',
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open(loc_file, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + text.encode('utf-8'))

print('Successfully cleaned loc keys.')
