from PIL import Image

p = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\event_report_bottom_win.dds'
im = Image.open(p)
print('Format:', im.format, 'Size:', im.size, 'Mode:', im.mode)
# Save a small PNG to inspect
im.save('scratch/bottom_win.png')
print('Saved scratch/bottom_win.png')
