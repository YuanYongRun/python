

"""
需求:使用handler来访问百度  获取网页源码
"""

import urllib.request

url = "http://www.baidu.com"

header ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

request = urllib.request.Request(url=url,headers=header)

# handler     build_opener   open

# 获取handler对象
handler = urllib.request.HTTPHandler()

# 通过handler获取opener对象
opener = urllib.request.build_opener(handler)

# 调用open方法
response =opener.open(request)

content =response.read().decode("utf-8")

print(content)