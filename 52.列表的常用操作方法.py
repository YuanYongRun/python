"""
演示数据容器之list列表的常用操作
"""

my_list = ["itheima","itcast","python"]
# 1.1查找某元素在列表内的下表索引

index = my_list.index("itheima")
print(index)

# 1.2如果被查找的元素不存在，会报错
# index = my_list.index("hello")
# print(index)

# 2.修改特定下标索引的值
my_list[0] = "传智教育"
print(f"列表修改后，结果是{my_list}")

# 3.在指定下标位置插入新元素
my_list.insert(1,"best")
print(f"列表插入元素后，结果是{my_list}")


# 4.在列表的尾部追加"单个元素"
my_list.append("黑马程序员")
print(f"列表在追加了元素之后，结果是{my_list}")

# 5.在列表的尾部追加一批元素
mylist2 = [1,2,3]
my_list.extend(mylist2)
print(f"列表在追加了新的一批列表之后，结果是{my_list}")

# 6.删除指定的下表索引元素
del my_list[2]
print(f"列表删除元素后结果是{my_list}")


my_list = ["itheima","itcast","python"]
elemnet = my_list.pop(2)
print(f"通过pop方法取出元素后的列表内容:{my_list},取出的元素是{elemnet}")

# 7.删除某元素在列表的第一个匹配项
my_list = ["itheima","itcast","itheima","itcast","python"]
my_list.remove("itheima")
print(f"通过remove方法移除元素后，列表的结果是:{my_list}")

# 8.清空列表
my_list.clear()
print(f"列表被清空了，结果是{my_list}")

# 9.统计列表内某元素的数量
my_list = ["itheima","itcast","itheima","itcast","python"]
count = my_list.count("itheima")
print(f"列表中itheima的数量是:{count}")

# 10.统计列表中总共有多少元素
my_list = ["itheima","itcast","itheima","itcast","python"]
count = len(my_list)
print(f"列表的元素总量有{count}个")

