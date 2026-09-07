with open('interface/eventwindow.gui', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('name = "EventWindow_News"')
idx2 = text.find('name = "options_grid"', idx)
print(text[idx2-50:idx2+250])
