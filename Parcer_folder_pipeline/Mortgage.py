import requests
from bs4 import BeautifulSoup
import re


def parser():
    URL = 'https://www.sravni.ru/ipoteka/zhile-na-vtorichnom-rynke/'
    HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params
    item_1 = 'span'
    item_2 = 'style_rate__HbspZ'

    # Request to send
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    # Parse html tree and return class containing the price
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.findAll(item_1, class_=item_2)
        # items = str(items[1])
        # print(items)
        items = re.findall(r'(\d,\d\d)|(\d\d,\d\d)|\d,\d\d', str(items[0]))
        # print(items)
        if len(items[0][1]) >= 5:
            output = str(items[0][1][0:2]) + str(items[0][1][-2:])
            output = int(output)

            return output

        else:
            pass

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
