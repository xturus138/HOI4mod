with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\eventwindow.gui', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(''.join(lines[530:570]))
