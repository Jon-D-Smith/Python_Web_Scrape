from bs4 import BeautifulSoup
import requests as r

doc = r.get('https://webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(doc.text, 'html.parser')

print(soup.title)
for image in soup.find_all('img'):
    print(image['src'])

for link in soup.find_all('a', href=True):
    print(link['href'])
