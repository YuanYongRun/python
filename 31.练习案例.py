"""
演示for循环的练习题，数一数有几个a
"""

# 统计如下字符串中，有多少个字符串
name = "itheima is a brand of itcast"

# 定义一个计数器
count = 0

# for循环统计
for x in name :
    if x == "a":
        count += 1
print(f"被统计的字符串中有{count}个a")