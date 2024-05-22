# class Verbose_attribute():
#     def __get__(self, obj, type=None) -> object:
#         print("Accessing the attribute to get the value")
#         return 42
#     def __set__(self, obj, value) -> None:
#         print("Accessing the attribute to set the value")
#         raise AttributeError("Cannot Change the value.")
    
# class Foo():
#     attribute1 = Verbose_attribute()

# my_foo_object = Foo()
# x = my_foo_object.attribute1
# print(x)


# # Using property()
# class Foo():
#     @property
#     def attribute1(self) -> object:
#         print("Accessing the attribute to get the value")
#         return 42

#     @attribute1.setter
#     def attribute1(self, value) -> None:
#         print("Accessing the attribute to set the value")
#         raise AttributeError("Cannot change the value")

# my_foo_object = Foo()
# x = my_foo_object.attribute1
# print(x)


# # Validation in a getter method
# class Foo:
#     def __init__(self, value):
#         if not isinstance(value, int):
#             raise TypeError(f'Expecting an integer, got {type(value)}')
#         else:
#             self.__value = value
    
#     @property
#     def value(self):
#         return self.__value
    
# f = Foo(5)


# # Alternatively,
# class Foo:
#     def __init__(self, value):
#         self.__value = self._check_value_input(value)
    
#     def _check_value_input(self,value):
#         if not isinstance(value, int):
#             raise TypeError(f'Expecting an integer, got {type(value)}')
#         else:
#             return value
    
#     @property
#     def value(self):
#         return self.__value

# f = Foo(9)