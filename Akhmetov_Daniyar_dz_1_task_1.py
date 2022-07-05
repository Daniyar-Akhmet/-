import requests
import json
from pprint import pprint


result = []

for i in range(1, 10):
    url = f"https://api.github.com/users/defunkt/repos?page={i}"
    session = requests.Session()
    try:
        response = session.get(url)
        result.extend([response.json()[i]['archive_url'].split('{', 1)[0].replace('api.', '').replace('repos/', '') for i in range(0, len(response.json()))])
    except requests.RequestException:
        print('Error')

result_json = json.dumps(result)

with open("result.json", 'w', encoding='utf-8') as f:
    json.dump(result, f)
