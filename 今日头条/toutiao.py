import sys
import json
import requests
import execjs

from urllib.parse import urlencode


folder_path = sys.path[0]

url = "https://www.toutiao.com/api/pc/list/feed?"

# params = {
#     "channel_id": "3189398999",
#     "min_behot_time": "0",
#     "offset": "0",
#     "refresh_count": "1",
#     "category": "pc_profile_channel",
#     "client_extra_params": '{"short_video_item":"filter"}',
#     "aid": "24",
#     "app_name": "toutiao_web",
# }

params = "channel_id=3189398999&min_behot_time=0&offset=0&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web"

# parse_params = urlencode(params)

target_url = url + params

with open(f"{folder_path}/toutiao.js", "r", encoding="utf-8") as f:
    js_code = f.read()

sign = execjs.compile(js_code).call("get_sign", target_url)
print(sign)

# params["_signature"] = sign

# parse_params_sign = urlencode(params)
# final_url = url + parse_params_sign
# print(final_url)

session = requests.session()

session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

response = session.get(url=f"{target_url}&_signature={sign}", proxies=proxies).text
# response = session.get(url=final_url, proxies=proxies).json()
print(response)

with open(f"{folder_path}/toutiao_data.json", "w", encoding="utf-8") as f:
    json.dump(response, f, ensure_ascii=False)



# # urlparse(url) -> 提取url中的域名
# parsed_url = urlparse(url)
# domain = parsed_url.scheme + "://" + parsed_url.netloc
# print(domain)
