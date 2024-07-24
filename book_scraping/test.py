import requests
from bs4 import BeautifulSoup
import pandas as pd
URL = "http://books.toscrape.com/"
response = requests.get(URL)
page_contents = response.text

#criar um file
with open('Scrappingrf.html', 'w') as f:
    f.write(page_contents)

doc = BeautifulSoup(page_contents, "html.parser")

