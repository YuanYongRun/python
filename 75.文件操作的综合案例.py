# 打开文件得到文件对象，准备读取
fr = open("C:/Users\Administrator\Desktop/bill.txt","r",encoding="UTF=8")


# 打开文件得到文件对象，准备写入
fw = open("C:/Users\Administrator\Desktop/bill.txt.bak","w",encoding="UTF=8")

# for循环读取文件
for line in fr:
    line = line.strip()
    #判断内容，将满足的内容写出
    if line.split(",")[4] == "测试":
        continue
    # 将内容写出去
    fw.write(line)
    # 由于前面内容进行了strip操作，所以要手动写出换行符
    fw.write("\n")

fr.close()
fw.close()
