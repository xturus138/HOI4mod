# Spesifikasi Desain: Default Prolog Revolusi Nasional 1936 (84 Hari)

**Tanggal:** 2026-09-06  
**Target Mod:** Indonesia Raya: Road to Merdeka (R56 Submod)  
**Tag:** `INS`  

---

## 1. Latar Belakang & Masalah
Sebelumnya, submod mengasumsikan pemain bermain sebagai pemerintah kolonial Hindia Belanda dari 1936 hingga 1945 melalui 11 fokus panjang (>400 hari). Untuk melompati era kolonial, pemain harus membuka menu Decisions dan mengklik shortcut artifisial *"Revolusi Dini (Shortcut 1936)"*.
Hal ini merusak imersi *alternate history*, memutus kontinuitas cerita, dan membuat fitur revolusi terkesan seperti tombol cheat/bypass opsional.

## 2. Tujuan Desain (User Requirements)
1. **Default Canonical Flow:** Revolusi bukan lagi *by choice* melalui decision, melainkan alur cerita baku mod saat permainan baru dimulai pada 1 Januari 1936.
2. **Realistis & Naratif:** Tidak langsung merdeka di hari ke-1, tetapi melewati prolog krisis yang logis dan dramatis.
3. **Batas Waktu Maksimal:** Puncak proklamasi/revolusi meletus dalam batas maksimal 3 bulan (tepatnya 84 hari / ~2,8 bulan) dari awal permainan.

---

## 3. Garis Cerita Alternate History 1936 (Storyline)

### Bulan 1 (Januari 1936) — Retaknya Pax Neerlandica
- **Latar:** Dampak berkepanjangan Depresi Ekonomi Dunia melumpuhkan ekspor gula, teh, karet, dan minyak Hindia Belanda.
- **Peristiwa:** Pemotongan upah dan pemecatan massal memicu pemogokan umum buruh kereta api (*Staatsspoorwegen*) dan buruh pelabuhan Tanjung Priok serta Tanjung Perak.
- **Fokus Nasional:** `dei_focus_root` (*Retaknya Pax Neerlandica*, 28 hari).
- **Event:** `dei_trunk.1` (*Gelombang Pemogokan Umum & Krisis Kepercayaan*) dan `dei_trunk.3` (*Respon Keras Gubernur Jenderal De Jonge*).

### Bulan 2 (Februari 1936) — Pembangkangan Militer & Retaknya Garis Kolonial
- **Latar:** Semangat pemberontakan kapal perang *De Zeven Provinciën* (1933) masih hidup di kalangan prajurit bumiputera.
- **Peristiwa:** Prajurit dan bintara bumiputera KNIL di Cimahi, Magelang, dan Malang menolak perintah menembak buruh yang mogok. Senjata di barak-barak militer diselundupkan ke tangan laskar pemuda dan buruh tani. Tokoh-tokoh pergerakan nasional yang dibuang mengonsolidasikan komite aksi bawah tanah.
- **Fokus Nasional:** `dei_focus_pembangkangan` (*Pembangkangan Militer & Bangkitnya Laskar*, 28 hari).
- **Event:** `dei_trunk.2` (*Pembangkangan di Barak KNIL*) dan `dei_trunk.4` (*Konsolidasi Komite Aksi Bawah Tanah*).

### Bulan 3 (Maret 1936) — Puncak Momentum Revolusi Nasional
- **Latar:** Kekuasaan pemerintah kolonial di Batavia lumpuh; jalur komunikasi ke Den Haag terputus; milisi rakyat menguasai stasiun radio NIROM di Bandung dan Surabaya.
- **Peristiwa:** Proklamasi revolusi dan kemerdekaan nasional dikumandangkan serentak di seantero Jawa dan Sumatra!
- **Fokus Nasional:** `dei_focus_momentum_kemerdekaan` (*Momentum Revolusi Nasional*, 28 hari — selesai akhir Maret 1936).
- **Event Utama:** `dei_trunk.6` (*Momentum Kemerdekaan Telah Tiba!*) meletus secara otomatis:
  - Pemain memilih 1 dari 6 jalur ideologi:
    - **Jalur A:** Republik Nasionalis-Demokratis (Sukarno / PNI)
    - **Jalur B:** Kolonial / Federalis (Hubertus van Mook / BFO)
    - **Jalur C:** Komunis (Musso / PKI)
    - **Jalur D:** Otoriter Militeristik (Gatot Subroto / Dewan Revolusi)
    - **Jalur E:** Islamis (Sekarmadji Maridjan Kartosoewirjo / NII)
    - **Jalur F:** Kemaharajaan Majapahit (Raden Wijaya)
  - Pembagian starter armies di Jawa, dedicated starter navy di Surabaya, starter air wings di Andir & Iswahyudi, pasokan 3.000 senapan, serta rekrutmen komandan legendaris.
  - 6 cabang ideologi langsung terbuka penuh mulai akhir Maret 1936.

---

## 4. Arsitektur Teknis & Perubahan Berkas

### A. Pohon Fokus Nasional (`DEI_00_shared_trunk.txt`)
- Merampingkan batang bersama menjadi 3 fokus krisis terhubung (masing-masing 28 hari = total 84 hari):
  1. `dei_focus_root`: x = 12, y = 0, cost = 4 (28 hari).
  2. `dei_focus_pembangkangan`: x = 12, y = 4, cost = 4 (28 hari), prerequisite = `dei_focus_root`.
  3. `dei_focus_momentum_kemerdekaan`: x = 12, y = 8, cost = 4 (28 hari), prerequisite = `dei_focus_pembangkangan`.
- **Preservasi Koordinat Cabang:** Karena `dei_focus_momentum_kemerdekaan` tetap berada di koordinat `(x=12, y=8)`, seluruh 6 cabang ideologi (A, B, C, D, E, F) yang menggunakan `relative_position_id = dei_focus_momentum_kemerdekaan` tetap memiliki posisi sempurna tanpa pergeseran atau tabrakan koordinat.

### B. Event Rangkaian Krisis (`events/DEI_00_shared_trunk_events.txt`)
- Memperbarui teks dan trigger event pembuka `dei_trunk.1` s/d `dei_trunk.5` agar berpadu harmonis dengan eskalasi krisis 3 bulan 1936.
- Mempertahankan 100% integrasi gambar sprite event vanilla/R56 yang sudah teruji.

### C. Pembersihan Decision Shortcut (`common/decisions/DEI_decisions.txt`)
- Menghapus `dei_decision_revolusi_dini` karena revolusi kini merupakan mekanisme baku (default) tanpa perlu decision buatan.
- Menjaga keutuhan 25 keputusan strategis lainnya (Proklamasi Tata Kelola, Riset, Mega-Proyek, Kedaulatan Wilayah).

### D. Lokalisasi (`DEI_indonesia_l_english.yml`)
- Memperbarui judul dan deskripsi fokus serta event batang pembuka dalam Bahasa Inggris dengan tetap mempertahankan orisinalitas istilah historis Indonesia.
- Memastikan format pengkodean tetap UTF-8 with BOM (`\xef\xbb\xbf`).

---

## 5. Rencana Pengujian & Verifikasi
1. Menjalankan skrip validasi sintaks dan koordinat fokus (`final_verification.py`).
2. Memastikan tidak ada missing localisation keys (`verify_all_loc.py`).
3. Memastikan seluruh sprite dan aset gambar tetap 100% valid (`comprehensive_asset_audit.py`).
4. Memastikan UTF-8 BOM pada file lokalisasi.
