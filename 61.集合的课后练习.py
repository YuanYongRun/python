my_list = ["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","best"]

# 定义空集合
my_set = set()

# 通过for循环遍历列表
for element in my_list:
    my_set.add(element)

# 最终得到元素去重后的集合对象，并打印输出
print(f"列表的内容是:{my_list}")
print(f"通过for循环后，得到的集合对象是{my_set}")