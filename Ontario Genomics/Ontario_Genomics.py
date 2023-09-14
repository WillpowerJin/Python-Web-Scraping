import requests
import execjs
import sys


folder_path = sys.path[0]


url = "https://www.ontariogenomics.ca/news-events/"

session = requests.session()

with open(f"{folder_path}/Ontario_Genomics.js", "r", encoding="utf-8") as f:
    js_code = f.read()

cookie = execjs.compile(js_code).call("get_cookie")
print(cookie)

session.headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

response = session.get(url=url, proxies=proxies)
print(response.text)
