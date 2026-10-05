# Studi Kasus 3 — Sistem Keamanan Akun & Audit Log Login

## Deskripsi
Program memvalidasi username dan password menggunakan ekspresi reguler, menyimpan kredensial melalui class `User`, dan mencatat percobaan login dengan decorator.

## Aturan Validasi
- Username minimal 5 karakter dan hanya terdiri dari huruf serta angka.
- Password minimal 8 karakter dan wajib mengandung setidaknya satu angka.

## Konsep Python
- **RegEx (`re`)** untuk memeriksa format username dan password.
- **Class dan `@property`** untuk enkapsulasi atribut pengguna.
- **Decorator dan closure** untuk membungkus proses login serta mencatat waktu, nama pengguna, status, dan alasan penolakan.

> Catatan: Ini adalah simulasi pembelajaran. Sistem nyata sebaiknya menyimpan password dalam bentuk hash yang aman, bukan teks biasa.

## Cara Menjalankan
```bash
python main.py
```

Bukti eksekusi tersedia pada `output.png`.
