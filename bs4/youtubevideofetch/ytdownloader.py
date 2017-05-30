from htmlscrubber import Scrubber
from htmlfetch import Fetcher
from googlelogin import SessionGoogle

htmlfile = 'html.txt'
savedfile = 'saved.txt'
url = 'https://www.youtube.com'
output = []

fetcher = Fetcher(url)
scrubber = Scrubber(htmlfile, savedfile)

fetcher.updateFile(htmlfile)
output = scrubber.scrubFile(htmlfile, output)

url_login = "https://accounts.google.com/ServiceLogin"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
session = SessionGoogle(url_login, url_auth, "arghalexander3000@gmail.com", "D@vid875")
print (session.get(url))
