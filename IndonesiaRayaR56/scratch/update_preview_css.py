with open('preview_app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_photo_css = '''.clipboard-photo-container {
      float: left;
      margin: 0 1.2rem 0.6rem 0;
      width: 210px;
      height: 176px;
      position: relative;
    }

    .paperclip-icon {
      position: absolute;
      top: 15px;
      left: -8px;
      width: 20px;
      height: 38px;
      border: 3px solid #8c939e;
      border-radius: 10px;
      border-bottom: none;
      z-index: 10;
      box-shadow: 1px 1px 2px rgba(0,0,0,0.4);
    }'''

new_photo_css = '''.clipboard-photo-container {
      margin: 0.5rem auto 1.2rem auto;
      width: 210px;
      height: 176px;
      position: relative;
      display: block;
      text-align: center;
    }

    .paperclip-icon {
      display: none;
    }'''

assert old_photo_css in text, "old_photo_css not found!"
text = text.replace(old_photo_css, new_photo_css)

with open('preview_app/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('preview_app/index.html updated: photo centered at top, paperclip hidden!')
