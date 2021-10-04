import youtube_dl as ydl

link = 'https://youtu.be/sCbbMZ-q4-I'

with ydl.YoutubeDL() as yd:
    yd.download()
