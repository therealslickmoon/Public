from bs4 import BeautifulSoup
import requests
import json

url = 'https://news.ycombinator.com/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser") .postArr
for post in content.findAll('tr',attrs={"class":"athing"}):
    postObject = {
        "title":post.find("a", attrs={"class":"storylink"}).text.encode('utf-8'),
        "url":post.find("a", attrs={"class":"storylink"}).href.encode('utf-8'),
        "author":post.find("a", attrs={"class":"hnuser"}).text.encode('utf-8'),                                                                
        "rank" :post.find("a", attrs={"class":"rank"}).text.encode('utf-8'),                                              
}
print (postObject)
