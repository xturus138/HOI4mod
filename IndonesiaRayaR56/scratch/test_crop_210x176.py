import os, glob
from PIL import Image

events_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\gfx\event_pictures"
preview_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\scratch\preview_210x176"
os.makedirs(preview_dir, exist_ok=True)

target_w, target_h = 210, 176
target_aspect = target_w / target_h

# Special crop center-x offsets if needed (default 0.5 = center)
custom_center_x = {
    # e.g., 'DEI_event_proklamasi.dds': 0.45,
}

for f in sorted(glob.glob(os.path.join(events_dir, "*.dds"))):
    fn = os.path.basename(f)
    im = Image.open(f)
    w, h = im.size
    
    # Calculate crop box for 210x176 aspect ratio
    crop_h = h
    crop_w = int(h * target_aspect)
    if crop_w > w:
        crop_w = w
        crop_h = int(w / target_aspect)
        
    cx = custom_center_x.get(fn, 0.5)
    left = int((w - crop_w) * cx)
    left = max(0, min(w - crop_w, left))
    top = int((h - crop_h) * 0.5)
    
    cropped = im.crop((left, top, left + crop_w, top + crop_h))
    resized = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Save as PNG preview
    png_name = fn.replace('.dds', '.png')
    resized.save(os.path.join(preview_dir, png_name))
    print(f"Processed {fn}: crop_box=({left}, {top}, {left+crop_w}, {top+crop_h}) -> ({target_w}, {target_h})")

print("Previews generated.")
