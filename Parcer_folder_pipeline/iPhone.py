import requests
from bs4 import BeautifulSoup
import re


def parser():
  
    URL = 'https://www.e-katalog.ru/ek-list.php?katalog_=122&brand_=apple&brands_=116&order_=price_desc'
    HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params
    item_1 = 'div'
    item_2 = 'model-price-range'
    # Request to send
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    # Parse html tree and return class containing the price
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find(item_1, class_=item_2)
        item = re.findall(r'(\d*?.\d*?)</span>', str(items), re.MULTILINE)

        # Some funny stuff for shitty whitespaces
        item_list = []
        for i in item:
            j = str(i)[:2]+str(i)[-3:]
            item_list.append(j)

        # count average
        result = (int(item_list[0]) + int(item_list[1]))/2
        return result

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
