"""
通过登陆 进入到主界面
通过找登陆接口，发现登录的时候需要参数很多
__VIEWSTATE: NIFFxsjejVmtil6FVNl/PVj2wFhSvdyeXA5G9cXvzlFKu87CYu1tWdm7DGv7HF1Og7IAFcXdUZz05pV1nMfZ7bgVCIUj1lV9wG2NbQqYSUvGIPz2Y7hhETR4QluBzBNrz8Ey8gwMA3zxeEPOoqAcXWjBius=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://so.gushiwen.cn/user/collect.aspx
email: YongRun_Yuan@yeah.net
pwd: 1234676765
code: 48jq
denglu: 登录

观察到__VIEWSTATE,__VIEWSTATEGENERATOR,code是可以变换的量

难点:(1)__VIEWSTATE,__VIEWSTATEGENERATOR   一般来说，看不到的数据都在页面源码中
上面两个数据在页面的源码中，所以我们需要获取的页面的源码，然后解析就可以获取了
(2)验证码

"""


import requests

url ="https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"

headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

response = requests.get(url=url,headers=headers)

content = response.text

# 解析页面源码，然后获取 __VIEWSTATE,__VIEWSTATEGENERATOR
from bs4 import BeautifulSoup
import lxml
soup = BeautifulSoup(content,"lxml")

# 获取__VIEWSTATE
view_state=soup.select("#__VIEWSTATE")[0].attrs.get('value')
# 获取__VIEWSTATEGENEROTOR
view_stategenerator = soup.select("#__VIEWSTATEGENERATOR ")[0].attrs.get("value")

# 获取验证码图片
code = soup.select("#imgCode")[0].attrs.get("src")
code_url = "https://so.gushiwen.cn"+code


"""
有坑
import urllib.request
urllib.request.urlretrieve(url=code_url,filename="code.jpg")

requests里面有一个方法 session()通过session返回值就能使请求变为一个对象
"""
# 获取到验证码的图片后，下载到本地，然后观察验证码，将这个值给code_name

# import urllib.request
#
# urllib.request.urlretrieve(url=code_url,filename="code.jpg")

session = requests.session()
# 验证码的url内容
response_code = session.get((code_url))
# 注意使用的是二进制数据，要进行图片的下载
conten_code = response_code.content

# wb模式就是将二进制数据写入到文件
with open("code.jpg","wb") as fp:
    fp.write(conten_code)



code_name = input("请输入你的验证码")


# 点击登录
urL_post = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"

data_post = {
'__VIEWSTATE': view_state,
"__VIEWSTATEGENERATOR": view_stategenerator,
"from":" http://so.gushiwen.cn/user/collect.aspx",
"email":"YongRun_Yuan@yeah.net",
"pwd":"LWDgood2004",
"code":code_name,
"denglu":'登录'
}

response_post=session.post(url=url,headers=headers,data=data_post)

conten_post = response_post.text

with open("gushiwen.html","w",encoding="utf-8") as fp:
    fp.write(conten_post)


"""
难点一:隐藏域
难点二:验证码
"""