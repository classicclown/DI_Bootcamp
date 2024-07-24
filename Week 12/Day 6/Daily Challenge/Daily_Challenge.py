from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd

url = 'https://github.com/topics'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

if response.status_code==200:

    first_100= (soup.get_text())
    first_100=first_100.strip()
    print(first_100[0:100])

    with open ('Week 12/Day 6/Daily Challenge/webpage.html','w', encoding='utf-8') as file:
        file.write(html)
        print('Content saved')


titles = soup.find_all('p', class_="f3 lh-condensed mb-0 mt-1 Link--primary")
description = soup.find_all('p',class_="f5 color-fg-muted mb-0 mt-1")

index=1
description_dict = {'Title':[],'Description':[]}
for title,description in zip(titles,description):
    print (f'{index}.{title.get_text()}')
    print(description.get_text().strip())
    print("")
    index+=1
    description_dict['Title'].append(title.get_text())
    description_dict['Description'].append(description.get_text().strip())

df= pd.DataFrame(description_dict)

print(df.head())