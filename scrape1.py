import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = 'https://www.bloomberg.com/quote/SPX:IND'
response = requests.get(url)
page = response.content

soup = BeautifulSoup(page,'html.parser')
name_box = soup.find('h1',attrs={'class':'name'})
name = name_box.text.strip()
price_box = soup.find('div',attrs = {'class':'price'})
price = price_box.text.strip()

with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name,price,datetime.now()])
