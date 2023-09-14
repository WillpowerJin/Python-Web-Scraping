import time, json, base64, re
import requests

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from urllib.parse import quote_plus


timestamp = round(time.time() * 1000)

def newEncrypt(data):
    n = "Hj6WfS4DskDSmFGP".encode("utf-8")
    t = "Hj6WfS4DskDSmFGP".encode("utf-8")
    e = data.encode("utf-8")
    a = AES.new(key=n, mode=AES.MODE_CBC, iv=t)
    cipher_text = a.encrypt(pad(e, AES.block_size))

    return base64.b64encode(cipher_text).decode()

f = {
    "body": {
        "loginMethod": "1",
        "name": "15910887649",
        "password": "vce94202"
    },
    "head": {
        "userCode": None,
        "channelCode": "101",
        "transTime": round(time.time() * 1000),
        # "transTime": 1694423142663,
        "transToken": "",
        "customerId": None,
        "transSerialNumber": ""
    }
}

jsonKey = newEncrypt(json.dumps(f, separators=(",", ":")))
print(jsonKey)


def newDecoto(data):
    n = base64.b64decode(data)
    t = "Hj6WfS4DskDSmFGP".encode("utf-8")
    e = "Hj6WfS4DskDSmFGP".encode("utf-8")
    cipher_params = {"ciphertext": n}
    
    aes = AES.new(key=t, mode=AES.MODE_CBC, iv=e)
    plain_text = aes.decrypt(cipher_params["ciphertext"])
    plain_text = unpad(plain_text, 16)

    return plain_text.decode("utf-8")

encryctReturns = "t25+y2GZdO8f2xNhlsqDBpHySSF/tZFmza/UcUlA9OGa2c6t+AjwWLtygKER7I/mBzWb1hje6gQM\nTKMc1bRNtniBsFYNrIuP+ObvFCUPfO9ZZIFW5cfdv07jAyZsKgSL4zzfdfTtMqcjioxUDfHLWomO\nSmggU8zp8aT6vDv4dyNgrk0aoxyc1evCgZ+4jhM6zm1V9U1RcsLNd1Qaf9mKjjIwc2BzAUwuSGiU\nuf6y66p3ZRCbun54iUmlbALKzDk77JhKqF3t8PPRdHAvDTJGLoD4+pi5LONJHBnusRmc+RSMxuG4\nqn1cv78Jm/8UH+IT"
encryctReturns = encryctReturns.replace("\r", "").replace("\n", "")
# encryctReturns = re.sub(r"[\r\n]", "", encryctReturns)
login_info = newDecoto(data=encryctReturns)


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

# jsonKey = quote_plus(jsonKey)
data = {"jsonKey": jsonKey}
data = json.dumps(data, separators=(",", ":"))
# data = f"jsonKey={jsonKey}"
print(data)

response = session.post(url=url, data=data, proxies=proxies).text
print(response)
