'''
An explanation of the argument 'self' in classes
-------------------------------------------------
Many instances can be created from the same class (instantiation)
    eg instance = class()

to identify the different instances when calling a method on an instance the instance itself is passed as an argument
to the method... as follows:

            class ex_class():
                def ex_method(self):
                    pass

            my_instance = ex_class()
            my_instance.ex_method(instance)       <--- we dont need to use instance.. this is what python does

instance is effectively passed to self.  However we dont need to specify "instance". it is implied by python.
However if we dont specify "self" as a parameter in method in a class an error will be produced as follows:

            TypeError: ex_method() takes 0 positional arguments but 1 was given

what follows is a program that demonstrates that "self" = object instance
'''


class Arith():
    w = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition():
        print(self, "         <------- prints 'self' which is the same as instance above [so self = instance]")
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y


a = Arith(10, 5)
print(a, "         <------- Instance comprising <class_module>.<class_name> + memory")
print(a.w)
print(a.addition())
print(a.subtraction())

b = Arith(10, 5)
print(b, "         <------- Instance comprising <class_module>.<class_name> + memory")
print(b.w)
print(b.addition())
print(b.subtraction())


'''
if class is defined in the __main__ module then <class_module> = __main__
    eg  <__main__.Arith object at 0x00716850> 

if class is defined in an imported module then <class_module> = module name
    eg  from app1 import Arith
        <app1.Arith object at 0x030AEBB0>

'''
