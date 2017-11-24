import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

data=[]
url = ['https://www.bloomberg.com/quote/SPX:IND','https://www.bloomberg.com/quote/CCMP:IND']
for pg in url:
    response = requests.get(pg)
    page = response.content

    soup = BeautifulSoup(page,'html.parser')
    name_box = soup.find('h1',attrs={'class':'name'})
    name = name_box.text.strip()
    price_box = soup.find('div',attrs = {'class':'price'})
    price = price_box.text.strip()
    data.append((name,price))
#print data

with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    for name,price in data:
        writer.writerow([name,price,datetime.now()])
