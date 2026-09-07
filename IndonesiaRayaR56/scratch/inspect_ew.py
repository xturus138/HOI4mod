with open('interface/eventwindow.gui', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('name = "EventWindow"')
print(text[idx:idx+1800])
