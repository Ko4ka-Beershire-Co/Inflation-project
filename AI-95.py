import requests
from bs4 import BeautifulSoup

URL = 'https://fuelprices.ru'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'https://fuelprices.ru'


def get_html(url, params=None, HEADERS):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='fuel-card border-ai95')
    price = items[0].find('span', itemprop='price').text
    print(price)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = get_content(html.text)
    else:
        print('Error')

parse()
