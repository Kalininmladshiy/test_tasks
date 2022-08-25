import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def download_news():
    news = []
    with open('OZON_Seller_news.html') as fp:
        soup = bs(fp)
    news_titles = soup.find_all('h3', class_='news-card__title')
    for i in range(5):
        news.append(news_titles[i].string)
    return news


if __name__ == '__main__':
    url = "https://seller.ozon.ru/news/"
    df = pd.DataFrame(data=download_news())
    df.to_csv('titles_ozon_news.csv')
