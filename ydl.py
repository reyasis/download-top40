from __future__ import unicode_literals
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def downloadSongs(songs): #change download directory

    ydl_opts = {
        'format': 'bestaudio/best',
        'download_archive': 'downloaded_songs.txt',
        'outtmpl': 'e:/python/downloadedsongs/%(title)s.%(ext)s', #file directory
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for song in songs:
            try:
                ydl.download([song])
                print 'downloading: {}'.format(song)
            except Exception:
                print 'Failed to download: {}'.format(song)
                continue