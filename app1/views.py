from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.scrapper_view import html_tag_scrapping

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def Index(request):
    return render(request, 'index.html')



def get_news():
    news_link = "https://news.google.com/news/rss"
    page = urlopen(news_link)
    xml_page = page.read()
    page.close()
    soup_page = soup(xml_page,"xml")
    news_list = soup_page.findAll("item")
    return news_list



def HtmlTagScrap(request):
    # html_tag = html_tag_scrapping.HtmlTagScrapper('http://trickbd.com', 'a')
    # print(html_tag)
    
    news_title = []
    for item in get_news():
        news_title.append(item.title.get_text())
    context = {
        #'html_tag': html_tag,
        "news_list": news_title
    }
    #print(get_news())
    return render(request, 'html_tag_scrapping.html', context=context)