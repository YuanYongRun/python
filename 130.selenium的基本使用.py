# 1.导入selenium
from selenium import webdriver

# 2.创建浏览器操作对象
path = "chromedriver.exe"


brower = webdriver.Chrome(path)


# 3 访问网站
# url = 'https://www.baidu.com'
#
#
# brower.get(url)

url = "https://www.jd.com/"
brower.get(url)

# page_source获取网页源码

content = brower.page_source

print(content)
