# Download-top40
Download song from UK top 40
# Motivation
I want an easy way to download UK top 40 songs using what i learn from python. 
# How to run. 
1. Clone this repo
2. Install requirements. 'pip install -r requirements.txt '
3. Get your youtube dev key. [Here's how](http://stackoverflow.com/questions/8832087/where-can-i-get-google-developer-key).
  - insert in ytsearch.py YOUTUBE_DEV_KEY
4. Run the script using 'python billboard-dl.py'
  - names of downloaded songs will be save in songs.txt
  - you can change the directory in ydl.py 'outtmpl': 'e:/python/downloadedsongs/%(title)s.%(ext)s', #file directory
