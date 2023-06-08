from pprint import pprint
from requests import get

response = get('https://newsapi.org/v2/everything?q=apple&from=2023-06-06&to=2023-06-06&sortBy=popularity&apiKey=ca18aebd834a4afbb53385bb02b899bd')
tesla_data = response.json()


author = tesla_data.get('articles')[1].get('author')
title = tesla_data.get('articles')[1].get('title')
published_at = tesla_data.get('articles')[1].get('publishedAt')

print(f'Author: {author}')
print(f'TiTle: {title}')
print(f'Published Date: {published_at}')
author_name = input('Author name: ')
for article in tesla_data.get('articles'):
   if article.get('author') == author_name:
           pprint(article)
