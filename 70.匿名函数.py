# 定义一个函数，接受其他函数的传入
def test_func(compute):
    result = compute(1,2)
    print(f"结果是:{result}")

# 通过lambda匿名函数形式，将匿名函数作为参数传入   无法重复使用，只能使用一次
test_func(lambda x,y:x + y)