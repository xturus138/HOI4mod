import codecs

path = 'localisation/english/DEI_indonesia_l_english.yml'

debug_loc = '''
 # =====================================================================
 # DEVELOPER DEBUGGING TOOLS LOCALISATION
 # =====================================================================
 dei_decisions_debug_tools: "§R[DEV DEBUG] Indonesia Raya Testing Tools§!"
 dei_decisions_debug_tools_desc: "Developer and testing controls to instantly bypass focus delays, change ideologies, promote historical leaders, deploy starter divisions, and test event layouts without waiting."

 dei_debug_instant_prologue: "🚀 [DEBUG] Instant Complete 1936 Revolution"
 dei_debug_instant_prologue_desc: "Instantly completes the 3 prologue focuses, ends Dutch puppet status, proclaims the Republic of Indonesia, appoints Interim President Sukarno, and deploys starter army & air wings."

 dei_debug_path_a: "🏛️ [DEBUG] Instant Path A - Republik Demokratis (Sukarno)"
 dei_debug_path_a_desc: "Instantly adopts Democratic path, seats Ir. Sukarno, and commissions Republican divisions & navy."

 dei_debug_path_b: "🦁 [DEBUG] Instant Path B - Kolonial Federalis BFO (Van Mook)"
 dei_debug_path_b_desc: "Instantly adopts Federalist path, seats Hubertus van Mook, and commissions KNIL divisions & navy."

 dei_debug_path_c: "🚩 [DEBUG] Instant Path C - Front Rakyat Komunis (Musso)"
 dei_debug_path_c_desc: "Instantly adopts Communist path, seats Musso, and commissions Red Army & navy."

 dei_debug_path_d: "🎖️ [DEBUG] Instant Path D - Dewan Revolusi Militer (Soedirman)"
 dei_debug_path_d_desc: "Instantly adopts Military Authoritarian path, seats General Soedirman, and commissions Revolutionary Guard divisions & navy."

 dei_debug_path_e: "🌙 [DEBUG] Instant Path E - Panji Islam NII (Kartosoewirjo)"
 dei_debug_path_e_desc: "Instantly adopts Islamic State path, seats S.M. Kartosoewirjo, and commissions Hizbullah divisions & navy."

 dei_debug_path_f: "👑 [DEBUG] Instant Path F - Kemaharajaan Majapahit (Wuryaningrat)"
 dei_debug_path_f_desc: "Instantly adopts Majapahit Empire path, crowns Maharaja Wuryaningrat, and commissions Bhayangkara divisions & navy."

 dei_debug_super_buff: "⚡ [DEBUG] Super Buff: +2000 PP, Max Stability & Huge Stockpile"
 dei_debug_super_buff_desc: "Grants 2,000 political power, 50% stability, 50% war support, and 20,000 rifles to freely test all decisions and mechanics."

 dei_debug_fire_events: "📰 [DEBUG] Fire 1936 Prologue News Events"
 dei_debug_fire_events_desc: "Triggers the 1936 General Strike and Military Defiance newspaper events to inspect top-banner layout and formatting."
'''

with open(path, 'rb') as f:
    raw = f.read()

assert raw.startswith(codecs.BOM_UTF8), "File missing BOM!"
text = raw.decode('utf-8-sig')

if 'dei_decisions_debug_tools:' not in text:
    text += debug_loc
    new_raw = codecs.BOM_UTF8 + text.encode('utf-8')
    with open(path, 'wb') as f:
        f.write(new_raw)
    print('Added debug localization keys with UTF-8 BOM successfully!')
else:
    print('Debug keys already present!')
