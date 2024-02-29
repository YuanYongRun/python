"""
语法：列表[下表索引]
正向索引:0,1,2...
反向索引:-1,-2,-3,-4......
"""

# 正向索引
my_list = ["tom","Lily","Rose"]
print(my_list[0])
print(my_list[1])
print(my_list[2])

# 反向索引
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])


# 取出嵌套的列表的元素
my_list = [[1,2,3],[4,5,6]]
print(my_list[1][1])