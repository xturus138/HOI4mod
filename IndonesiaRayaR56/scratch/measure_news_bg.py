from PIL import Image

im = Image.open('scratch/event_news_bg.png')
w, h = im.size

# Look for darker horizontal line between y=400 and y=520
# Let's inspect rows around y=440..500
center_x = w // 2
for y in range(430, 520):
    pix = im.getpixel((center_x, y))
    # Check contrast with surrounding
    if pix[0] < 180: # significantly darker than paper (paper is ~220)
        print(f'Dark line detected at y = {y}: {pix}')
