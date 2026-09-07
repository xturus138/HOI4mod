# Rencana Mod HOI4: Indonesia (Submod Road to 56) — v2, Full Scope

> **[ARSIP — Status Sept 2026]** Dokumen ini adalah rencana perencanaan AWAL proyek (draf v0.1–v0.7) dan sudah jauh dilampaui oleh perkembangan aktual mod. Status nyata saat ini: **v1.0.2**, 139 fokus nasional, 155 event, 6 jalur ideologi lengkap dengan `ruling_party`/partai/pemimpin yang sudah diverifikasi konsisten, lulus 100% pada seluruh script audit otomatis, dan sudah di-deploy ke folder mod HOI4 untuk playtest. Lihat [README.md](README.md) untuk dokumentasi fitur dan struktur file yang akurat & terkini. Isi di bawah ini dipertahankan sebagai arsip sejarah perencanaan, bukan sebagai rujukan status terkini.

> Revisi dari draf pertama. Perubahan utama: scope diperluas dari "satu jalur MVP" menjadi **semua jalur ideologi/alternatif sejarah Indonesia**, dengan penekanan pada **kepadatan event** (event-rich) di setiap jalur, bukan cuma focus tree kering.

## 1. Ringkasan proyek

Mod Hearts of Iron IV baru, fokus Indonesia, dibangun sebagai **submod di atas Road to 56 (R56)** (dependency, minim overwrite — lihat bagian 6). Rentang waktu mengikuti R56 penuh: 1936–1956.

Perubahan visi dari draf pertama: ini bukan lagi "satu jalur Republik lalu selesai", tapi **pohon fokus bercabang besar** dengan banyak jalur ideologi/alternatif yang benar-benar berbeda arah, masing-masing dengan rangkaian event sendiri — mirip filosofi mod overhaul besar (Kaiserreich, R56 sendiri): ada **batang sejarah bersama** (kolonial 1936–1942, sama untuk semua jalur), lalu di titik percabangan (sekitar 1942–1945) pemain memilih arah yang saling eksklusif.

Referensi yang sudah ada dan perlu dijadikan pembanding (bukan dijiplak): submod **"East Indies Reworked – A Road to 56 Submod"** (mangkrak sejak 2024, tapi punya tokoh sejarah & beberapa jalur serupa: kolonial, dominion, otoriter, republik, komunis).

## 2. Jalur-jalur yang direncanakan ("semua kemungkinan")

Semua jalur berbagi **batang bersama** dulu:

**Batang bersama (1936–1942, semua jalur lewat sini)**
- Hindia Belanda kolonial: Volksraad, tokoh nasionalis awal (M.H. Thamrin dkk.), tekanan ekonomi krisis 1930-an, ancaman Jepang.
- Pendudukan Jepang (1942–1945): pembentukan PETA, Jepang membina sekaligus menekan tokoh nasionalis (Sukarno–Hatta di bawah pendudukan). Titik ini jadi **percabangan utama**.

Dari titik percabangan, jalur-jalur berikut direncanakan **semuanya ada**, masing-masing playable dan berbeda arah:

| Jalur | Inti cerita | Basis |
|---|---|---|
| **A. Republik Nasionalis-Demokratis** | Proklamasi 1945 → revolusi fisik melawan Belanda → demokrasi liberal parlementer → (opsi lanjut) demokrasi terpimpin ala Sukarno di akhir linimasa. Jalur "historis utama". | Historis |
| **B. Kolonial/Federalis (Belanda menang)** | Agresi Militer Belanda berhasil, atau Republik Indonesia Serikat federal (NIT, Pasundan, dll — negara-negara boneka Belanda) jadi permanen di bawah pengaruh Belanda/Uni Belanda-Indonesia. | Historis (skenario "Belanda menang") |
| **C. Komunis** | PKI/Front Rakyat menang perebutan pengaruh pasca-1945 (kebalikan dari Peristiwa Madiun historis) → Republik Rakyat Indonesia condong Soviet/Tiongkok. | Historis-kontrafaktual |
| **D. Otoriter Militeristik/Nasionalis Radikal** | Faksi militer/nasionalis radikal ambil alih lewat kudeta atau darurat perang, rezim represif-ekspansionis (semacam "fasis Nusantara"). | Kontrafaktual, gaya umum di mod overhaul untuk hampir semua negara |
| **E. Islamis** | Berbasis gerakan Darul Islam historis (Kartosoewirjo dkk.) — jalur ke Negara Islam Indonesia kalau menang, bukan cuma jadi pemberontakan kecil seperti di sejarah asli. | Historis-kontrafaktual |
| **F. Kebangkitan Majapahit / Nusantara Raya** | Gerakan revivalis yang mengangkat warisan Kemaharajaan Majapahit untuk menyatukan/mengklaim seluruh Nusantara (termasuk wilayah di luar Indonesia modern). **Ditandai eksplisit sebagai konten fantasi/ahistoris**, sama seperti jalur-jalur "what if" ekstrem di Kaiserreich atau R56 sendiri — sebaiknya digerbang lewat game rule terpisah ("Aktifkan jalur ahistoris") supaya pemain yang mau pengalaman historis-murni bisa mematikannya. | Fantasi/ahistoris eksplisit |

Catatan desain penting:
- Jalur **F (Majapahit)** secara sengaja saya beri label fantasi/ahistoris karena Majapahit adalah kerajaan abad ke-14 yang runtuh jauh sebelum 1936 — tidak ada jalur "realistis" untuk itu bangkit lagi di linimasa 1936–1956. Ini murni konten alternate-history/fantasi ala game strategi, sama seperti mod-mod besar biasa punya jalur ekstrem seperti itu (dan itu wajar serta lazim dalam genre ini). Saya akan bangun ini sebagai cabang yang jelas terpisah dan diberi tag/gate sendiri, bukan dicampur ke jalur historis.
- Jalur **D dan E** memakai elemen kontrafaktual/gerakan historis yang diperbesar dampaknya — ini pola standar HOI4 modding (semua mod besar melakukan ini untuk faksi kalah dalam sejarah asli) dan tidak masalah, tapi tetap saya buat sebagai *game content* (nama gerakan, tokoh fiksi turunan gerakan, bukan memfitnah tokoh nyata dengan tindakan yang tidak mereka lakukan).

## 3. Filosofi "rich in event" (permintaan utama kamu)

Supaya benar-benar padat event dan bukan cuma pohon fokus kering, event dibangun berlapis:

1. **Event pendamping tiap focus penting** — bukan cuma efek instan pas focus selesai, tapi popup event dengan 2-4 pilihan (A/B/C/D) yang punya konsekuensi berbeda (national spirit, war support, stability, hubungan dengan negara lain, unlock/lock focus berikutnya).
2. **Event chain multi-tahap per jalur** — misalnya jalur Majapahit: event 1 "penemuan/klaim pusaka & dukungan tokoh adat" → event 2 reaksi tokoh nasionalis lain (pro/kontra) → event 3 reaksi negara tetangga (Malaya Britania, Filipina) → baru unlock focus ekspansi. Bukan satu event berdiri sendiri.
3. **Flavor event acak periodik**, bobot kemunculannya beda-beda tergantung jalur/ideologi yang sedang dimainkan (mekanisme umum di R56/Kaiserreich: pakai `on_actions` + `mean_time_to_happen` yang dikondisikan ke ideologi negara berjalan).
4. **Event reaktif dari AI lain** — Belanda, Jepang, Inggris (Malaya) bereaksi beda tergantung jalur Indonesia yang dipilih pemain (mis. Belanda lebih agresif kalau pemain ambil jalur Komunis/Majapahit, lebih akomodatif kalau jalur Federalis).
5. **Decision juga trigger event kecil**, bukan cuma efek diam-diam — supaya decision terasa hidup, bukan sekadar tombol.

Implikasi teknis: tiap jalur butuh file event sendiri (`events/ID_jalur_a_republik.txt`, `ID_jalur_b_kolonial.txt`, dst.) plus file event bersama untuk batang 1936–1942. Ini realistis dikerjakan bertahap per jalur, bukan sekaligus — lihat roadmap di bagian 5.

## 3a. Fitur "Revolusi Dini" (opsi buat pemain tidak sabaran)

Tambahan sesuai permintaanmu: supaya tidak wajib menunggu sampai ~1945 baru sampai ke bagian seru (perang kemerdekaan, pilih ideologi), disediakan **opsi percepatan** dari awal game:

- Sesaat setelah game dimulai (1936, awal linimasa R56), muncul event: **"Percepat Menuju Revolusi?"** — menjelaskan bahwa jalur historis penuh (kolonial → pendudukan Jepang → baru revolusi) akan makan waktu, dan menawarkan jalan pintas.
  - **Pilih "Tidak" / historis**: lanjut ke batang bersama seperti rencana semula (bagian 2), semua build-up 1936–1945 dimainkan penuh.
  - **Pilih "Ya" / Revolusi Dini**: men-trigger rangkaian event pemberontakan yang mulai jauh lebih awal dari sejarah asli (semacam skenario "bagaimana jika revolusi pecah lebih cepat") — kerusuhan/pemberontakan muncul dalam beberapa bulan sejak start, lalu pemain langsung diarahkan ke titik percabangan 6 jalur ideologi (bagian 2) tanpa harus menunggu tahun 1945.
- Ini **ditandai jelas sebagai mode ahistoris/opsional** (sama seperti jalur Majapahit) — bukan klaim bahwa revolusi "seharusnya" terjadi di 1936, tapi fitur kenyamanan buat pemain yang mau langsung ke bagian strategis (pilih ideologi & jalankan negara) tanpa menunggu build-up panjang.
- Efek samping yang perlu digarap supaya tidak terasa aneh: kalau ambil Revolusi Dini, tokoh-tokoh yang historisnya baru menonjol di 1945 (mis. beberapa tokoh militer TKR) perlu punya versi "versi muda/versi awal" di data karakter, atau event dibuat generik dulu (mis. "seorang perwira KNIL pembelot" tanpa nama spesifik) supaya tidak ganjil secara waktu. Ini saya tandai sebagai detail implementasi v0.1, bukan alasan untuk membatalkan fiturnya.
- Teknis: dibuat sebagai **decision** yang selalu tersedia dari hari pertama (bukan cuma event sekali muncul yang gampang kelewat), plus satu event pemicu ringan di awal supaya pemain yang tidak buka menu decision tetap ditawari pilihan ini. Begitu dipilih, decision itu hilang/terkunci (one-time).

Fitur ini masuk ke **v0.1** (skeleton), karena dia bagian dari fondasi pacing seluruh mod, bukan tambahan belakangan.

## 4. Skala realistis: ini proyek besar

Supaya ekspektasi jelas: dengan 6 jalur (1 batang + 5-6 cabang) dan tiap cabang butuh belasan-puluhan focus plus event pendamping berlapis, ini setara skala **total conversion kecil**, bukan lagi "submod ringan". Wajar dan bagus sebagai visi jangka panjang, tapi realistisnya dikerjakan **satu jalur penuh dulu sampai matang** (termasuk event-nya), baru lanjut jalur berikutnya — bukan bikin 6 jalur setengah jadi sekaligus. Roadmap di bawah saya susun begitu, tapi **semua 6 jalur tetap masuk peta jalan akhir**, tidak ada yang dicoret dari visi.

## 5. Roadmap (build order incremental, cakupan akhir = semua jalur)

- ✅ **v0.1 — Skeleton & batang bersama** — SELESAI: descriptor + dependency ke R56, struktur folder, focus tree batang 1936–1945 lengkap dengan event pendamping, titik percabangan ke 6 jalur, plus decision/event "Revolusi Dini".
- ✅ **v0.2 — Jalur A (Republik Nasionalis-Demokratis)** — SELESAI: 10 focus + 9 event.
- ✅ **v0.3 — Jalur B (Kolonial/Federalis)** — SELESAI: 8 focus + 8 event.
- ✅ **v0.4 — Jalur C (Komunis)** — SELESAI: 8 focus + 8 event, termasuk pilihan poros Soviet vs Tiongkok.
- ✅ **v0.5 — Jalur D (Otoriter/Militeristik) & E (Islamis)** — SELESAI: masing-masing 8 focus + 8 event.
- ✅ **v0.6 — Jalur F (Majapahit/Nusantara Raya)** — SELESAI: 7 focus + 9 event (termasuk event chain 3-tahap "pencarian pusaka"), digerbang toggle ahistoris.
- **v0.7+ — Polish lintas-jalur** (belum dikerjakan): flavor event acak non-focus, unit & national spirit unik per jalur, art custom (flag per ideologi, portrait tokoh, ikon focus sendiri — semua masih pakai GFX generik vanilla di v0.6), tokoh sejarah sebagai `character` formal HOI4, playtest kompatibilitas R56 menyeluruh & tuning modifier berdasarkan hasil playtest.

Status total di v0.6: 60 focus + 58 event + 19 national spirit di seluruh mod, sudah lolos validasi otomatis (brace seimbang, semua id/loc key konsisten) — tapi **belum pernah dites di HOI4 sungguhan** karena dikerjakan tanpa akses ke game. Lihat README.md di dalam paket mod untuk detail asumsi yang perlu diverifikasi.

## 6. Strategi kompatibilitas teknis dengan R56 (tidak berubah dari draf pertama)

- `descriptor.mod`/`.metadata` pakai `dependencies = { "The Road to 56" }` supaya R56 dimuat duluan.
- Minimalkan overwrite file R56 — file baru pakai nama unik; timpa file R56 cuma kalau benar-benar perlu, dan itu dicatat sebagai risiko maintenance jangka panjang.
- R56 punya struktur/penamaan tidak lazim dibanding vanilla → wajib buka file R56 asli dulu (state ID, tag negara Hindia Belanda/Indonesia yang sudah ada) sebelum mulai coding v0.1, supaya semua 6 jalur nanti konsisten dengan pola R56, bukan mengasumsikan dari vanilla.
- Load order: submod selalu di bawah R56.
- R56 aktif dikembangkan → perlu proses cek changelog R56 berkala supaya submod tidak pecah setelah update mereka.

## 7. Tools yang dibutuhkan (tidak berubah)

HOI4 + Road to 56 (testing), VS Code (syntax highlighting Paradox script), GIMP/Paint.NET (`.dds` untuk flag/ikon/portrait), Git untuk version control mod, tools komunitas tambahan dicari saat mulai butuh (converter DDS, focus tree visualizer).

## 8. Risiko & hal yang perlu diawasi

- **Scope besar** = risiko terbesar: kalau dikerjakan sekaligus 6 jalur, gampang jadi tidak ada yang selesai. Mitigasi: disiplin ke urutan roadmap, satu jalur matang dulu (fokus + event lengkap) sebelum pindah jalur berikutnya.
- **R56 update** bisa mengubah file yang kita timpa/rujuk.
- **Konvensi non-standar R56** — verifikasi ke file asli, jangan asumsi dari tutorial vanilla.
- **Jalur F (Majapahit) perlu framing jelas sebagai fantasi/ahistoris** sejak awal (nama file, gate game rule, deskripsi in-game) supaya tidak membingungkan dengan jalur historis, dan supaya jelas ini konten hiburan alternate-history, bukan klaim sejarah.
- **Overlap dengan "East Indies Reworked"** — bukan masalah teknis, tapi nilai jual modmu perlu jelas beda (lebih lengkap jalurnya, lebih rich event, lebih aktif di-maintain).

## 9. Langkah selanjutnya

Rekomendasi konkret: mulai dari **v0.1** — skeleton mod + batang bersama 1936–1945 dengan event pendamping penuh, plus riset file R56 asli untuk tag/ID yang tepat. Begitu batang bersama ini solid dan teruji jalan bareng R56, jalur A (Republik) digarap penuh sebagai "jalur pembuktian pola" sebelum lima jalur lain menyusul sesuai roadmap.

Kalau kamu setuju urutan ini, saya bisa langsung mulai kerjakan v0.1 (folder struktur mod + descriptor + focus tree batang bersama + event awal) di sesi ini.

---

**Sumber riset:**
- [The Road to 56 – Hearts of Iron 4 Wiki](https://hoi4.paradoxwikis.com/The_Road_to_56)
- [Mod structure – Hearts of Iron 4 Wiki](https://hoi4.paradoxwikis.com/Mod_structure)
- [GitHub – deliciousmods/1956_beta (Road to 56 Beta Build)](https://github.com/deliciousmods/1956_beta)
- [Steam Workshop – East Indies Reworked: A Road to 56 Submod](https://steamcommunity.com/sharedfiles/filedetails/?id=3116352427)
- [Steam Workshop – Hollandia Historica: East Indies Reworked](https://steamcommunity.com/sharedfiles/filedetails/?id=2898713030)
