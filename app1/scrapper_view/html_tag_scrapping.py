from bs4 import BeautifulSoup
#import requests
from urllib.request import urlopen
def HtmlTagScrapper(url='http://prothom-alo.com', tag_name='a'):
    request_url = urlopen(url)
    soup = BeautifulSoup(request_url.text, 'html.parser')
    #print(soup.get_text())
    for tag in soup.find_all(tag_name):
         print(str(tag.get_text()))
         
