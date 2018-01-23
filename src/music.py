import youtube_dl
from bs4 import BeautifulSoup
try:
    from scripts.actions import notify
except:
    pass
import os
from urllib.request import urlopen

def execute(link):
    text=link.replace(" ","+")
    print(text)
    url = 'https://www.youtube.com/results?search_query='+text
    fhand=urlopen(url).read()
    soup = BeautifulSoup(fhand, "html.parser")
    songs = soup.findAll('div', {'class': 'yt-lockup-video'})
    hit = songs[0].find('a')['href']
    notify("Downloading "+link)
    ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '192',
                                        }],
                                        'quiet': True,
                                        'restrictfilenames': True,
                                        'outtmpl': os.environ['HOME']+'/Music/new/%(title)s.%(ext)s'
                                        }

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download(['https://www.youtube.com'+hit])
    notify("Song Download Complete")
    print("Song download complete")
