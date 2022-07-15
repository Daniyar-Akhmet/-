import requests
from fake_useragent import UserAgent


def get_html(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    session = requests.Session()
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except (ConnectionError, TypeError):
        print("Error")
        return None
