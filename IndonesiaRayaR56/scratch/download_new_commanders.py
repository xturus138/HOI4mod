import os, io, requests
from PIL import Image

output_dir = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\gfx\leaders\INS'
os.makedirs(output_dir, exist_ok=True)

headers = {'User-Agent': 'IndonesiaModBot/1.0 (radit@example.com)'}

downloads = {
    'portrait_INS_ahmad_yani.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3f/Ahmad_Yani.jpg/500px-Ahmad_Yani.jpg',
    'portrait_INS_ngurah_rai.dds': 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Gusti_ngurah_rai.jpg',
    'portrait_INS_tb_simatupang.dds': 'https://upload.wikimedia.org/wikipedia/commons/d/df/Djenderal_Major_TB_Simatupang.png',
    'portrait_INS_soengkono.dds': 'https://upload.wikimedia.org/wikipedia/commons/4/42/Col_Sungkono%2C_Kenang-Kenangan_Pada_Panglima_Besar_Letnan_Djenderal_Soedirman%2C_p27.jpg',
    'portrait_INS_john_lie.dds': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/John_Lie%2C_Jalesveva_Jayamahe%2C_p216.jpg',
    'portrait_INS_slamet_rijadi.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/5f/Zaterdag%2C_12_november_werd_in_het_stadion_te_Solo_een_grote_massabijeenkomst_geh%2C_Bestanddeelnr_924_%28Slamet_Rijadi%2C_cropped%29.jpg/500px-Zaterdag%2C_12_november_werd_in_het_stadion_te_Solo_een_grote_massabijeenkomst_geh%2C_Bestanddeelnr_924_%28Slamet_Rijadi%2C_cropped%29.jpg',
    'portrait_INS_djamin_ginting.dds': 'https://upload.wikimedia.org/wikipedia/commons/c/c0/Djamin_Ginting.jpg',
    'portrait_INS_djatikoesoemo.dds': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/07/Brigjen_TNI_GPH._Djatikoesoemo_%28cropped%29.jpg/500px-Brigjen_TNI_GPH._Djatikoesoemo_%28cropped%29.jpg'
}

for fname, url in downloads.items():
    out_path = os.path.join(output_dir, fname)
    try:
        print(f'Downloading {fname} from {url}...')
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        img = Image.open(io.BytesIO(r.content)).convert('RGBA')
        img = img.resize((156, 210), Image.Resampling.LANCZOS)
        img.save(out_path, format='DDS')
        print(f'Saved {fname} ({img.size}) as DDS')
    except Exception as e:
        print(f'Error processing {fname}: {e}')

print('ALL COMMANDER PORTRAITS PROCESSED.')
