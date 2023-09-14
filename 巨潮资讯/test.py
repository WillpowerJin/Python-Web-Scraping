# import time, math, base64

# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad

# time1 = str(math.floor(time.time()))
# time1 = time1.encode("utf-8")
# time1 = pad(time1, 16)

# iv = "1234567887654321".encode("utf-8")
# aes = AES.new(key=iv, mode=AES.MODE_CBC, iv=iv)
# a = aes.decrypt(time1)
# # a = unpad(a, 16)
# r = base64.b64encode(a).decode()
# print(r)

import time, math, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# time1 = str(math.floor(time.time()))
time1 = "1694191894"
time1 = time1.encode("utf-8")
time1 = pad(time1, 16)

iv = "1234567887654321".encode("utf-8")
aes = AES.new(key=iv, mode=AES.MODE_CBC, iv=iv)
a = aes.encrypt(time1)
# a = unpad(a, 16)
r = base64.b64encode(a).decode()
print(r)

# 1694191894
# tDqYSxCA2p7LvUdYtVEbWg==