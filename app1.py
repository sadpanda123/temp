class Arith():
    w = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        print(self)
        return self.x + self.y

    def subtraction(self):
        print(self)
        return self.x - self.y


a = Arith(10, 5)
print(a)
print(a.w)
print(a.addition())
print(a.subtraction())

b = Arith(10, 5)
print(b)
print(b.w)
print(b.addition())
print(b.subtraction())



