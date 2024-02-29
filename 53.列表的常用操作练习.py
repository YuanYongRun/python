# 1.定义这个列表，并用变量接收他

mylist = [21,25,21,23,22,20]

# 2.追加一个数字
mylist.append(31)

# 3.追加一个新列表[29,33,30]
mylist.extend([29,33,30])

# 4.取出第一个元素
num1 = mylist[0]
print(f"从列表中取出来的第一个元素，应该是21，实际上是:{num1}")

# 5.取出最后一个元素
num2 = mylist[-1]
print(f"从列表中取出来的最后一个元素，应该是30，实际上是:{num2}")

# 6.查找元素31，在列表的下标位置
index = mylist.index(31)
print(f"元素31在列表的下表位置是{index}")
print(f"最后列表的内容是{mylist}")