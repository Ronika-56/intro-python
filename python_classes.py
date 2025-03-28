from python_classes2 import Cylinder
from python_classes3 import Account


class Person:
    def __init__(self ,name ,age):
        print("Creating a person")
        self.name = name
        self.age = age

    def say_hello(self):
         print(f"Hello,Iam {self.name} and I am {self.age} years old")

p1 = Person(name="John", age=28)
p2 = Person(name="Tamar", age=18)
p3 = Person(name="Rose", age=19)

p1.say_hello()
p2.say_hello()
p3.say_hello()

name ="Dan"
name.upper()

c1 = Cylinder(10 ,32)
c2 = Cylinder(66.5 ,84)


c1.area()
c1.volume()

acc1 = Account("0001" ,"Dan Kimani" ,90000)
acc2 = Account("0002","Jane Clare" ,56000)


acc2.deposit(1000)
acc2.check_balance()
acc2.withdraw()
acc2.check_balance()




















