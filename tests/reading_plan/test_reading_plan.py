from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch, Mock


noticia_pequena = {
    "url": "https://blog.betrybe.com/novidades/noticia-bacana",
    "title": "Notícia bacana",
    "timestamp": "04/04/2021",
    "writer": "Eu",
    "reading_time": 4,
    "summary": "Algo muito bacana aconteceu",
    "category": "Ferramentas",
}
noticia_grande = {
    "url": "https://blog.betrybe.com/novidades/noticia-grande",
    "title": "Notícia grande",
    "timestamp": "10/10/2020",
    "writer": "Tu",
    "reading_time": 20,
    "summary": "Algo muito grande aconteceu",
    "category": "Produtos",
}
noticia_minuscula = {
    "url": "https://blog.betrybe.com/novidades/noticia-minuscula",
    "title": "notícia minuscula",
    "timestamp": "01/01/2019",
    "writer": "Ele",
    "reading_time": 1,
    "summary": "Algo muito minusculo aconteceu",
    "category": "Dinheiro",
}


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
        ReadingPlanService.group_news_for_available_time(-1)

    mock_find_news = Mock(return_value=[
        noticia_pequena,
        noticia_grande,
        noticia_minuscula,
    ])

    with patch("tech_news.database.find_news", mock_find_news):
        result = ReadingPlanService.group_news_for_available_time(5)

    assert result == {"readable": [
        {
            "unfilled_time": 1,
            "chosen_news": [("Notícia bacana", 4)],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [("Notícia bacana", 4), ("notícia minuscula", 1)],
        },
    ], "unreadable": [("Notícia grande", 20)]}
