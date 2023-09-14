import math
import time
import base64
import requests
import execjs
import sys

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

folder_path = sys.path[0]

"""
'iv': CryptoJS["enc"]["Utf8"]["parse"]("1234567887654321"),
'mode': CryptoJS["mode"]["CBC"],
'padding': CryptoJS["pad"]["Pkcs7"]
"""

timestamp = str(math.floor(time.time()))
timestamp = timestamp.encode("utf-8")
timestamp = pad(timestamp, 16)

iv = "1234567887654321".encode("utf-8")
aes = AES.new(key=iv, mode=AES.MODE_CBC, iv=iv)
a = aes.encrypt(timestamp)
accept_enckey = base64.b64encode(a).decode("utf-8")
print(accept_enckey)

# ts = str(math.floor(time.time()))

# with open(f"{folder_path}/juchao_zixun.js", "r", encoding="utf-8") as f:
#     js_code = f.read()

# accept_enckey = execjs.compile(js_code).call("getResCode", ts)

url = "https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007"

session = requests.session()

session.headers = {
    "Accept-Enckey": accept_enckey,
    # "Accept-Enckey": "Oc5F5PFYKe+sBbb9XIv4sQ==",
    "Referer": "https://webapi.cninfo.com.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

data = {
    "tdate": "2023-09-07",
    "market": "SZE"
}

response = session.post(url=url, data=data, proxies=proxies).text
print(response)