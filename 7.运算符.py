"""
演示Python中的各类运算符
"""

# 算术(数学)运算符
print("1 + 1 =",1+1)
print("1 - 1 =",1-1)
print("3 * 3 =",3*3)
print("4 / 2 =",4/2)
print("9 % 2 =",9%2)
print("11 // 2 =",11//2)
print("2 ** 2 =",2**2)

#赋值运算符
num =1 + 2 * 3

# 复合赋值运算符
num = 1
num += 1   # num =num + 1
print("num +=",num)
num -= 1
print("num -=",num)
num *= 4
print("num *=",num)
num = 3
num %= 2
print("num %=",num)

num //=2
print("num // =2",num)
