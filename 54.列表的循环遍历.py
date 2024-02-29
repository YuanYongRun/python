"""
演示list列表的循环，使用while和for循环两种方式
"""

def list_while_func():
    """
    使用while循环遍历列表
    :return: None
    """
    my_list = ["传智教育","黑马程序员","Python"]
    # 循环控制变量通过下表索引来控制
    # 每一次循环将下表索引加1
    # 循环条件：下表索引变量<列表元素变量

    #定义一个变量用来标记列表下标
    index = 0
    while index < len(my_list):
        # 通过index变量取出对应下表元素
        element = my_list[index]
        print(f"列表的元素:{element}")

        #至关重要 循环变量index取出对应的下标元素
        index += 1

list_while_func()

def list_for_func():
    """
    for循环进行遍历
    :return: None
    """
    my_list = ["传智教育", "黑马程序员", "Python"]
    for element in my_list:
        print(f"列表的元素是{element}")

list_for_func()