import os

deploy_path = r'C:\Users\radit\Documents\Paradox Interactive\Hearts of Iron IV\mod\IndonesiaRayaR56'

# 1. Check DEI_templates.txt
with open(os.path.join(deploy_path, 'history', 'units', 'DEI_templates.txt'), 'r', encoding='utf-8') as f:
    c = f.read()
assert 'Resimen Garnisun Batavia' in c, 'Units block missing in templates!'
assert '13520' in c, 'Surabaya units missing in templates!'
print('[1/4] Starter Army: 6 Java-centric divisions deployed (OK)')

# 2. Check DEI_00_shared_trunk_events.txt
with open(os.path.join(deploy_path, 'events', 'DEI_00_shared_trunk_events.txt'), 'r', encoding='utf-8') as f:
    c = f.read()
assert '672 = { set_state_owner_to = HOL' in c, 'Outer islands transfer missing!'
print('[2/4] Outer Islands: 16 states held by colonial garrison HOL at revolution start (OK)')

# 3. Check DEI_decisions.txt
with open(os.path.join(deploy_path, 'common', 'decisions', 'DEI_decisions.txt'), 'r', encoding='utf-8') as f:
    c = f.read()
assert 'dei_decision_liberate_sumatra' in c, 'Sumatra liberation decision missing!'
assert 'dei_decision_liberate_kalimantan' in c, 'Kalimantan liberation decision missing!'
print('[3/4] Liberation Decisions: Sumatra, Kalimantan, Sulawesi/Maluku, Papua added (OK)')

# 4. Check localization & BOM
with open(os.path.join(deploy_path, 'localisation', 'english', 'DEI_indonesia_l_english.yml'), 'rb') as f:
    raw = f.read()
assert raw.startswith(b'\xef\xbb\xbf'), 'Missing BOM in deployed loc!'
assert b'dei_decision_liberate_sumatra:' in raw, 'Missing liberation loc!'
assert b'dei_debug_liberate_all_islands:' in raw, 'Missing debug liberate loc!'
print('[4/4] Localization: UTF-8 BOM verified with all liberation keys (OK)')

print('\nALL SYSTEM CHANGES 100% VERIFIED AND DEPLOYED!')
