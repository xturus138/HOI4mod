import os, io, requests
from PIL import Image

output_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\gfx\event_pictures'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://id.wikipedia.org/'
}

downloads = {
    'DEI_event_kmb.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/8/89/Ronde_Tafel_Conferentie_%2C_slotzitting_in_Ridderzaal%2C_Hatta_tekent%2C_Bestanddeelnr_903-6874.jpg/960px-Ronde_Tafel_Conferentie_%2C_slotzitting_in_Ridderzaal%2C_Hatta_tekent%2C_Bestanddeelnr_903-6874.jpg',
    'DEI_event_pertempuran_surabaya.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f0/IWM-SE-5865-tank-Surabaya-19451127.jpg/960px-IWM-SE-5865-tank-Surabaya-19451127.jpg',
    'DEI_event_ambarawa.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/cc/Ambarawa_waar_de_Republiek_opnieuw_probeert_de_bevolking_van_Indonesi%C3%AB_te_veron%2C_Bestanddeelnr_3920.jpg/960px-Ambarawa_waar_de_Republiek_opnieuw_probeert_de_bevolking_van_Indonesi%C3%AB_te_veron%2C_Bestanddeelnr_3920.jpg',
    'DEI_event_adisoetjipto.dds': 'https://upload.wikimedia.org/wikipedia/commons/8/83/Potret_Adisucipto.jpg',
    'DEI_event_pasteur.dds': 'https://upload.wikimedia.org/wikipedia/commons/e/ed/Bio_Farma_Bandung.jpg',
    'DEI_event_prambanan.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/66/Yogyakarta_Indonesia_Prambanan-temple-complex-02.jpg/960px-Yogyakarta_Indonesia_Prambanan-temple-complex-02.jpg',
    'DEI_event_tanjung_priok.dds': 'https://upload.wikimedia.org/wikipedia/commons/6/62/Tanjung_priok2.jpg',
    'DEI_event_ikada.dds': 'https://upload.wikimedia.org/wikipedia/commons/8/87/COLLECTIE_TROPENMUSEUM_Luchtfoto_van_het_stadion_waarin_de_opening_van_de_Nationale_Olympische_Week_%28Pekan_Olahraga_Nasional%29_te_Djakarta_plaatsvindt_TMnr_10017790.jpg',
    'DEI_event_linggarjati.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a7/%22LINGGADJATI%22_GETEKEND-PGM4011927.webm/500px--%22LINGGADJATI%22_GETEKEND-PGM4011927.webm.jpg',
    'DEI_event_pancasila.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d0/Garuda_Pancasila_Poster_%28color%29.jpg/960px-Garuda_Pancasila_Poster_%28color%29.jpg'
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

print('BATCH 2 DOWNLOAD COMPLETE.')
