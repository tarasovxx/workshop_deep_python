'''

Асинхронный веб-скрапинг и анализ новостей

Цель этой задачи - создать асинхронное приложение, которое собирает новостные заголовки
с разных новостных сайтов и выполняет их анализ на предмет тональности (позитивная, нейтральная, негативная).
Для этого можно использовать библиотеки, такие как aiohttp для выполнения HTTP-запросов асинхронно и nltk для анализа тональности текста.

'''



import aiohttp
import asyncio
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Инициализация анализатора тональности nltk
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Список новостных сайтов
news_sites = [
    "https://www.bbc.com",
    "https://www.nytimes.com"
]

async def fetch_headlines(session, url):
    async with session.get(url) as response:
        return await response.text()

def extract_headlines(html):
    soup = BeautifulSoup(html, 'html.parser')
    headlines = [headline.text for headline in soup.find_all('h2')]
    return headlines

def analyze_sentiment(headline):
    sentiment = sia.polarity_scores(headline)
    if sentiment['compound'] >= 0.05:
        return 'Позитивная'
    elif sentiment['compound'] <= -0.05:
        return 'Негативная'
    else:
        return 'Нейтральная'

async def analyze_headlines(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_headlines(session, url)
        headlines = extract_headlines(html)
        return headlines

async def main():
    tasks = []
    for site in news_sites:
        headlines = await analyze_headlines(site)
        for headline in headlines:
            sentiment = analyze_sentiment(headline)
            print(f"Заголовок: {headline}, Тональность: {sentiment}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
