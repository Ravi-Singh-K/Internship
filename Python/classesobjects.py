# class MyClass:      # MyClass is the name of class
#     x = 5           # x is the property of MyClass

# p1 = MyClass()      # p1 is the object of MyClass
# print(p1.x)         # object is used to access property of MyClass

# class Animal:
#     x = 6
# class Dog(Animal):
#     y = 9
# d1 = Dog()
# print(d1.x)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Man(Person):
#     def bodyType(self):
#         print("Muscular")
# m = Man("Hello", 45)
# print(m.name, m.age)
# m.bodyType()

# # Using __init__() to assign values for name and age:
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# h1 = Human("Ravi", 27)
# print(h1.name)
# print(h1.age)


# # With and without __str__():
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Human("John", 29)
# print(p1)

# # With __str__()
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} ({self.age})"
# p1 = Human("John", 36)
# print(p1)


# # Object methods
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunction(self):
#         print("Hello my name is " + self.name)
# p = Person("Ravi", 25)
# p.myfunction()


# # using custom 'self' parameter
# class Person:
#     def __init__(ranger, number):
#         ranger.number = number
#     def myFunc(ranger):
#         if ranger.number % 2 == 0:
#             print("The square of the number is ", ranger.number ** 2)
#         else:
#             print("The double of the number is ", ranger.number * 2)
# p = Person(24)
# p.number = 35    # Modifying object property
# p1 = Person(66)
# p1.myFunc()
# del p     # Deletes the object called ' p '
# # p.myFunc()   #  'p' object is not defined



# Using ' pass ' statement to avoid getting error
# class AvoidError:
#     pass


# Class variable and Instance variable
# class Dog:
#     animal = 'Dog'    # Class Variable
#     def __init__(self, breed, color):
#         self.breed = breed    # Instance variables
#         self.color = color

# # Objects of the class
# Rodger = Dog("Pug", "Brown")
# Buzo = Dog("Bulldog", "Black")

# print("Rodger details : ")
# print("Rodger is a ", Dog.animal)    # Accessing using class name
# print("Breed : ", Rodger.breed)
# print("Color : ", Rodger.color)

# print()

# print("Buzo details : ")
# print("Buzo is a ", Buzo.animal)    # Accessing using object
# print("Breed : ", Buzo.breed)
# print("Color : ", Buzo.color)


# Defining instance variables using normal method
# class Dog:
#     animal = 'Dog'

#     def __init__(self, breed):
#         self.breed = breed
    
#     def setColor(self, color):
#         self.color = color
    
#     def getColor(self):
#         return self.color
    
# Rodger = Dog("Pug")
# Rodger.setColor("White")
# print(Rodger.getColor())



# # Instance Method Example
# class Dog:
#     species = "Canis Familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name} is {self.age} years old."
    
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
    
# d = Dog("Rocky", 19)
# print(d.speak("Woof Woof"))
# print(d)

# class Person(Dog):
#     def __init__(self, name, age, address, position):
#         super().__init__(name, age)
#         self.position = position

# obj1 = Person("Ravii",25,"Swoyambhu","CEO")
# print(obj1.name, obj1.age, obj1.position)


# class Greeter:
#     def __init__(self, name, formal=False):
#         self.name = name
#         self.formal = formal
    
#     def greet(self):
#         if self.formal:
#             print(f"Goodmorning, {self.name} !")
#         else:
#             print(f"Hello, {self.name} !")

# g = Greeter("Ravi", True)
# g.greet()


# Inheritance example
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)
        # pass

class Student(Person):  # Child class that inherits Person class
    # def __init__(self, fname, lname, year):   # Overrides the parent's init function
    #     # Person.__init__(self, fname, lname)  # call to the parent's init function
    #     super().__init__(fname, lname)
    #     self.graduationyear = year

    def printname(self):
        return super().printname()
    
x = Student("Ravi", "Singh")
# print(x.graduationyear)
x.printname()


# # Demonstration of single inheritance
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
# obj = Child()
# obj.func1()
# obj.func2()


# # Demonstration of Multiple Inheritance
# # BASE CLASS 
# class Father:
#     fathername = ""
#     def father(self):
#         print(self.fathername)

# # BASE CLASS
# class Mother:
#     mothername = ""
#     def mother(self):
#         print(self.mothername)

# # DERIVED CLASS
# class Son(Father, Mother):
#     def __init__(self, sonname):
#         self.sonname = sonname
#     def parents(self):
#         print("Father : ", self.fathername)
#         print("Mother : ", self.mothername)
#         print("Son : ", self.sonname)

# # object of DERIVED CLASS : SON
# s = Son("Ravi")
# s.fathername = "Ram"
# s.mothername = "Rama"
# s.parents()



# # Demonstration of MULTI LEVEL INHERITANCE
# # BASE CLASS
# class Grandfather:
#     def __init__(self, grandfather):
#         self.grandfather = grandfather
    
# # INTERMEDIATE CLASS
# class Father(Grandfather):
#     def __init__(self, father, grandfather):
#         super().__init__(grandfather)
#         self.father = father

# # CHILD CLASS
# class Son(Father):
#     def __init__(self, son, father, grandfather):
#         super().__init__(father, grandfather)
#         self.son = son
    
#     def printNames(self):
#         print("Grandfather : ", self.grandfather)
#         print("Father : ", self.father)
#         print("Son : ", self.son)

# s = Son("Ravi", "Ram", "Bekha")
# s.printNames()


# # DEMONSTRATION OF HIERARCHICAL INHERITANCE
# class Parent:
#     def func1(self):
#         print("Parent Function")
# class Child1(Parent):
#     def func2(self):
#         print("Child 1 Function")
# class Child2(Parent):
#     def func3(self):
#         print("Child 2 Function")
# o1 = Child1()
# o2 = Child2()
# o1.func1()
# o1.func2()
# o2.func1()
# o2.func3()



# #  DEMONSTRATION OF HYBRID INHERITANCE
# class F:
#     def func1(self):
#         print("F function")
# class G:
#     def func2(self):
#         print("G Function")
# class E(F, G):
#     def func3(self):
#         print("E function from F and G")
# class B(F):
#     def func4(self):
#         print("B function from F")
# class A(B, F):
#     def func5(self):
#         print("A function from B and F")
# class C(B, F):
#     def func6(self):
#         print("C function from B and F")

# OE = E()
# OE.func1()
# OE.func2()
# OE.func3()
# oa = A()
# oa.func1()
# oa.func4()
# oa.func5()
# oc = C()
# oc.func1()
# oc.func4()
# oc.func6()
# ob = B()
# ob.func1()
# ob.func4()


# # super() in inheritance
# class Animal:
#     name = ""
#     def eat(self):
#         print("I can eat")
# class Dog(Animal):
#     def eat(self):
#         super().eat()  # Access the eat() of Parent class
#         print("I like to eat Bones")
# lab = Dog()
# lab.eat()  # access eat() of Animal and Dog class



# # Multiple and Multi level inheritance
# class A:
#     def __init__(self, a_name):
#         self.a_name = a_name
#     def get_a(self):
#         print(self.a_name)
# class B(A):
#     def __init__(self, a_name, b_name):
#         self.b_name = b_name
#         A.__init__(self,a_name)
#     def get_b(self):
#         print(self.b_name)
# class C(A):
#     def __init__(self, a_name, c_name):
#         self.c_name = c_name
#         A.__init__(self,a_name)
#     def get_c(self):
#         print(self.c_name)
# class D(B,C):
#     def __init__(self, a_name, b_name, c_name, d_name):
#         self.d_name = d_name
#         B.__init__(self,a_name, b_name)
#         C.__init__(self,a_name, c_name)
#     def get_d(self):
#         print(self.d_name)
# names = D("Apple", "Ball", "Cartoon", "Dance")
# names.get_a()
# names.get_b()
# names.get_c()
# names.get_d()

# # Diamond Problem
# class A:
#     def greet(self):
#         print("Hello From Parent")
# class B(A):
#     def greet(self):
#         print("Hello from CHILD B")
#         super().greet()
# class C(A):
#     def greet(self):
#         print("Hello from CHILD C")
#         super().greet()
# class D(B,C):
#     def greet(self):
#         print("Hello from CHILD D")
#         super().greet()
# d = D()
# d.greet()