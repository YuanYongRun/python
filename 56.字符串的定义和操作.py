# 通过下表索引取值(不能修改，只能取值）
my_str = "itheima and itcast"
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值为{value},取下标为-16的元素，值为{value2}")

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and,起始下标是:{value}")

# replace方法
new_my_str = my_str.replace("it","程序")
print(f"将字符串{my_str}，进行替换后得到{new_my_str}")

# split分割
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切割后得到:{my_str_list}")

# strip 方法
my_str = "   itheima and cast   "
new_my_str = my_str.strip()
print(f"将字符串{my_str}进行strip后得到:{new_my_str}")


my_str = "12itheima and cast12"
new_my_str = my_str.strip("12")
print(f"将字符串{my_str}进行strip后得到:{new_my_str}")

# 统计字符串中某个字符串出现的次数
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是:{count}")

# 统计字符串的长度
num = len(my_str)
print(f"{my_str}的长度是:{num}")

