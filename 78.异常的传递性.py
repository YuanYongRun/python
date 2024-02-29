# 定义一个出现异常的方法:
def func_1():
    print("func1 开始执行")
    num =1 /0
    print("func1 结束执行")

# 定义一个无异常的方法，调用上面的方法

def func_2():
    print("func_2开始执行")
    func_1()
    print("func_2结束执行")

def main():
    try:
        func_2()
    except Exception as e:
        print(f"出现异常了，异常的信息是{e}")

main()