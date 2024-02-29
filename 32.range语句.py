""""
演示 Python中的range()语句的基本使用
"""

# range语法1 range(num)
for x in range(10):
    print(x)

# range语法2 range(num1,num2)
for x in range(5,10):
    print(x)


# range语法3 range(num1,num2,step)
for x in range(5,10,2):
    # 从5开始，到10结束(不包含10本身)的一个数字系列，数字之间间隔为2
    print(x)


for i in range(10):
    print("送玫瑰花")