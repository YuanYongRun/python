"""
适用的场景:数据采集的时候，需要绕过登陆，然后进入某个页面
个人信息页面是utf-8，但是还是报错了编码错误，因为没有进入到个人信息页面，而是跳转了登陆页面
登录页面并非是Utf-8
"""

import  urllib.request

url ="https://weibo.com/u/2727797541"

header= {
# 'authority':' www.weibo.com',
# 'method':' GET',
# 'path':' /u/2727797541',
# 'scheme':' https',
# 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'accept-encoding':' gzip, deflate, br',
# 'accept-language':'zh-CN,zh;q=0.9',
# 'cache-control':' max-age=0',
# cookie中携带了你的登陆信息，如果登陆之后的cookie，那么就可以携带者cookie进入任何任免
'cookie':'SINAGLOBAL=5433412101336.128.1687094654861; PC_TOKEN=c4131ca45d; login_sid_t=2ada1ed998ff7d3df7cecdcbae3ed358; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=7604011883140.496.1688972639500; ULV=1688972639503:2:1:1:7604011883140.496.1688972639500:1687094654877; XSRF-TOKEN=HKn43up-Rg-3QjnFrbtcM3Q5; SUB=_2A25Jr8FYDeRhGeRJ6VUW-SnJzz2IHXVq3LWQrDV8PUNbmtAbLVDTkW9NUmQfSRUEfVRHEyGeRbRoJjoos0cvU2OS; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whe6iTiVEBr-.L_EbDaVYFb5JpX5KzhUgL.FozNeoMN1KMfSh22dJLoI7fWg-L1xXf8CHi8KoyB; ALF=1720509575; SSOLoginState=1688973576; WBPSESS=Dt2hbAUaXfkVprjyrAZT_NNirRg6lU6XKfaInjot6Gx0DMOGN5KXbPUSSYF9FOYf-9D5uQYf5CmJdHxQ5cYcSgjJxDsqJMAfgPmIYv782BUuCpq41CbbjlF582vuyNEF-MyieRYIYQuFohU60hFUTt2WxUL5QJez8rZUT8g_h_G4BYtfE8b7a2t-y6q0Ym-tfz9JXcNtfNffJOnBz5AWeQ==',
# referer是防盗链，判断当前路径是不是由上一个路劲进来的  一般做图片防盗链
"referer":"https://www.weibo.com/"
# 'sec-fetch-dest':'document',
# 'sec-fetch-mode':'navigate',
# 'sec-fetch-site':'same-origin',
# 'sec-fetch-user':'?1',
# 'upgrade-insecure-requests':'1',
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# 请求对象定制
request =urllib.request.Request(url = url,headers=header)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取相应数据
content = response.read().decode("utf-8")

print(content)

with open("weibo.html", "w", encoding="utf-8")  as fp:
    fp.write(content)