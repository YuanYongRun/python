my_str = "itheima itcast boxuegu"

# 统计字符串内有多少个it字符
count = my_str.count("it")
print(f"字符串{my_str}中it的字符个数为{count}")


# 将字符串内的空格，全部替换为字符"|"
new_my_str = my_str.replace(" "," |")
print(f"字符串{my_str}被替换空格后，结果是{new_my_str}")

# 并按照|进行字符串分割，得到列表
my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}进行分割后的结果是{my_str_list}")