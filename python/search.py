#Jangan Di Hapus
#yt=https://youtube.com/@rendyx_solo-player
#Credits By Reyhan6610
#MT 2024-2045
import sys
from youtubesearchpython import VideosSearch

def search_youtube(query, max_results=5):
    videos_search = VideosSearch(query, limit=max_results)
    results = videos_search.result()

    if not results['result']:
        print("Tidak ada hasil ditemukan.")
        return
    
    for idx, video in enumerate(results['result'], start=1):
        title = video['title']
        link = video['link']
        print(f"{idx}. {title}\n   {link}\n")

def main():
    if len(sys.argv) < 2:
        print("Kata kunci pencarian tidak boleh kosong.")
        return
    
    query = ' '.join(sys.argv[1:])
    search_youtube(query)

if __name__ == "__main__":
    main()