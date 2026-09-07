with open('preview_app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('country-event')
if idx != -1:
    print('Found country-event:')
    print(text[idx-50:idx+600])
else:
    print('country-event not found, checking event classes...')
    import re
    print(re.findall(r'class="[^"]*event[^"]*"', text)[:10])
