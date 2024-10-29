#Jangan Di Hapus
#yt=https://youtube.com/@rendyx_solo-player
#Credits By Reyhan6610
#MT 2024-2045
import requests
import socket
from urllib.parse import urlparse

def get_status_code(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return None

def get_ip_address(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

def check_status(status_code):
    if status_code and 200 <= status_code < 400:
        return "Online"
    else:
        return "Offline"

def main():
    url = input("Masukkan tautan (URL): ").strip()
    
    # Pastikan URL memiliki skema (http:// atau https://)
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Default ke http jika tidak ada

    status_code = get_status_code(url)
    ip_address = get_ip_address(url)
    status = check_status(status_code)

    print("\nHasil:")
    print(f"Status Kode: {status_code if status_code else 'Tidak dapat diakses'}")
    print(f"IP Website: {ip_address if ip_address else 'Tidak dapat ditemukan'}")
    print(f"Tautan: {url}")
    print(f"Status: {status}")

if __name__ == "__main__":
    main()