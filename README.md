# YouTube Video Downloader (Versi Python & yt-dlp)

Ini adalah sebuah skrip Python sederhana yang berfungsi sebagai pengunduh video dari YouTube. Program ini berjalan di terminal (command-line) dan menggunakan **yt-dlp** sebagai backend untuk memastikan keandalan dan kompatibilitas dengan perubahan terbaru dari YouTube.

## ✨ Fitur Utama
- **Pilih Kualitas**: Menampilkan daftar lengkap format video dan audio yang tersedia (resolusi, fps, ukuran file) sebelum mengunduh.
- **Andal**: Ditenagai oleh yt-dlp, yang secara aktif diperbarui dan jauh lebih stabil daripada library lainnya.
- **Penyimpanan Otomatis**: Video yang diunduh secara otomatis disimpan di folder **Downloads** bawaan sistem operasi Anda.
- **Sederhana**: Antarmuka berbasis teks yang mudah digunakan langsung dari terminal.

## ⚙️ Prasyarat
Sebelum memulai, pastikan Anda sudah menginstal **Python 3.7 atau lebih baru**.

👉 Anda bisa mengunduh Python dari [python.org](https://www.python.org/downloads/).

> Penting: Saat instalasi di Windows, pastikan untuk mencentang kotak **"Add python.exe to PATH"**.

## 🚀 Instalasi & Persiapan
Ikuti langkah-langkah ini di terminal atau command prompt Anda untuk menyiapkan proyek.

1. **Clone atau Unduh Repositori**  
   Unduh file `downloader_v2.py` dan letakkan di dalam sebuah folder khusus untuk proyek ini.

2. **Buka Terminal di Folder Proyek**  
   Arahkan terminal Anda ke direktori tempat Anda menyimpan file tersebut.

3. **Buat Lingkungan Virtual (Virtual Environment)**  
   Disarankan menggunakan virtual environment agar library yang diinstal tidak bercampur dengan proyek lain.
   ```bash
   python -m venv .venv
   ```

4. **Aktifkan Lingkungan Virtual**
   - Di **Windows (PowerShell/CMD)**:
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - Di **MacOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```
   Jika berhasil, Anda akan melihat `(.venv)` di awal baris terminal.

5. **Instal Library yang Dibutuhkan**
   ```bash
   pip install yt-dlp
   ```

## ▶️ Cara Menggunakan
Setelah instalasi selesai, Anda siap untuk mengunduh video!

1. Pastikan lingkungan virtual (`.venv`) sudah aktif.  
2. Jalankan skrip dengan perintah berikut:
   ```bash
   python downloader_v2.py
   ```
3. Masukkan URL video YouTube saat diminta.  
4. Program akan menampilkan daftar format video yang tersedia.  
5. Pilih ID dari format yang ingin Anda unduh (contoh: `18` untuk 360p atau `22` untuk 720p).  
6. Proses unduhan akan dimulai, dan file akan disimpan di folder **Downloads** Anda.

## ⚠️ Disclaimer
Program ini dibuat untuk tujuan **edukasi**. Mohon gunakan secara bijak dan hormati **hak cipta** dari konten yang Anda unduh.  
Mengunduh materi berhak cipta tanpa izin dapat melanggar hukum di negara Anda.
