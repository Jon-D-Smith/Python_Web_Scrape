from bs4 import BeautifulSoup
import requests as r

doc = r.get('https://webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(doc.text, 'html.parser')

print(soup.title)