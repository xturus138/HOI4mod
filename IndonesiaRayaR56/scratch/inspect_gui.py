with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\eventwindow.gui', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'name\s*=\s*"([^"]+)"', text)
print('Names in eventwindow.gui:', matches[:15])

# Find EventWindow definition
idx = text.find('"EventWindow"')
if idx != -1:
    print('EventWindow found:')
    print(text[idx-50:idx+600])
