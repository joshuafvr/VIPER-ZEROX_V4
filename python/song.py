#Jangan Di Hapus
#yt=https://youtube.com/@rendyx_solo-player
#Credits By Reyhan6610
#MT 2024-2045
import os
import subprocess
import sys

def download_video_as_mp3(url):
    # Nama file output
    output_file = "output.mp3"
    
    # Command untuk mengunduh dan mengonversi video ke MP3
    command = f'yt-dlp -x --audio-format mp3 "{url}" -o "{output_file}"'
    
    # Menjalankan command
    try:
        subprocess.run(command, shell=True, check=True)
        print(output_file)  # Mengirimkan nama file output
    except subprocess.CalledProcessError as e:
        print(f'Terjadi kesalahan saat mengunduh video: {e}')

# Mendapatkan URL dari argumen
if __name__ == "__main__":
    video_url = sys.argv[1]
    if video_url.startswith('http://') or video_url.startswith('https://'):
        download_video_as_mp3(video_url)
    else:
        print("URL tidak valid. Pastikan URL diawali dengan http:// atau https://")