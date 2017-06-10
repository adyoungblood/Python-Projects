from htmlscrubber import Scrubber
from htmlfetchselenium import Fetcher
from pytube import YouTube, exceptions
import pytube
import os
import time

#nbm = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
        try:
            yt = YouTube(download)
        except ValueError:
            print(yt.filename + ' was not found.')
            continue
        if (yt.filename.startswith('Chro - SubReview')):
            print('Skipping a Chro Subreview')
            continue
        print("Downloading (" + str(output.index(video) + 1) + "/" + str(len(output)) + "): " + yt.filename + " (" + video + ")")
        try:
            vidfile = yt.get('mp4', '720p')
        except pytube.exceptions.DoesNotExist:
            vidfile = yt.get('mp4', '480p')
        except pytube.exceptions.DoesNotExist:
            vidfile = yt.get('mp4', '360p')
        except pytube.exceptions.DoesNotExist:
            vidfile = yt.get('mp4', '240p')
        except pytube.exceptions.DoesNotExist:
            vidfile = yt.get('mp4', '144p')
        vidfile.download(download_folder, force_overwrite=True)
        s.write(video + " ")
print('Done, writing to log.')
with open('log.txt', 'a', encoding='utf-8') as l:
    l.write('Save at ' + str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + '\n')

print('Written to log, quitting.')
