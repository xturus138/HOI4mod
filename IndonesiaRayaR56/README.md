# Indonesia Raya: Road to Merdeka — Submod Road to 56

Submod Hearts of Iron IV komprehensif untuk Hindia Belanda / Indonesia (1936–1956) yang dibangun terintegrasi di atas **The Road to 56 (R56)**.

**Status Saat Ini:** `v1.0 (Hybrid R56 Integration)` — 102 Fokus Nasional, 61 Event Interaktif (100% bergambar), 8 Keputusan Regional & Tata Kelola, 19 National Spirits, 6 Tokoh Pemimpin R56, dan Lokalisasi Bahasa Inggris dengan preservasi istilah historis Indonesia.

---

## Ringkasan Fitur v1.0

### 1. Pohon Fokus Hibrida (102 Fokus Nasional)
Menggabungkan kebebasan 6 jalur politik submod dengan kedalaman riset militer dan industri khas Road to 56 tanpa tumpang tindih koordinat:
- **Batang Bersama 1936–1945 (11 Fokus, X=7..10):** Dinamika politik pra-kemerdekaan (Volksraad, KNIL, ekonomi, pendidikan pribumi, ancaman Jepang) bermuara pada "Momentum Kemerdekaan".
- **Jalur A: Republik Nasionalis-Demokratis (10 Fokus, X=0..3):** Proklamasi 17 Agustus 1945, pembentukan TKR, diplomasi PBB, perang gerilya hadapi Agresi Militer Belanda I & II, KMB, demokrasi parlementer, pembebasan Irian Barat, dan Demokrasi Terpimpin.
- **Jalur B: Kolonial / Federalis (8 Fokus, X=4..7):** Penumpasan gerilyawan, reformasi terbatas, pembentukan negara-negara federal (NIT, Pasundan), Uni Belanda-Indonesia, status dominion, dan Persemakmuran Belanda.
- **Jalur C: Komunis (8 Fokus, X=8..11):** Kemenangan Front Rakyat (kebalikan Peristiwa Madiun), land reform radikal, pembersihan elemen borjuis, pembentukan Tentara Rakyat, poros Soviet vs Tiongkok, industrialisasi sosialis, ekspor revolusi.
- **Jalur D: Otoriter Militeristik (8 Fokus, X=12..15):** Kudeta dewan militer, darurat militer, pembubaran partai, ekonomi perang, doktrin laskar pemuda militan, klaim Nusantara Raya, hegemoni laut selatan.
- **Jalur E: Islamis / Negara Islam Indonesia (8 Fokus, X=16..18):** Proklamasi NII (Darul Islam / Kartosoewirjo), Dewan Ulama, hukum syariat, pembentukan Tentara Islam Indonesia (TII), diplomasi dunia Arab, persatuan Islam Nusantara.
- **Jalur F: Kemaharajaan Majapahit [Ahistoris] (7 Fokus, X=19..20):** Kebangkitan semangat Majapahit, pencarian pusaka pusaka keramat, Dewan Adat Nusantara, armada laut agung, integrasi keraton & kesultanan, proklamasi Kekaisaran Baru Nusantara.
- **Cabang Industri & Riset R56 (14 Fokus, X=26..30):** Industrialisasi Batavia, Institut Teknologi Bandung (slot riset ke-5), eksplorasi minyak BPM di Plaju/Balikpapan, perkebunan karet Sumatra, industri kimia & semen.
- **Cabang Militer AD / AU / AL R56 (28 Fokus, X=33..43):**
  - *Angkatan Darat (KNIL / TNI):* Doktrin infanteri tropis KNIL, artileri medan Bandung, motorisasi kavaleri, modernisasi persenjataan.
  - *Penerbangan Militer (Militaire Luchtvaart):* Pangkalan udara Andir & Kalijati, doktrin pertahanan udara kepulauan, lisensi pesawat tempur & pembom taktis.
  - *Angkatan Laut (Marine):* Pangkalan armada Ujung Surabaya, flotila kapal selam perairan dangkal, doktrin pengawalan konvoi selat, kapal perusak ringan.

### 2. Event Interaktif & Visual Penuh (61 Event, 100% Bergambar)
- **55 Event Berpilihan Fokus:** Mengiringi setiap fokus penting dengan konsekuensi politik, stabilitas, dan hubungan internasional.
- **6 Flavor Event Acak Berkala (Non-Focus MTTH):**
  1. `dei_flavor.1`: Suara Pers Bumiputera (*Medan Prijaji* & *Bintang Timoer*).
  2. `dei_flavor.2`: Panen Raya Komoditas Tropis (karet, teh, kina).
  3. `dei_flavor.3`: Mogok Buruh Pelabuhan & Kereta Api.
  4. `dei_flavor.4`: Semarak Pasar Malam Gambir.
  5. `dei_flavor.5`: Erupsi Gunung Berapi & Solidaritas Gotong Royong.
  6. `dei_flavor.6`: Gema Radio Gelombang Pendek Antar-Pulau.
- **Visualisasi Gambar Event:** 7 DDS custom arsip historis + 54 sprite terpadu HOI4/R56 (0 event tanpa gambar).

### 3. Sistem Keputusan Spesifik (Decisions)
- **Revolusi Dini:** Keputusan awal 1936 untuk langsung melompat ke percabangan ideologi tanpa menunggu 1945.
- **Kedaulatan Wilayah Nusantara:** Integrasi Papua Barat (state 669 & 1073), Timor Portugis (state 721), Unifikasi Pulau Borneo/Sarawak (state 333), dan Tuntutan Melayu Raya (state 336).
- **Tata Kelola Kepulauan & Ekonomi:** Program Transmigrasi antarpulau, Penerbitan Oeang Republik Indonesia (ORI), dan Operasi Patroli Maritim kepulauan.

### 4. Integrasi Tokoh Pemimpin Historis R56
Tiap jalur ideologi pada event `dei_trunk.6` otomatis mengangkat karakter pemimpin ber-portrait resmi dari database karakter R56 (`history/countries/INS - Indonesia.txt`):
- **Republik Demokratis:** Sukarno (`INS_sukarno`)
- **Kolonial / Federalis:** Hubertus van Mook (`INS_hubertus_van_mook`)
- **Komunis:** Musso (`INS_musso`)
- **Otoriter Militeristik:** Jenderal Soedirman (`INS_soedirman`)
- **Negara Islam Indonesia:** S.M. Kartosoewirjo (`INS_sekarmaji_kartosuwiryo`)
- **Majapahit Revival:** K.P.H. Soerjodiningrat / Wuryaningrat (`INS_wuryaningrat`)

### 5. Lokalisasi Bahasa Inggris Berpreservasi
- Seluruh teks narasi event, opsi respon, deskripsi fokus, dan decisions disajikan dalam Bahasa Inggris standar HOI4.
- Istilah orisinal historis, militer, institusi, dan kultural Indonesia tetap dipertahankan (*Volksraad*, *KNIL*, *TKR*, *TII*, *Proklamasi*, *Merdeka*, *KMB*, *ORI*, *Majapahit*, *Pusaka*, *Dewan Adat*, *Ulama*, *Syariat*, *Negara Islam Indonesia*, *Front Rakyat*, *Gotong Royong*, *Pancasila*, dsb.).
- Format pengkodean: **UTF-8 with BOM** (`\xef\xbb\xbf`), wajib untuk engine Clausewitz.

---

## Struktur File Mod

```
IndonesiaRayaR56/
├── descriptor.mod
├── common/
│   ├── national_focus/
│   │   ├── DEI_00_shared_trunk.txt        # Batang bersama 1936-1945 (11 fokus)
│   │   ├── DEI_01_path_a_republik.txt     # Jalur Republik (10 fokus)
│   │   ├── DEI_02_path_b_kolonial.txt     # Jalur Kolonial/Federal (8 fokus)
│   │   ├── DEI_03_path_c_komunis.txt      # Jalur Komunis (8 fokus)
│   │   ├── DEI_04_path_d_otoriter.txt     # Jalur Otoriter Militer (8 fokus)
│   │   ├── DEI_05_path_e_islamis.txt      # Jalur Islamis NII (8 fokus)
│   │   ├── DEI_06_path_f_majapahit.txt    # Jalur Majapahit Revival (7 fokus)
│   │   ├── DEI_r56_industry.txt           # Integrasi Industri R56 (14 fokus)
│   │   └── DEI_r56_armed_forces.txt       # Integrasi AD/AU/AL R56 (28 fokus)
│   ├── decisions/
│   │   ├── categories/
│   │   │   └── DEI_decision_categories.txt
│   │   └── DEI_decisions.txt              # 8 Keputusan regional & tata kelola
│   ├── ideas/
│   │   └── DEI_ideas.txt                  # 19 National Spirits
│   └── ideologies/
│       └── DEI_custom_ideologies.txt      # Ideologi federalist, islamist, majapahit
├── events/
│   ├── DEI_00_shared_trunk_events.txt     # Event batang bersama + percabangan pemimpin
│   ├── DEI_01_revolusi_dini_events.txt    # Event revolusi dini
│   ├── DEI_02_path_a_events.txt           # Event jalur Republik (Agresi, KMB, Irian)
│   ├── DEI_03_path_b_events.txt           # Event jalur Kolonial
│   ├── DEI_04_path_c_events.txt           # Event jalur Komunis
│   ├── DEI_05_path_d_events.txt           # Event jalur Otoriter
│   ├── DEI_06_path_e_events.txt           # Event jalur Islamis
│   ├── DEI_07_path_f_events.txt           # Event jalur Majapahit
│   └── DEI_flavor_events.txt              # 6 Flavor event acak berkala (MTTH)
├── interface/
│   └── DEI_event_pictures.gfx             # Wiring sprite event custom
├── gfx/
│   ├── flags/                             # Bendera INS & DEI (Standar, Medium, Small)
│   └── event_pictures/                    # Event pictures arsip historis DDS
└── localisation/english/
    └── DEI_indonesia_l_english.yml        # 396 Kunci lokalisasi (UTF-8 with BOM)
```

---

## Petunjuk Instalasi Manual

> [!NOTE]
> Proyek saat ini berada di folder repositori lokal. Jika ingin memasang ke game HOI4:

1. Pastikan Steam Hearts of Iron IV dan mod workshop **The Road to 56** sudah terpasang.
2. Salin folder `IndonesiaRayaR56/` ke:
   `C:\Users\<User>\Documents\Paradox Interactive\Hearts of Iron IV\mod\IndonesiaRayaR56`
3. Salin file `IndonesiaRayaR56.mod` ke:
   `C:\Users\<User>\Documents\Paradox Interactive\Hearts of Iron IV\mod\IndonesiaRayaR56.mod`
4. Di HOI4 Playset Launcher, aktifkan **The Road to 56** dan **Indonesia Raya: Road to Merdeka**.
5. Jalankan game dan pilih negara **Dutch East Indies** (Tag engine: `INS`).
