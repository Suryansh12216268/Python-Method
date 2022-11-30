class student:
    def method1(selfself, name = None, wish = None):
        print(name,wish)
obj1 = student()
obj1.method1()
obj1.method1("Ram")
obj1.method1("Ram", "Good Morning")

class parent:
    def method2(self):
        print("Parent")
class child(parent):
    def method1(self):
        print("Child")

obj1 = child()
obj1.method1()
obj1.method2()

class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal): #derived class name(parent)
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()

class DogChild(Dog):
    def eat(self):
        print("Eating Bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()

class Calculation1:
    def Summation(self,a,b):
        return a+b
class Calculation2:
    def Multiplication(self,a,b):
        return a*b
class Derived(Calculation1, Calculation2): # Multiple Ingheritance
    def Divide(self,a,b):
        return a/b
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(100,200))
print(d.Divide(100,20))

class Animal:
    def speak(self):
        print("speaking")
class Dog(Animal):
    def speak(self):
        print("Barking")
d = Dog()
d.speak()
a = Animal()
a.speak()

class SuperClass:
    x  = 3
class SubClass1(SuperClass):
    pass
class SubClass2(SuperClass):
    pass
class SubClass3(SuperClass):
    pass
a = SubClass1()
b = SubClass2()
c = SubClass3()
print(a.x, b.x, c.x)


class one:
    x = 20
    def fun1(self):
        print(self.x)
class two(one):
    y = 200
    def fun2(self):
        print(one.x+self.y)
t1 = two()
t1.fun1()
t1.fun2()


a = None
b = None
c = None
def data(self):
    input.a = int(input('enter a'))
    input.b = int(input('enter b'))

class Sum(input()):
    def add(self):
        input.c = input.a + input.b
        print(input.c)
class Avg(Sum):
    def av(self):
        print((input.c)/2)
d = Avg()
d.data()
d.add()
d.av()








