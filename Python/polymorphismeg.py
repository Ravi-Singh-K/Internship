# Inbuilt Polymorphic Functions
print(len("Hello World"))  # len() for string
print(len([10, 2, 3, 5]))  # len() for list


# User defined polymorphic function
def add(x, y, z = 0):
    return x + y + z
print(add(2,3))
print(add(2,3,4))


# Polymorphism with class methods:
class Nepal:
    def capital(self):
        print("Capital : Kathmandu")
    def language(self):
        print("Language : Nepali")
class USA:
    def capital(self):
        print("Capital : Washington D.C")
    def language(self):
        print("Language : English")
obj_Nepal = Nepal()
obj_USA = USA()
for country in (obj_Nepal, obj_USA):
    country.capital()
    country.language()

