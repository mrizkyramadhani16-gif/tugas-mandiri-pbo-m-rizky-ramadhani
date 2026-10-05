# Studi Kasus 2 — Streaming Data Sensor IoT Hemat Memori

## Deskripsi
Program mensimulasikan 10 pembacaan suhu sensor. Data dihasilkan dan dikonsumsi satu per satu, kemudian dikategorikan menjadi Dingin, Normal, atau Panas.

## Konsep Python
- **Generator function** menggunakan `yield` untuk menghasilkan data bertahap.
- **Iterator pattern** dengan mengambil data menggunakan `next()`.
- **Efisiensi memori** karena program tidak menyimpan seluruh aliran data ke dalam list besar.

## Aturan Kategori
- Dingin: suhu < 20°C
- Normal: suhu 20°C sampai 30°C
- Panas: suhu > 30°C

## Cara Menjalankan
```bash
python main.py
```

Bukti eksekusi tersedia pada `output.png`.
