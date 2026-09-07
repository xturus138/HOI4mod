import os, glob
from PIL import Image, ImageEnhance

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
events_dir = os.path.join(mod_dir, "gfx", "event_pictures")

target_w, target_h = 210, 176
target_aspect = target_w / target_h

files = sorted(glob.glob(os.path.join(events_dir, "*.dds")))
print(f"Resizing {len(files)} event pictures to {target_w}x{target_h} (HOI4 report event standard)...")

for f in files:
    fn = os.path.basename(f)
    im = Image.open(f).convert("RGB")
    w, h = im.size
    
    # Calculate crop box for 210x176 aspect ratio
    crop_h = h
    crop_w = int(h * target_aspect)
    if crop_w > w:
        crop_w = w
        crop_h = int(w / target_aspect)
        
    left = (w - crop_w) // 2
    top = (h - crop_h) // 2
    
    cropped = im.crop((left, top, left + crop_w, top + crop_h))
    resized = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Ensure 100% grayish monochrome & crisp archival contrast
    enhancer = ImageEnhance.Contrast(resized)
    resized = enhancer.enhance(1.15)
    
    pixels = []
    for r, g, b in resized.getdata():
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        pixels.append((gray, gray, gray))
    resized.putdata(pixels)
    
    # Save as DDS
    resized.save(f, format="DDS")
    print(f"Saved {fn}: {resized.size} pure grayish DDS")

print("All event pictures successfully resized to 210x176!")
