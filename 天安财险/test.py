import requests
import execjs
import sys
import json
import time


folder_path = sys.path[0]

params1 = {
    "body": {
        "loginMethod": "1",
        "name": "15910887649",
        "password": "12345678"
    },
    "head": {
        "userCode": None,
        "channelCode": "101",
        "transTime": round(time.time() * 1000),
        "transToken": "",
        "customerId": None,
        "transSerialNumber": ""
    }
}

params1 = json.dumps(params1, separators=(",", ":"))

with open(f"{folder_path}/tianan.js", "r", encoding="utf-8") as f:
    js_code = f.read()

jsonKey = execjs.compile(js_code).call("newEncrypt", params1)
# print(jsonKey)


url = "https://tianaw.95505.cn/tacpc/tiananapp/customer_login/taPcLogin"

session = requests.session()

session.headers = {
    "Referer": "https://tianaw.95505.cn/tacpc/",
    # "Keys": "mYb5QhIirN+gEFY6WTty3/5nPgIkB8d1EaIhH7n74gCwoXYl/rZZJr4Q1zJKElAX0SZJujfpK6+S2K0EqP8RZuiMOgfIn5iHkz/m2ymZzyA=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

data = {
    "jsonKey": jsonKey
}
data = json.dumps(data, separators=(",", ":"))
print(data)

response = session.post(url=url, data=data, proxies=proxies).text
print(response)
