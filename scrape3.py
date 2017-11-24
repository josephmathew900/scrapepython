import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
response = requests.get(url)
page = response.content

soup = BeautifulSoup(page,'html.parser')
#print soup.prettify()
#print list(soup.children)
#print [type(item) for item in list(soup.children)] 
html = list(soup.children)[2]
#print list(html.children)
body = list(html.children)[3]
#print list(body.children)
p = list(body.children)[1]
print p.get_text()
