"""
使用type()获取数据类型
"""

# 1.在print语句中，直接输出类型信息
print(type("黑马程序员"))
print(type(666))
print(type(13.14))

# 2.用变量存储type()的结果(返回值)
string_type=type("黑马程序员")
int_type=type(666)
float_type=type("13.14")
print(string_type)
print(int_type)
print(float_type)

#3.使用type()语句，查看变量存储的类型
name="黑马程序员"
name_type=type(name)
print(name_type)

