# # Using Normal Function 
# class Geek:
#     def __init__(self, age=0):
#         self._age = age
    
#     # getter method
#     def get_age(self):
#         return self._age

#     # setter method
#     def set_age(self, x):
#         self._age = x

# hello = Geek()

# # setting age using setter
# hello.set_age(21)

# # retrieving age using getter
# print(hello.get_age())

# print(hello._age)


# # Use of Property() function
# class Geeks:
#     def __init__(self):
#         self._age = 0

#     # Function to get value of _age
#     def get_age(self):
#         print("Getter method called")
#         return self._age

#     # Function to set value of _age
#     def set_age(self, a):
#         print("Setter method called")
#         self._age = a

#     # Function to delete _age attribute
#     def del_age(self):
#         del self._age
    
#     age = property(get_age, set_age, del_age)

# mark = Geeks()
# mark.age = 10
# print(mark.age)


# # Using @property decorators

# class Geeks:
#     def __init__(self):
#         self._age = 0
    
#     @property # invokes age() method
#     def age(self):
#         print("Getter method called")
#         return self._age
    
#     # a setter function
#     @age.setter
#     def age(self, a ):
#         if(a < 18):
#             raise ValueError("Sorry your age is below eligibility criteria")
#         print("Setter method called")
#         self._age = a

# mark = Geeks()
# mark.age = 19
# print(mark.age)



# property()
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get Radius")
        return self._radius
    
    def _set_radius(self, value):
        print("Set Radius")
        self._radius = value
    
    def _del_radius(self):
        print("Delete Radius")
        del self._radius
    
    radius = property(
        fget = _get_radius,
        fset = _set_radius,
        fdel = _del_radius,
        doc = "This is radius property"
    )
r = Circle(10)


# Providing Read - Only Attributes
# class Point:
#     def __init__(self, x, y):
#         self._x = x    # non-public attributes and no access using . notation
#         self._y = y
#     @property
#     def x(self):
#         return self._x
    
#     @property
#     def y(self):
#         return self._y

# class WriteCoordinateError(Exception):
#     pass

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     @property
#     def x(self):
#         return self._x
    
#     @x.setter
#     def x(self, value):
#         raise WriteCoordinateError("x coordinate is read - only")
    
#     @property
#     def y(self):
#         return self._y
    
#     @y.setter
#     def y(self, value):
#         raise WriteCoordinateError("y Coordinate is read - only")
    
# x = Point(12, 5)
# print(x.x)
# x.x = 90  # cannot write as x attribute is read - only 
# print(x.x)



# # Validating Input Values
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     @property
#     def x(self):
#         return self._x
#     @x.setter
#     def x(self, value):
#         try:
#             self._x = float(value)
#             print("Validated")
#         except ValueError:
#             raise ValueError('"y" must be a number') from None
        
# p = Point(12, 5)
# print(p.x)