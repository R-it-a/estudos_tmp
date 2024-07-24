import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_book_titles(doc):
    book_title_tags = doc.find_all('h3')
    book_titles = [tag.find('a')['title'] for tag in book_title_tags]
    return book_titles

def get_book_price(doc):
    book_price_tags = doc.find_all('p', class_='price_color')
    book_prices = [tag.text.replace('Â', '') for tag in book_price_tags]
    return book_prices

def get_stock(doc):
    book_stock_tags = doc.find_all('p', class_='instock availability')
    book_stock = [tag.text.strip() for tag in book_stock_tags]
    return book_stock

def get_book_urls(doc):
    book_title_tags = doc.find_all('h3')
    book_urls = ['http://books.toscrape.com/catalogue/' + tag.find('a')['href'] for tag in book_title_tags]
    return book_urls

def get_doc(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(url))
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc

def scrape_multiple_pages(n):
    base_url = 'http://books.toscrape.com/catalogue/page-'
    titles, prices, stock_availability, urls = [], [], [], []

    for page in range(1, n + 1):
        url = base_url + str(page) + '.html'
        doc = get_doc(url)
        titles.extend(get_book_titles(doc))
        prices.extend(get_book_price(doc))
        stock_availability.extend(get_stock(doc))
        urls.extend(get_book_urls(doc))

    book_dict = {
        'Title': titles,
        'Price': prices,
        'Stock Availability': stock_availability,
        'URL': urls
    }
    return pd.DataFrame(book_dict)

if __name__ == "__main__":
    df = scrape_multiple_pages(5)
    df.to_csv('SCB.csv', index=None)
    print("Scraping completed and data saved to SCB.csv")
