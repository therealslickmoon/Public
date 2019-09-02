from bs4 import BeautifulSoup
import requests
import json
import urllib3 
url = 'https://news.ycombinator.com/'
                                           
def make_soup(url):
    http = urllib3.PoolManager()
    r - http.request("get",url)
    return BeautifulSoup(r.data,'lxml')

rec= {
    tr:{":class":"athing"}
"title":result["class":"storylink"]
        "url":result.a.[href]
        "author":result["class":"hnuser"]                                                               
        "rank" :result["class":"rank"
