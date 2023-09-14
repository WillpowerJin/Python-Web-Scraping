import requests
import sys
import execjs
import json


folder_path = sys.path[0]

url = "https://www.endata.com.cn/API/GetData.ashx"

session = requests.session()

data = {
    "year": "2023",
    "MethodName": "BoxOffice_GetYearInfoData"
}

session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

response = session.post(url=url, data=data, proxies=proxies).text
# print(response)

with open(f"{folder_path}/endata.js", "r", encoding="utf-8") as f:
    js_code = f.read()

result_str = execjs.compile(js_code).call("webInstace.shell", response)

result_json = json.loads(result_str)
with open(f"{folder_path}/endata.json", "w", encoding="utf-8") as f:
    json.dump(result_json, f, ensure_ascii=False)

number = result_json["Data"]["Table"]
print(len(number))
