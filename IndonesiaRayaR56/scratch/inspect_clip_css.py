with open('preview_app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.clipboard-window')
print(text[idx:idx+900])
