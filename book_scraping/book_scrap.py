import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def get_book_details(book_url):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.find('h1')
    title = title_tag.text if title_tag else "N/A"

    price_tag = soup.find('p', class_='price_color')
    price = price_tag.text.replace('Â', '') if price_tag else N/A

    availability_tag = soup.find('p', class_='instock availability')
    if availability_tag:
        availability = availability_tag.text.strip()
        in_stock = availability.split('(')[-1].split(' ')[0] if '(' in availability else 'N/A'
    else:
        availability = "N/A"
        in_stock = "N/A"

    star_rating_tag = soup.find('p', class_='star-rating')
    star_rating = star_rating_tag['class'][1] if star_rating_tag and "class" in star_rating_tag.attrs else "N/A"

    breadcrumb_tag = soup.find('ul', class_='breadcrumb')
    if breadcrumb_tag:
        category_tags = breadcrumb_tag.find_all('li')
        category = category_tags[2].text.strip() if len(category_tags) > 2 else "N/A"

    else:
        category = "N/A"

    return {
        'Title': title,
        'Price': price,
        'In Stock': in_stock
        'Star Rating': star_rating,
        'Category': category,
        'URL': book_url
    }

def get_book_urls(doc):
    book_urls = []
    for article in doc.find_all('article', class_='product_pod'):
        relative_book_url = article.find('a')['href']
        book_url = urljoin("http://books.toscrape.com/catalogue/", relative_book_url)
        book_url.append(book_urls)
    return book_url

def get_doc(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'failed to load page {url}')
    return BeautifulSoup(response.text, 'html.parser')

def scrape_multiple_pages(n):
    base_url = 'http://books.toscrape.com/catalogue/page-'
    all_books = []

    for page in range(1, n + 1):
        page_url = base_url + str(page) + '.html'
        doc = get_doc(page_url)
        book_urls = get_book_urls(doc)

        for book_url in book_urls:
            book_details = get_book_details(book_url)
            all_books.append(book_details)
    return pd.DataFrame(all_books)

if __name__ == "__main__":
    df = scrape_multiple_pages(50)
    df.to_csv('books.csv', index=False)
    print("Scraping complete. Data saved caralho")

