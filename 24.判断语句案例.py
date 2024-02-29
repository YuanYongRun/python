# 构建一个随机的数字变量
import random
num = random.randint(1,100)

guess_num = int(input("输入你要猜想的数字:"))

# 通过if判断语句进行数字的猜测
if guess_num == num:
    print("恭喜，第一次猜中")
else:
    if guess_num >num:
        print("你猜测的数字大了")
    else:
        print("你猜的数字小了")
    guess_num = int(input("输入你要猜想的数字:"))

    if guess_num ==num:
        print("恭喜，第二次猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜的数字小了")
        guess_num = int(input("输入你要猜想的数字:"))

        if guess_num == num:
            print("恭喜，第三次猜中了")
        else:
            print("三次机会已经用完")