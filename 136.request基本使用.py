import requests

url = "http://www.baidu.com"


response = requests.get(url)


# print(type(response))
#
#
# # 设置响应的编码格式
# response.encoding="utf-8"
# # 以字符串形式来返回网页的源码
# print(response.text)

# # 返回一个网址
# print(response.url)


# # 返回的是二进制的数据
# print(response.content)


# # 返回响应的状态码
# print(response.status_code)


# 返回的是响应头
print(response.headers)
