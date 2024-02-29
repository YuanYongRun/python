# 定义集合
my_set = {"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
my_set_empty = set()
print(f"my_set的内容是:{my_set},类型是:{type(my_set)}")
print(f"my_set_empty的内容是:{my_set_empty},类型是:{type(my_set_empty)}")

# 集合是无序的，无法使用下表索引去访问
# 添加新元素
my_set.add("python")
my_set.add("传智教育") # 被去重
print(f"my_set添加元素后的内容是:{my_set},类型是:{type(my_set)}")

# 移除元素
my_set.remove("黑马程序员")
print(f"my_set移除黑马程序员后的内容是:{my_set},类型是:{type(my_set)}")

# 随机取一个元素
my_set = {"传智教育","黑马程序员","itheima","传智教育"}
element = my_set.pop()
print(f"集合被取出的元素是:{element},取出元素后:{my_set}")

# 清空集合
my_set.clear()
print(f"集合被清空的结果是:{my_set}")

# 集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出的差集后的结果:{set3}")
print(f"取出差集后的set1的内容是{set1}")
print(f"取出差集后的set2的内容是{set2}")

# 消除差集
set1.difference_update(set2)
print(f"消除差集后set1的结果是:{set1}")
print(f"消除差集后set2的结果是:{set2}")

# 2个集合合并
set3 = set1.union(set2)
print(f"两个集合合并后的结果是{set3}")

# 统计集合的元素
num1 = len(set1)
num2 = len(set2)
print(f"集合1的元素数量有{num1}")
print(f"集合2的元素数量有{num2}")

# 集合的遍历  集合不支持下标索引，所以不能用while循环
for element in set3:
    print(element)