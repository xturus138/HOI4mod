from PIL import Image

p = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\event_report_bottom_win_2.dds'
im = Image.open(p)
print('Format:', im.format, 'Size:', im.size, 'Mode:', im.mode)
im.save('scratch/bottom_win_2.png')
print('Saved scratch/bottom_win_2.png')
