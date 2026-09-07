with open('interface/eventwindow.gui', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('name = "EventWindow_Operative"')
print(text[idx+800:idx+1800])
