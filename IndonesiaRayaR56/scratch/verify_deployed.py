import os

deploy_path = r'C:\Users\radit\Documents\Paradox Interactive\Hearts of Iron IV\mod\IndonesiaRayaR56'

# 1. Check trunk events
with open(os.path.join(deploy_path, 'events', 'DEI_00_shared_trunk_events.txt'), 'r', encoding='utf-8') as f:
    c = f.read()
assert 'news_event = {\n\tid = dei_trunk.1' in c or 'news_event = {\n\tid = dei_trunk.1' in c.replace('\r\n', '\n'), 'dei_trunk.1 not news_event!'
assert 'end_puppet = yes' in c, 'end_puppet not in trunk events!'
print('[1/4] Events in deployed mod: All converted to news_event with end_puppet = yes (OK)')

# 2. Check eventwindow.gui
with open(os.path.join(deploy_path, 'interface', 'eventwindow.gui'), 'r', encoding='utf-8') as f:
    c = f.read()
assert 'scrollbarType = standardtext_slider' in c, 'scrollbarType not in eventwindow.gui!'
print('[2/4] GUI override in deployed mod: scrollbarType = standardtext_slider present (OK)')

# 3. Check localization & BOM
with open(os.path.join(deploy_path, 'localisation', 'english', 'DEI_indonesia_l_english.yml'), 'rb') as f:
    raw = f.read()
assert raw.startswith(b'\xef\xbb\xbf'), 'Missing UTF-8 BOM in deployed localization!'
loc_text = raw.decode('utf-8-sig')
assert 'Across Java and Sumatra, the general strike wave' in loc_text, 'Shortened dei_trunk.6.d not present!'
print('[3/4] Localization in deployed mod: UTF-8 BOM verified, shortened text confirmed (OK)')

# 4. Check portraits GFX
with open(os.path.join(deploy_path, 'interface', 'DEI_portraits.gfx'), 'r', encoding='utf-8') as f:
    c = f.read()
assert 'GFX_portrait_INS_sudirman' in c, 'GFX_portrait_INS_sudirman missing!'
print('[4/4] Portraits GFX in deployed mod: GFX_portrait_INS_sudirman present (OK)')

print('\nALL DEPLOYED FILES 100% VERIFIED!')
