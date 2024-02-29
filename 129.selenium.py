# 浏览器可能不会完全把数据返回给你
import urllib.request

url ="https://www.jd.com/"

response = urllib.request.urlopen(url)

content = response.read().decode("utf-8")

print(content)