# 设计一个闹钟类
class Clock:
    id = None
    price = None


    def ring(self):
        import winsound
        winsound.Beep(2000,3000)


clock1 = Clock()
clock1.id = "00302"
clock1.price = 19.99
print(f"闹钟id:{clock1.id},价格:{clock1.price}")
clock1.ring()


clock2 = Clock()
clock2.id = "00303"
clock2.price = 19.99
print(f"闹钟id:{clock2.id},价格:{clock2.price}")
clock2.ring()


