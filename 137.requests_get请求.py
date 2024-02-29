"""
urllib
（1）一个类型和六个请求
（2）get请求
（3）post请求    百度翻译
（4）ajax的get请求
（5）ajax的post请求
（6）cookie登陆
（7）代理
"""




""""
requests
(1)一个类型及其六个属性
(2)get请求
(3)post请求
(4)代理
(5)cookie   验证码破解
"""



import requests

url = "https://www.baidu.com/s"

headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

data = {
    "wd":"北京"
}


"""
url:请求资源路径
params:参数  
kwargs:字典
"""
response = requests.get(url=url,params=data,headers=headers)

content = response.text

print(content)



"""
参数使用params传递
参数无需使用urlenconde编码
不需要请求对象定制
请求路径资源中的?可以加也可以不加
"""