"""
演示数据容器的通用功能
"""

my_list = [1,2,3,4,5,6]
my_tuple = (1,2,3,4,5,6)
my_str = "abcdefg"
my_set = {1,2,3,4,5,6}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}

# len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

# max函数
print(f"列表最大元素：{max(my_list)}")
print(f"元组最大元素：{max(my_tuple)}")
print(f"字符串最大元素：{max(my_str)}")
print(f"集合最大元素：{max(my_set)}")
print(f"字典最大元素：{max(my_dict)}")

# min函数
print(f"列表最小元素：{min(my_list)}")
print(f"元组最小元素：{min(my_tuple)}")
print(f"字符串最小元素：{min(my_str)}")
print(f"集合最小元素：{min(my_set)}")
print(f"字典最小元素：{min(my_dict)}")


# 类型转换:容器转列表
print(f"列表转列表：{list(my_list)}")
print(f"元组转列表：{list(my_tuple)}")
print(f"字符串转列表：{list(my_str)}")
print(f"集合转列表：{list(my_set)}")
print(f"字典转列表：{list(my_dict)}")

# 容器转元组
print(f"列表转元组：{tuple(my_list)}")
print(f"元组转元组：{tuple(my_tuple)}")
print(f"字符串转元组：{tuple(my_str)}")
print(f"集合转元组：{tuple(my_set)}")
print(f"字典转元组：{tuple(my_dict)}")

# 容器转字符串
print(f"列表转字符串：{str(my_list)}")
print(f"元组转字符串：{str(my_tuple)}")
print(f"字符串转字符串：{str(my_str)}")
print(f"集合转字符串：{str(my_set)}")
print(f"字典转字符串：{str(my_dict)}")

# 容器转集合
print(f"列表转集合：{set(my_list)}")
print(f"元组转集合：{set(my_tuple)}")
print(f"字符串转集合：{set(my_str)}")
print(f"集合转集合：{set(my_set)}")
print(f"字典转集合：{set(my_dict)}")


my_list = [1,2,3,4,5,6]
my_tuple = (1,2,3,4,5,6)
my_str = "abcdefg"
my_set = {1,2,3,4,5,6}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}

# sorted排序 结果会变成列表对象
print(f"列表对象排序结果:{sorted(my_list)}")
print(f"元组对象排序结果:{sorted(my_tuple)}")
print(f"字符串对象排序结果:{sorted(my_str)}")
print(f"集合对象排序结果:{sorted(my_set)}")
print(f"字典对象排序结果:{sorted(my_dict)}")


# 反向排序
print(f"列表对象排序结果:{sorted(my_list,reverse=True)}")
print(f"元组对象排序结果:{sorted(my_tuple,reverse=True)}")
print(f"字符串对象排序结果:{sorted(my_str,reverse=True)}")
print(f"集合对象排序结果:{sorted(my_set,reverse=True)}")
print(f"字典对象排序结果:{sorted(my_dict,reverse=True)}")


