import requests
import json
from API_key import key


params = {
    "key": key,
    "q": "Astana, Kazakhstan",
    "format": "json",
    "num_of_days": "5"

}

url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
session = requests.Session()
try:
    response = session.get(url, params=params)
    tem_C = response.json()['data']["current_condition"][0]['temp_C']
    feels_likes_C = response.json()['data']["current_condition"][0]['FeelsLikeC']
    with open("result_task_2.json", "w", encoding="utf-8") as f:
        json.dump(response.json(), f)
    print(f"Погода в {params['q']}: {tem_C} C, ощущается как {feels_likes_C} C")
except requests.RequestException:
    print("Error")





