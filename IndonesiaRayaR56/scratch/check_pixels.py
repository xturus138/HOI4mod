from PIL import Image

im = Image.open('scratch/bottom_win.png')
# Check if left side (where photo was, x=5..215, y=5..180) has any special graphics or if it's plain paper
print('Pixel at (50, 50):', im.getpixel((50, 50)))
print('Pixel at (300, 50):', im.getpixel((300, 50)))
print('Pixel at (50, 150):', im.getpixel((50, 150)))
print('Pixel at (300, 150):', im.getpixel((300, 150)))
