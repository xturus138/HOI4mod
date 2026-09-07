with open('events/DEI_00_shared_trunk_events.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('load_oob = DEI_templates')
print(text[idx-50:idx+600])
