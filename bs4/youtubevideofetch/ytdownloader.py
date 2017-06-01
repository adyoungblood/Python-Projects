from htmlscrubber import Scrubber
from htmlfetch import Fetcher
from pytube import YouTube
import os

htmlfile = 'html.txt'
savedfile = 'saved.txt'
url = 'https://www.youtube.com'
output = []
download_folder = '/Users/elizabethyoungblood/Desktop/ToWatch'

fetcher = Fetcher(url)
scrubber = Scrubber(htmlfile, savedfile)

fetcher.updateFile(htmlfile)
output = scrubber.scrubFile(htmlfile, savedfile, output)

with open(savedfile, 'a', encoding='utf-8') as s:
    for link in output:
        s.write(link + " ")

with open(htmlfile, 'r', encoding='utf-8') as v:
    td = v.read()
    td = td.split()
    print(td)
    
with open(savedfile, 'r', encoding='utf-8') as v:
    td = (td - v.read())
  

"""
for video in td:
    download = 'https://www.youtube.com' + video
    yt = YouTube(download)
    video = yt.get('mp4', '720p')
    video.download(download_folder)
"""
