import glob, os
from PIL import Image
import numpy as np

def make_feather_mask(w, h, border=12):
    alpha = np.ones((h, w), dtype=np.float32) * 255.0
    for y in range(h):
        for x in range(w):
            dx = min(x, w - 1 - x)
            dy = min(y, h - 1 - y)
            d = min(dx, dy)
            if d < border:
                factor = d / border
                # Smooth curve (Hermite / smoothstep)
                factor = factor * factor * (3.0 - 2.0 * factor)
                alpha[y, x] = factor * 255.0
    return alpha

def process_all():
    files = glob.glob('gfx/event_pictures/DEI_event_*.dds')
    print(f'Processing {len(files)} event pictures...')
    mask = make_feather_mask(210, 176, border=10)
    
    for f in files:
        im = Image.open(f).convert('RGBA')
        if im.size != (210, 176):
            print(f'Skipping {f}, size is {im.size}')
            continue
        arr = np.array(im, dtype=np.float32)
        arr[:, :, 3] = mask
        out = Image.fromarray(arr.astype(np.uint8), mode='RGBA')
        out.save(f)
        print(f'Feathered: {os.path.basename(f)}')

if __name__ == '__main__':
    process_all()
