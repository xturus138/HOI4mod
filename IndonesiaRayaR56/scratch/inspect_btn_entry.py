import os
from PIL import Image

vanilla_gfx = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx'
for root, dirs, files in os.walk(vanilla_gfx):
    for f in files:
        if 'event_option_entry' in f:
            full = os.path.join(root, f)
            try:
                im = Image.open(full)
                print('Found:', full, 'Size:', im.size)
            except Exception as e:
                print(full, e)
