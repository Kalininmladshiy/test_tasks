import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def download_news(response):
    news = []
    soup = bs(response.text, "html.parser")
    news_titles = soup.find_all('div', itemprop="headline")
    for i in range(10):
        news.append(news_titles[i].string)
    return news


if __name__ == '__main__':
    url = "https://market.yandex.ru/partners/news"
    response = requests.get(url)
    response.raise_for_status()
    df = pd.DataFrame(data=download_news(response))
    df.to_csv('titles_market_news.csv')
