#定义函数func_b
def fun_b():
    print("-----2")

# 定义函数func_a
def fun_a():
    print("-----1")

    # 嵌套循环fun_b
    fun_b()

    print("-----3")

#调用函数fun_a
fun_a()