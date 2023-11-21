from bs4 import BeautifulSoup
import requests

websitePs1 = 'https://psxdatacenter.com/ulist.html'
websitePs2 = 'https://psxdatacenter.com/psx2/ulist2.html'

data = requests.get(websitePs1).text
soup = BeautifulSoup(data, 'html.parser')

tables = soup.find_all('table', attrs={'class':'sectiontable'})

cont = 0

for table in tables:
  rowsByTable = table.find_all('tr')
  for row in rowsByTable:
    gameName = row.find('td', attrs={'class':'col3'})
    gameLanguage = row.find('td', attrs={'class':'col4'})
    if gameName and len(gameLanguage.text) != 1:
      if(gameLanguage.text[-3:] == '[S]'):
        print(gameName.text, gameLanguage.text)