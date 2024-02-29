from selenium import webdriver

path = "chromedriver.exe"

browser = webdriver.Chrome(path)


url = "https://www.baidu.com"


browser.get(url)


# 元素定位


# 根据ID找到对象  常用
# button = browser.find_element_by_id("su")
# print(button)


# 根据标签属性值来获取对象
# button =browser.find_element_by_name("wd")
# print(button)

# 利用xpath语句来获取对象 常用
# button = browser.find_element_by_xpath('//input[@id="su"]')
# print(button)


# 根据标签名来获取对象
# button = browser.find_elements_by_tag_name("input")
# print(button)

# 使用BS4的语法来获取对象  常用
# button = browser.find_elements_by_css_selector("#su")
# print(button)


button = browser.find_element_by_link_text("视频")
print(button)


