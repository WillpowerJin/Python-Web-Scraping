from curl_cffi import requests


url = "https://radar.cloudflare.com/traffic/verified-bots"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

# TLS 模拟浏览器指纹检测
response = requests.get(url=url, proxies=proxies, impersonate="chrome101")
print(response.text)
