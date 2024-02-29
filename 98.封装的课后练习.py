# 设计一个类，用来描述手机
class Phone:
    # 提供私有成员变量: __is_5G__ enable
    __is_5G__enable = True   # 5g状态

    # 提供私有的成员方法:__check_5G()
    def __check_5G(self):
        if self.__is_5G__enable:
            print("5G模式已打开")
        else:
            print("5G关闭，使用4G网络")


    # 提供公开成员的方法：call_by_5G
    def call_by_5G(self):
        self.__check_5G()
        print("正在通话中")


phone = Phone()
phone.call_by_5G()