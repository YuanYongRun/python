from selenium import webdriver
import time
# 创建浏览器对象
path ="chromedriver.exe"

browser = webdriver.Chrome(path)



# 定义url
url = "http://www.baidu.com"
browser.get(url)



time.sleep(2)

# 获取文本框对象
Input = browser.find_element_by_id("kw")

# 在文本框中输入周杰伦
Input.send_keys("周杰伦")

time.sleep(2)

# 获取一下百度一下的按钮
button = browser.find_element_by_id("su")


# 点击按钮
button.click()

time.sleep(2)

# 滑到底部
js_botton = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_botton)

time.sleep(2)


# 获取下一页的按钮
next = browser.find_element_by_xpath("//a[@class='n']")

# 点击下一页
next.click()

time.sleep(2)

# 返回上一页
browser.back()


# 回去
browser.forward()
time.sleep(3)


# 退出
browser.quit()
