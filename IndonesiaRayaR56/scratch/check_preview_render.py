with open('preview_app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('renderEvent(')
if idx == -1:
    idx = text.find('function showEvent')
if idx == -1:
    idx = text.find('event-preview')
if idx != -1:
    print(text[idx:idx+800])
else:
    print('Event rendering function not found directly by name, searching render...')
    import re
    print(re.findall(r'function\s+[a-zA-Z0-9_]*event[a-zA-Z0-9_]*', text, re.IGNORECASE))
