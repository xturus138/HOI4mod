import re

with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\eventwindow.gui', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see if any instantTextBoxType has scrollbartype in eventwindow.gui
matches = re.findall(r'instantTextBoxType\s*=\s*\{[^}]*scrollbartype[^}]*\}', text, re.IGNORECASE)
print('Matches in eventwindow.gui:', matches)

with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\nationalfocusview.gui', 'r', encoding='utf-8') as f:
    nf_text = f.read()

matches2 = re.findall(r'instantTextBoxType\s*=\s*\{[^}]*scrollbartype[^}]*\}', nf_text, re.IGNORECASE)
print('Matches in nationalfocusview.gui (first 2):', matches2[:2])
