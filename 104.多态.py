"""
以父类做定义声明
以子类做实际工作
以获得统一行为，不同状态
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal:Animal):
    # 制造点噪音,传入Animal对象
    animal.speak()


# 演示多态
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

# 演示抽象类
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing_l_r(self):
        print("美的空调左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac =Midea_AC()
gree_ac = GREE_AC()
make_cool(midea_ac)
make_cool(gree_ac)
