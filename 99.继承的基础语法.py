# 演示单继承
class Phone:
    IMEI = None
    producer = "itcast"



    def call_by_4g(self):
        print("4g通话")



class Phone2022(Phone):
    face_id = "1001"   # 面部识别ID

    def call_by_5g(self):
        print("2022新功能:5G通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()



# 演示多继承
class NFC_reader:
    ncf_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_read(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控已开启")


class MyPhone(Phone,NFC_reader,RemoteControl):
    # 不想写什么东西
    pass

my_phone = MyPhone()
my_phone.call_by_4g()
my_phone.read_card()
my_phone.write_read()
my_phone.control()

print(my_phone.producer)  # 若有同名，先继承的优先级高于后继承