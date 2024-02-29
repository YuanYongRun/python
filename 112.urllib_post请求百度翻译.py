# pos请求
import urllib.request
import urllib.parse

url = "https://fanyi.baidu.com/sug"

header ={
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

data = {
    "kw":'transform'
}

# post的请求参数必须要进行编码
data = urllib.parse.urlencode(data).encode("utf-8")
# pos请求的参数，是不会拼接在url后面的，而是放在需要定制的请求定制对象的参数中
# pos请求的参数，必须进行编码
request = urllib.request.Request(url=url,data = data,headers=header)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content =response.read().decode("utf-8")
# 打印数据
# print(content)
# print(type(content))

# 字符串转json数据
import json
obj = json.loads(content)
print(obj)

"""
pos请求方式的参数必须编码  data = urllib.parse.urlencode(data)
编码之后必须，必须调用encode方法 data = urllib.parse.urlencode(data).encode("utf-8")
参数是放在请求对象定制的方法中request = urllib.request.Request(url=url,data = data,headers=header)
"""