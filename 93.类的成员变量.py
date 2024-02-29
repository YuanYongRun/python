2# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好呀，我是{self.name},欢迎大家多多关照")

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")



stu1 = Student()

stu1.name = '周杰伦'
stu1.say_hi2("哎哟，不错哟")


stu2 = Student()

stu2.name = '林俊杰'
stu2.say_hi2("小伙子，我看好你")

stu3 = Student()
stu3.name="王力宏"
stu3.say_hi()



