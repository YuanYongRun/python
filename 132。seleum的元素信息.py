from selenium import webdriver


path = "chromedriver.exe"

brower = webdriver.Chrome(path)



url = 'https://www.baidu.com'

brower.get(url)


input = brower.find_element_by_id("su")
# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签的名字
print(input.tag_name)

# 获取元素文本
a = brower.find_element_by_link_text("新闻")
print(a.text)