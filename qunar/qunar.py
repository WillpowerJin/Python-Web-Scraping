# Destination URl: https://m.flight.qunar.com/h5/flight/

import time
import requests
from hashlib import sha1, md5


# __m__ 加密位置：e.data["__m__"] = u.default.encryptToken(u.default.encrypt());
"""
{
    key: "encryptFunction",
    value: function () {
        return [function (e) {
            var t = (0,
                u.default)(e).toString();  // u.default -> SHA1
            return (0,
                f.default)(t).toString()   // f.default -> MD5
        }
            , function (e) {
                var t = (0,
                    f.default)(e).toString();
                return (0,
                    u.default)(t).toString()
            }
        ]
    }
}
"""
# u.default.encrypt()
def encryptFunction(r, t, n):
    if r == 0:
        # u_default = SHA1
        obj = sha1()
        obj.update((t+n).encode("utf-8"))
        sha1_value = obj.hexdigest()
        # f_default = MD5
        obj = md5()
        obj.update(sha1_value.encode("utf-8"))
        md5_value = obj.hexdigest()
        return md5_value
    else:
        # f_default = MD5
        obj = md5()
        obj.update((t+n).encode("utf-8"))
        md5_value = obj.hexdigest()
        # u_default = SHA1
        obj = sha1()
        obj.update(md5_value.encode("utf-8"))
        sha1_value = obj.hexdigest()
        return sha1_value

t = "b936f284-f732-43f8-bc43-e43a07554d72"
timestamp = round(time.time() * 1000)
r = timestamp % 2
encrypt = encryptFunction(r, t, n=str(timestamp))
print(f"encrypt: {encrypt}")


"""
{
    key: "encryptToken",
    value: function(t) {
        return (0,
        f.default)(t).toString()
    }
}
"""
# u.default.encryptToken()
obj = md5()
obj.update(encrypt.encode("utf-8"))
__m__ = obj.hexdigest()
print(f"__m__: {__m__}")


# headers 加密位置：e.headers, u.default.getToken();
"""
{
    key: "getRandomKey",
    value: function(t) {
        var n = "";
        var r = ("" + t).substr(4);
        r.split("").forEach(function(e) {
            n += e.charCodeAt()
        });
        var i = (0,
        f.default)(n).toString();
        return i.substr(-6)
    }
}

{
    key: "getToken",
    value: function() {
        var t = {};
        t[this.getRandomKey(this.getQtTime((0,
        s.default)(this.dencryptCode(this.qtTime))))] = this.encrypt();
        return t
    }
}
"""
headers_param = {}
ord_int_list = [ord(str(i)) for i in str(timestamp)[4:]]
ord_str_list = [str(i) for i in ord_int_list]
ord_str = "".join(ord_str_list)
obj = md5()
obj.update(ord_str.encode("utf-8"))
ord_str_md5 = obj.hexdigest()
getRandomKey = ord_str_md5[-6:]
headers_param = {
    getRandomKey: encrypt
}
# print(f"headers_param: {headers_param}")


url = "https://m.flight.qunar.com/flight/api/touchInnerList"

session = requests.session()

session.headers = {
    getRandomKey: encrypt,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

print(session.headers)
