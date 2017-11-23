import requests
import pandas as pd
from BeautifulSoup import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
#print soup.title.string
#all_links = soup.findAll("a")
#for link in all_links:
#    print link.get("href")

all_tables = soup.findAll("table")
right_table = soup.find('table', {"class": 'wikitable sortable plainrowheaders'})
#print right_table
A = []
B = []
C = []
D = []
E = []
F = []
G = []
for row in right_table.findAll("tr"):
    cells = row.findAll("td")
    states = row.findAll("th")
    if len(cells) == 6:
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

#for temp in B:
#    print temp
#df=pd.DataFrame(A,columns=['Number'])
#df['State/UT']=B
#df['Admin_Capital']=C
#df['Legislative_Capital']=D
#df['Judiciary_Capital']=E
#df['Year_Capital']=F
#df['Former_Capital']=G
#print df
	

 


