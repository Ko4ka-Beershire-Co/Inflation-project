import requests
from datetime import datetime
import re
from bs4 import BeautifulSoup


def parser():
    URL = 'http://www.mosvodokanal.ru/forpeople/tariffs/'
    HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params
    item_1 = 'table'
    item_2 = 'data'

    # Request to send
    def get_html(url, params=None):
        r = requests.get(url, verify=False, headers=HEADERS, params=params)
        return r

    # Parse html tree and return class containing the price
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find(item_1, class_=item_2)
        table_body = items.find('tbody')
        i = re.findall(r'<p align="center">(.*\d)</p>', str(table_body), re.MULTILINE)

        if datetime.now() <= datetime(2021, 6, 6):
            return i[0]
        else:
            return i[2]

    # If error check and get full html tree
    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            j = get_content(html.text)
        else:
            print('Чет не работает нихрена...')
            j = 'Error'
        item = re.sub(r',', '.', str(j), 0, re.MULTILINE)
        return item

    return str(parse())


if __name__ == "__main__":
    parser()
