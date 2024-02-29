# 打开文件，以读取模式打开
f = open("D:\word.txt","r",encoding= "UTF-8")


# 方式1 读取全部内容，通过count方法统计itheima单词数量
# content = f.read()
# count = content.count("itheima")
# print(f"itheima在文件中出现了:{count}次")

# 方法2：读取内容:一行一行读取
count = 0
for line in f:
    line = line.strip()     #取出开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word =="itheima":
            count +=1

print(f"itheima出现的次数是{count}")

# 关闭文件
f.close()
