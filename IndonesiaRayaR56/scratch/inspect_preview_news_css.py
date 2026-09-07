with open('preview_app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.news-options')
if idx != -1:
    print(text[idx-50:idx+600])
else:
    print('news-options not found, looking for news-button...')
    idx = text.find('.news-button')
    print(text[idx-50:idx+600])
