"""
(1)获取网页源码
(2)解析 解析的服务器响应的文件   etree.HTML
(3)打印
"""

import urllib.request
url = "https://www.baidu.com/"

header ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

request = urllib.request.Request(url=url,headers=header)


response = urllib.request.urlopen(request)


content = response.read().decode("utf-8")

# 解析网页源码，获取我们想要的数据
from lxml import etree
# 解析服务器响应的数据
tree = etree.HTML(content)

# 获取想要的数据  xpath的返回值是一个列表数据类型
result = tree.xpath("//input[@id='su']/@value")

print(result)