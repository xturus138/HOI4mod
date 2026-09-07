with open(r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\national_focus\congo.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('autonomy_state = autonomy_free')
print(text[idx-200:idx+250])
