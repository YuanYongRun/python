"""
输出不换行代码
print("hello",end="")

\t 可以对齐
"""
#
# print("hello",end="")
# print("world",end="")

# print("hello world")
# print("itheima best")
#
#
# print("hello\twoeld")
# print("itheima\tbest")

# 定义外层循环
i = 1
while i <= 9:
    #定义内层循环的控制变量
    j=1
    while j <= i :
        #内层循环的语句，不要换行
        print(f"{j}*{i}={j *i}\t",end="")
        j += 1
    i += 1
    print()  #print空内容，输出一个换行