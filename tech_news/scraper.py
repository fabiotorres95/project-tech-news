from parsel import Selector
import requests
import time


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
    links = selector.css('article a::attr(href)').getall()
    if links == []:
        return links
    for link in links:
        index = links.index(link)
        if 'author' in link:
            links.pop(index)
    links = list(dict.fromkeys(links))
    links.pop(0)

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
