import requests
import sys
import execjs
import re

from lxml import etree


folder_path = sys.path[0]

# url = "https://youzhicai.com/nd/c93b8018-328a-40f4-950b-3d4bdbac44c1-1.html"
url = "https://www.youzhicai.com/nd/a5e97ff9-6816-4407-8cc5-44189e562953-1.html"

session = requests.session()

session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

response = session.get(url=url, proxies=proxies)

with open(f"{folder_path}/first_requests.html", "w", encoding="utf-8") as f:
    f.write(response.text)

# requests.utils.dict_from_cookiejar: cookiejar -> dict
cookies = requests.utils.dict_from_cookiejar(session.cookies)
# print(cookies)

response = re.sub("\s", "", response.text)  # 把response里面的空格等，替换成空
var_a = re.findall("vara='(.*?)';", response)[0]
var_b = re.findall("varb='(.*?)';", response)[0]

with open(f"{folder_path}/优质采.js", "r", encoding="utf-8") as f:
    js_code = f.read()

spvrscode = execjs.compile(js_code).call("get_cookies", var_a, var_b)
# print(spvrscode)

cookies["spvrscode"] = spvrscode

real_response = session.get(url=url, proxies=proxies, cookies=cookies)
# print(real_response.text)

with open(f"{folder_path}/page_source.html", "w", encoding="utf-8") as f:
    f.write(real_response.text)
