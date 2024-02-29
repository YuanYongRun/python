# height = int(input("请输入你的身高"))
# vip_level = int(input("请输入你的Vip等级"))
# day = int(input("今天是几号"))
if int(input("请输入你的身高")) <120:
    print("身高小于120cm，不需要买票")
elif int(input("请输入你的Vip等级")) >3:
    print(("vip级别大于3，可以免费。"))
elif  int(input("今天是几号")) ==1:
    print("今天是一号免费日，可以免费")
else:
    print("不好意思，条件均不满足，需要买票10元")