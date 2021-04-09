import requests
from bs4 import BeautifulSoup

URL = 'http://tsenomer.ru/produkti/moloko/'
HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params
item_1 = 'td'
item_2 = 'korzina_shop_price'


def parser(URL, HEADERS, item_1, item_2):
    # Request to send
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    # Parse html tree and return class containing the price
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find(item_1, class_=item_2)
        # trim the class and print the price
        print(items.text)
        # moloko = str(items)
        # price = moloko[38:43]
        # print(price)

    # If error check and get full html tree
    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Чет не работает нихрена...')

    parse()


parser(URL, HEADERS, item_1, item_2)