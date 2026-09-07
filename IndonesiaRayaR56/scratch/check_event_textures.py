import os
from PIL import Image

# Find GFX_event_report_top_win in vanilla gfx
vanilla_gfx = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx'
for root, dirs, files in os.walk(vanilla_gfx):
    for f in files:
        if 'event_report_top_win' in f:
            full = os.path.join(root, f)
            im = Image.open(full)
            print('Found:', full, 'Size:', im.size)
        if 'event_report_tileable_midsection' in f:
            full = os.path.join(root, f)
            im = Image.open(full)
            print('Found midsection:', full, 'Size:', im.size)
        if 'event_report_bottom_win' in f:
            full = os.path.join(root, f)
            im = Image.open(full)
            print('Found bottom:', full, 'Size:', im.size)
