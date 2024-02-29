import urllib.request

url = "https://www.baidu.com"

"""
url的组成
http和https

https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
协议   主机  端口号   路径   参数
http        80     
https       443
mysql       3306
"""


headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

"""
因为urlopen不支持存储字典，所以header不能传递进去
请求对象定制
因为参数顺序的问题，不能直接写url和headers
"""
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')
print(content)