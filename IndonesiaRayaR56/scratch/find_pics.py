with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\eventwindow.gui', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'name\s*=\s*"event_picture"', text)]
print(f'Found {len(matches)} event_picture occurrences:')
for idx in matches:
    # find parent containerWindowType
    parent_idx = text.rfind('containerWindowType', 0, idx)
    print('Parent container:')
    print(text[parent_idx:parent_idx+120])
    print('Element:')
    print(text[idx-20:idx+150])
    print('---')
