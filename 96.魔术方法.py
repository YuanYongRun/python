class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __定义魔术方法
    def __str__(self):
        return f"Student的类对象,name:{self.name},age:{self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age <other.age


    # __le__魔术方法
    def __le__(self,other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("周杰伦",31)
stu2 = Student("周结论",31)

print(stu1)
print(str(stu1))
print(stu1 < stu2)

print(stu1 <= stu2)

print(stu1 == stu2)

