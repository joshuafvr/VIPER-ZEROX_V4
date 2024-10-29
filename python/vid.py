#Jangan Di Hapus
#yt=https://youtube.com/@rendyx_solo-player
#Credits By Reyhan6610
#MT 2024-2045
import os
import subprocess
import sys

def donlotBokep(url):
    # Nama file output
    output_file = "output.mp4"
    
    # Command untuk mengunduh video ke format MP4
    command = f'yt-dlp -f best "{url}" -o "{output_file}"'
    
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
        donlotBokep(video_url)
    else:
        print("URL tidak valid. Pastikan URL diawali dengan http:// atau https://")