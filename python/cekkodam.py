#Jangan Di Hapus
#yt=https://youtube.com/@rendyx_solo-player
#Credits By Reyhan6610
#MT 2024-2045
import random
import sys

# Daftar karakter
karakter = [
    "Ambatukan", "Jawir", "Ambaruwo", "Masrusdi", "Mas Fais", 
    "Kakangku", "Bundah Rahma", "Jarjit", "Roblox", "Skibidi Toilet", 
    "Kaicenat", "Fanum Tax", "King Riblox", "Skibidi Riz", "Komeng", 
    "Mas Narji", "Fladimir Putin", "Fufufafa", "Ronaldo", "Mesi", 
    "Neymar", "Mbape", "Katak Bizer", "Pelé", "Maradona", 
    "Johan Cruyff", "George Best", "MarkZukerberek", "Lu cinta Luna", 
    "Kiboy", "Baloy", "Kobokanaeru", "Naruto", "Sasuke", 
    "Itachi", "Rahfiahmad", "Denji", "Gojo Satoru", "Anya Forger", 
    "Tanjiro Kamado", "Eren Yeager", "Makima", "Luffy"
]

# Dictionary untuk menyimpan karakter berdasarkan nama pengguna
reyhan_rendyx = {}

# Fungsi untuk memunculkan karakter acak atau yang sudah ada
def pilih_karakter(nama):
    if nama in reyhan_rendyx:
        # Jika nama sudah ada, ambil karakter yang sudah disimpan
        karakter_acak = reyhan_rendyx[nama]
    else:
        # Jika nama belum ada, pilih karakter acak dan simpan
        karakter_acak = random.choice(karakter)
        reyhan_rendyx[nama] = karakter_acak
    
    return f"{nama}, Kodammu Itu: {karakter_acak}"

# Cek apakah ada argumen yang diberikan
if len(sys.argv) > 1:
    nama_pengguna = sys.argv[1]
    print(pilih_karakter(nama_pengguna))
else:
    print("Nama pengguna tidak diberikan.")