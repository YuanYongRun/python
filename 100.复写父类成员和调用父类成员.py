class Phone:
    IMEI = None
    producer = "TICAST"

    def call_by_5g(self):
        print("父类的5G通话")


# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("子类的5G通话")
        # 调用父类的
        # print(f"父类的厂商是{Phone.producer}")
        # Phone.call_by_5g(self)   
        print(f"父类的厂商是:{super().producer}")
        super().call_by_5g()

my_phone = MyPhone()
print(my_phone.producer)
my_phone.call_by_5g()



