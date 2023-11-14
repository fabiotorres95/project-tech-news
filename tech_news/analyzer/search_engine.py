from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    if not isinstance(title, str):
        return []
    title = title.lower()
    query = {"title": {"$regex": title}}
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
    """Seu código deve vir aqui"""
    raise NotImplementedError
