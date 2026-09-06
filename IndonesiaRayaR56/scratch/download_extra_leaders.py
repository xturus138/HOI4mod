import os, subprocess
from PIL import Image

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
leaders_dir = os.path.join(mod_dir, "gfx", "leaders", "INS")
scratch_dir = os.path.join(mod_dir, "scratch", "tmp_downloads")

os.makedirs(leaders_dir, exist_ok=True)
os.makedirs(scratch_dir, exist_ok=True)

targets = [
    ("sultan_hamid_ii", "https://upload.wikimedia.org/wikipedia/commons/3/37/Syarif_Hamid_II_of_Pontianak.jpg"),
    ("hamengkubuwono_ix", "https://upload.wikimedia.org/wikipedia/commons/8/8b/Hamengku_Buwono_IX_%281973%29.jpg"),
    ("wahid_hasyim", "https://upload.wikimedia.org/wikipedia/commons/f/f6/KHA_Wahid_Hasyim%2C_Pekan_Buku_Indonesia_1954%2C_p242.jpg"),
    ("soeharto", "https://upload.wikimedia.org/wikipedia/commons/7/7a/Jenderal_TNI_Soeharto.png"),
    ("maharaja_suryawikrama", "https://upload.wikimedia.org/wikipedia/commons/a/a2/COLLECTIE_TROPENMUSEUM_Portret_van_de_Soesoehoenan_van_Soerakarta_TMnr_10001903.jpg")
]

for name, url in targets:
    tmp_path = os.path.join(scratch_dir, f"{name}.jpg" if not url.endswith('.png') else f"{name}.png")
    out_dds = os.path.join(leaders_dir, f"portrait_INS_{name}.dds")
    
    print(f"Downloading {name}...")
    cmd = ["curl.exe", "-A", "HOI4SubmodBot/1.0 (contact: bot@hoi4indonesia.org)", "-L", "-o", tmp_path, url]
    subprocess.run(cmd, check=True)
    
    # Process portrait
    target_w, target_h = 156, 210
    with Image.open(tmp_path) as im:
        im = im.convert("RGBA")
        w, h = im.size
        target_ratio = target_w / target_h
        current_ratio = w / h

        if current_ratio > target_ratio:
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            im = im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / target_ratio)
            im = im.crop((0, 0, w, new_h))

        im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im.save(out_dds)
        print(f"Saved portrait_INS_{name}.dds (156x210)")

print("Extra leaders download and conversion complete!")
