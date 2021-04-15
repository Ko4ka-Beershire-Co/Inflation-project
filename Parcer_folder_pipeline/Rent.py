import requests
import re
from bs4 import BeautifulSoup


def parser():
  
    URL = 'https://moskva.naydidom.com/tseny/adtype-arenda'
    HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params
    item_1 = 'table'
    item_2 = 'table table-striped table-bordered table-condensed'
    # Request to send
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    # Parse html tree and return class containing the price
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find(item_1, class_=item_2)
        table_body = items.find('tbody')
        prices = re.findall("<td>(\d*?)</td>", str(table_body), re.MULTILINE)
        return prices[2]  # кв метр в 2-к

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
