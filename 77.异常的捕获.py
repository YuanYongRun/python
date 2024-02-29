"""
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""

# 基本捕获语法
try:
    f = open("D:/abc.txt","r",encoding="UTF-8")
except:
    print(f"出现异常了，因为文件不存在，将制度模式改为w模式去打开")
    f = open('D:/abc.txt',"w",encoding="UTF-8")


#  捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未定义 或者 除以0的异常错误")

# 未正确奢姿捕获异常类型，将无法捕获异常

# 捕获所有异常
try:
    print("HELLO")
except Exception as e:
    print("出现异常了")
else:
    print("好高兴，没有异常")
    

# finally表示的是无论是否异常都执行都要执行
try:
    f = open("D:/123.txt","r",encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    f = open("D:/123.txt", "w", encoding="UTF-8")
else:
    print("好高兴，没有异常")
finally:
    print("我是finally，有没有异常我都要执行")
    f.close()