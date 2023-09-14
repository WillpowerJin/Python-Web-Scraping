import sys, json
import requests
import execjs


folder_path = sys.path[0]

url = "https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank"

session = requests.session()

params = {
    "channel": "movielist",
    "sign": "5f3cce6a40c09a221b21104cc98436a3"
}

session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url=url, params=params).json()
# print(response)

timestamp = response["lastFetchTime"]
data = response["data"]


with open(f"{folder_path}/rank.js", "r", encoding="utf-8") as f:
    js_code = f.read()

plaintext = execjs.compile(js_code).call("AES123", timestamp, data)
print(plaintext)

with open(f"{folder_path}/{params['channel']}.json", "w", encoding="utf-8") as f:
    json.dump(plaintext, f, ensure_ascii=False)