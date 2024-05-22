# abs()   convert into positive number
from math import ceil


print(abs(-7.2))   # 7.2
print(abs(7+3j))   # 7.615773105863909

# any() returns true if any element is true 
list1 = [True, True, True]
print(any(list1))

# all() returns true if all elements are true
list2 = [False, True, False]
print(all(list2))

# ascii() returns readable version of any object(string, tuple, list)
print(ascii("Hello World å"))  # Hello World \xe5

# bin() returns binary form of any number with the prefix 0b
print(bin(45))
# print(bin("He")) # cannot return from string

# bool() returns true unless empty, None, False or 0
x = 1
print(bool(x))

# bytearray() returns bytearray
x = 23
print(bytearray(x))

# callable() method checks if the function is callable or not. returns true
def sum():
    x = 5 + 6
print(callable(sum))
x = 5 + 6
print(callable(x))  # x is not callable

# exec() method
x = 'name = "Ravi"\nprint(name)'
exec(x)

# divmod() returns quotient and remainder as tuple 
x = divmod(5,2)  # returns (2, 1)
print(x)

# enumerate() adds index as counter like (0, 'apple')
x = ('apple','apple','ball','cat','dog','ear')
y = enumerate(x)
print(list(y))   # [(0, 'apple'), (1, 'apple')]

# delattr() deletes attribute of the class
class Person:
    name = "Ravi"
    age = 27
    country = "USA"
delattr(Person, 'age')
print(Person.name)
print(Person.country)
# print(Person.age)

# filter() filters the specified content # filter(function, iterable)
age = [2,4,5,77,5,34,23,11]
def myFunc(ages):
    if ages > 18:
        return True
    return False
result = filter(myFunc, age)  # age is iterable    myFunc is function
print(list(result))

# frozenset() works like set but it is unchangeable
mylist = ['apple','ball','cat']
x = frozenset(mylist)
# x[1] = 'dog'   # frozenset() does not support item assignment i.e. not changeable
# print(x)

# getattr() setattr() hasattr() delattr()
class Animal:
    name = 'Horse'
    age = 15
    breed = 'Stallion'
print(hasattr(Animal, 'color'))  # checks if Animal has attribute 'color' or not and returns true if it has
setattr(Animal, 'color', 'White')  # add attribute and its value
print(getattr(Animal, 'color'))  # print the value of color attribute
print(Animal.breed)
print(hasattr(Animal, 'color'))
# x = delattr(Animal, 'age')
# print(getattr(Animal,'age'))   # Throws exception AttributeError as there is no attribute 'age'


# hash() function uses hash algorithm. only immutable can be hashed i.e. tuple but not list dictionary set
x = 2423
y = "Ravi"
z = (1,2,3)
print(hash(x))
print(hash(y))
print(hash(z))
# custom object to the function and returns hash of the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("Ravi",26)
print(hash(person))


# isinstance() checks if the given element is instance of any object or iterable and return true or false
x = 5
print(isinstance(5,int))
print(isinstance("Hello",(str,int,float,dict)))  # checks if "Hello" is instance of any of the given type


# iter() return iterable object
x = iter(["Apple","Banana","Catfish"])
print(next(x))
print(next(x))

x = iter("Hello World") # iterable
print(next(x))   # iterator
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x))  # throws stopIteration Error

# map() executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
def map_func(a, b, c):
    return a + b +c
x = map(map_func, ('A','B','C'),(':',':',':'),('Apple','Ball','Cat'))
print(list(x))  #  ['A:Apple', 'B:Ball', 'C:Cat']

x = map(lambda x : x*x, (2,4,6,8))  # using lambda with map 
print(list(x))

x = ["apple", "ball", "cat"]
y = map(list, x)
print(list(y))   #  [['a', 'p', 'p', 'l', 'e'], ['b', 'a', 'l', 'l'], ['c', 'a', 't']]


#  reversed() method reverses the list
x = ["apple", "ball", "cat"]
y = reversed(x)    #  iterator reverse
x.reverse()   # list reverse
print(x)
print(y)
for i in y:
    print(i)


# round() method acts like ceil and floor 

print(round(1.5456, 2))
print(round(2.5))
print(round(2.4))
print(ceil(-4.8))


# Slice() method slices the object
list1 = [1,2,3,4,5,6,7,8,9,0]
y = slice(3)      # returns no. of sliced objects = 3
print(list1[y])    # returns [1,2,3]


# sum() method adds numbers
# list1 = (1,2,3,4,5)
# x = sum(list1, 4)
# print(x)


# super() method enables child class to access method and properties of parent class
class Parent:
    def __init__(self, text):
        self.message = text
    def displayMessage(self):
        print(self.message)
class Child(Parent):
    def __init__(self, text):
        super().__init__(text)
x = Child("Hello Everyone !")
x.displayMessage()


# zip() returns zip object in which each passed iterator is paired together with second item passed in each iterator
a = (1, 2, 3)
b = ("Apple", "Banana", "Dragon Fruit")
c = zip(a,b)
print(tuple(c))

