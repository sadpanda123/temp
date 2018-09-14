class Arith():
    w = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        print(self, "         <------- prints 'self' which is the same as instance above [so self = instance]")
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y


a = Arith(10, 5)
print(a, "         <------- Instance comprising __name__ + class_name + memory")
print(a.w)
print(a.addition())
print(a.subtraction())

b = Arith(10, 5)
print(b, "         <------- Instance comprising __name__ + class_name + memory")
print(b.w)
print(b.addition())
print(b.subtraction())



