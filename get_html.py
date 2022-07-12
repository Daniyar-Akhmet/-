import requests
from fake_useragent import UserAgent


def get_html(url: str, headers):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    try:
        session = requests.Session()
        result = session.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Error")
        return None
