import requests
import sys, json


folder_path = sys.path[0]

url = "http://www.whggzy.com/front/search/category"

session = requests.session()

session.headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

data = '{"utm":"sites_group_front.2ef5001f.0.0.f98a02604d5e11eea6816963610709cf","categoryCode":"MostImportant","pageSize":15,"pageNo":1}'

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

response = session.post(url=url, data=data, proxies=proxies)
# print(response.text)

with open(f"{folder_path}/website_headlines.json", "w", encoding="utf-8") as f:
    json.dump(response.json(), f, ensure_ascii=False)
