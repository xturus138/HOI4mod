agents_file = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\AGENTS.md'

with open(agents_file, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Struktur Konten v1.3', 'Struktur Konten v1.4.1 (Dynamic Ideological Naming & Multi-Option Customization)')
old_sec7 = '7. **Lokalisasi Alutsista & Doktrin (832 Kunci):**'
new_sec7 = '''7. **Sistem Nomenklatur Dinamis & Kustomisasi Ideologi (18 Proklamasi Negara):**
   - 18 Cosmetic Tags & Map Colors (3 opsi penamaan resmi per ideologi via Decisions "Tata Kelola dan Penamaan Resmi Negara").
   - 24 Grup Namelist Kapal dengan prefix spesifik: KRI (Republik), Hr.Ms. (Kolonial), KPR (Komunis), KRI (Otoriter), KNI (Islamis), JPS/KMN (Majapahit).
   - 6 Dedicated Starter Navy OOBs di Surabaya yang otomatis dimuat sesuai jalur yang dipilih di event `dei_trunk.6`.
   - 11 Grup Namelist Divisi AD (TNI, Laskar, KKO, KNIL, TMRI, TII, Bhayangkara, RPKAD, Panser, Garnizun, Dewan Revolusi).
   - 108 bendera kosmetik TGA tersinkronisasi di folder standar, medium, dan small.

8. **Lokalisasi Alutsista, Doktrin & Identitas Negara (1.020 Kunci):**'''

text = text.replace(old_sec7, new_sec7)

with open(agents_file, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated AGENTS.md successfully.')
