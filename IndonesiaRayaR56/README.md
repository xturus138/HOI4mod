# Indonesia Raya: Road to Merdeka — Submod Road to 56

Submod Hearts of Iron IV komprehensif untuk Hindia Belanda / Indonesia (1936–1956) yang dibangun terintegrasi di atas **The Road to 56 (R56)**.

**Status Saat Ini:** `v1.0.1 (R56 Complete Compatibility, Mutual Exclusivity & UX Polish)` — 134 Fokus Nasional, 124 Event Interaktif (98 Fokus + 26 Flavor Acak MTTH, 100% bergambar kustom), Batang Prolog Krisis 1936 (84 Hari), 6 Jalur Ideologi Mutual Exclusive, 36 Focus Goals Kustom (82x82 DDS), 24 Technologies & Equipment (120x50 DDS, 55 interface sprites), 19 Potret Komandan (156x210 DDS), 18 Proklamasi Tata Kelola Negara (3 Opsi per Ideologi), 18 Cosmetic Tags & Warna Peta Dinamis, 108 Bendera TGA Tersinkronisasi, 6 Dedicated Starter Naval OOBs di Pangkalan Surabaya, 14 Division Templates Doktrinal, 11 Namelist Divisi AD, 24 Namelist Kapal Autentik, 14 Varian Alutsista, 25 Keputusan Strategis & Proklamasi, 5 Komandan Legendaris, 8 Desainer Industri MIO, dan 1.217 Kunci Lokalisasi Ber-BOM (0 missing keys, 0 errors).

---

## Catatan Rilis v1.0.1 (Pembaruan & Perbaikan)

1. **Penguncian Mutual Exclusivity 6 Jalur Politik:**
   - Seluruh 6 akar cabang ideologi (A: Republik, B: Kolonial, C: Komunis, D: Otoriter, E: Islamis, F: Majapahit) kini saling mengunci secara eksklusif (`mutually_exclusive`).
   - Dilengkapi proteksi trigger `available = { NOT = { has_country_flag = dei_jalur_dipilih } }`.
   - Mengambil satu jalur menetapkan flag yang secara dinamis melipat (`allow_branch`) 5 jalur lainnya agar pohon fokus tetap rapi dan bebas glitch.

2. **Pembersihan Konflik Event R56 (Anti-Colonial Glitch):**
   - Event bawaan R56 `indonesia.100` ("Removing Colonialist Influence" / opsi penamaan dari Belanda) dinonaktifkan secara permanen (`always = no`) agar tidak menimpa narasi revolusi submod.
   - Dependensi event internal R56 (seperti `indonesia.105` pada setup negara) tetap dipertahankan penuh tanpa merusak engine.

3. **Banner World News Proklamasi 1936 Baru:**
   - Mengganti ilustrasi kapal Belanda dengan arsip bersejarah Bung Karno membacakan teks Proklamasi Kemerdekaan Indonesia (`DEI_news_event_1936_revolution.dds`).

4. **Koreksi Sintaks & Integritas Modifier:**
   - Menyelaraskan modifier trait komandan ke standar Clausewitz modern (`army_infantry_attack_factor = 0.10`, `army_speed_factor = 0.10`, `naval_retreat_speed = 0.20`).
   - Mengganti efek riset usang pada flavor event Observatorium Bosscha dengan `add_tech_bonus` kategori elektronika.

5. **Stabilitas Tekstur Bendera (Crash-Proof):**
   - Menggunakan format bendera 24bpp uncompressed standar guna memastikan kompatibilitas penuh dengan DirectX texture pipeline Clausewitz engine.

---

## Ringkasan Fitur Utama Mod

### 1. Pohon Fokus Hibrida Komprehensif (134 Fokus Nasional)
Menggabungkan kebebasan 6 jalur politik submod yang diperdalam hingga era Perang Dingin dengan kedalaman riset militer dan industri khas Road to 56:
- **Batang Prolog Krisis 1936 (3 Fokus, 84 Hari, X=12, Y=0..8):** Mengisahkan retaknya Pax Neerlandica, gelombang pemogokan massal, dan pembangkangan barak KNIL pada Januari–Maret 1936 yang bermuara pada meletusnya *Momentum Revolusi Nasional 1936* (akhir Maret 1936) sebagai alur default tanpa memerlukan decision shortcut.
- **Jalur A: Republik Nasionalis-Demokratis (16 Fokus, X=0..4):** Proklamasi 17 Agustus 1945, pembentukan TKR, diplomasi PBB, perang gerilya hadapi Agresi Militer Belanda I & II, KMB, demokrasi parlementer, Konferensi Asia-Afrika (KAA) Bandung 1955, Pembebasan Irian Barat (Trikora), Dekrit Presiden 1959, Konfrontasi Dwikora, Falsafah Pancasila, dan Doktrin Trisakti.
- **Jalur B: Kolonial / Federalis (14 Fokus, X=4..7):** Penumpasan gerilyawan, reformasi federal, Sidang Raya BFO (Bijeenkomst voor Federaal Overleg), Angkatan Bersenjata Federalis KNIL, Pakta Keamanan Maritim ANZAC, Modernisasi Perkebunan Deli, Piagam Otonomi Swapraja & Kraton, dan Jaringan Pelabuhan Bebas Nusantara.
- **Jalur C: Komunis (14 Fokus, X=8..11):** Kemenangan Front Rakyat, land reform radikal, pembersihan elemen borjuis, pembentukan Tentara Merah Rakyat, Kolektivisasi Komune Tani, Nasionalisasi Total Aset Imperialis Asing, Pembentukan Angkatan Kelima (Buruh & Tani Bersenjata), Mobilisasi Budaya LEKRA, Poros Anti-Imperialis Asia, dan Rencana Pembangunan Semesta Berencana.
- **Jalur D: Otoriter Militeristik (14 Fokus, X=12..15):** Kudeta militer, darurat perang, pembubaran parlemen partai, Dewan Revolusi Militer Tertinggi, Doktrin Dwifungsi ABRI, Benteng Samudra Nusantara (bunker selat & radar), Wajib Militer Bela Negara Menyeluruh, Komando Strategis Selat Malaka, dan Hegemoni Militer Samudra Hindia.
- **Jalur E: Islamis / Negara Islam Indonesia (14 Fokus, X=16..18):** Proklamasi NII (Darul Islam / Kartosoewirjo), Dewan Ulama, Tentara Islam Indonesia (TII), Pendirian Baitul Mal Pusat, Mahkamah Syariah Tertinggi (Kodifikasi Qanun), Akademi Militer Mujahidin, Sistem Keuangan Muamalah Anti-Riba, Liga Perjuangan Muslim Sedunia, dan Khilafah Islamiyah Nusantara.
- **Jalur F: Kemaharajaan Majapahit [Ahistoris] (13 Fokus, X=19..22):** Kebangkitan semangat Majapahit, pencarian pusaka keramat, Dewan Adat Nusantara, Pemenuhan Sumpah Palapa Baru, Restorasi Ibu Kota Suci Trowulan, Pembentukan Resimen Ksatria Dharmaputra, Armada Jung Raksasa Berpelindung, Kodifikasi Hukum Kutaramanawa Dharmasastra, dan Penobatan Maharaja Nusantara Raya (Surya Majapahit).
- **Cabang Industri & Riset R56 (14 Fokus, X=26..30):** Industrialisasi Batavia, Institut Teknologi Bandung (slot riset ke-5), eksplorasi minyak BPM di Plaju/Balikpapan, perkebunan karet Sumatra, industri kimia & semen.
- **Cabang Militer AD / AU / AL R56 (28 Fokus, X=33..43):**
  - *Angkatan Darat (KNIL / TNI):* Doktrin infanteri tropis KNIL, artileri medan Bandung, motorisasi kavaleri, modernisasi persenjataan.
  - *Penerbangan Militer (Militaire Luchtvaart):* Pangkalan udara Andir & Kalijati, doktrin pertahanan udara kepulauan, lisensi pesawat tempur & pembom taktis.
  - *Angkatan Laut (Marine):* Pangkalan armada Ujung Surabaya, flotila kapal selam perairan dangkal, doktrin pengawalan konvoi selat, kapal perusak ringan.

### 2. 18 Proklamasi Tata Kelola & Penamaan Resmi Negara (3 Opsi per Ideologi)
Pemain memiliki kendali penuh atas identitas, bentuk negara, warna peta, dan nama partai resmi melalui keputusan kategori **`Tata Kelola & Penamaan Resmi Negara`** (`dei_decisions_proclamations`):

| Cabang Ideologi | Opsi 1 (Default / Utama) | Opsi 2 (Federal / Alternatif) | Opsi 3 (Radikal / Luas) |
|---|---|---|---|
| **A. Republik** | **Negara Kesatuan Republik Indonesia** (*PNI*) | **Republik Indonesia Serikat** (*RIS-Koalisi*) | **Republik Sosialis Demokratis Indonesia** (*PSI*) |
| **B. Kolonial** | **Hindia Belanda** (*Gouvernement*) | **Uni Negara-Negara Indonesia** (*BFO*) | **Persemakmuran Mahkota Hindia** (*Kroonraad*) |
| **C. Komunis** | **Republik Rakyat Indonesia** (*PKI*) | **Uni Soviet Indonesia** (*Komintern-PKI*) | **Front Demokrasi Rakyat Nusantara** (*FDR*) |
| **D. Otoriter** | **NKRI Revolusioner** (*Dewan Revolusi*) | **Komando MB Revolusi Militer** (*Junta ABRI*) | **Imperium Militer Indonesia Raya** (*Bela Negara*) |
| **E. Islamis** | **Negara Islam Indonesia** (*Majelis Syuro*) | **Daulah Islamiyah Nusantara** (*Diwan Imam*) | **Khilafah Islamiyah Nusantara** (*Baitul Mal & Syuro*) |
| **F. Majapahit** | **Kemaharajaan Majapahit** (*Kraton Wilwatikta*) | **Imperium Surya Wilwatikta** (*Surya Kencana*) | **Maha-Imperium Nusantara Raya** (*Bhayangkara Raya*) |

- **Warna Peta Dinamis (`common/countries/cosmetic.txt`):** 18 cosmetic tags memiliki kode warna RGB khas untuk membedakan identitas negara di peta dunia secara visual.
- **Sinkronisasi Bendera:** 108 bendera TGA tersinkronisasi di folder `standard`, `medium`, dan `small`.

### 3. Nomenklatur Militer Bersih & Penghapusan Akronim Artifisial
Menghapus seluruh singkatan artifisial seperti `JPS`, `KMN`, `KNI`, dan `KPR`. Standardisasi alutsista laut kini mengikuti kaidah sejarah dan tradisi militer autentik:
- **Republik & Otoriter (TNI-AL):** Menggunakan prefix resmi historis **`KRI `** (*KRI Bung Karno, KRI Diponegoro, KRI Macan Tutul, KRI Nanggala, KRI Dewaruci*).
- **Kolonial (KM-NI):** Menggunakan prefix resmi historis **`Hr.Ms. `** (*Hr.Ms. De Zeven Provinciën, Hr.Ms. Java, Hr.Ms. Evertsen, Hr.Ms. O-19*).
- **Majapahit:** Tanpa akronim artifisial (seperti standar IJN di HOI4). Kapal langsung menyandang nama agung klasik: *Hayam Wuruk, Senapati Nala, Tribhuwana Tunggadewi, Gadjah Mada, Warastra Laut, Naga Baruna, Antaboga Laut*.
- **Islamis / NII:** Tanpa akronim artifisial. Kapal langsung menyandang nama pejuang & pusaka Islam: *Baitul Maqdis, Fatahillah, Sultan Agung, Iskandar Muda, Pedang Tauhid, Zulfikar*.
- **Komunis:** Tanpa akronim artifisial. Kapal menyandang nama tokoh revolusioner: *Proletar, Karl Marx, Vladimir Lenin, Musso, Bintang Merah, Martir Madiun, Hiu Merah*.

### 4. Dedicated Starter Fleet OOBs per Ideologi
Saat pemain memilih ideologi pada event `dei_trunk.6`, armada laut starter di Pangkalan Armada Ujung Surabaya (Provinsi 13520) langsung dimuat sesuai cabang:
- `DEI_navy_starter_a.txt` -> *Armada Laut Republik Indonesia (ALRI)*
- `DEI_navy_starter_b.txt` -> *Zeemacht in Nederlandsch-Indië (KM-NI)*
- `DEI_navy_starter_c.txt` -> *Armada Laut Rakyat Proletar (ALRP)*
- `DEI_navy_starter_d.txt` -> *Komando Armada Pertahanan Samudra (KAPS)*
- `DEI_navy_starter_e.txt` -> *Armada Laut Mujahidin Samudra (ALMS)*
- `DEI_navy_starter_f.txt` -> *Armada Jung Segara Wilwatikta*

### 5. Sistem Divisi, Namelist & Alutsista Historis (14 Templates & 11 Namelists)
- **14 Division Templates Doktrinal (`history/units/DEI_templates.txt`):**
  1. *Divisi Infanteri Siliwangi* (Republik)
  2. *Divisi Infanteri Diponegoro* (Republik)
  3. *Resimen Komando Angkatan Darat (RPKAD)* (Republik)
  4. *Korps Komando Operasi (KKO Marinir)* (Republik)
  5. *Resimen Kavaleri Lapis Baja* (Republik/Kolonial)
  6. *Brigade Laskar Rakyat & Tentara Pelajar* (Republik/Komunis/Islamis)
  7. *Resimen Mujahidin TII / Hizbullah* (Islamis)
  8. *Brigade Barisan Buruh Merah* (Komunis)
  9. *KNIL Infanterie Divisie* (Kolonial)
  10. *Garnizun Stadswacht & Pertahanan Pantai* (Kolonial/Republik)
  11. *Prajurit Utama Bhayangkara* (Majapahit)
  12. *Resimen Ksatria Dharmaputra* (Majapahit)
  13. *Resimen Pengawal Dewan Revolusi* (Otoriter)
  14. *Barisan Pemuda Bela Negara* (Otoriter)
- **11 Grup Namelist Divisi Darat (`common/units/names_divisions/INS_names_divisions.txt`):**
  - `DEI_INF_TNI`, `DEI_LASKAR`, `DEI_MARINIR`, `DEI_KNIL_COLONIAL`, `DEI_KOMUNIS`, `DEI_ISLAMIS`, `DEI_MAJAPAHIT`, `DEI_KOMANDO`, `DEI_KAVALERI`, `DEI_GARNIZUN`, `DEI_OTORITER`.

### 6. Event Interaktif & Visual Penuh (119 Event, 100% Bergambar)
- **93 Event Berpilihan Fokus:** Mengiringi setiap fokus penting dengan konsekuensi politik, stabilitas, dan hubungan internasional (14-16 event per cabang ideologi).
- **26 Flavor Event Acak Berkala (Non-Focus MTTH):**
  - Pers bumiputera, panen komoditas, tambang batubara Ombilin & timah Bangka, Observatorium Bosscha, Institut Pasteur Bandung, Tamansiswa Ki Hadjar Dewantara, Kongres Perempuan Indonesia, perdebatan Sukarno-Natsir, bioskop Terang Boelan, Kongres Pemuda 1928, pemberontakan De Zeven Provinciën, pemugaran Borobudur, Karapan Sapi Madura, penyelundupan senjata Selat Malaka, ramalan Ratu Adil, armada Pinisi Dobo, penerbangan Adisucipto, Laskar Putri Surakarta, dan kilang Pangkalan Brandan.
- **Visualisasi Gambar Event:** 100% event memiliki sprite bergambar valid terintegrasi (0 missing sprites).

### 7. Riset & Doktrin Militer Strategis (26 Decisions Total)
- **Keputusan Proklamasi Tata Kelola Negara (18 Decisions Baru):** Pemilihan nama resmi negara, bentuk negara, dan partai.
- **Arah Riset & Doktrin Strategis (8 Decisions):** Doktrin Gerilya Wilayah (Sishanrata), Doktrin Gerilya Selat Dangkal, Doktrin Dirgantara Khatulistiwa, Standardisasi Senjata Pindad, Panser Cepat Braat, Dirgantara IPTN, Eksplorasi Minyak Pertamina, Komisioning Armada KRI.
- **Mega-Proyek Infrastruktur & Pertahanan (6 Decisions):** Pangkalan Ujung Surabaya, Arsenal Bandung, Kilang Minyak Plaju & Balikpapan, Jalan Raya Pos & Rel Trans-Jawa, Benteng Selat Sunda/Malaka, Lanud Iswahyudi & Kalijati.
- **Mekanik Militer Khusus (4 Decisions):** Sishanrata, Logistik Maritim Pinisi, Dapur Umum & Palang Merah, Pabrik Senjata Darurat Pegunungan.
- **Kedaulatan Wilayah (8 Decisions):** Revolusi Dini, Papua Barat, Timor Portugis, Borneo/Sarawak, Melayu Raya, Transmigrasi, ORI, Patroli Maritim.

---

## Struktur Berkas Mod

```
IndonesiaRayaR56/
├── common/
│   ├── characters/
│   │   └── DEI_characters.txt          # Komandan legendaris (Sudirman, Urip, Nasution, Kawilarang, Yos Sudarso)
│   ├── countries/
│   │   └── cosmetic.txt                # 18 Cosmetic Tags & warna peta RGB dinamis
│   ├── decisions/
│   │   └── DEI_decisions.txt           # 26 keputusan (Proklamasi Negara, Mega-Proyek, Sishanrata, Alutsista)
│   ├── ideas/
│   │   └── DEI_ideas.txt               # 41 gagasan nasional & spirit ideologi
│   ├── ideologies/
│   │   └── DEI_custom_ideologies.txt   # Definisi ideologi custom (federalist, islamist, majapahit)
│   ├── national_focus/
│   │   ├── DEI_00_shared_trunk.txt     # Batang bersama pra-kemerdekaan 1936-1945 (11 fokus)
│   │   ├── DEI_01_path_a_republik.txt  # Jalur A: Republik Nasionalis-Demokratis (16 fokus)
│   │   ├── DEI_02_path_b_kolonial.txt  # Jalur B: Kolonial / Federalis BFO (14 fokus)
│   │   ├── DEI_03_path_c_komunis.txt   # Jalur C: Komunis Front Rakyat (14 fokus)
│   │   ├── DEI_04_path_d_otoriter.txt  # Jalur D: Otoriter Militeristik ABRI (14 fokus)
│   │   ├── DEI_05_path_e_islamis.txt   # Jalur E: Islamis / NII Kartosoewirjo (14 fokus)
│   │   ├── DEI_06_path_f_majapahit.txt # Jalur F: Kemaharajaan Majapahit (13 fokus)
│   │   ├── DEI_r56_industry.txt        # Cabang industri & riset R56 (14 fokus)
│   │   └── DEI_r56_armed_forces.txt    # Cabang militer AD/AU/AL R56 (28 fokus)
│   ├── unit_leader/
│   │   └── DEI_traits.txt              # Trait unik jenderal & laksamana
│   └── units/
│       ├── names_divisions/
│       │   └── INS_names_divisions.txt # 11 grup namelist divisi darat
│       └── names_ships/
│           └── INS_names_ships.txt     # 24 grup namelist kapal (prefix autentik KRI & Hr.Ms.)
├── events/
│   ├── DEI_00_shared_trunk_events.txt  # Event awal & pemicu proklamasi ideologi dei_trunk.6
│   ├── DEI_01_path_a_events.txt        # Event Jalur A (Republik)
│   ├── DEI_02_path_b_events.txt        # Event Jalur B (Kolonial)
│   ├── DEI_03_path_c_events.txt        # Event Jalur C (Komunis)
│   ├── DEI_04_path_d_events.txt        # Event Jalur D (Otoriter)
│   ├── DEI_05_path_e_events.txt        # Event Jalur E (Islamis)
│   ├── DEI_06_path_f_events.txt        # Event Jalur F (Majapahit)
│   └── DEI_flavor_events.txt           # 26 event flavor berkala (non-focus MTTH)
├── gfx/
│   ├── event_pictures/                 # Sprite gambar event
│   └── flags/                          # Bendera TGA (108 file: standard, medium, small)
├── history/
│   └── units/
│       ├── DEI_templates.txt           # 14 templat divisi doktrinal
│       ├── DEI_air_starter.txt         # Skadron udara awal Lanud Andir & Iswahyudi
│       ├── DEI_navy_starter_a.txt      # Starter fleet Surabaya: ALRI (Republik)
│       ├── DEI_navy_starter_b.txt      # Starter fleet Surabaya: KM-NI (Kolonial)
│       ├── DEI_navy_starter_c.txt      # Starter fleet Surabaya: ALRP (Komunis)
│       ├── DEI_navy_starter_d.txt      # Starter fleet Surabaya: KAPS (Otoriter)
│       ├── DEI_navy_starter_e.txt      # Starter fleet Surabaya: ALMS (Islamis)
│       └── DEI_navy_starter_f.txt      # Starter fleet Surabaya: Jung Segara (Majapahit)
├── interface/                          # Berkas GFX descriptor
└── localisation/
    └── english/
        └── DEI_indonesia_l_english.yml # 1.217 entri teks lokalisasi (UTF-8 with BOM)
```

---

## Prosedur Verifikasi Integritas

Submod dilengkapi skrip audit otomatis yang dapat dijalankan melalui terminal:
- `python scratch/final_verification.py` -> Memastikan 134 fokus, 124 event, koordinat utuh, kurung kurawal seimbang, dan UTF-8 BOM aktif.
- `python scratch/verify_all_loc.py` -> Memastikan seluruh 1.217 kunci lokalisasi terdefinisi lengkap (0 missing).
- `python scratch/comprehensive_asset_audit.py` -> Memastikan 0 missing sprites, 0 missing portraits, dan 0 missing flags.
- `python scratch/master_audit.py` -> Master audit 8 dimensi submod (100% Lulus).


---

## Aturan Pengembangan & Kebijakan Workspace
1. **Aturan Deploy ("JANGAN PASANG DULU"):** Berkas mod tidak disalin ke folder instalasi game Steam sampai pengguna memberikan perintah eksplisit.
2. **Aturan Bahasa:** Narasi event, deskripsi fokus, dan keputusan ditulis dalam Bahasa Inggris, dengan mempertahankan istilah historis asli Indonesia (*Volksraad, KNIL, TKR, TII, Proklamasi, Merdeka, KMB, ORI, Majapahit, Sishanrata, Pancasila*, dll).
3. **Format Pengkodean:** Berkas `DEI_indonesia_l_english.yml` wajib menggunakan **UTF-8 with BOM (`\xef\xbb\xbf`)**.
