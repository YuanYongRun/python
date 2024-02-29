# 打开文件
import time

F = open("D:\测试.txt","r",encoding= "UTF-8")
print(type(F))

# 读取文件 read()
# print(f"读取10字节的结果:{F.read(10)}")
# print(f"读取全部内容的结果:{F.read()}")

# 读取文件 readlines()
lines = F.readlines()   #读取文件的全部行，封装全部行
print(f"Line的对象的类型是:{type(lines)}")
print(f"line的内容是:{lines}")
print(lines[0])

# 读取文件 - readline()
# line1 = F.readline()
# line2 = F.readline()
# line3 = F.readline()
# print(f"第一行:{line1}")
# print(f"第二行:{line2}")
# print(f"第三行:{line3}")
# i = 0
# while i <3:
#     line = F.readline()
#     print(line)
#     i = i+1

# 利用for循环读文件
for i in F:
    print(f"每一行的数据；{i}")

# 文件的关闭
# F.close()

# with open 语法  会自动关闭文件
with open("D:\测试.txt","r",encoding= "UTF-8") as f:
    print(f.readlines())
#     for line in f:
#         print(f"每一行的数据；{line}")