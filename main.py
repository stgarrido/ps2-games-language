from bs4 import BeautifulSoup
import requests

websitePs1 = 'https://psxdatacenter.com/ntsc-u_list.html'
websitePs2 = 'https://psxdatacenter.com/psx2/ulist2.html'

data = requests.get(websitePs2).text
soup = BeautifulSoup(data, 'html.parser')

tables = soup.find('table', attrs={'class':'sectiontable'})

print(tables)