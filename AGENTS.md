# AGENTS.md — Submod HOI4 "Indonesia Raya: Road to Merdeka" (R56)

Dokumen memori kerja dan aturan preferensi permanen untuk semua sesi agen Antigravity berikutnya pada workspace ini.

---

## 1. Identitas & Arsitektur Proyek

- **Nama Mod:** Indonesia Raya: Road to Merdeka
- **Target Engine / Dependency:** Hearts of Iron IV (Steam version) + **The Road to 56 (R56)**.
- **Lokasi Proyek:** `c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56`
- **Tag Negara:**
  - Di base game dan Road to 56, tag negara Hindia Belanda / Indonesia adalah **`INS`** (bukan `DEI`).
  - Definisi pohon fokus harus memiliki bobot override:
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
  - Semua bendera disimpan dalam dua set: `INS*.tga` dan `DEI*.tga` (standar, medium, small).

---

## 2. Struktur Konten v1.0 (Hybrid Tree & Expansion)

1. **Pohon Fokus Hibrida (102 Fokus Total):**
   - **Batang Bersama 1936–1945 (11 Fokus, X=7..10):** `DEI_00_shared_trunk.txt`
   - **Jalur A — Republik Demokratis (10 Fokus, X=0..3):** `DEI_01_path_a_republik.txt`
   - **Jalur B — Kolonial/Federalis (8 Fokus, X=4..7):** `DEI_02_path_b_kolonial.txt`
   - **Jalur C — Komunis (8 Fokus, X=8..11):** `DEI_03_path_c_komunis.txt`
   - **Jalur D — Otoriter Militeristik (8 Fokus, X=12..15):** `DEI_04_path_d_otoriter.txt`
   - **Jalur E — Islamis / NII (8 Fokus, X=16..18):** `DEI_05_path_e_islamis.txt`
   - **Jalur F — Kemaharajaan Majapahit [Ahistoris] (7 Fokus, X=19..20):** `DEI_06_path_f_majapahit.txt`
   - **Cabang Industri & Riset R56 (14 Fokus, X=26..30):** `DEI_r56_industry.txt`
   - **Cabang Militer AD / AU / AL R56 (28 Fokus, X=33..43):** `DEI_r56_armed_forces.txt`
   - *Aturan koordinat:* Jangan pernah menempatkan fokus yang bertubrukan koordinat (X, Y) atau memutus rantai `prerequisite`.

2. **Karakter Pemimpin R56:**
   - Road to 56 sudah merekrut 91 karakter Indonesia di `history/countries/INS - Indonesia.txt`.
   - Event percabangan `dei_trunk.6` (`events/DEI_00_shared_trunk_events.txt`) menggunakan `retire_country_leader = yes` dan `promote_character`:
     - Republik: `INS_sukarno`
     - Kolonial: `INS_hubertus_van_mook`
     - Komunis: `INS_musso`
     - Otoriter: `INS_soedirman`
     - Islamis: `INS_sekarmaji_kartosuwiryo`
     - Majapahit: `INS_wuryaningrat`

3. **Event Interaktif & Visual Penuh (61 Event):**
   - 55 event fokus di `DEI_00` s/d `DEI_07`.
   - 6 flavor event acak berkala (MTTH) di `events/DEI_flavor_events.txt`.
   - **Aturan Visual:** 100% event wajib memiliki gambar (`picture = GFX_...`). Gunakan sprite valid vanilla / R56 / 7 event art custom DDS.

4. **Decisions (8 Keputusan):**
   - Di `common/decisions/DEI_decisions.txt`: Revolusi Dini, klaim Papua Barat, klaim Timor Portugis, unifikasi Borneo, tuntutan Melayu Raya, Transmigrasi, penerbitan ORI, dan patroli maritim.

---

## 3. Aturan Preferensi Wajib Pengguna (User Preferences)

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

4. **Gaya Komunikasi Agen:**
   - Ultra-terse, telegraphic, maximum compression.
   - Pola: `[thing] [action] [reason]. [next step].`
   - Jangan gunakan basa-basi pembuka ("Sure!", "Tentu saja!", "Halo!").
   - Bahasa percakapan dengan user: Bahasa Indonesia.
   - Semua tautan berkas harus dapat diklik menggunakan format markdown `[teks](file:///path/to/file)`.

---

## 4. Prosedur Verifikasi Cepat

Sebelum menyatakan pekerjaan selesai, jalankan skrip verifikasi otomatis:
- Cek kunci lokalisasi: `python -c "import re; ..."` memastikan 0 missing loc keys.
- Cek integritas event, gambar, dan kurung kurawal `{ }`.
- Pastikan tidak ada karakter non-ASCII di konsol PowerShell mentah yang merusak encoding file.
