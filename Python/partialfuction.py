# from functools import partial

# def add(a,b,c):
#     print('from add function',a,b,c)
#     return 100*a + 10*b + c
# # add_part = partial(add, 2,3)
# # print(add_part(4))

# def div(strings, *args,**kwargs):
#     print(strings)
#     print(args)
#     f1=args[0]
#     print(f1)
#     if f1:
#         f1()

# def f(a,b,c,x):
    
#     g = partial(add, 3, 1, 4)

#     div("Name",g)
#     return 1000*a + 100*b + 10*c + x
# # print(g(5))
# f(3,4,5,6)

# # def multiply(a,b):
#     # return a * b
# # result = partial(multiply, 4)
# # print(result(29))

# # import this


class Animal:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
    def dislayName(self):
        return self.name
    
class Dog(Animal):
    def _init__(self):
        Animal.__init__()
    def displayColor(self):
        return self.color
d = Dog("Lion","Brown","Bulldog")
d.displayColor()
print(d.dislayName())
print(d.displayColor())