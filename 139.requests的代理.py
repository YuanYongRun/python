import requests
url ="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=44004473_95_oem_dg&wd=iP%E6%9F%A5%E8%AF%A2"

headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}


data = {
    "wd":"ip"
}

proxy = {
    "http":"61.216.156.222:60808"
}
response = requests.get(url=url,params=data,headers=headers,proxies=proxy)

content = response.text

with open("daili3.html","w",encoding="utf-8") as fp:
    fp.write(content)