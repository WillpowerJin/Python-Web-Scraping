# Destination URL: https://www.oklink.com/cn/btc/tx-list

import sys
import time
import requests
import execjs
import json


folder_path = sys.path[0]

timestamp = str(round(time.time() * 1000))

# 调用JS 获取X-Apikey
with open(f"{folder_path}/oklink.js", "r", encoding="utf-8") as f:
    js_code = f.read()
X_Apikey = execjs.compile(js_code).call("getApiKey")


url = "https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict"

session = requests.session()

session.headers = {
    "X-Apikey": X_Apikey,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

params = {
    "t": timestamp,
    "offset": "0",
    "txType": "",
    "limit": "20",
    "curType": ""
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

response = session.get(url=url, params=params, proxies=proxies).json()
# print(response)

with open(f"{folder_path}/oklink_data.json", "w", encoding="utf-8") as f:
    json.dump(response["data"]["hits"], f, ensure_ascii=False)
