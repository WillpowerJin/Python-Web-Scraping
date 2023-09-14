import requests
import base64
import binascii
import sys, json

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


folder_path = sys.path[0]

url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list"

session = requests.session()

session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

params = {
    "pg": "0",
    "pgsz": "15",
    "total": "450"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

response = session.get(url=url, params=params, proxies=proxies).text
# print(response)

t = response
f = "jo8j9wGw%6HbxfFn"
m = "0123456789ABCDEF"

"""
f = d.a.enc.Utf8.parse("jo8j9wGw%6HbxfFn"), m = d.a.enc.Utf8.parse("0123456789ABCDEF");

function h(t) {
    var e = d.a.enc.Hex.parse(t)
        , n = d.a.enc.Base64.stringify(e)
        , a = d.a.AES.decrypt(n, f, {
        iv: m,
        mode: d.a.mode.CBC,
        padding: d.a.pad.Pkcs7
    })
        , r = a.toString(d.a.enc.Utf8);
    return r.toString()
}
"""

f = f.encode("utf-8")
m = m.encode("utf-8")

e = binascii.a2b_hex(t)
n = base64.b64encode(e).decode("utf-8")

aes = AES.new(key=f, mode=AES.MODE_CBC, iv=m)
a = aes.decrypt(base64.b64decode(n))
a = unpad(a, 16)
r = a.decode("utf-8")

json_data = json.loads(r)
with open(f"{folder_path}/jzsc.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False)
