# Destination URL: https://www.qimingpian.com/finosda/project/pinvestment

import sys
import requests
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

response = session.post(url=url, data=data, proxies=proxies).json()
encrypt_data = response["encrypt_data"]
# print(encrypt_data)

# execjs 调用 JS 代码
with open(f"{folder_path}/qimingpian.js", "r", encoding="utf-8") as f:
    js_code = f.read()
data = execjs.compile(js_code).call("s", encrypt_data)

# 保存 json 文件
with open(f"{folder_path}/qimingpian_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
