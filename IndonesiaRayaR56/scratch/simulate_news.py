from PIL import Image, ImageDraw, ImageFont

bg = Image.open('scratch/event_news_bg.png').convert('RGBA')
draw = ImageDraw.Draw(bg)

# Draw simulated elements
# Title: y=260..290
draw.rectangle([(20, 260), (508, 290)], outline=(255, 0, 0, 200))

# Description: starts y=291, 10 lines (~180px) -> y=291..471
draw.rectangle([(39, 291), (499, 450)], outline=(0, 0, 255, 200))

# If bottom_Window is at 475:
# With options_grid at y = -35:
# Button 1: 475 - 35 = 440
# Button 2: 440 + 42 = 482
# Let's test with bottom_Window around 490:
# Button 1 at 455..497
# Button 2 at 497..539
draw.rectangle([(88, 455), (88 + 352, 455 + 42)], fill=(40, 50, 60, 200), outline=(200, 180, 100))
draw.rectangle([(88, 500), (88 + 352, 500 + 42)], fill=(40, 50, 60, 200), outline=(200, 180, 100))

bg.save('scratch/simulated_news.png')
print('Simulated layout saved to scratch/simulated_news.png!')
