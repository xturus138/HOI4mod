import os
from PIL import Image, ImageOps, ImageEnhance

target_w, target_h = 397, 153

def create_banner(src_path, dst_path, y_focus=0.5):
    im = Image.open(src_path).convert('RGB')
    w, h = im.size
    scale = max(target_w / w, target_h / h)
    nw, nh = int(w * scale), int(h * scale)
    im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
    
    top = int((nh - target_h) * y_focus)
    left = int((nw - target_w) / 2)
    top = max(0, min(top, nh - target_h))
    left = max(0, min(left, nw - target_w))
    
    cropped = im_resized.crop((left, top, left + target_w, top + target_h))
    gray = ImageOps.grayscale(cropped)
    contrast = ImageEnhance.Contrast(gray).enhance(1.15)
    sharp = ImageEnhance.Sharpness(contrast).enhance(1.2)
    final_img = sharp.convert('RGB')
    final_img.save(dst_path)
    print(f'Created {dst_path} ({target_w}x{target_h}) from {src_path}')

banners = [
    ('gfx/event_pictures/DEI_event_ikada.dds', 'gfx/event_pictures/DEI_news_event_strike.dds', 0.2),
    ('gfx/event_pictures/DEI_event_ambarawa.dds', 'gfx/event_pictures/DEI_news_event_mutiny.dds', 0.4),
    ('gfx/event_pictures/DEI_event_volksraad.dds', 'gfx/event_pictures/DEI_news_event_crisis.dds', 0.5),
    ('gfx/event_pictures/DEI_event_linggarjati.dds', 'gfx/event_pictures/DEI_news_event_underground.dds', 0.3),
    ('gfx/event_pictures/DEI_event_proklamasi.dds', 'gfx/event_pictures/DEI_news_event_threshold.dds', 0.3)
]

for src, dst, yf in banners:
    create_banner(src, dst, yf)

print('All 5 news banners created successfully!')
