my_dict = {"周杰伦":99,"林俊杰":88,"张学友":77}
# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果是{my_dict}")

# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新后的结果是:{my_dict}")

# 删除元素
score = my_dict.pop("周杰伦")
print(f"字典中被移除了一个元素，结果是{my_dict},周杰伦的分数是{score}")

# 清空元素
my_dict.clear()
print(f"字典被清空了，内容是{my_dict}")

# 获取全部的key
my_dict = {"周杰伦":99,"林俊杰":88,"张学友":77}
keys = my_dict.keys()
print(f"字典的全部key是:{keys}")

# 遍历字典
# 方式1
for key in keys:
    print(f"字典的key是{key}")
    print(f"字典的value是:{my_dict[key]}")

# 方式2
for key in my_dict:
    print(f"2字典的key是:{key}")
    print(f"2字典的value是:{my_dict[key]}")

# 统计字典的元素数量
num = len(my_dict)
print(f"字典中的元素数量是:{num}个")