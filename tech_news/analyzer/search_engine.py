from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    if not isinstance(title, str):
        return []
    query = {"title": {"$regex": title, "$options": "i"}}
    data = search_news(query)
    result = []
    for news in data:
        result.append((news["title"], news["url"]))

    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    if not isinstance(category, str):
        return []
    query = {"category": {"$regex": category, "$options": "i", }}
    data = search_news(query)
    result = []
    for news in data:
        result.append((news["title"], news["url"]))

    return result
