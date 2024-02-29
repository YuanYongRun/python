# 创建my_utils包，在包内创建:str_util.py和file_util.py2个模块，并提供相应的函数

import  my_util.str_util
from my_util import file_util
print(my_util.str_util.str_reverse("黑马程序员"))
print(my_util.str_util.substrs("itheima",0,4))


file_util.append_to_file("D:/test_append.txt","itheima")
file_util.print_file_info("D:/test_append.txt")