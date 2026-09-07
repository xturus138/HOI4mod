with open('preview_app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_css = '''.news-button {
      display: block;'''

new_css = '''#news-options-container {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      margin-top: 1rem;
    }

    .news-button {
      display: block;'''

if '#news-options-container {' not in text:
    text = text.replace(old_css, new_css, 1)
    with open('preview_app/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated preview_app/index.html with #news-options-container flex gap!')
else:
    print('#news-options-container already present!')
