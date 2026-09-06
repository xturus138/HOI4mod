import os
import urllib.request
from PIL import Image, ImageOps

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
leaders_dir = os.path.join(mod_dir, "gfx", "leaders", "INS")
goals_dir = os.path.join(mod_dir, "gfx", "interface", "goals")
tech_dir = os.path.join(mod_dir, "gfx", "interface", "technologies")

os.makedirs(leaders_dir, exist_ok=True)
os.makedirs(goals_dir, exist_ok=True)
os.makedirs(tech_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) HOI4AssetTool/1.0'}

def download_image(url, dest_path):
    print(f"Downloading {url} ...")
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        with open(dest_path, "wb") as f:
            f.write(resp.read())

def process_portrait(src_img_path, out_dds_path):
    # HOI4 Leader portrait: 156 x 210
    target_w, target_h = 156, 210
    with Image.open(src_img_path) as im:
        im = im.convert("RGBA")
        w, h = im.size
        target_ratio = target_w / target_h
        current_ratio = w / h

        if current_ratio > target_ratio:
            # image is wider: crop sides
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            im = im.crop((left, 0, left + new_w, h))
        else:
            # image is taller: crop bottom (keep top for faces)
            new_h = int(w / target_ratio)
            im = im.crop((0, 0, w, new_h))

        im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im.save(out_dds_path)
        print(f"Saved portrait {out_dds_path} (156x210)")

def process_focus_icon(src_img_path, out_dds_path):
    # HOI4 Goal/Focus icon: 82 x 82 (or 128x128)
    target_w, target_h = 82, 82
    with Image.open(src_img_path) as im:
        im = im.convert("RGBA")
        im = ImageOps.fit(im, (target_w, target_h), method=Image.Resampling.LANCZOS)
        im.save(out_dds_path)
        print(f"Saved focus icon {out_dds_path} (82x82)")

def process_tech_icon(src_img_path, out_dds_path):
    # HOI4 Equipment icon: 120 x 50
    target_w, target_h = 120, 50
    with Image.open(src_img_path) as im:
        im = im.convert("RGBA")
        im = ImageOps.fit(im, (target_w, target_h), method=Image.Resampling.LANCZOS)
        im.save(out_dds_path)
        print(f"Saved tech icon {out_dds_path} (120x50)")

portraits = [
    ("yos_sudarso", "https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1e/Josaphat_Soedarso%2C_Jalesveva_Jayamahe%2C_p28.jpg/500px-Josaphat_Soedarso%2C_Jalesveva_Jayamahe%2C_p28.jpg"),
    ("suryadi_suryadarma", "https://thumb.wikimedia.org/wikipedia/commons/thumb/0/04/Suryadarma.jpg/500px-Suryadarma.jpg"),
    ("halim_perdanakusuma", "https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d1/Halim_Perdanakusuma.jpg/500px-Halim_Perdanakusuma.jpg"),
    ("re_martadinata", "https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2c/R.E_Martadinata_colorized_by_colorbykevin.jpg/500px-R.E_Martadinata_colorized_by_colorbykevin.jpg"),
    ("moestopo", "https://upload.wikimedia.org/wikipedia/id/3/3e/Prof-Dr-Moestopo1.jpg")
]

focus_icons = [
    ("focus_dei_itb_bandung", "https://upload.wikimedia.org/wikipedia/commons/d/da/COLLECTIE_TROPENMUSEUM_Technische_Hogeschool_aan_het_IJzermanpark_te_Bandung_Java_TMnr_10002359.jpg"),
    ("focus_dei_radar_nusantara", "https://thumb.wikimedia.org/wikipedia/commons/thumb/2/26/COLLECTIE_TROPENMUSEUM_Malabar_Radiostation_op_de_Malabarberg_TMnr_10006813.jpg/500px-COLLECTIE_TROPENMUSEUM_Malabar_Radiostation_op_de_Malabarberg_TMnr_10006813.jpg"),
    ("focus_dei_kilang_minyak", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Braat_overvalwagen_van_de_stadswacht%2C_vermoedelijk_op_Java%2C_KITLV_179148.tiff/lossy-page1-500px-Braat_overvalwagen_van_de_stadswacht%2C_vermoedelijk_op_Java%2C_KITLV_179148.tiff.jpg")
]

tech_icons = [
    ("INS_braat_overvalwagen", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Braat_overvalwagen_van_de_stadswacht%2C_vermoedelijk_op_Java%2C_KITLV_179148.tiff/lossy-page1-500px-Braat_overvalwagen_van_de_stadswacht%2C_vermoedelijk_op_Java%2C_KITLV_179148.tiff.jpg"),
    ("INS_marmon_herrington_ctls", "https://upload.wikimedia.org/wikipedia/commons/e/e5/Marmon_Herrington_Tanks_LOC_fsa_8e09169u.jpg"),
    ("INS_cw21_demon", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Curtiss-Wright_CW-21_%28photo%29.jpg/500px-Curtiss-Wright_CW-21_%28photo%29.jpg"),
    ("INS_b25_mitchell", "https://upload.wikimedia.org/wikipedia/commons/8/8f/North_American_B-25_Mitchell_G%C3%B3raszka_2007.jpg")
]

scratch_dir = os.path.join(mod_dir, "scratch", "tmp_downloads")
os.makedirs(scratch_dir, exist_ok=True)

# Process Portraits
for name, url in portraits:
    tmp_path = os.path.join(scratch_dir, f"{name}.jpg")
    out_dds = os.path.join(leaders_dir, f"portrait_INS_{name}.dds")
    try:
        download_image(url, tmp_path)
        process_portrait(tmp_path, out_dds)
    except Exception as e:
        print(f"Error processing portrait {name}: {e}")

# Process Focus Icons
for name, url in focus_icons:
    tmp_path = os.path.join(scratch_dir, f"{name}.jpg")
    out_dds = os.path.join(goals_dir, f"{name}.dds")
    try:
        download_image(url, tmp_path)
        process_focus_icon(tmp_path, out_dds)
    except Exception as e:
        print(f"Error processing focus icon {name}: {e}")

# Process Tech Icons
for name, url in tech_icons:
    tmp_path = os.path.join(scratch_dir, f"{name}.jpg")
    out_dds = os.path.join(tech_dir, f"{name}.dds")
    try:
        download_image(url, tmp_path)
        process_tech_icon(tmp_path, out_dds)
    except Exception as e:
        print(f"Error processing tech icon {name}: {e}")

print("Asset download and processing pipeline completed successfully.")
