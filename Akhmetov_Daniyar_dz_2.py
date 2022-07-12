from bs4 import BeautifulSoup
from sys import argv
from get_html import get_html
from hh_db import insert_data
from pprint import pprint


result = []

# key_word = input("Введите вакансию: ")
# page_num = input("Введите количество запрашиваемых страниц: ")
# while not page_num.isdigit():
#     page_num = input("Введите количество запрашиваемых страниц: ")
# page_num = int(page_num)

key_word = argv[1]
page_num = int(argv[2])

for i in range(0, page_num):
    url = f'https://nur-sultan.hh.kz/search/vacancy?text={key_word}&salary=&clusters=true&area=159&ored_clusters=true&' \
          f'enable_snippets=true&only_with_salary=true&page={i}'
    html = get_html(url, headers)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_vacancy = soup.find_all('div', class_='vacancy-serp-item-body__main-info')
        for item in all_vacancy:
            vacancy = {}
            vacancy['position'] = item.find('a').text
            # здесь не разобрался как брать ссылку, атрибут href возвращает None, поэтому пришлось работать со строкой
            vacancy['url'] = str(item.find('a')).split(' ')[3].split('=', 1)[-1].strip('\"')
            income = item.findAllNext('span', {'class': 'bloko-header-section-3'})[0].text.\
                replace('\u202f', '').strip(' ')
            try:
                if 'от' in income:
                    max_ = None
                    min_ = int(income.split(' ')[1])
                    currency = income.split(' ')[2]
                elif 'до' in income:
                    max_ = int(income.split(' ')[1])
                    min_ = None
                    currency = income.split(' ')[2]
                else:
                    min_ = int(income.split(' ')[0])
                    max_ = int(income.split(' ')[2])
                    currency = income.split(' ')[-1]
            except (ValueError, IndexError) as t:
                print(t)
            vacancy['min'] = min_
            vacancy['max'] = max_
            vacancy['currency'] = currency
            vacancy['main_url'] = url
            result.append(vacancy)

insert_data(result)
