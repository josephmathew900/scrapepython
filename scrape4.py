import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = 'http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html'
response = requests.get(url)
page = response.content

soup = BeautifulSoup(page,'html.parser')
#print soup
print soup.findAll('p',class_='outer-text')
print soup.findAll(id="first")
