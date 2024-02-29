"""

"""


import requests

url = "https://fanyi.baidu.com/sug"

headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}


data = {
    "kw":'eye'
}


"""
url: 请求路径
data:请求参数
kwarg:字典
"""

response = requests.post(url=url,data=data,headers=headers)

content =response.text

import json
obj = json.loads(content)


print(obj)
print(content)


"""
post请求不需要编解码的
post请求的参数必须是data
不需要请求对象的定制
"""

