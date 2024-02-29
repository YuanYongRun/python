from bs4 import BeautifulSoup
import lxml

"""
通过解析本地文件来将bs4的基础语法进行讲解
默认打开文件的编码格式是gbk，所以打开文件的时候需要编码
"""

soup = BeautifulSoup(open("bs4的解析实例.html",encoding="utf-8"),"lxml")

# # 根据标签名查找节点
# print(soup.a)      # 找到的是第一个符合条件的数据
#
# # 获取标签的属性或者属性值
# print(soup.a.attrs)


"""
bs4的一些函数
find   返回的是第一个符合条件的数据
find_all
select
"""
# find
# print(soup.find("a"))
# print(soup.find("a",title="a2"))   #根据title的值来找到对应的标签
#
# # 不能直接使用class来找到对应的标签对象，注意的class需要添加下划线
# print(soup.find("a",class_="a1"))
#
#
#
#
# # find_all
#
# print(soup.find_all("a"))
#
# # 如果想获取的是多个数据，那么需要再find_all中添加的是列表数据
# print(soup.find_all(['a','span']))
#
# # limit查找前几个
# print(soup.find_all("li",limit=2))


# select方法返回的是一个列表，并且会返回多个数据
print(soup.select('a'))

#通过点代表class,成为类选择器
# print(soup.select('.a1'))
#
#
# # 根据ID进行选择
# print(soup.select("#l1"))
#
#
# # 通过属性来寻找对应的标签
# # 查找到li标签中有id的标签
# print(soup.select('li[id]'))
#
# # 查找到li标签中id为l2的标签
#
# print(soup.select('li[id="l2"]'))



"""
层次选择器
后代选择器   div+空格
子代选择器 
某标签的第一级子标签  div > ur > li  可以不加空格

"""
# print(soup.select(('div li')))
#
# print(soup.select('div >ur >li'))
#
#
# # 找到a标签和li标签的所有对象
# print(soup.select('a,li'))
#
# """
# 节点信息，获取节点内容
# """
#
# obj = soup.select('#d1')[0]
# # 如果标签对象中只有内容，那么string和get_text()都可以使用
# # 如果标签对象中，除了内容还有标签，那么只有get_text()可以获取
# print(obj.string)
# print(obj.get_text())
#
# """
# 节点的属性
#
# """
# obj = soup.select(('#p'))[0]
# print(obj.name )  # name是标签的名字
#
# # 将属性值作为一个字典返回
# print(obj.attrs)
#
# # 获取节点属性
# obj = soup.select("#p")[0]
# print(obj.attrs.get("class"))
# print(obj.get("class"))
#
# print(obj.get("class"))

