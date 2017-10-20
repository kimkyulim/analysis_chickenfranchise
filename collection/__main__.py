import crawler
from bs4 import BeautifulSoup
import pandas as pd
from data_dict import sido_dict, gungu_dict

RESULT_DIRECTORY = '../__result__/crawling'


def proc_bbq(html):
    bs = BeautifulSoup(html, 'html.parser')
    tag_tbody = bs.find('tbody')

    result = []
    for tag_tr in tag_tbody.findAll('tr'):
        strings = list(tag_tr.strings)

        name = strings[1]
        address = strings[3]
        sidogu = address.split()[:2]

        result.append((name, address) + tuple(sidogu))

    return result


def store_bbq(data):
    table = pd.DataFrame(data, columns=['name', 'address', 'sido', 'gungu'])

    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))

    table.to_csv('{0}/bbq_table.csv'.format(RESULT_DIRECTORY), encoding='cp949', mode='w', index=True)


def crawling_pelicana():
    pass



if __name__ == '__main__':

    # collection
    crawler.crawling(
        url='https://www.bbq.co.kr/shop/shop_ajax.asp?page=1&pagesize=2000&gu=&si=',
        proc=proc_bbq,
        store=store_bbq)