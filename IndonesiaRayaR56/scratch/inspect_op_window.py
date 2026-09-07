with open('interface/eventwindow.gui', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('name = "EventWindow_Operative"')
if idx != -1:
    print(text[idx:idx+1500])
else:
    print('EventWindow_Operative not found')
