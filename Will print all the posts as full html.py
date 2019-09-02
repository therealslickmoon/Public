from bs4 import BeautifulSoup
import requests

url = 'https://news.ycombinator.com/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


post = content.findAll('tr', attrs={"class": 'athing'})


print (post)
