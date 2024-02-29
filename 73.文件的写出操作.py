# 打开文件,不存在的文件
import time

f = open("D:/test.txt","w",encoding = "UTF-8")
# write写入
f.write("HEllo world2")

# flush刷新
f.flush()

g = open(r"D:/test.txt","r",encoding="utf-8")
print(g.read())
# 关闭
f.close()

# 打开一个存在的文件  //会把之前的内容覆盖掉
# f = open("D:/test.txt","w",encoding="UTF-8")
# f.write("黑马程序员")
# f.flush()
# f.close()