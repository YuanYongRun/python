"""
演示模块的导入
"""

# 使用import导入time模块使用sleep功能
# import time
# print("你好")
# time.sleep(5)   # 通过.可以使用模块内置的全部功能(类、函数)
# print("我好")

# 使用from导入time的sleep功能
# from time import  sleep
# print("你好")
# sleep(5)
# print("我好")


# 使用 *导入time模块内部的所有功能
# from time import  *
# print("开始")
# sleep(5)
# print("结束")

# 使用as 给特定功能加别名
# import time as t
# print("开始")
# t.sleep(5)
# print("结束")

from time import sleep as sl
print("开始")
sl(5)
print("结束")