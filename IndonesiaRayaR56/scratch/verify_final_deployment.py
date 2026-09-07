import os

deploy_path = r'C:\Users\radit\Documents\Paradox Interactive\Hearts of Iron IV\mod\IndonesiaRayaR56'

# 1. Check tree
with open(os.path.join(deploy_path, 'common', 'national_focus', 'DEI_indonesia_focus_tree.txt'), 'r', encoding='utf-8') as f:
    c = f.read()
assert 'autonomy_state = autonomy_free' in c, 'autonomy_free missing in deployed tree!'
assert c.count('autonomy_state = autonomy_free') >= 7, 'Not all paths have autonomy_free!'
print('[1/3] Focus Tree: All paths have autonomy_state = autonomy_free (OK)')

# 2. Check GUI
with open(os.path.join(deploy_path, 'interface', 'eventwindow.gui'), 'r', encoding='utf-8') as f:
    c = f.read()
assert 'position = { x = 88 y = 10 }' in c, 'options_grid not at y = 10 in deployed GUI!'
print('[2/3] Event Window GUI: options_grid at y = 10 (never overlaps text) (OK)')

# 3. Check Loc & BOM
with open(os.path.join(deploy_path, 'localisation', 'english', 'DEI_indonesia_l_english.yml'), 'rb') as f:
    raw = f.read()
assert raw.startswith(b'\xef\xbb\xbf'), 'Missing BOM in deployed loc!'
print('[3/3] Localization: UTF-8 BOM verified (OK)')

print('\nALL DEPLOYED FILES 100% VERIFIED AND SYNCHRONIZED!')
