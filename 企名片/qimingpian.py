import requests
import sys
import execjs
import json


folder_path = sys.path[0]

url = "https://vipapi.qimingpian.cn/DataList/productListVip"

session = requests.session()

session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

data = {
    "time_interval": "",
    "tag": "",
    "tag_type": "",
    "province": "",
    "lunci": "",
    "page": "1",
    "num": "20",
    "unionid": ""
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

response = session.post(url=url, proxies=proxies).json()
encrypt_data = response["encrypt_data"]
# print(encrypt_data)

with open(f"{folder_path}/qimingpian.js", "r", encoding="utf-8") as f:
    js_code = f.read()

result = execjs.compile(js_code).call("s", encrypt_data)
# print(result)

with open(f"{folder_path}/qimingpian_data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False)
