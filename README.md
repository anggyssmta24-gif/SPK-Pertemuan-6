**Sistem Pendukung Keputusan Pemilihan Tempat PKL Siswa SMK**

**Deskripsi Project**
Project ini merupakan aplikasi Sistem Pendukung Keputusan (SPK) berbasis web yang digunakan untuk membantu siswa SMK dalam menentukan tempat Praktik Kerja Lapangan (PKL) yang paling sesuai.

Aplikasi ini dibuat menggunakan Python Flask dan MySQL sebagai database. Sistem ini menerapkan metode Simple Additive Weighting (SAW) untuk menghitung nilai setiap alternatif tempat PKL berdasarkan beberapa kriteria.

**Tujuan Project**
1. Membantu siswa memilih tempat PKL yang sesuai dengan jurusan dan kebutuhan.
2. Membantu pihak sekolah memberikan rekomendasi tempat PKL secara objektif.
3. Mengurangi subjektivitas dalam pemilihan tempat PKL.
4. Menghasilkan ranking tempat PKL berdasarkan data dan bobot kriteria.
   
**Metode yang Digunakan**
Metode yang digunakan pada project ini adalah Simple Additive Weighting (SAW).
Kriteria yang digunakan:
1. Jarak
2. Fasilitas
3. Reputasi
   
**Bobot kriteria:**
Jarak = 20%
Fasilitas = 30%
Reputasi = 50%

**Konversi nilai:**
Jarak
Dekat = 3
Sedang = 2
Jauh = 1

Fasilitas
Lengkap = 3
Cukup = 2
Kurang = 1

Reputasi
Sangat Baik = 3
Baik = 2
Cukup = 1

**Fitur Aplikasi**
Dashboard
Tambah Data Tempat PKL
Daftar Tempat PKL
Edit Data Tempat PKL
Hapus Data Tempat PKL
Data Kriteria
Data Penilaian
Hasil Ranking Tempat PKL

**Teknologi yang Digunakan**
Python
Flask
MySQL
HTML
CSS
phpMyAdmin
Visual Studio Code

**Struktur Folder**
spk_pkl/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── tempat_pkl.html
│   ├── list_tempat_pkl.html
│   ├── edit_tempat_pkl.html
│   ├── kriteria.html
│   ├── penilaian.html
│   └── hasil.html
│
├── static/
│   └── css/
│       └── style.css
│
└── database/
    └── spk_pkl.sql

**Cara Menjalankan Project**

1. Clone repository ini.
2. Buka project menggunakan Visual Studio Code.
3. Pastikan Python dan MySQL sudah terinstall.
4. Install library yang dibutuhkan:
5. pip install flask
6. pip install flask-mysqldb
7. Buat database MySQL dengan nama: _spk_pkl_
8. Jalankan file app.py: python app.py
9. Buka browser dan akses: http://127.0.0.1:5000
10. Tampilan Aplikasi
