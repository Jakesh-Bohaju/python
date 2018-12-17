import requests as req
from bs4 import BeautifulSoup

homepage_request = req.get('https://www.onlinekhabar.com')
homepage_parsed = BeautifulSoup(homepage_request.content, "html.parser")
# print(homepage_request.text)

a_tags = homepage_parsed.find_all('a')
links = set()
# a_tags is list of dictionary form
for a_tag in a_tags:
    # print(a_tag.get('href'))
    # link = a_tag.get('href', '')
    if '/2018/' in a_tag.get('href', ''):
        links.add(a_tag.get('href'))
        # links.add(link)

for link in links:
    single_news_request = req.get(link)
    # print(single_news_request.text)
    single_news_parsed = BeautifulSoup(single_news_request.content, "html.parser")
    print(single_news_parsed.find('title').text)
    print(single_news_parsed.select_one('.ok18-single-post-content-wrap').text)
