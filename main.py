from lxml import html
from get_html import get_html
from datetime import date
from pprint import pprint


url = "https://lenta.ru/"
dom = html.fromstring(get_html(url))

all_news = []

top_news = dom.xpath("//a[contains(@class, 'card-big')]")
name_top_news = top_news[0].xpath(".//h3[@class='card-big__title']//text()")[0]
link_top_news = 'https://lenta.ru' + top_news[0].xpath("@href")[0]
published_top_news = str(date.today()) + ' ' + top_news[0].xpath(".//time[@class='card-big__date']//text()")[0]
news = {}
news['name'] = name_top_news
news['link'] = link_top_news
news['published'] = published_top_news
all_news.append(news)

items = dom.xpath("//a[contains(@class, 'card-mini _topnews')]")
for item in items:
    news = {}
    name = item.xpath(".//span[@class='card-mini__title']//text()")[0]
    link = 'https://lenta.ru' + item.xpath("@href")[0]
    published = str(date.today()) + ' ' + item.xpath(".//time[@class='card-mini__date']//text()")[0]
    news['name'] = name
    news['link'] = link
    news['published'] = published
    all_news.append(news)

pprint(all_news)

