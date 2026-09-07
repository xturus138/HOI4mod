with open('preview_app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="clipboard-view"')
print(text[idx-50:idx+800])
