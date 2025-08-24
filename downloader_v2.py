import os
import sys # Import library sys
import subprocess # Library untuk menjalankan perintah dari luar

def download_with_yt_dlp():
    """Fungsi untuk download video menggunakan yt-dlp."""

    print("=" * 50)
    print("====== YOUTUBE DOWNLOADER (Versi yt-dlp) ======")
    print("=" * 50)

    # 1. Meminta URL dari pengguna
    video_url = input("\nMasukkan URL video YouTube yang ingin diunduh:\n> ")

    try:
        # 2. Menampilkan daftar resolusi yang tersedia
        print("\n⏳ Mengambil daftar format video, mohon tunggu...")
        
        # PERUBAHAN: Memanggil yt-dlp sebagai modul python agar pasti ditemukan
        list_formats_command = [sys.executable, "-m", "yt_dlp", "-F", video_url]
        
        # Menjalankan perintah dan menangkap outputnya
        result = subprocess.run(list_formats_command, capture_output=True, text=True, check=True, encoding='utf-8')
        
        print("\n" + "="*20 + " FORMAT TERSEDIA " + "="*20)
        print("Pilih 'ID' format yang diinginkan (utamakan yang ada video + audio).")
        print(result.stdout) # Menampilkan output dari perintah yt-dlp
        print("=" * 58)

    except subprocess.CalledProcessError as e:
        print("\n🚨 Gagal mengambil data video. Pastikan URL valid dan yt-dlp terinstal.")
        print(f"Detail Error:\n{e.stderr}")
        return
    except FileNotFoundError:
        print("\n🚨 Perintah 'yt-dlp' tidak ditemukan.")
        print("Pastikan Anda sudah menginstalnya dengan 'py -m pip install yt-dlp'")
        return


    # 3. Meminta pengguna memilih format
    while True:
        format_id = input("\nMasukkan ID format yang ingin diunduh (contoh: 22, 18): ")
        if format_id.strip():
            break
        else:
            print("🚨 ID tidak boleh kosong.")

    # 4. Menentukan lokasi penyimpanan (folder Downloads)
    save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    os.makedirs(save_path, exist_ok=True)
    
    print("\nProses download akan dimulai...")
    print(f"File akan disimpan di folder: {save_path}")

    try:
        # 5. Memulai proses download dengan format yang dipilih
        # PERUBAHAN: Memanggil yt-dlp sebagai modul python
        download_command = [
            sys.executable, "-m", "yt_dlp",
            "-f", format_id,
            "-o", os.path.join(save_path, '%(title)s.%(ext)s'),
            video_url
        ]
        
        # Menjalankan perintah download. yt-dlp akan menampilkan progress bar sendiri.
        subprocess.run(download_command, check=True)
        
        print("\n✅ Download selesai!")

    except subprocess.CalledProcessError as e:
        print("\n🚨 Gagal mengunduh video. Mungkin ID format tidak valid atau ada masalah jaringan.")
        print(f"Detail Error:\n{e.stderr}")
    except FileNotFoundError:
        print("\n🚨 Perintah 'yt-dlp' tidak ditemukan.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    download_with_yt_dlp()
