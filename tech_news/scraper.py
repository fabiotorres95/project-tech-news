from parsel import Selector
import requests
import time
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
        )

        if response.status_code != 200:
            return None
        return response.text

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content) or None
    if selector is None:
        return []
    links = selector.css('#content article a::attr(href)').getall()
    if links == []:
        return links
    for link in links:
        index = links.index(link)
        if 'author' in link:
            links.pop(index)
    links = list(dict.fromkeys(links))

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content) or None
    if selector is None:
        return []

    link = selector.css('a.next.page-numbers::attr(href)').get()
    return link


# Requisito 4
def scrape_news(html_content):
    data = {}

    selector = Selector(text=html_content)

    data['url'] = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('h1.entry-title::text').get()
    title = title.strip()
    data['title'] = title
    data['timestamp'] = selector.css('li.meta-date::text').get()
    data['writer'] = selector.css('a.url.fn.n::text').get()
    reading_time = selector.css('li.meta-reading-time::text').get()
    reading_time = int(reading_time.split(' ')[0])
    data['reading_time'] = reading_time
    summary_data = selector.css('div.entry-content p').get()
    summary = BeautifulSoup(summary_data, 'html.parser')
    data['summary'] = summary.get_text().strip()
    data['category'] = selector.css('span.label::text').get()

    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
