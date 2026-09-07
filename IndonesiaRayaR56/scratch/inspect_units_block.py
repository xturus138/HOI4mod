with open('history/units/DEI_templates.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('units = {')
if idx != -1:
    print('Found units block in DEI_templates.txt:')
    print(text[idx:idx+1500])
else:
    print('No units block in DEI_templates.txt, only templates!')
