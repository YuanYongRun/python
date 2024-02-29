# get请求
# 获取豆瓣电影的第一页数据，并保存起来
import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

header ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}


# 请求对象定制
request = urllib.request.Request(url=url,headers=header)


# 获取响应的数据
response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

# 数据下载到本地
# open方法默认使用gbk编码，如果要保存汉字，那么需要在open中方法指定为utf-8
f = open('douban.json',"w",encoding="utf-8")
f.write(content)
f.close()

print(content)