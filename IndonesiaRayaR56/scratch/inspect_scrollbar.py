with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\nationalfocusview.gui', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'standardtext_slider' in line:
        print(f'Line {i+1}:')
        print(''.join(lines[max(0, i-10):min(len(lines), i+10)]))
        break
