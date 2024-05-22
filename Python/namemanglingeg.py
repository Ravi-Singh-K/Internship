# class Testing:
#     def __init__(self, name):
#         self.__name = name

# t = Testing("Hello World")

# print("The name mangled variable is : ", t._Testing__name)
# print(t.__name) # Raises an error



# # Name mangling process using dir() method
# class Testing:
#     def __init__(self, name):
#         self.__name = name

#     def displayName(self):
#         print(self.__name)

# t = Testing("Hello World")
# # print(t.__name)
# print(t._Testing__name)
# print(t.__dict__)
# print(dir(t))




# # Name mangling using method overriding

# class Map:
#     def __init__(self):
#         self.__geek()

#     def geek(self):
#         print("From Parent Class")
    
#     __geek = geek

# class SubMap(Map):
#     def geet(self):
#         print("From Child Class")

# obj = SubMap()
# obj.geek()




### Tricky question

# class Parent:
#     def __init__(self, parent_name, address):
#         self.parent_name = parent_name
#         self.__address = address

#     def father_name(self):
#         print("Name : ", self.parent_name)
#         print("Address : ", self.__address)

#     @property
#     def get_name(self):
#         return self.parent_name
    
# class Child(Parent):
#     def __init__(self, name, address, parent_name):
#         super().__init__(parent_name, address)
#         self.name = name
    
# ravi = Child("Ravi", "Kathmandu", "my dad")
# # print(ravi.displayName())
# print(ravi.father_name())
# # print(ravi.get_name)
# # print(ravi.name)
# # print(ravi._Parent__address)



