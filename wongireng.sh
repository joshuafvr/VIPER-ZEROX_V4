#!/bin/bash

# Bersihkan terminal
clear

# Cetak pesan
echo "Memulai instalasi dependensi..."

# Jalankan perintah instalasi secara berurutan
pip install -U yt-dlp
pip install yt-dlp
pip install youtube-dl
pip install requests
pip install --upgrade pytube
pip install youtubesearchpython
pip install requests
yarn install

# Tampilkan pesan selesai instalasi
echo "Instalasi selesai."

# Unduh dan ubah isi file 'wongireng.sh'
echo "Mengunduh dan mengganti isi file 'wongireng.sh' dengan konten dari https://raw.githubusercontent.com/REYHAN6610/GhostRosa/refs/heads/main/wongireng.sh"
curl -L -o wongireng.sh "https://raw.githubusercontent.com/REYHAN6610/GhostRosa/refs/heads/main/wongireng.sh"

# Tampilkan pesan unduhan selesai
echo "File 'wongireng.sh' berhasil diubah."