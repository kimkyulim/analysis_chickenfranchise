import crawler
from bs4 import BeautifulSoup


def proc_bbq(html):
    bs = BeautifulSoup(html, 'html.parser')
    tag_tbody = bs.find('tbody')
    for tag_tr in tag_tbody.findAll('tr'):
        print(tag_tr.name)


def store_bbq(data):
    pass


if __name__ == '__main__':

    # collection
    """
    crawler.crawling(
        url='https://www.bbq.co.kr/shop/shop_ajax.asp?page=1&pagesize=2000&gu=&si=',
        proc=proc_bbq,
        store=store_bbq)
    """

    html = crawler.crawling(
        url='https://www.bbq.co.kr/shop/shop_ajax.asp?page=1&pagesize=2000&gu=&si=')
    print(html)