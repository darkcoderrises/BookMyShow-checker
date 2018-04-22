from bs4 import BeautifulSoup

f = open('./website.html').read()
soup = BeautifulSoup(f, 'html.parser')
theaters = list(map(lambda i: i.text.replace('\n', ''), soup.findAll('a', attrs={'class': '__venue-name'})))
theaters.sort()

for i in theaters:
    print i

