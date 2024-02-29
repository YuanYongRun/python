"""
1.请求对象定制
2.获取网页源码
3.下载
"""


# 需求:下载前10页的图片
"""
第一页地址:https://sc.chinaz.com/tupian/qinglvtupian.html
第二页地址:https://sc.chinaz.com/tupian/qinglvtupian_2.html
第三页地址:https://sc.chinaz.com/tupian/qinglvtupian_3.html
"""
import urllib.request
from lxml import etree
def create_request(page):
    if page ==1:
        url = "https://sc.chinaz.com/tupian/qinglvtupian.html"
    else:
        url ='https://sc.chinaz.com/tupian/qinglvtupian_'+str(page)+".html"
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'cz_statistics_visitor=90ab9ec1-ed43-0f7d-d70a-5fe55d6a6dc9; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1689040424; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1689043610',
        'Host': 'sc.chinaz.com',
        'Referer': 'https://sc.chinaz.com/tupian/qinglvtupian.html',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    }
    request = urllib.request.Request(url=url,headers=header)
    return request


def get_content(request):
    response =urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content

def down_load(content):
    # 下载图片
    #urllib.request.urlretrieve('图片地址','文件名字')
    tree = etree.HTML(content)
    name_list = tree.xpath("//div[@class='container']//div/img/@alt")
    # 一般设计到图片的网站，都会进行懒加载
    src_list = tree.xpath('//div[@class="container"]//div/img/@data-original')
    for i in range(len(name_list)):
        name =name_list[i]
        src = src_list[i]
        url = "http:"+src
        # url=url.replace("_s","")
        urllib.request.urlretrieve(url=url,filename='./love1_image/'+name+".jpg")
       #  print(url)





if __name__ == '__main__':
    start_page = int(input("请输入起始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page,end_page+1):
        # 请求对象定制
        request = create_request(page)
        # 获取网页的源码
        content=get_content(request)
        # 下载
        down_load(content)