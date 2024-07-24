import requests
from bs4 import BeautifulSoup
import pandas as pd

# boa sorte! <3

#beautifulsoup = parse com as infos do html
#find procurar as infos que a gente quer. Entender o q eu quero e como eu vou pegar isso


def get_book_titles(doc):
    Book_title_tags = doc.find_all('h3')
    Book_titles = []
    for tags in Book_title_tags:
        Book_titles.append(tags.text)
    return Book_titles

def get_book_price(doc):
    Book_price_tags = doc.find_all('p', class_= 'price_color')
    Book_price = []
    for tags in Book_price_tags:
        Book_price.append(tags.text.replace('Â', ''))
    return Book_price

def get_stock(doc):
    Book_stock_tag = doc.find_all('p', class_ = 'instock availability')
    Book_stock = []
    for stocks in Book_stock_tag:
        Book_stock.append(stocks.text.strip())
    return Book_stock

def get_book_url(doc):
    Book_url = []
    for article in doc.find_all('h3'):
        for link in article.find_all('a', href=True):
            url = link['href']
            links = 'http://books.toscrape.com/catalogue/' + url
            if links not in Book_url:
                Book_url.append(links)
    return Book_url

def get_doc(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(response))
    return BeautifulSoup(response.text, 'html.parser')

def scrape_multiple_pages(n):
    URL = 'https://books.toscrape.com/catalogue/page-'
    titles, prices, stock_availability, urls = [], [], [], []

    for page in range(1,n+1):
        doc = get_doc(URL + str(page)+ '.html')
        titles.extend(get_book_titles(doc))
        prices.extend(get_book_price(doc))
        stock_availability.extend(get_stock(doc))
        urls.extend(get_book_url(doc))

    book_dict1 = {
        'TITLE': titles,
        'PRICE': prices,
        'STOCK_AVAILABILITY': stock_availability,
        'URL': urls
    }
    return pd.DataFrame(book_dict1)


URL = "http://books.toscrape.com/"
response = requests.get(URL)
page_contents = response.text

#criar um file
with open('Scrappingrf.html', 'w') as f:
    f.write(page_contents)

doc = BeautifulSoup(page_contents, "html.parser")


if __name__ == "__main__":
    df = scrape_multiple_pages(5)
    df.to_csv('SCB.csv', index=None)
    print("Feito caralho")