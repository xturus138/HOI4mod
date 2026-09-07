# AGENTS.md — Submod HOI4 "Indonesia Raya: Road to Merdeka" (R56)

Dokumen memori kerja dan aturan preferensi permanen untuk semua sesi agen Antigravity berikutnya pada workspace ini.

---

## 1. Identitas & Arsitektur Proyek

- **Nama Mod:** Indonesia Raya: Road to Merdeka
- **Target Engine / Dependency:** Hearts of Iron IV (Steam version) + **The Road to 56 (R56)**.
- **Lokasi Proyek:** `c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56`
- **Tag Negara:**
  - Di base game dan Road to 56, tag negara Hindia Belanda / Indonesia adalah **`INS`** (bukan `DEI`).
  - Definisi pohon fokus memiliki bobot override:
    ```pdx
    focus_tree = {
        id = dei_focus_tree
        country = {
            factor = 0
            modifier = {
                add = 50
                tag = INS
            }
        }
        default = no
        ...
    }
    ```
  - Semua bendera disimpan dalam dua set: `INS*.tga` dan `DEI*.tga` (folder standar, medium, dan small).

---

## 2. Struktur Konten v1.0.0 (Canonical Release & Complete Visual Assets)

1. **Pohon Fokus Hibrida Terpadu (134 Fokus Total dalam 1 Master File):**
   - Disatukan dalam `common/national_focus/DEI_indonesia_focus_tree.txt` (mencegah bug Clausewitz yang mengabaikan deklarasi focus_tree duplikat di file terpisah).
   - **Batang Prolog Krisis 1936 (3 Fokus, 84 Hari, X=12, Y=0..8):**
     1. *Fracture of the Pax Neerlandica* (28 hari, Jan 1936 — krisis ekonomi & pemogokan umum).
     2. *Military and Popular Defiance* (28 hari, Feb 1936 — pembangkangan barak KNIL & barisan pemuda).
     3. *Momentum of the 1936 National Revolution* (28 hari, Mar 1936 — proklamasi kemerdekaan meletus, membuka 6 jalur).
   - **Jalur A — Republik Demokratis (16 Fokus, X=0..4):** (+KAA Bandung, Trikora, Dekrit Presiden, Dwikora, Pancasila, Trisakti)
   - **Jalur B — Kolonial/Federalis (14 Fokus, X=4..7):** (+Sidang BFO, Angkatan Federal, Pakta ANZAC, Deli, Swapraja, Free Ports)
   - **Jalur C — Komunis (14 Fokus, X=8..11):** (+Komune Tani, Sita Aset Asing, Angkatan Kelima, LEKRA, Pakta Asia Merah, Semesta)
   - **Jalur D — Otoriter Militeristik (14 Fokus, X=12..15):** (+Dewan Revolusi, Dwifungsi ABRI, Benteng Samudra, Bela Negara, Selat Malaka, Hegemoni Selatan)
   - **Jalur E — Islamis / NII (14 Fokus, X=16..18):** (+Baitul Mal, Mahkamah Syariah, Akademi Mujahidin, Anti-Riba, Liga Muslim, Khilafah Nusantara)
   - **Jalur F — Kemaharajaan Majapahit [Ahistoris] (13 Fokus, X=19..22):** (+Sumpah Palapa Baru, Restorasi Trowulan, Dharmaputra, Jung Raksasa, Kutaramanawa, Penobatan Maharaja)
   - **Cabang Industri & Riset Canggih (18 Fokus, X=26..30, Y=0..8):** (+ITB Bandung [5th Research Slot], Radar & Telekomunikasi, Metalurgi & Sintesis, Proyek Fisika Atom & Dirgantara)
   - **Cabang Militer AD / AU / AL R56 (28 Fokus, X=33..43):** (+Standardisasi Alutsista, Doktrin Wilayah Sishanrata, Pangkalan Udara, Armada Kepulauan)

2. **Karakter Pemimpin & Komandan Legendaris (Trait Unik):**
   - Di `common/characters/DEI_characters.txt` & `common/unit_leader/DEI_traits.txt`:
     - Soedirman (`trait_dei_sudirman`: Bapak TNI & Maestro Gerilya)
     - Urip Sumohardjo (`trait_dei_urip`: Arsitek Angkatan Bersenjata)
     - A.H. Nasution (`trait_dei_nasution`: Konseptor Perang Wilayah)
     - Alexander Evert Kawilarang (`trait_dei_kawilarang`: Panglima Pasukan Khusus)
     - Yos Sudarso (`trait_dei_yos_sudarso`: Macan Laut Kepulauan)
     - 19 potret komandan kustom (156x210) berformat vintage grayish monochrome 1930–1940.

3. **Sistem Divisi, Kapal & Templates OOB (14 Templates Doktrinal + 6 Dedicated Starter Navies):**
   - `common/units/names_divisions/INS_names_divisions.txt`: 11 grup namelist (TNI/Kodam, Laskar Rakyat, KKO Marinir, KNIL, Tentara Merah, TII, Bhayangkara Majapahit, Komando/RPKAD, Kavaleri Lapis Baja, Garnizun Pantai, Dewan Revolusi).
   - `common/units/names_ships/INS_names_ships.txt`: 24 grup namelist kapal dengan prefix historis murni (`KRI ` untuk Republik & Otoriter; `Hr.Ms. ` untuk Kolonial; nama agung klasik murni tanpa singkatan artifisial untuk Majapahit, Islamis, dan Komunis).
   - `history/units/DEI_templates.txt`: 14 Templat Doktrinal lengkap untuk 6 ideologi.
   - `history/units/`: 6 Dedicated Starter Naval OOBs di Pangkalan Surabaya (`DEI_navy_starter_a.txt` s/d `f.txt`) yang dimuat otomatis oleh event `dei_trunk.6` sesuai ideologi yang dipilih.
   - `history/units/DEI_air_starter.txt`: Starter Air Wings Lanud Andir & Iswahyudi (60x Fighters, 20x Tactical Bombers).
   - `events/DEI_00_shared_trunk_events.txt`: Event `dei_trunk.6` otomatis men-spawn starter army di pulau Jawa (5-6 divisi bersenjata per ideologi), memuat armada laut spesifik ideologi, skadron udara, dan menyuntikkan 3.000 senapan ke stockpile.

4. **Event Interaktif & Flavor Acak (124 Event Total):**
   - **98 Event Naratif Fokus:** di `DEI_00` s/d `DEI_07` (14-16 event interaktif per cabang ideologi + 5 event rangkaian krisis prolog 1936).
   - **26 Flavor Events Acak Berkala (Non-Focus MTTH):** di `events/DEI_flavor_events.txt` mencakup dinamika pers, panen kina/rempah, tambang Ombilin/Bangka, Bosscha, Lembaga Pasteur, Tamansiswa, Kongres Perempuan, debat Sukarno-Natsir, film Terang Boelan, Sumpah Pemuda, mutini De Zeven Provinciën, Borobudur, Karapan Sapi, penyelundupan Selat Malaka, Ratu Adil, Pinisi Dobo, penerbang Adisucipto, Laskar Putri, kilang Brandan.
   - 100% event memiliki gambar teruji (`picture = GFX_...`) dengan 32 berkas DDS arsip monokrom grayish.

5. **Aset Grafis Goals & Technologies (100% Grayish Vintage Monokrom):**
   - **Focus Goals:** 36 berkas DDS (82x82) di `gfx/interface/goals/` dan 36 sprite di `interface/DEI_goals.gfx`.
   - **Technologies & Equipment:** 24 berkas DDS (120x50) di `gfx/interface/technologies/` dan 55 sprite di `interface/DEI_technologies.gfx` (Bambu Runcing, Hembrug M.95, Pindad SP-1 & SS-1, Meriam TKR, Panser Braat, CTLS, Stuart M3, AMX-13, Cureng, Mustang Cocor Merah, C-47 Seulawah, KRI Gadjah Mada, KRI Tjakra, KRI Irian).

6. **Mega-Proyek Strategis, Pertahanan & Proklamasi Tata Kelola (25 Decisions Total):**
   - **Proklamasi Tata Kelola & Penamaan Negara (18 Decisions):** Kategori `dei_decisions_proclamations` memungkinkan pemain memilih 3 variasi bentuk negara, warna peta RGB, dan partai per ideologi.
   - **Arah Riset & Doktrin Strategis (8 Decisions):** Doktrin Gerilya Wilayah (Sishanrata), Doktrin Gerilya Selat Dangkal, Doktrin Dirgantara Khatulistiwa, Standardisasi Senjata Pindad, Panser Cepat Braat, Dirgantara IPTN, Eksplorasi Minyak Pertamina, Komisioning Armada KRI.
   - **Mega-Proyek Bangunan (6 Decisions):** Pangkalan Ujung Surabaya, Arsenal Bandung, Kilang Minyak Plaju & Balikpapan, Jalan Raya Pos & Rel Trans-Jawa, Benteng Selat Sunda/Malaka, Lanud Iswahyudi & Kalijati.
   - **Mekanik Militer Khusus (4 Decisions):** Sishanrata, Logistik Maritim Pinisi, Dapur Umum & Palang Merah, Pabrik Senjata Darurat Pegunungan.
   - **Kedaulatan Wilayah (7 Decisions):** Papua Barat, Timor Portugis, Borneo/Sarawak, Melayu Raya, Transmigrasi, ORI, Patroli Maritim.

7. **Industrial Concerns & Military Designers (R56 Integrated GFX):**
   - Pabrik Senjata Pindad & AI Bandung (Materiel)
   - Braat Machinefabriek Soerabaja (Tanks/Armor)
   - PT PAL & Droogdok Soerabaja (Naval)
   - IPTN & KNILM (Aircraft)
   - BPM / Pertamina (Refining)
   - Staatsspoorwegen & Bank Indonesia (Industrial/Economy)
   - ITB Bandung (Electronics & Radar)

8. **Sistem Nomenklatur Dinamis & Kustomisasi Ideologi (18 Proklamasi Negara):**
   - 18 Cosmetic Tags & Map Colors (3 opsi penamaan resmi per ideologi via Decisions "Tata Kelola dan Penamaan Resmi Negara").
   - 24 Grup Namelist Kapal dengan prefix spesifik: KRI (Republik), Hr.Ms. (Kolonial), KRI (Otoriter); nama murni tanpa akronim artifisial untuk Komunis, Islamis, dan Majapahit.
   - 6 Dedicated Starter Navy OOBs di Surabaya yang otomatis dimuat sesuai jalur yang dipilih di event `dei_trunk.6`.
   - 11 Grup Namelist Divisi AD (TNI, Laskar, KKO, KNIL, TMRI, TII, Bhayangkara, RPKAD, Panser, Garnizun, Dewan Revolusi).
   - 108 bendera kosmetik TGA tersinkronisasi di folder standar, medium, dan small.

9. **Lokalisasi Alutsista, Doktrin & Identitas Negara (1.217 Kunci):**
   - Varian alutsista: Panser Braat Overvalwagen, Marmon-Herrington CTLS-4TA, Stuart M3A3, KRI Gadjah Mada, KRI Macan Tutul, KRI Nanggala, KRI Dewaruci, CW-21 Demon, B-25 Mitchell Si Djimat, P-51D Mustang Cocor Merah, C-47 Seulawah, dsb. (UTF-8 with BOM, 0 missing keys).

---

## 3. Catatan Pembaruan v1.0.1 (R56 Full Compatibility, UX Polish & Zero-Error Clean)

1. **Penguncian Mutual Exclusivity 6 Jalur Politik:**
   - Semua akar cabang ideologi (A, B, C, D, E, F) di `common/national_focus/DEI_indonesia_focus_tree.txt` kini memiliki cross `mutually_exclusive = { ... }` satu sama lain.
   - Dilengkapi trigger pencegah `available = { NOT = { has_country_flag = dei_jalur_dipilih } }`.
   - Mengambil salah satu cabang menetapkan country flag `dei_jalur_dipilih` dan `dei_path_<x>_chosen`, yang secara dinamis melipat/menyembunyikan (`allow_branch`) 5 cabang ideologi lainnya agar tampilan UX pohon fokus bersih.

2. **Arsitektur Override Total Kompatibilitas Road to 56:**
   - **Keputusan:** `common/decisions/INS.txt` dioverride berkas kosong untuk menonaktifkan 63 keputusan usang bawaan R56 yang bentrok dengan submod.
   - **Event Kolonial:** `events/indonesia.txt` dan `events/TAOG_Indonesia.txt` dioverride berkas kosong untuk membungkam event lawas R56 (seperti `indonesia.100` "Removing Colonialist Influence" dari Belanda).
   - **Penamaan Kota Otomatis:** Perubahan nama Batavia -> Jakarta, Buitenzorg -> Bogor, Telukbetung -> Bandar Lampung, Hollandia -> Jayapura, Fort Victoria -> Ambon disematkan langsung di Fokus 3 (`dei_focus_momentum_kemerdekaan`), `dei_trunk.7`, dan keputusan proklamasi NKRI.
   - **Bookmark Gathering Storm:** `common/bookmarks/the_gathering_storm.txt` dioverride menampilkan 3 fokus prolog krisis 1936 submod.
   - **AI Strategy Plans:** `common/ai_strategy_plans/` mengarahkan AI Indonesia ke pohon fokus submod.

3. **Audit Bebas Error (`error.log` Clean):**
   - Perbaikan trait komandan: `army_soft_attack_factor` diganti `army_infantry_attack_factor = 0.10` di `common/unit_leader/DEI_traits.txt`.
   - Perbaikan event riset: `add_research_slot_speed_factor` diganti `add_tech_bonus` di `events/DEI_flavor_events.txt`.
   - Konversi 156 bendera TGA ke format standar 32bpp RGBA tanpa RLE untuk menghilangkan peringatan bit-depth Clausewitz.
   - Banner World News Proklamasi 1936 (`DEI_news_event_1936_revolution.dds`) menggunakan foto Bung Karno membacakan teks Proklamasi Kemerdekaan.

---

## 4. Aturan Preferensi Wajib Pengguna (User Preferences)

> [!IMPORTANT]
> Agen baru HARUS mematuhi semua aturan berikut tanpa kompromi:

1. **Aturan Instalasi ("JANGAN PASANG DULU"):**
   - Jangan menyalin/memasang file mod ke `C:\Users\<User>\Documents\Paradox Interactive\Hearts of Iron IV\mod` secara sepihak.
   - Pemasangan ke game HANYA dilakukan jika pengguna memberikan perintah eksplisit: "pasang", "deploy", atau "install ke game".

2. **Aturan Bahasa Lokalisasi:**
   - Semua teks narasi cerita event, opsi tombol respon, deskripsi fokus, dan decisions ditulis dalam **Bahasa Inggris**.
   - **KECUALI istilah historis, militer, institusi, dan kultural Indonesia yang penting, WAJIB dipertahankan orisinalitasnya**:
     *Volksraad*, *KNIL*, *TKR*, *TII*, *Proklamasi*, *Merdeka*, *KMB*, *ORI*, *Majapahit*, *Pusaka*, *Dewan Adat*, *Ulama*, *Syariat*, *Negara Islam Indonesia*, *Front Rakyat*, *Gotong Royong*, *Pancasila*, *Kraton*, *Sumpah Palapa*, dll.

3. **Format Pengkodean Berkas Lokalisasi:**
   - Berkas `localisation/english/DEI_indonesia_l_english.yml` **WAJIB menggunakan UTF-8 with BOM (`\xef\xbb\xbf`)**. Engine Clausewitz akan memunculkan teks rusak jika BOM tidak ada.

4. **Aturan Nomenklatur Tanpa Akronim Artifisial:**
   - DILARANG menciptakan singkatan 3-huruf artifisial seperti `JPS`, `KMN`, `KNI`, atau `KPR`.
   - Prefix militer laut resmi hanya dua: **`KRI `** (Republik/TNI) dan **`Hr.Ms. `** (Kolonial Hindia Belanda).
   - Untuk Majapahit, Islamis, dan Komunis: gunakan nama klasik atau historis murni secara langsung.

5. **Gaya Komunikasi Agen:**
   - Ultra-terse, telegraphic, maximum compression.
   - Pola: `[thing] [action] [reason]. [next step].`
   - Jangan gunakan basa-basi pembuka ("Sure!", "Tentu saja!", "Halo!").
   - Bahasa percakapan dengan user: Bahasa Indonesia.
   - Semua tautan berkas harus dapat diklik menggunakan format markdown `[teks](file:///path/to/file)`.

---

## 5. Prosedur Verifikasi Cepat

Sebelum menyatakan pekerjaan selesai, jalankan skrip verifikasi otomatis:
- Master Audit 8 Dimensi: `python "c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\scratch\master_audit.py"` (100% Lulus).
- Cek sintaks, event & fokus: `python "c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\scratch\final_verification.py"` (134 fokus, 124 event, 0 collision).
- Cek kunci lokalisasi: `python "c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\scratch\verify_all_loc.py"` (1.217 keys, 0 missing).
- Cek aset & gambar: `python "c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\scratch\comprehensive_asset_audit.py"` (0 missing sprites/flags).
- Cek UTF-8 BOM: `python -c "assert open(r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml', 'rb').read().startswith(b'\xef\xbb\xbf')"`
