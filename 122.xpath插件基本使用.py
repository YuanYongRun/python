from lxml import etree

"""
xpath解析
（1）本地文件  etree.parse()
（2）直接解析服务响应的数据  response.read().decode("utf-8")     etree.HTML()
"""

# xpath解析本地文件
tree = etree.parse("xpath基本使用.html")

"""
路径查询:tree.xpath("路径")
谓词查询
"""

# 查找ul下的li
li_list = tree.xpath("//body/ul//li")

# 查找所有带有ID的属性li标签
# text()获取标签中的内容

li_list = tree.xpath('//ul/li[@id]/text()')


# 查找id为l1的标签
li_list = tree.xpath('//ul/li[@id="l1"]/text()')


# 查找到id为l1标签的class属性值
li_list = tree.xpath('//ul/li[@id ="l1"]/@class')


#查找id中包含l的li的标签

li_list=tree.xpath("//ul/li[contains(@id,'l')]/text()")


# 查询id的值以l开头的li标签

li_list = tree.xpath("//ul/li[starts-with(@id,'c')]/text()")


# 查询id为l1和class为c1的

li_list = tree.xpath("//ul/li[@id='l1' and @class ='c1']/text() ")


li_list = tree.xpath("//ul/li[@id = 'l1']/text() | //ul/li[@id='l2']/text()")

# 判断列表的长度
print(li_list)
print(len(li_list))