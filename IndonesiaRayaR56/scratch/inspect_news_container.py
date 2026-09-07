with open('preview_app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('news-options-container')
print(text[idx-50:idx+400])
