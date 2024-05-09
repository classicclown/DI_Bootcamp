import requests

x = requests.get('https://www.google.com').elapsed.total_seconds()
print(x)


