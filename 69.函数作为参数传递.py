# 定义一个函数
def test_func(compute,x,y):
    result = compute(x,y)
    print(f"结果是{result},compute类型是{type(compute)}")

# 定义一个函数，准备作为参数传入另外一个函数
def compute(x,y):
    return x + y

test_func(compute,4,5)