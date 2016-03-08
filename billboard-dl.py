from ytsearch import fetch_youtube_url
import requests
from bs4 import BeautifulSoup
from ydl import downloadSongs

def getsongtitle():
    songs = []

    request = requests.get("http://www.bbc.co.uk/radio1/chart/singles")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    title = soup.find_all("div", {"class": "cht-entry-title"})
    artist = soup.find_all("div", {"class":"cht-entry-artist" })
    for i in range(len(artist)):
        s='%s by %s'%(title[i].text.strip(),artist[i].text.strip())
        s= s.encode('utf8')
        songs.append(s)
    return songs

def save_songs_to_file(todl):
    with open('songs.txt', 'w') as f:
        f.write('\n'.join(todl))
    f.close()

SONGS = getsongtitle()
save_songs_to_file(SONGS) #
dlLink = []
for song in SONGS:
    downloadLink = fetch_youtube_url(song)
    dlLink.append(downloadLink)
downloadSongs(dlLink)

