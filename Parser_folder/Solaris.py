import requests
from bs4 import BeautifulSoup
import re

URL = 'https://auto.ru/moskva/cars/hyundai/solaris/new/?do_not_redirect=true'
HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params
item_1 = 'div'
item_2 = 'ListingItemGroup__price'


def parser(URL, HEADERS, item_1, item_2):
    # Request to send
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    # Parse html tree and return class containing the price
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all(item_1, class_=item_2)
        item = re.findall(r'(\d\d\d)...(\d\d\d)(.*?)(\d)...(\d\d\d)...(\d\d\d)', str(items), re.MULTILINE)
        for m in item:
            # count average
            i = str(m[0])+str(m[1])
            j = str(m[3])+str(m[4])+str(m[5])
            result = (int(i)+int(j))/2
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

    parser(URL, HEADERS, item_1, item_2)
