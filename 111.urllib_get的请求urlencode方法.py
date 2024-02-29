"""
urllencode应用场景:多个参数的时候
"""
import urllib.parse

# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=男

# data = {
#     "wd":"周杰伦",
#     "sex":"男",
#     "location":"中国台湾省"
# }
#
# a = urllib.parse.urlencode(data)
# print(a)

# 获取网页源码 https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81
import  urllib.request
base_url = "https://www.baidu.com/s?"

data = {
    "wd":"周杰伦",
    "sex":"男",
    "location":"中国台湾省"
}

new_data = urllib.parse.urlencode(data)
url = base_url+new_data   #请求资源路径
print(url)
# header ={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
# }
#
# # 请求对象定制
# request =  urllib.request.Request(url=url,headers=header)
#
# response = urllib.request.urlopen(request)
#
#
# # 获取网页源码数据
# content = response.read().decode("utf8")
#
# print(content)