import os, math
from PIL import Image, ImageOps, ImageDraw, ImageFilter, ImageEnhance

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
events_dir = os.path.join(mod_dir, "gfx", "event_pictures")
goals_dir = os.path.join(mod_dir, "gfx", "interface", "goals")
tech_dir = os.path.join(mod_dir, "gfx", "interface", "technologies")
vanilla_tech_dir = r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\technologies"

os.makedirs(goals_dir, exist_ok=True)
os.makedirs(tech_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. PROCESS FOCUS GOALS (82x82 Circular Medal Badge, Grayish)
# -------------------------------------------------------------

goal_mappings = {
    "focus_dei_pax_neerlandica": "DEI_event_volksraad.dds",
    "focus_dei_pembangkangan": "DEI_event_zeven_provincien.dds",
    "focus_dei_momentum_kemerdekaan": "DEI_event_ikada.dds",
    "focus_dei_proklamasi": "DEI_event_proklamasi.dds",
    "focus_dei_tkr": "DEI_event_ambarawa.dds",
    "focus_dei_kaa_bandung": "DEI_event_kaa_bandung.dds",
    "focus_dei_trikora": "DEI_event_path_a.dds",
    "focus_dei_dwikora": "DEI_event_pertempuran_surabaya.dds",
    "focus_dei_pancasila": "DEI_event_pancasila.dds",
    "focus_dei_trisakti": "DEI_event_linggarjati.dds",
    "focus_dei_dekrit_presiden": "DEI_event_dekrit.dds",
    "focus_dei_sidang_bfo": "DEI_event_path_b.dds",
    "focus_dei_angkatan_federal": "DEI_event_tanjung_priok.dds",
    "focus_dei_perkebunan_deli": "DEI_event_ombilin.dds",
    "focus_dei_swapraja": "DEI_event_kmb.dds",
    "focus_dei_angkatan_kelima": "DEI_event_path_c.dds",
    "focus_dei_lekra": "DEI_event_tamansiswa.dds",
    "focus_dei_komune_tani": "DEI_event_karapan_sapi.dds",
    "focus_dei_pakta_asia_merah": "DEI_event_kongres_perempuan.dds",
    "focus_dei_dewan_revolusi": "DEI_event_path_d.dds",
    "focus_dei_benteng_samudra": "DEI_event_pasteur.dds",
    "focus_dei_dwifungsi": "DEI_event_bosscha.dds",
    "focus_dei_bela_negara": "DEI_event_sumpah_pemuda.dds",
    "focus_dei_baitul_mal": "DEI_event_path_e.dds",
    "focus_dei_mahkamah_syariah": "DEI_event_adisoetjipto.dds",
    "focus_dei_akademi_mujahidin": "DEI_event_kartosuwiryo.dds",
    "focus_dei_khilafah_nusantara": "DEI_event_prambanan.dds",
    "focus_dei_sumpah_palapa": "DEI_event_borobudur.dds",
    "focus_dei_restorasi_trowulan": "DEI_event_trowulan.dds",
    "focus_dei_dharmaputra": "DEI_event_trunk6.dds",
    "focus_dei_jung_raksasa": "DEI_event_pinisi.dds",
    "focus_dei_penobatan_maharaja": "DEI_event_path_f.dds"
}

def create_goal_badge(src_dds_path, out_dds_path):
    # Base size 82x82
    size = 82
    center = size / 2.0
    outer_r = 38.0
    inner_r = 34.0

    # Load and crop source image
    with Image.open(src_dds_path) as im:
        im = im.convert("RGBA")
        w, h = im.size
        # Square crop from center
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        sq = im.crop((left, top, left + min_dim, top + min_dim))
        sq = sq.resize((size, size), Image.Resampling.LANCZOS)

    # Convert source to pure grayish
    gray_data = []
    enhancer = ImageEnhance.Contrast(sq)
    sq = enhancer.enhance(1.25)
    for p in sq.getdata():
        g = int(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2])
        gray_data.append((g, g, g, 255))
    sq.putdata(gray_data)

    # Create badge canvas with circular frame
    badge = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    pixels = []
    for y in range(size):
        for x in range(size):
            dx = x - center + 0.5
            dy = y - center + 0.5
            dist = math.hypot(dx, dy)

            if dist > outer_r + 1.0:
                # Outside badge
                pixels.append((0, 0, 0, 0))
            elif dist > outer_r:
                # Anti-aliased outer edge
                alpha = int(255 * (1.0 - (dist - outer_r)))
                val = 140
                pixels.append((val, val, val, alpha))
            elif dist >= inner_r:
                # Metallic double-bevel bezel ring
                # subtle gradient from top-left to bottom-right
                angle_factor = (dx - dy) / (2.0 * outer_r)
                if dist > outer_r - 2.0 or dist < inner_r + 2.0:
                    val = int(180 + 40 * angle_factor) # bright rim
                else:
                    val = int(110 + 30 * angle_factor) # groove
                val = max(50, min(230, val))
                pixels.append((val, val, val, 255))
            else:
                # Inside picture area with subtle vignette
                vignette = 1.0 - 0.25 * (dist / inner_r) ** 2
                sp = sq.getpixel((x, y))
                val = int(sp[0] * vignette)
                val = max(10, min(245, val))
                pixels.append((val, val, val, 255))

    badge.putdata(pixels)
    badge.save(out_dds_path)
    print(f"Created goal icon: {os.path.basename(out_dds_path)} (82x82)")

print("=== Generating Focus Goals ===")
for goal_name, src_file in goal_mappings.items():
    src_path = os.path.join(events_dir, src_file)
    dst_path = os.path.join(goals_dir, f"{goal_name}.dds")
    if os.path.exists(src_path):
        create_goal_badge(src_path, dst_path)
    else:
        print(f"Warning: source missing {src_path}")


# -------------------------------------------------------------
# 2. PROCESS TECHNOLOGIES (120x50 RGBA, Grayish)
# -------------------------------------------------------------

tech_mappings = {
    # Infantry Weapons
    "INS_infantry_weapons": "infantry_equipment_0.dds",      # Level 0 (GW)
    "INS_infantry_weapons1": "infantry_weapons.dds",          # Level 1
    "INS_improved_infantry_weapons": "infantry_weapons2.dds", # Level 2
    "INS_advanced_infantry_weapons": "infantry_weapons3.dds", # Level 3
    "INS_tech_support": "support_equipment_1.dds",            # Support equipment
    "INS_motorised_infantry": "motorized_equipment_1.dds",    # Motorized

    # Artillery
    "INS_gw_artillery": "artillery1.dds",                     # GW Artillery
    "INS_artillery1": "artillery1.dds",                       # Artillery 1
    "INS_interwar_antiair": "antiair1.dds",                   # AA
    "INS_interwar_antitank": "antitank1.dds",                 # AT

    # Armor
    "INS_gwtank": "gwtank.dds",                               # Carden-Loyd Mk VI
    "INS_basic_light_tank": "basic_light_tank.dds",           # Stuart M3A3
    "INS_improved_light_tank": "improved_light_tank.dds",     # AMX-13

    # Air
    "INS_fighter1": "fighter1.dds",                           # Ki-43 / Cureng
    "INS_fighter2": "fighter2.dds",                           # P-51D Mustang
    "INS_early_bomber": "early_bomber.dds",                   # Martin B-10
    "INS_transport_plane": "transport_plane_1.dds",           # C-47 Seulawah

    # Naval
    "INS_early_destroyer": "early_destroyer.dds",             # KRI Gadjah Mada
    "INS_early_submarine": "early_submarine.dds",             # KRI Tjakra / Nanggala
    "INS_early_light_cruiser": "advanced_light_cruiser.dds"   # KRI Irian / Hr.Ms. De Ruyter
}

def create_tech_icon(src_dds_path, out_dds_path):
    target_w, target_h = 120, 50
    with Image.open(src_dds_path) as im:
        im = im.convert("RGBA")
        # Fit inside target dimensions while preserving aspect ratio
        orig_w, orig_h = im.size
        ratio = min((target_w - 6) / orig_w, (target_h - 6) / orig_h)
        new_w = max(1, int(orig_w * ratio))
        new_h = max(1, int(orig_h * ratio))
        resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)

        # Place onto 120x50 transparent canvas
        canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
        offset_x = (target_w - new_w) // 2
        offset_y = (target_h - new_h) // 2
        canvas.paste(resized, (offset_x, offset_y), resized)

        # Convert to pure monochrome grayish
        pixels = []
        for p in canvas.getdata():
            if p[3] == 0:
                pixels.append((0, 0, 0, 0))
            else:
                g = int(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2])
                # slight contrast enhancement
                g = int(128 + 1.2 * (g - 128))
                g = max(0, min(255, g))
                pixels.append((g, g, g, p[3]))
        canvas.putdata(pixels)
        canvas.save(out_dds_path)
        print(f"Created tech icon: {os.path.basename(out_dds_path)} (120x50)")

print("\n=== Generating Technologies ===")
for tech_name, vanilla_file in tech_mappings.items():
    src_path = os.path.join(vanilla_tech_dir, vanilla_file)
    dst_path = os.path.join(tech_dir, f"{tech_name}.dds")
    if os.path.exists(src_path):
        create_tech_icon(src_path, dst_path)
    else:
        print(f"Warning: vanilla tech missing {src_path}")

print("\nAll assets generated successfully.")
