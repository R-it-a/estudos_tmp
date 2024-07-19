import requests
import json
import jsbeautifier
from urllib.request import urlopen
import pandas as pd

from bs4 import BeautifulSoup

if __name__ == "__main__":
    # boa sorte! <3

    #beautifulsoup = parse com as infos do html
    #find procurar as infos que a gente quer. Entender o q eu quero e como eu vou pegar isso

    # Definir o link (linh_html = "link")
    URL = "http://books.toscrape.com/"
    html = urlopen(URL).read()

    # get (conseguir os dados do html)
    #response = requests.get(URL)


    #html_text = response.text
    #print(html_text)
    #print(type(html_text))
    soup = BeautifulSoup(html, "html.parser")
        #print(soup)
        #print(type(soup))
        #json_response =json.dumps(html_text)
        #print(json_response)

    # break into lines and remove leading and trailing space on each
   # if html.status_code != 200:
    #    print("Error")
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)


    # Select all list item tags
    list_items = soup.select('li')

    print("List items: ")
    for item in list_items:
        print(item)

