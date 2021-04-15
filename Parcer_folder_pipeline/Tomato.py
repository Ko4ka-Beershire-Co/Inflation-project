import requests
from bs4 import BeautifulSoup
import re


def parser():
  
    URL = 'https://lenta.com/product/tomaty-na-vetke-ves-1kg-015182/'
    HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params
    item_1 = 'span'
    item_2 = "sku-price__integer"
    # Request to send
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    # Parse html tree and return class containing the price
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find(item_1, class_=item_2)
        item = re.findall(r'(.*\d)', str(items), re.MULTILINE)
        item = re.sub(r'\s', '', str(item), 0, re.MULTILINE)
        return item[2:5]

    # If error check and get full html tree
    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            j = get_content(html.text)
        else:
            print('Чет не работает нихрена...')
            j = 'Error'
        return j

    return str(parse())


if __name__ == "__main__":
  
    parser()
