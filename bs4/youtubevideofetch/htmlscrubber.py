from bs4 import BeautifulSoup

search_term = "/watch?v="

class Scrubber():
    """A class used to get the current Youtube HTML from the file,
        then strip it for links"""

    def __init__(self, htmlfile, savedfile):
        self.htmlfile = htmlfile
        self.savedfile = savedfile

    def scrubFile(self, htmlfile, savedfile, output):
        f = open(htmlfile, 'r', encoding='utf-8')
        htmldoc = f.read()

        soup = BeautifulSoup(htmldoc, 'html.parser')
        f.close()

        #print(soup.prettify(encoding='utf-8'))

        links = []

        for link in soup.find_all('a'):
            if link.get('href') != None:
                if search_term in link.get('href'):
                    links.append(link.get('href'))
                    print(link.get('href'))

        del links[1::2]
                    
        return(links)
