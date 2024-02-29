# 获取范围在1-100的随机数字
import  random
num = random.randint(1,1000)
count =0
# 通过一个bool类型变量，做循环是否继续的标记
flag = True
while flag:
    get_num = int(input("请输入你猜测的数字:"))
    count += 1
    if get_num == num:
        print("猜中了")
        # 将flag设置为false是终止条件
        flag=False
    else:
        if get_num > num:
            print("你猜的太大了")
        else:
            print("猜的太小了")
print(f"你总共猜测了{count}次")