from htmlscrubber import Scrubber
from htmlfetch import Fetcher
from pytube import YouTube
import os
import sys
nbm = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

htmlfile = 'html.txt'
savedfile = 'saved.txt'
url = 'https://www.youtube.com'
output = []
download_folder = '/Users/elizabethyoungblood/Desktop/ToWatch'

fetcher = Fetcher(url)
scrubber = Scrubber(htmlfile)

fetcher.updateFile(htmlfile)
output = scrubber.scrubFile(htmlfile, output)

with open(savedfile, 'r', encoding='utf-8') as v:
    s = set(v.read().split())
    output = [x for x in output if x not in s]
    print(output)
  

with open(savedfile, 'a', encoding='utf-8') as s:
    for link in output:
        s.write(link + " ")

"""
for video in td:
    download = 'https://www.youtube.com' + video
    yt = YouTube(download)
    video = yt.get('mp4', '720p')
    video.download(download_folder)
"""
