# 定义一个全局变量
money = 5000000
name = None

#要求客户输入姓名
name = input("请输入你的姓名")

# 定义查询函数
def query(show_header):
    if show_header:
      print("------查询余额------")
      print(f"{name}，你好，你的余额剩余:{money}元")

# 定义存款函数
def saving(num):
    global  money
    money += num
    print("------存款-------")
    print(f"{name},你好，你存款{num}成功")
    # 调用query函数查询余额
    query(False)

# 定义取款函数
def use(num):
    global  money
    money -= num
    print("------取款-------")
    print(f"{name},你好，你取款{num}成功")
    # 调用query函数查询余额
    query(False)

# 定义主菜单函数
def main():
    print("------主菜单------")
    print(f"{name}，你好，欢迎来到黑马银行ATM，请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入你的选择:")

# 设置无限循环，确保程序不退出
while True:
    keyborad_input = main()
    if keyborad_input == "1":
        query(True)
        continue   # 通过continue继续进行下一次循环
    elif keyborad_input == "2":
        num = int(input("请输入你存款的金额"))
        saving(num)
        query(False)
        continue
    elif keyborad_input == "3":
        num = int(input("请输入你取款的金额"))
        use(num)
        query(False)
        continue
    else:
        print("程序退出啦")
        break