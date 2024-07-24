from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import ssl

url = 'https://www.bbc.com/news'
response = requests.get(url)
html_ocean_ws = response.text
soup_ocean_ws = BeautifulSoup(html_ocean_ws, 'html.parser')
# print(soup_ocean_ws.prettify())

title = soup_ocean_ws.find('title')
print (title.text)

for paragraphs in soup_ocean_ws.find_all('p'):
    print(paragraphs.get_text())

for links in soup_ocean_ws.find_all('a'):
    print (links.get('href'))


# Exercise 2

url2 = 'http://en.wikipedia.org/robots.txt'
response=requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
soup.prettify()
print(soup.get_text())


#Exercise 3

# url = 'https://en.wikipedia.org/wiki/Main_Page'
# html = requests.get(url).text
# soup = BeautifulSoup(html,'html.parser')

# headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# for heading in headings:
#     print (heading.get_text())


#Exercise 4

#Using code from ex. 3

# title = soup.find_all('title')
# if title:
#     print('title found')
# else:
#     print('No title found')

#Exercise 5

alert_url = 'https://www.cisa.gov/news-events/cybersecurity-advisories'
html = requests.get(alert_url).text
soup = BeautifulSoup(html,'html.parser')

alerts = soup.find_all('div',class_='c-teaser__meta',string='Alert')
time_elements = soup.find_all('time')
dates = [time_element['datetime'] for time_element in time_elements]

num_alerts=0



for alert,date in zip(alerts,dates):
    if alert.get_text().strip() == 'Alert' and date.startswith('2024'):
        num_alerts+=1



print(f'Number of alerts in 2024: {num_alerts}')


#Exercise 6

# alert_url = 'https://editorial.rottentomatoes.com/article/most-anticipated-movies-of-2024/'
# html = requests.get(alert_url).text
# soup = BeautifulSoup(html,'html.parser')

# movie_details = soup.find_all('p')

# for movie in movie_details:
#         if 'Directed by:' in movie.get_text():
#                 print (movie.get_text())
#                 blurb=movie.find_next_sibling('p')
#                 print(blurb.get_text())


