from PIL import Image

p = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\event_news_bg.dds'
im = Image.open(p)
print('Format:', im.format, 'Size:', im.size, 'Mode:', im.mode)
im.save('scratch/event_news_bg.png')
print('Saved scratch/event_news_bg.png')
