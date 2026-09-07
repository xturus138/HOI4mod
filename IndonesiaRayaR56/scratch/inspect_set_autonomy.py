with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\national_focus\australia.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('set_autonomy = {')
print(text[idx-50:idx+350])
