from htmlscrubber import Scrubber
from htmlfetchselenium import Fetcher
from pytube import YouTube, exceptions
import pytube
from selenium import webdriver

#nbm = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

htmlfile = 'html.txt'
savedfile = 'saved.txt'
url = 'https://www.youtube.com'
output = []
download_folder = '/Users/elizabethyoungblood/Desktop/ToWatch'

fetcher = Fetcher(htmlfile, url)
scrubber = Scrubber(htmlfile, output)

fetcher.updateFile()
output = scrubber.scrubFile()

with open(savedfile, 'r', encoding='utf-8') as v:
    s = set(v.read().split())
    output = [x for x in output if x not in s]
    print(output)
  

with open(savedfile, 'a', encoding='utf-8') as s:
    for video in output:
        download = 'https://www.youtube.com' + video
        yt = YouTube(download)
        print("Downloading (" + str(output.index(video) + 1) + "/" + str(len(output)) + "): " + yt.filename + " (" + video + ")")
        try:
            vidfile = yt.get('mp4', '720p')
        except pytube.exceptions.DoesNotExist:
            vidfile = yt.get('mp4', '480p')
        vidfile.download(download_folder, force_overwrite=True)
        s.write(video + " ")
print('Done!')
