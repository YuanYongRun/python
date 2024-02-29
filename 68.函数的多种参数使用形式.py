def user_info(name,age,gender):
    print(f"姓名:{name},年龄:{age},性别:{gender}")

# 位置参数
user_info("小明",20,"男")


# 关键字参数
user_info(name="小王",age = 11,gender= "女孩")

# 混合参数
user_info("恬恬",gender="女",age =9)


# 缺省参数 默认值只能在最后
def user_info(name,age,gender = "男"):
    print(f"姓名:{name},年龄:{age},性别:{gender}")

user_info("小王",18)
user_info("小王",18,"女")

# 不定长 位置不定长 *
#不定长定义的形式参数会作为元组存在
def user_info(*args):
    print(f"arg的类型是{type(args)},内容是{args}")


user_info(1,2,3,"小明","男孩")


#不定长 关键字不定长 **号
def user_info(**args):
    print(f"arg参数的类型是:{type(args)},内容是:{args}")

user_info(name = "小王",age = 13,gender = "男")