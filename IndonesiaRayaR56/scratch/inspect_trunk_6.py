with open('events/DEI_00_shared_trunk_events.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id = dei_trunk.6')
print(text[idx:idx+1800])
