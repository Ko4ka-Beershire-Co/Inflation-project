import requests
import re
from bs4 import BeautifulSoup


def parser():
    URL = 'https://energovopros.ru/spravochnik/elektrosnabzhenie/tarify-na-elektroenergiju/moskva/29449/'
    HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params
    item_1 = 'div'
    item_2 = 'articles-list items_scope'

    # Request to send
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    # Parse html tree and return class containing the price
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find(item_1, class_=item_2)
        canvas = re.findall(r'<p>Одноставочный тариф на электроэнергию</p>\n<ul>\n<li><strong>(.*?) руб</strong>'
                            r' за 1 кВт.ч</li>\n</ul>', str(items), re.MULTILINE)
        return canvas[0]  # Цена по однозонному тарифу

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
