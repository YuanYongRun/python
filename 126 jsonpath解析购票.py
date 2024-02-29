import urllib.request


url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1689057149392_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true"

headers = {
# ':authority': 'dianying.taobao.com',
# ':method': 'GET',
# ':path': '/cityAction.json?activityId&_ksTS=1689057149392_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
# ':scheme': 'https',
'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
# 'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'bx-v': '2.5.1',
'cookie': 't=196e3dfdf6a9390693cb798a82fc48fa; cna=ziTQHIPjWEYCAToTA+GlJILJ; _m_h5_tk=4c19019e893200076af889cb9b80caa4_1688725584323; _m_h5_tk_enc=7690ae77d20bfa4964f07c9b81fc6cf9; cookie2=11f3503ee7128d7aa66808cfbdabe1c5; v=0; _tb_token_=e373e4beeb5e1; xlly_s=1; tfstk=cOwGB0Dm_5l6nRXYRPM1B-NyEUCRZNxEWrz_LiPOHeRmNJeFiFRea9LAt24gHI1..; l=fBQK7Y2gNsz6MhGvBO5Cnurza77OfIRbzsPzaNbMiIEGa6sRtFMDeNC1vRYvSdtjgT50KetPkdi_7RnJyD438NsWHpfuKtyuJfp6ReM3N7AN.; isg=BIqKYgAa2mnHElY4RB_sqChG23Asew7VzZaEIBTD2V1oxyiB_A-F5Jk51zMbN4Zt',
'referer': 'https://dianying.taobao.com/',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")
print(content)
# split进行切割
content = content.split("(")[1].split(")")[0]


# with open("taopiaopiao.json","w",encoding="utf-8") as f:
#     f.write(content)


import json
import jsonpath

obj = json.load(open('taopiaopiao.json','r',encoding="utf-8"))

city_list = jsonpath.jsonpath(obj,"$..regionName")

print(city_list)