# Indonesia Sub Mod 56 — Indonesia Raya: Road to Merdeka

Submod Hearts of Iron IV komprehensif untuk Hindia Belanda / Indonesia (1936–1956) yang dirancang terintegrasi penuh di atas **The Road to 56 (R56)**.

- **Status Versi:** `v1.0.2 (Ideology/Party Consistency & Exploit Fixes)` — sudah di-deploy ke folder mod HOI4 untuk playtest.
- **Folder Mod Utama:** [IndonesiaRayaR56/](file:///c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia%20Sub%20Mod%2056/HOI4mod/IndonesiaRayaR56/)
- **Dokumentasi Lengkap:** [IndonesiaRayaR56/README.md](file:///c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia%20Sub%20Mod%2056/HOI4mod/IndonesiaRayaR56/README.md)
- **Instruksi Agent & Memori Kerja:** [AGENTS.md](file:///c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia%20Sub%20Mod%2056/HOI4mod/AGENTS.md)
- **Berkas Launcher HOI4:** [IndonesiaRayaR56.mod](file:///c:/Users/radit/Project/VisualStudioProject/Personal/HOI4MODS/Indonesia%20Sub%20Mod%2056/HOI4mod/IndonesiaRayaR56.mod)

---

## Catatan Rilis v1.0.2 (Perbaikan Ideologi, Partai & Exploit)
1. **Perbaikan Ketidakcocokan Ideologi/Partai/Pemimpin:** Jalur B (Kolonial), D (Otoriter), E (Islamis) sebelumnya men-set `ruling_party` ke grup yang tidak cocok dengan ideologi tokoh pemimpinnya (mis. Jalur D `neutrality` padahal pemimpinnya `fascism_ideology`), menyebabkan UI partai menampilkan nama salah (termasuk "NSB" yang bocor dari fallback partai fasis Belanda). Diperbaiki: B→`democratic`, D→`fascism`, E→`neutrality`, semua kini punya `set_party_name` sendiri.
2. **Pemulihan `events/indonesia.txt`:** File overwrite R56 ini sebelumnya rusak oleh 35 baris `picture=` tersisip salah tempat. Dipulihkan ke asli R56 + 1 perubahan sengaja (nonaktifkan `indonesia.100`).
3. **Perbaikan Exploit Political Power:** 18 decision proklamasi identitas negara bisa di-farming PP tanpa batas — ditambahkan cooldown 90 hari & hadiah PP dinetralkan.
4. **Perbaikan Referensi & Sprite Hilang:** 5/6 template unit debug decision salah nama; 10 sprite `GFX_idea_INS_*` designer industri tidak pernah terdefinisi — dipetakan ke sprite generic vanilla yang valid.
5. **Perbaikan Scope Script Audit:** Script audit sendiri ikut men-scan file dasar R56 seolah konten submod — diperbaiki agar hanya scan file `DEI_*`.

## Catatan Rilis v1.0.1 (Pembaruan & Perbaikan)
1. **Penguncian Mutual Exclusivity 6 Jalur:** 6 akar ideologi saling mengunci dan melipat 5 jalur lainnya saat dipilih.
2. **Pembersihan Konflik R56:** Event kolonial R56 `indonesia.100` dinonaktifkan (`always = no`) tanpa merusak dependensi event internal setup negara.
3. **Banner World News 1936 Baru:** Ilustrasi Bung Karno membacakan teks proklamasi kemerdekaan.
4. **Koreksi Trait & Event:** Sanitasi modifier trait komandan dan reward event Observatorium Bosscha.
5. **Stabilitas Tekstur:** Memulihkan format bendera 24bpp uncompressed standar bebas crash.

---

## Ringkasan Fitur Utama Mod

1. **139 Fokus Nasional Hibrida:**
   - Batang Prolog Krisis 1936 (3 Fokus)
   - Jalur A: Republik Nasionalis-Demokratis (16 Fokus)
   - Jalur B: Kolonial / Federalis BFO (14 Fokus)
   - Jalur C: Komunis Front Rakyat (14 Fokus)
   - Jalur D: Otoriter Militeristik ABRI (14 Fokus)
   - Jalur E: Islamis / Negara Islam Indonesia (14 Fokus)
   - Jalur F: Kemaharajaan Majapahit [Ahistoris] (13 Fokus)
   - Cabang Industri & Riset R56 (14 Fokus)
   - Cabang Militer AD/AU/AL R56 (28 Fokus)

2. **18 Proklamasi Tata Kelola & Penamaan Resmi Negara:**
   - 3 opsi nama resmi per ideologi via keputusan `Tata Kelola & Penamaan Resmi Negara` (`dei_decisions_proclamations`).
   - 18 Cosmetic Tags dengan kode warna peta RGB spesifik (`common/countries/cosmetic.txt`).
   - 108 bendera TGA tersinkronisasi di folder standard, medium, dan small.

3. **Nomenklatur Militer Autentik & Pembersihan Singkatan Artifisial:**
   - Seluruh akronim artifisial (`JPS`, `KMN`, `KNI`, `KPR`) telah dihapus.
   - Prefix resmi yang dipertahankan: **`KRI `** (TNI-AL) dan **`Hr.Ms. `** (KNIL/Marine).
   - Nama murni klasik & revolusioner untuk Majapahit (*Hayam Wuruk, Senapati Nala*), Islamis (*Baitul Maqdis, Fatahillah*), dan Komunis (*Proletar, Karl Marx*).

4. **Sistem Alutsista & Templates OOB Lengkap:**
   - 6 Dedicated Starter Navy OOBs Surabaya (`DEI_navy_starter_a.txt` s/d `f.txt`).
   - 14 Division Templates Doktrinal (`history/units/DEI_templates.txt`).
   - 11 Grup Namelist Divisi Darat (`common/units/names_divisions/INS_names_divisions.txt`).
   - 24 Grup Namelist Kapal Laut (`common/units/names_ships/INS_names_ships.txt`).
   - 14 Varian Alutsista Dual-Mode (Tank Braat, Stuart, CW-21, P-51 Cocor Merah, B-25 Si Djimat, C-47 Seulawah, KRI Gadjah Mada).

5. **124 Event Naratif & Flavor Acak (100% Bergambar):**
   - 98 Event berpilihan fokus per ideologi.
   - 26 Flavor Event acak berkala (dinamika pers, tambang Ombilin/Bangka, Bosscha, Tamansiswa, debat Sukarno-Natsir, Sumpah Pemuda, Borobudur, dll).
   - 32 gambar event kustom berformat vintage grayish silver-gelatin era 1930–1940.

6. **Aset Grafis Goals & Technologies Kustom (100% Grayish Monokrom):**
   - 36 Focus Goals (82x82 DDS) terdaftar di `DEI_goals.gfx`.
   - 24 Technologies & Equipment (120x50 DDS, 55 interface sprites) terdaftar di `DEI_technologies.gfx`.

7. **25 Keputusan Strategis & Proklamasi:**
   - 18 Proklamasi Tata Kelola & Bentuk Negara (3 opsi per ideologi).
   - Pangkalan Ujung Surabaya, Arsenal Bandung, Kilang Plaju & Balikpapan, Jalan Raya Pos & Trans-Jawa, Benteng Selat Sunda/Malaka, Lanud Iswahyudi & Kalijati.
   - Doktrin Gerilya Wilayah (Sishanrata), Perahu Pinisi, Pindad, Panser Braat, IPTN, Pertamina.

8. **Integritas Lokalisasi & Pengkodean:**
   - 1.217 entri teks lokalisasi di `DEI_indonesia_l_english.yml` dengan **UTF-8 with BOM (`\xef\xbb\xbf`)**.
   - 0 missing localization keys, 0 missing sprites, 0 syntax/brace errors.

