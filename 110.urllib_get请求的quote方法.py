# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 需求 获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6的网页源码
import urllib.request
import urllib.parse



url = "https://www.baidu.com/s?wd="

# 请求对象定制:解决反爬的第一手段
header ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
# 将周杰伦三个字变为Unicode编码的格式，依赖于urllib.parse
name = urllib.parse.quote("谜样的人生：阿加莎·克里斯蒂传")
print(name)
# %E5%85%A8%E9%83%A8
# url = url+name
# print(url)
# request = urllib.request.Request(url=url,headers=header)
# # 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)
#
# #获取响应内容
# content = response.read().decode("utf-8")
#
# # 打印数据
# print(content)

