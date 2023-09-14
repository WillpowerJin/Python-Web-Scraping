import sys, time, json, re
import requests
import execjs


folder_path = sys.path[0]

"""
j = h(d.token + "&" + i + "&" + g + "&" + c.data)
sign: j
"""

token = "771acb930af6ca1dbb20c6a1a2bd51be"
i = round(time.time() * 1000)
g = "12574478"
data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=10166&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\"}"}'
str = token + "&" + str(i) + "&" + g + "&" + data

with open(f"{folder_path}/1688_sign.js", "r", encoding="utf-8") as f:
    js_code = f.read()

sign = execjs.compile(js_code).call("h", str)
# print(sign)

url = "https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/"

session = requests.session()

session.headers = {
    "Referer": "https://sale.1688.com/",
    "Cookie": f"cbu_mmid=7E3C55520E991B9B1BDBA6471218C73350CADB71CCC1D79114E357B73D4A9BF309F848C1F03189F2DDDCA31D76FEC845842C0AD7CBD3AD68B67FAE76F5236435; xlly_s=1; lid=%E5%BD%93%E7%81%AB%E8%BD%A6%E5%BC%80%E8%B5%B0%E4%B9%8B%E5%90%8E; ali_apache_track=c_mid=b2b-301764877185e5|c_lid=%E5%BD%93%E7%81%AB%E8%BD%A6%E5%BC%80%E8%B5%B0%E4%B9%8B%E5%90%8E|c_ms=1; last_mid=b2b-301764877185e5; __mwb_logon_id__=%25E5%25BD%2593%25E7%2581%25AB%25E8%25BD%25A6%25E5%25BC%2580%25E8%25B5%25B0%25E4%25B9%258B%25E5%2590%258E; mwb=ng; _m_h5_tk=771acb930af6ca1dbb20c6a1a2bd51be_1694162043702; _m_h5_tk_enc=5e4e807adf6c6a39bd9158058143b7fc; cna=DEl4HQZKeQ0CAXL99c1FnmOb; t=d2f0fd330ffd52ab7273f81e242a337e; __cn_logon__=false; cookie1=UUiHXxF4kpLzYLSdeedfMf%2F4ac4OTdSUBIjNW74AcIk%3D; cookie2=13e59cb99c3e2989087149d6a300cb96; cookie17=UNDVdRbDBifk; sgcookie=E100IJYHpsMvK5VCuQUpfTuG3xHmTgA3dt1woTSdmfMOPaouJk5u98GEqEVlOCiyVoNWQD49QKHdhhRf3sGeTulNKFYIXqdvDBkhMhPU2wDmNmTJfzlqKx5KUxIm%2FKdv%2Bs2n; _tb_token_=7553e8dbe3565; sg=%E5%90%8E73; csg=6367755f; unb=301764877; uc4=id4=0%40UgclGKA2K50SV5kMz1IAVS41JCg%3D&nk4=0%401E%2BWVCNBKLELhPzOfz8AgmKcLjlNLXVPqA%3D%3D; _nk_=%5Cu5F53%5Cu706B%5Cu8F66%5Cu5F00%5Cu8D70%5Cu4E4B%5Cu540E; _csrf_token=1694156324829; l=fBMiCZFmNvUXyWzaBOfaFurza77txIRYouPzaNbMi9fP_85e5TiFW1TZJGYwCnGVFsaBR3-WjmOpBeYBqCbQm72xjsx8S2HmnmOk-Wf..; isg=BIWF9FnlTf41gGmhaaBZUE7OlMG_QjnUG_gTg4fqBrzLHqWQT5eZpGbwKELoWFGM",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

# proxies = {
#     "http": "127.0.0.1:7890",
#     "https": "127.0.0.1:7890"
# }

params = {
    "jsv": "2.6.1",
    "appKey": "12574478",
    "t": i,
    "sign": sign,
    "v": "1.0",
    "type": "jsonp",
    "isSec": "0",
    "timeout": "20000",
    "api": "mtop.taobao.widgetService.getJsonComponent",
    "dataType": "jsonp",
    "jsonpIncPrefix": "mboxfc",
    "callback": "mtopjsonpmboxfc3",
    "data": data
}

response = session.get(url=url, params=params).text

obj = re.compile(r"\((?P<json_data_str>.*)\)", re.S)
json_data_str = obj.search(response).group("json_data_str")
result = json.loads(json_data_str)

with open(f"{folder_path}/1688_sign_data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False)
