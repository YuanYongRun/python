# 定义私有成员的方式:变量名只需要__开头,方法名__开头

class Phone:
    __current_voltage = 0.5  #当前运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >=1:
            print("5G通话已经开启")
        else:
            self.__keep_single_core()
            print("电量不足，已经设置为单核模式运行并省电。")



phone = Phone()
# Phone.__keep.single.core
# print(phone.__current_voltage)
phone.call_by_5g()