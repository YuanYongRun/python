# 通过键盘输入获取身高数据
height = int(input("请输入你的身高(cm):"))
# 通过 if -else进行判断
if height >=120:
    print("你的身高大于120cm,需要买票，10元")
else:
    print("你的身高低于120cm,不需要买票")