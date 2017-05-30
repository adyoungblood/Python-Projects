from bs4 import BeautifulSoup


html = open('html.txt', 'r', encoding='utf-8')

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
