# 打开文件，不存在的文件
f = open("D:/test.txt","a",encoding="UTF-8")
# write写入，flush刷新
f.write("\n学python的最佳选择")
f.write("\n月薪过万")
f.close()
