# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup as soup
# url = 'https://www.khmer24.com/km/property.html'
# req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

# webpage = urlopen(req).read()
# page_soup = soup(webpage, "html.parser")
# title = page_soup.find(class_="detail")
# print(title)
# containers = page_soup.find_all(class_="detail")
# print('in container : ', containers)
# for container in containers:
#     print(container)

import requests 
from bs4 import BeautifulSoup as soup
url = 'https://www.khmer24.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}

response = requests.get(url, headers=headers)
data = soup(response.content, 'html.parser')

containers = data.find_all(class_="detail")

for container in containers:
    print(container)