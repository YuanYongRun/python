# 定义 一个变量数字
num =5
# 通过键盘输入获取猜想的数字，通过多次if和elif组合

if int(input("请猜猜一个数字")) == num:
    print("恭喜你一次猜对了")
elif int(input("猜错了，再猜一次")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次")) == num:
    print("恭喜，最后一次机会，猜对了")
else:
    print("Sorry，猜错了")