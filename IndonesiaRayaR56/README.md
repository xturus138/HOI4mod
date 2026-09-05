# Indonesia Raya: Road to Merdeka — Submod Road to 56

Mod HOI4 fokus Indonesia (Hindia Belanda → Indonesia, 1936–1956), dibangun sebagai **submod di atas Road to 56 (R56)**. Status saat ini: **v0.7 — semua 6 jalur ideologi penuh (v0.6) + aset gambar pertama** (bendera per ideologi, ikon focus custom, event picture) supaya event dan focus tidak lagi tampil kosong/generik total.

Dokumen ini penting dibaca sebelum main — ada beberapa **asumsi teknis yang belum diverifikasi ke file R56 asli** (karena mod ini dibuat tanpa akses langsung ke game/R56), dijelaskan di bagian "Asumsi & yang perlu kamu verifikasi".

## Cara install

1. Salin folder `IndonesiaRayaR56/` ke `Documents/Paradox Interactive/Hearts of Iron IV/mod/`.
2. Salin juga file `IndonesiaRayaR56.mod` (ada di level yang sama dengan folder di atas) ke `Documents/Paradox Interactive/Hearts of Iron IV/mod/` (bukan ke dalam folder `IndonesiaRayaR56/`, tapi sejajar dengannya).
3. Buka launcher HOI4, aktifkan **Road to 56** dan **Indonesia Raya: Road to Merdeka**, pastikan urutan mod-nya R56 duluan (mod ini punya `dependencies = { "The Road to 56" }` di descriptor, harusnya otomatis diurutkan launcher, tapi cek manual kalau ada masalah).
4. Mulai game sebagai **Dutch East Indies (DEI)**.

## Asumsi & yang perlu kamu verifikasi

Karena mod ini dibuat tanpa akses ke game/file R56 yang sebenarnya, ada beberapa asumsi yang **kamu perlu cek sendiri** di instalasi R56 kamu sebelum atau sambil main:

1. **Tag negara = `DEI`.** Ini tag vanilla standar untuk Dutch East Indies. Kalau R56 versi kamu memakai tag lain untuk Hindia Belanda/Indonesia, cari-ganti semua kemunculan `DEI` (dan `tag = DEI`) di seluruh file mod ini ke tag yang benar.
2. **`history/countries/DEI - ....txt` TIDAK saya sentuh/timpa.** Ini sengaja — R56 kemungkinan sudah punya file ini dengan konvensi penamaan/isinya sendiri (lihat catatan di rencana awal soal "struktur R56 tidak lazim dibanding vanilla"), dan menimpanya secara membabi buta berisiko merusak kompatibilitas. Supaya DEI benar-benar bisa dipilih & dimainkan dari awal game dengan lancar, kamu mungkin perlu membuka file history country R56 untuk DEI secara manual dan pastikan: negara ini tidak diset sebagai puppet permanen, punya ibu kota & OOB yang valid, dan partai politik awal terdaftar (`set_politics`, `set_popularities`).
3. **Mekanisme pendudukan Jepang disederhanakan.** Saya sengaja TIDAK membuat skrip pemaksaan "Jepang otomatis menaklukkan DEI" atau mekanisme occupation/puppet khusus, karena itu berisiko memakai efek yang salah tanpa bisa diuji langsung di game. Sebagai gantinya, batang fokus berhenti di "Waspada Ancaman Jepang" (naratif) lalu langsung ke "Momentum Kemerdekaan" — perang dengan Jepang (kalau terjadi) berjalan sebagai perang HOI4 normal, hasilnya ditentukan gameplay, bukan skrip paksa. Ini pilihan desain yang aman, bukan kelalaian.
4. **Ikon focus**: 8 focus "tulang punggung" (root batang bersama, titik percabangan, dan root tiap 6 jalur) sekarang pakai ikon custom bikinan sendiri (lihat bagian "Aset gambar v0.7" di bawah) — sisanya (52 focus lain) masih pakai GFX generik vanilla (`GFX_goal_generic_national_unity`, dll.), yang seharusnya aman karena kemungkinan besar sudah ada di base game/R56. Kalau ada yang tampil kotak pink (missing texture), itu kemungkinan besar dari yang generik ini, tinggal ganti baris `icon = ` di file focus terkait.
5. **Localisation ditaruh di bawah key `l_english:`** meski isinya Bahasa Indonesia — karena `l_indonesian:` kemungkinan belum resmi didukung HOI4. Kalau ternyata versi game kamu sudah mendukungnya, salin isi `DEI_indonesia_l_english.yml` ke file baru di `localisation/indonesian/` dengan key `l_indonesian:`.
6. **Belum pernah dites di game sungguhan** (dibuat tanpa akses ke HOI4). Kemungkinan ada typo sintaks kecil atau balance kasar (angka modifier belum di-tuning). Playtest pertama kamu sebaiknya fokus: (a) apakah mod bisa aktif tanpa crash bareng R56, (b) apakah semua focus dan event muncul dan bisa diklik/diambil, (c) baru setelah itu nilai-nilai modifier di-balance.

## Aset gambar v0.8 — status per kategori

- **8 bendera** (`gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`, TGA 82x52 / 41x26 / 10x7), semuanya digambar via Gen AI (bukan lagi PIL programatik): `DEI` (default pra-percabangan, Prinsenvlag), `DEI_democratic` (A), `DEI_federalist` (B, ideologi custom), `DEI_communism` (C), `DEI_fascism` (D), `DEI_islamist` (E, ideologi custom), `DEI_majapahit` (F, ideologi custom), `DEI_neutrality` (default sebelum ideologi dipilih). Jalur B/E/F masing-masing punya ideologi & bendera sendiri lewat `common/ideologies/DEI_custom_ideologies.txt` — lihat bagian di bawah.
- **Ikon focus: DIHAPUS, kembali ke ikon generik vanilla R56 untuk semua 60 focus.** Sempat dibuat 8 ikon custom (siluet flat krem), tapi setelah dibandingkan ke ikon vanilla asli (medali emas berukir dengan bingkai laurel, shading detail) gayanya kelihatan sangat beda/gak menyatu — jadi dihapus. Lihat tabel icon generik yang dipakai di bagian bawah README ini (atau tanya sesi berikutnya untuk daftar lengkapnya). Kalau mau bikin ikon custom lagi ke depannya, **harus mengikuti gaya medali/wreath vanilla**, bukan siluet flat, supaya menyatu.
- **7 event picture** (`gfx/event_pictures/*.dds`, 456x228), gaya foto arsip hitam-putih 1930-40an (bukan ilustrasi 2D — ini gaya HOI4 event art asli untuk major event): event percabangan (`dei_trunk.6`) dan event pembuka tiap 6 jalur (`dei_path_x.1`). Event pembuka Jalur A pakai **foto asli** Proklamasi Kemerdekaan 17 Agustus 1945, bukan hasil AI. Diwire lewat `interface/DEI_event_pictures.gfx`.

Yang **masih belum ada**: 52 dari 60 focus masih ikon generik vanilla (lihat poin di atas — ini pilihan sadar, bukan kelalaian), 50 dari 57 event masih tanpa gambar sama sekali (cuma event percabangan + pembuka tiap jalur yang punya), tidak ada portrait tokoh formal.

**Belum pernah dirender di game HOI4 sungguhan** — dimensi TGA/DDS di atas dikonfirmasi cocok dengan file asli v0.7 (82x52 bendera besar, 128x128 ikon focus, 456x228 event picture), tapi tampilan gabungan semua elemen ini di UI beneran belum pernah dites.

## Ideologi custom (Jalur B/E/F) — v0.8, PALING BERISIKO belum dites

Sejak v0.8, jalur B (Kolonial/Federalis), E (Islamis), F (Majapahit) tidak lagi berbagi flag `neutrality` — masing-masing sekarang punya **ideologi custom sendiri** (`federalist`, `islamist`, `majapahit`) yang didefinisikan di `common/ideologies/DEI_custom_ideologies.txt`, dan event percabangan `dei_trunk.6` di `events/DEI_00_shared_trunk_events.txt` di-update supaya `set_politics = { ruling_party = ... }` mengarah ke ideologi baru ini alih-alih `neutrality`.

Ini secara teknis **bagian HOI4 modding yang paling gampang salah tanpa akses game langsung** — sintaks `common/ideologies/` punya banyak field opsional yang perilakunya baru ketahuan salah di UI politik in-game (bukan di validasi brace/ID biasa). Yang perlu kamu cek pertama kali playtest jalur B/E/F:
- Apakah negara benar-benar berubah ke ideologi baru (bukan tetap "neutrality" atau malah error) setelah pilih opsi di event `dei_trunk.6`.
- Apakah flag `DEI_federalist.tga`/`DEI_islamist.tga`/`DEI_majapahit.tga` benar-benar muncul menggantikan flag lama.
- Apakah menu politik dalam negeri (political view) tetap bisa dibuka tanpa error/crash untuk ketiga ideologi baru ini.

Kalau ada yang aneh di salah satu poin di atas, kemungkinan besar perbaikannya ada di file ideologi ini (field yang kurang/salah), bukan di focus/event.

## Struktur file

```
IndonesiaRayaR56/
  descriptor.mod
  common/
    national_focus/
      DEI_00_shared_trunk.txt        # batang bersama 1936-1945, 11 focus
      DEI_01_path_a_republik.txt     # jalur A: Republik, 10 focus
      DEI_02_path_b_kolonial.txt     # jalur B: Kolonial/Federalis, 8 focus
      DEI_03_path_c_komunis.txt      # jalur C: Komunis, 8 focus
      DEI_04_path_d_otoriter.txt     # jalur D: Otoriter Militeristik, 8 focus
      DEI_05_path_e_islamis.txt      # jalur E: Islamis, 8 focus
      DEI_06_path_f_majapahit.txt    # jalur F: Majapahit (ahistoris), 7 focus
    decisions/
      DEI_decisions.txt              # decision "Revolusi Dini"
    ideas/
      DEI_ideas.txt                  # semua national spirit (19 total)
  events/
    DEI_00_shared_trunk_events.txt
    DEI_01_revolusi_dini_events.txt
    DEI_02_path_a_events.txt
    DEI_03_path_b_events.txt
    DEI_04_path_c_events.txt
    DEI_05_path_d_events.txt
    DEI_06_path_e_events.txt
    DEI_07_path_f_events.txt
  localisation/english/
    DEI_indonesia_l_english.yml      # 291 loc key, semua sudah dicek konsisten
  interface/
    DEI_event_pictures.gfx           # wiring 7 event picture custom
  gfx/
    flags/                           # 8 bendera ideologi x 3 ukuran (TGA)
    event_pictures/                  # 7 event picture custom (DDS)
```

## Fitur yang sudah jalan di v0.6

- **Batang fokus bersama** (1936–1945): 11 focus, tiap focus penting punya event pendamping dengan pilihan (bukan cuma efek instan) — reformasi Volksraad, ekonomi liberal vs monopoli kolonial, pendidikan pribumi, sikap ke gerakan nasionalis (represif vs akomodatif), reformasi KNIL, cari dukungan asing, waspada Jepang.
- **Decision "Revolusi Dini"** — selalu tersedia sejak hari pertama. Kalau diambil, langsung memicu pemberontakan dan melompat ke titik percabangan ideologi tanpa perlu memainkan batang fokus penuh. Ditandai jelas sebagai mode opsional/ahistoris di teks event-nya.
- **Titik percabangan "Momentum Kemerdekaan"** dengan 6 pilihan jalur (event `dei_trunk.6`).
- **Semua 6 jalur ideologi digarap PENUH** (bukan lagi stub), total 60 focus + 58 event di seluruh mod:
  - **Jalur A — Republik Nasionalis-Demokratis** (10 focus, 9 event): Proklamasi → bentuk TKR → diplomasi internasional → dua gelombang Agresi Militer Belanda → Perundingan Meja Bundar → demokrasi parlementer → sengketa Papua Barat → Demokrasi Terpimpin.
  - **Jalur B — Kolonial/Federalis** (8 focus, 8 event): padamkan revolusi → tumpas gerilyawan / reformasi terbatas → negara-negara federal → Uni Belanda-Indonesia → status dominion → gabung Persemakmuran Belanda.
  - **Jalur C — Komunis** (8 focus, 8 event): Front Rakyat menang (kebalikan Peristiwa Madiun) → land reform radikal → singkirkan faksi nasionalis → Tentara Rakyat → pilihan poros Soviet vs Tiongkok (mutually exclusive) → industrialisasi sosialis → ekspor revolusi.
  - **Jalur D — Otoriter Militeristik** (8 focus, 8 event): kudeta militer → darurat militer → bubarkan partai → industri militer → propaganda radikal → barisan pemuda militan → klaim wilayah Nusantara → ambisi regional.
  - **Jalur E — Islamis** (8 focus, 8 event, berbasis gerakan Darul Islam/Kartosoewirjo yang diperbesar jadi jalur menang): proklamasi Negara Islam Indonesia → dewan ulama & syariat → Tentara Islam Indonesia (TII) → hubungan dunia Arab → hadapi faksi sekuler → persatuan Islam Nusantara.
  - **Jalur F — Kebangkitan Majapahit (AHISTORIS, selalu tersedia sebagai opsi — tidak ada toggle terpisah)** (7 focus, 9 event termasuk event chain 3-tahap "pencarian pusaka"): bangkitkan semangat Majapahit → ekspedisi pusaka (3 tahap: penemuan → reaksi tokoh nasionalis lain → reaksi negara tetangga) → dewan adat → angkatan laut agung → klaim "Nusantara Raya" → satukan kerajaan-kerajaan → proklamasikan kekaisaran baru.
- **Toggle konten ahistoris** (decision terpisah) yang menggerbang jalur Majapahit — pemain yang mau pengalaman historis-murni bisa mematikannya.
- **Validasi otomatis dijalankan sebelum paket ini dikirim**: brace `{ }` seimbang di semua file, 291 loc key semuanya terpakai & terpenuhi, 58 event id semuanya didefinisikan & dipanggil konsisten, 60 focus id semuanya konsisten (termasuk `prerequisite`, `mutually_exclusive`, `relative_position_id`), 19 idea id semuanya konsisten, tidak ada dua focus yang bertumpuk di koordinat sama.

## Roadmap lanjutan (di luar v0.6)

Semua 6 jalur sudah ada sebagai fondasi bermain penuh (bukan stub lagi). Yang masih realistis buat versi berikutnya, sesuai rencana awal:

- **v0.8+ — Polish**: lebih banyak flavor event acak per jalur (event non-focus yang muncul random selama game — semua event saat ini terikat ke focus, `is_triggered_only`), unit & national spirit unik per jalur yang lebih detail, portrait tokoh sejarah, ikon focus custom bergaya medali/wreath vanilla (lihat bagian "Aset gambar" di atas), playtest kompatibilitas R56 menyeluruh, tuning modifier berdasarkan hasil playtest sungguhan.
- **Tokoh sejarah bernama** (van Mook di jalur B, Kartosoewirjo-style figure di jalur E, dll.) belum dimasukkan sebagai `character` HOI4 formal (portrait + leader trait) — event-event saat ini menyebut peran/situasi secara naratif tapi belum mengikat ke sistem country_leader/advisor HOI4. Ini pekerjaan v0.7+.

## Kalau ada error saat load

Paling sering di HOI4 modding: typo bracket `{ }` yang tidak seimbang, atau referensi ke idea/focus/event id yang belum didefinisikan. Semua file di mod ini saya susun konsisten (prefix `dei_`/`DEI_`), jadi kalau game log (`error.log` di folder `Documents/Paradox Interactive/Hearts of Iron IV/logs/`) menyebut satu id spesifik yang error, cari id itu persis di file-file di atas — kemungkinan besar cuma butuh penyesuaian kecil (paling mungkin: nama GFX icon yang tidak ada, sesuai poin 4 di atas).
