import os, io, requests
from PIL import Image

output_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\gfx\event_pictures'
os.makedirs(output_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://id.wikipedia.org/'
}

downloads = {
    'DEI_event_proklamasi.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f1/Indonesia_declaration_of_independence_17_August_1945.jpg/960px-Indonesia_declaration_of_independence_17_August_1945.jpg',
    'DEI_event_trunk6.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f1/Indonesia_declaration_of_independence_17_August_1945.jpg/960px-Indonesia_declaration_of_independence_17_August_1945.jpg',
    'DEI_event_path_a.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f1/Indonesia_declaration_of_independence_17_August_1945.jpg/960px-Indonesia_declaration_of_independence_17_August_1945.jpg',
    'DEI_event_kaa_bandung.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/02/Plenary_session_during_the_Bandung_Conference.png/960px-Plenary_session_during_the_Bandung_Conference.png',
    'DEI_event_borobudur.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/2/25/Pradaksina.jpg/960px-Pradaksina.jpg',
    'DEI_event_dekrit.dds': 'https://upload.wikimedia.org/wikipedia/commons/a/af/1959_Sukarno%27s_Presidential_Decree.jpg',
    'DEI_event_trowulan.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fb/Bajang_Ratu_Gate_Trowulan.jpg/960px-Bajang_Ratu_Gate_Trowulan.jpg',
    'DEI_event_path_f.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fb/Bajang_Ratu_Gate_Trowulan.jpg/960px-Bajang_Ratu_Gate_Trowulan.jpg',
    'DEI_event_pinisi.dds': 'https://upload.wikimedia.org/wikipedia/commons/e/e6/COLLECTIE_TROPENMUSEUM_Haven_te_Makassar_Zuid-Celebes_TMnr_10007907.jpg',
    'DEI_event_bosscha.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7f/Bosscha_001.JPG/960px-Bosscha_001.JPG',
    'DEI_event_zeven_provincien.dds': 'https://upload.wikimedia.org/wikipedia/commons/0/0b/COLLECTIE_TROPENMUSEUM_%27Het_schip_%27De_Zeven_Provinci%C3%ABn%27_in_de_Straat_van_Malakka_met_erboven_een_vliegtuig%27_TMnr_10002144.jpg',
    'DEI_event_tamansiswa.dds': 'https://upload.wikimedia.org/wikipedia/commons/2/22/COLLECTIE_TROPENMUSEUM_%27De_heer_Soerjoadipoetro_houdt_een_voordracht_over_de_school_van_Tagore_voor_o.a._kwekelingen_van_het_Nationaal_Onderwijs_Instituut_%27Taman_Siswa%27_te_Bandung_Java%27_TMnr_10002308.jpg',
    'DEI_event_ombilin.dds': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/COLLECTIE_TROPENMUSEUM_Een_ingang_van_de_Ombilin_steenkoolmijnen_TMnr_20018524.jpg',
    'DEI_event_karapan_sapi.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/89/Sapi_Brujul_Probolinggo.jpg/960px-Sapi_Brujul_Probolinggo.jpg',
    'DEI_event_volksraad.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/41/Gedpancasila.jpg/960px-Gedpancasila.jpg',
    'DEI_event_sumpah_pemuda.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/30/Historical_Indonesian_Youth_Pledge%2C_Sumpah_Pemuda_in_1928.jpg/960px-Historical_Indonesian_Youth_Pledge%2C_Sumpah_Pemuda_in_1928.jpg',
    'DEI_event_kartosuwiryo.dds': 'https://upload.wikimedia.org/wikipedia/commons/d/d6/Kartosuwirjo_17_August_1950_KR.jpg',
    'DEI_event_path_e.dds': 'https://upload.wikimedia.org/wikipedia/commons/d/d6/Kartosuwirjo_17_August_1950_KR.jpg',
    'DEI_event_kongres_perempuan.dds': 'https://upload.wikimedia.org/wikipedia/commons/8/8a/Congres_Perempoean_Indonesia_%281928%29.jpg',
}

target_w, target_h = 456, 228

for fname, url in downloads.items():
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code != 200:
            print(f'Failed {fname}: HTTP {r.status_code}')
            continue
        img = Image.open(io.BytesIO(r.content)).convert('RGB')
        
        # Center crop to 2:1 aspect ratio
        w, h = img.size
        aspect = target_w / target_h
        if w / h > aspect:
            new_w = int(h * aspect)
            left = (w - new_w) // 2
            img = img.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / aspect)
            top = (h - new_h) // 2
            img = img.crop((0, top, w, top + new_h))
            
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        out_path = os.path.join(output_dir, fname)
        img.save(out_path, format='DDS')
        print(f'Successfully processed & saved: {fname}')
    except Exception as e:
        print(f'Error processing {fname}: {e}')

print('ALL CUSTOM EVENT PICTURES DOWNLOADED AND PROCESSED.')
