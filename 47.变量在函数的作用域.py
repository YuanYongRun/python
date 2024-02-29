# 演示局部变量
# def test_a():
#     num = 100
#     print(num)
#
# test_a()
# 出了函数就不能使用了
# print(num)

# 定义全局变量
# num = 200
# def test_n():
#     print(num)
#
# def test_m():
#     print(num)
#
# test_n()
# test_m()
# print(num)

# 在函数内修改全局变量
# num = 200
# def test_a():
#     print(f"test_a:{num}")
# #
#
# def test_b():
#     # global 关键字
#     global num # 设置内部定义的变量为全局变量
#     num = 500  #局部变量
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)