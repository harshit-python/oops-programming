"""
Instance methods are used to work with instance attributes
Class methods are used to work with class attributes
Static methods are used for utility functions that don't require access to instance or class attributes
"""

# instance method
class MyClass1:
    def instance_method(self):
        print("This is an instance method")

obj1 = MyClass1()
obj1.instance_method()

# class method
class MyClass2:
    class_variable = "class variable"

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(cls.class_variable)

obj2 = MyClass2()
obj2.class_method()

# static method
class MyClass3:
    @staticmethod
    def static_method():
        print("This is a static method")

obj3 = MyClass3()
obj3.static_method()