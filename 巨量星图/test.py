import requests
import sys
import execjs


folder_path = sys.path[0]

c = {
    "hot_list_id": "0",
    "tag": "61e792904fe6649d1ba9aeee",
    "service_name": "author.AdStarAuthorService",
    "service_method": "GetHotListData",
    "sign_strict": 1
}

l = {
    "include": [
        "hot_list_id",
        "tag",
        "download",
        "image_download",
        "province",
        "city",
        "rlid"
    ]
}

v = True

with open(f"{folder_path}/test.js", "r", encoding="utf-8") as f:
    js_code = f.read()

text = execjs.compile(js_code).eval("text")
sign = execjs.compile(js_code).call("getSigndata", text)
# print(text)
# print(sign)

url = "https://www.xingtu.cn/h/api/gateway/handler_get/"

session = requests.session()

session.headers = {
    "Cookie": "tt_webid=7277750458863633939; csrf_session_id=eff5015fe9797a6baf0b1b3bb96105cb; csrftoken=kuPWSE5i-SaIzVD1hT5SxoDY89xtu7kRU6cM; ttcid=94eff44bff4148e88a6cf0c8aa5f953a28; tt_scid=4PCPz4Y.nbIxYiKvIEhx03rdo86QDP6RKr8FMpQwNTuZLvDs-I53JvQO1QbmAXpAa811; passport_csrf_token=b4159e9c241fca3515affb8206e1aaa5; passport_csrf_token_default=b4159e9c241fca3515affb8206e1aaa5; passport_auth_status=880b85fa4ec4cd3a0bf394abbf86052e%2C; passport_auth_status_ss=880b85fa4ec4cd3a0bf394abbf86052e%2C; sid_guard=0b8494bc8b415ad6aa2c3d9d210af7eb%7C1694483369%7C5184002%7CSat%2C+11-Nov-2023+01%3A49%3A31+GMT; uid_tt=8c8bcdcee947e1ad2ddea612d94aa4aa; uid_tt_ss=8c8bcdcee947e1ad2ddea612d94aa4aa; sid_tt=0b8494bc8b415ad6aa2c3d9d210af7eb; sessionid=0b8494bc8b415ad6aa2c3d9d210af7eb; sessionid_ss=0b8494bc8b415ad6aa2c3d9d210af7eb; sid_ucp_v1=1.0.0-KGViMGViYTk4YmIxYTE3ZmQ2OGRlM2RhZWU0NDg5NjAxNjJkMWEwMGUKFwis1qDz_s2EBRCph_-nBhj6EzgCQPEHGgJobCIgMGI4NDk0YmM4YjQxNWFkNmFhMmMzZDlkMjEwYWY3ZWI; ssid_ucp_v1=1.0.0-KGViMGViYTk4YmIxYTE3ZmQ2OGRlM2RhZWU0NDg5NjAxNjJkMWEwMGUKFwis1qDz_s2EBRCph_-nBhj6EzgCQPEHGgJobCIgMGI4NDk0YmM4YjQxNWFkNmFhMmMzZDlkMjEwYWY3ZWI; x-jupiter-uuid=16944833699392048; star_sessionid=0b8494bc8b415ad6aa2c3d9d210af7eb; s_v_web_id=verify_lmfnnf9h_TbN7LKPP_4Lj9_4wub_9tBT_SgJos3ks4Bn1; msToken=EpFGZs6nNA6YCRR9tqvsPuIYiyCN6o0vgs8cHDHDJrfUL3wyCK3X0JAqok4CNfQJJgawhAn1GliDcS9JEEVNiCPkDIwAfhOeLTb7EEQZ",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

proxies = {
    "http": "127.0.0.1:7890",
    "https": "127.0.0.1:7890"
}

params = {
    "hot_list_id": "0",
    "tag": "61e541324fe6649d1b8a2ee3",
    "service_name": "author.AdStarAuthorService",
    "service_method": "GetHotListData",
    "sign_strict": "1",
    "sign": "1f0a215db72ea3a2ad2788a89cbcaec0"
}

response = session.get(url=url, proxies=proxies, params=params).text
print(response)

# X-Csrftoken
# X-Secsdk-Csrf-Token