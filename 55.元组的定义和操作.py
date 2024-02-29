# 定义元组
t1 = (1,"hell0",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是:{type(t1)},内容是{t1}")
print(f"t2的类型是:{type(t2)},内容是{t2}")
print(f"t3的类型是:{type(t3)},内容是{t3}")


# 定义单个元素的元组
t4 = ("hello",)
print(f"t4的类型是:{type(t4)},内容是{t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是:{type(t5)},内容是{t5}")

# 下表索引取出内容
num = t5[1][2]
print(f"从嵌套元素中取出的数据:{num}")

# 元组的操作
t6 = ("传智教育","黑马程序员","Python")
index = t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序员的下标是{index}")

# 元组的操作:count的统计方法
t7 = ("传智教育","黑马程序员","黑马程序员","黑马程序员","Python")
num = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有{num}个")

# 元组的操作
t8 = ("传智教育","黑马程序员","黑马程序员","黑马程序员","Python")
num = len(t8)
print(f"t8的元组中元素个数有{num}个")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有:{t8[index]}")
    index += 1

# 元组的遍历:for
for element in t8:
    print(f"2元组的元素有:{element}")


# 修改元组内容 直接修改元组内容不行，但是可以修改元组中嵌套的list容器
# t8[0] = "itcast"
t9 = (1,2,["itheima","itcast"])
print(f"t9的内容是:{t9}")
t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
print(f"t9的内容是:{t9}")
