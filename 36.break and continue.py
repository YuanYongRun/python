"""
演示循环语句的中断控制
"""

# 演示循环中断语句 continue
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")


# 演示continue的嵌套运用
for i in range(1,6):
    print("语句1")
    for j in range (1,6):
        print("语句2")
        continue
        print("语句3")

    print("语句4")



# 演示循环中断语句 break
for i in range(1,101):
    print("语句1")
    break
    print("语句2")
print("语句3")


# 演示break的嵌套运用
for i in range (1,6):
    print("语句1")
    for j in range (1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")