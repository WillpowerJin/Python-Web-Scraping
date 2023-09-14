import time
import random
import requests
import sys
import re
import json


folder_path = sys.path[0]

url = "https://widget.1688.com/front/getJsonComponent.json"

session = requests.session()

session.headers = {
    "Referer": "https://show.1688.com/",
    "Cookie": f"cbu_mmid=7E3C55520E991B9B1BDBA6471218C73350CADB71CCC1D79114E357B73D4A9BF309F848C1F03189F2DDDCA31D76FEC845842C0AD7CBD3AD68B67FAE76F5236435; ta_info=431EEA0EF470984D28D52453CC0DA41297234972A6103BDF50F0FE8F811E949D09EAF4563BC57F777E448EB059A88EB629639DA62201B5813CA456A0F96B32D425DF072B65366AF9F591632068CD27FA23353CF97B100118F6ABC7375BE99A02A3F756679E97C843441472937FA08459AF5628A3F492DF46F267175132C2E1E3F03267AA90423A56; xlly_s=1; cookie2=1a1683a865fd166e766a8b1481130394; t=d2f0fd330ffd52ab7273f81e242a337e; _tb_token_=ee63d7776e37b; _m_h5_tk=7093a4f26d8dcb0d260dd0852dc7d50d_1694153604200; _m_h5_tk_enc=7e6e6edc4d72538d8626f00e8a62b0b1; cookie1=UUiHXxF4kpLzYLSdeedfMf%2F4ac4OTdSUBIjNW74AcIk%3D; cookie17=UNDVdRbDBifk; sgcookie=E100%2Bo6fTQpjT0S%2F5ZBw3gpMbBudteuTpmQf9v81SqSiX0zx6zYVxZOTs2dnptmHYbm4V6tJHXbYbJq4GyfqzQK7aW4WpX7zXH2D2HI8PM3Ayh2WraGoiL3NUk5%2FPqeUU58%2B; sg=%E5%90%8E73; csg=84c58391; lid=%E5%BD%93%E7%81%AB%E8%BD%A6%E5%BC%80%E8%B5%B0%E4%B9%8B%E5%90%8E; unb=301764877; uc4=nk4=0%401E%2BWVCNBKLELhPzOfz8AgmKcLjlMwsvQGA%3D%3D&id4=0%40UgclGKA2K50SV5kMz1IAVGbC0dQ%3D; __cn_logon__=true; __cn_logon_id__=%E5%BD%93%E7%81%AB%E8%BD%A6%E5%BC%80%E8%B5%B0%E4%B9%8B%E5%90%8E; ali_apache_track=c_mid=b2b-301764877185e5|c_lid=%E5%BD%93%E7%81%AB%E8%BD%A6%E5%BC%80%E8%B5%B0%E4%B9%8B%E5%90%8E|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; _nk_=%5Cu5F53%5Cu706B%5Cu8F66%5Cu5F00%5Cu8D70%5Cu4E4B%5Cu540E; last_mid=b2b-301764877185e5; _csrf_token={round(time.time() * 1000)}; __mwb_logon_id__=%25E5%25BD%2593%25E7%2581%25AB%25E8%25BD%25A6%25E5%25BC%2580%25E8%25B5%25B0%25E4%25B9%258B%25E5%2590%258E; mwb=ng; isg=BBQUwzVjDD2JxZjywN-4M6eJ5VKGbThX4p_CMK7loB8imbbj135h5vBYmZEBZ3Cv; l=fBMiCZFmNvUXyFPOBO5IFurza77OonAbzrVzaNbMiIEGa6dCOFZbzNC67RO65dtjgT5VPeKyVhmX9dHySJU38AkDBeYIujcjftY9RetzRyMc.",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

# c = "" + r.prefix + Math.floor(100 * Math.random() + 1) + (new Date).getTime()
callback = "" + "callback" + str(random.randint(1, 100)) + str(round(time.time() * 1000))
# print(callback)

params = {
    "namespace": "TpFacRecommendService",
    "widgetId": "TpFacRecommendService",
    "methodName": "execute",
    "params": '{"pageNo":1,"query":"pinleiId=5344&mainCate=7","pageSize":20,"from":"PC","showType":"transverse","trafficSource":"pc_index_recommend","sort":"mix"}',
    "pageNo": "1",
    "query": "pinleiId=5344&mainCate=7",
    "pageSize": "20",
    "from": "PC",
    "showType": "transverse",
    "trafficSource": "pc_index_recommend",
    "sort": "mix",
    "_tb_token_": "ee63d7776e37b",
    "callback": callback
}

response = session.get(url=url, params=params, proxies=proxies)
# print(response.text)

obj = re.compile(r"\((?P<json_data_str>.*)\)", re.S)
json_data_str = obj.search(response.text).group("json_data_str")
result = json.loads(json_data_str)

with open(f"{folder_path}/1688_callback_data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False)
