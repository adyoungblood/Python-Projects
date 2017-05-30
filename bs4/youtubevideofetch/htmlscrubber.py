from bs4 import BeautifulSoup

search_term = "/watch?v="

class Scrubber():
    """A class used to get the current Youtube HTML, then strip it for links"""

    def __init__(self, htmlfile, savedfile):
        self.htmlfile = htmlfile
        self.savedfile = savedfile

    def scrubFile(self, file, output):
        f = open(file, 'r', encoding='utf-8')
        htmldoc = f.read()

        soup = BeautifulSoup(htmldoc, 'html.parser')
        f.close()

        links = []

        for link in soup.find_all('a'):
            if link.get('href') != None:
                if search_term in link.get('href'):
                    links.append(link.get('href'))
        return(links)

