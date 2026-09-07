with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\eventwindow.gui', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'name\s*=\s*"Description"', text)]
print(f'Found {len(matches)} Description fields at indices {matches}:')
for idx in matches:
    print('---')
    print(text[idx-40:idx+250])
