import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint


def get_html(url: str, headers):
    try:
        session = requests.Session()
        result = session.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Error")
        return None


ua = UserAgent()
headers = {"User-Agent": ua.random}

result = []

key_world = input("Введите вакансию: ")
page_num = input("Введите количество запрашиваемых страниц: ")
while not page_num.isdigit():
    page_num = input("Введите количество запрашиваемых страниц: ")
page_num = int(page_num)


for i in range(0, page_num):
    url = f'https://nur-sultan.hh.kz/search/vacancy?text={key_world}&salary=&clusters=true&area=159&ored_clusters=true&' \
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


pprint(result)
print(len(result))


