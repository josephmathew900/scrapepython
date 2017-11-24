import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WhfizUqWbIU'
response = requests.get(url)
page = response.content
pd.set_option('display.expand_frame_repr', False)

soup = BeautifulSoup(page,'html.parser')
#html = soup.prettify().encode('utf-8')
#filef = open("weatherhtml","w")
#filef.write(html)
#filef.close()

#seven_day = soup.find(id="seven-day-forecast")
A=[]
B=[]
C=[]
D=[]
forecast_items = soup.findAll(class_="tombstone-container")
for each in forecast_items:
    A.append(each.find(class_="period-name").get_text())
    B.append(each.find(class_="short-desc").get_text())
    C.append(each.find(class_="temp").get_text())
    D.append(each.find("img").get("title"))
weather = pd.DataFrame({"period":A,"short_desc":B,"temp":C,"desc":D})
print weather
