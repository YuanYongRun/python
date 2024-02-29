import urllib.request
import urllib.error
# url = "https://blog.csdn.net/weixin_43569396/article/details/1256444301"

url ='http://www.goudan111.com'

header ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
try:

    request = urllib.request.Request(url=url,headers=header)

    response = urllib.request.urlopen(request)

    content = response.read().decode()

    print(content)
except urllib.error.HTTPError:
    print("系统正在升级.....")
except urllib.error.URLError:
    print("我都说了，系统正在升级")