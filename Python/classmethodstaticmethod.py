# # Simple Class Method
# class Nepal:
    
#     capital = "Kathmandu"

#     def displayCapital(city):
#         print("Capital city of Nepal : ", city.capital)

# Nepal.displayCapital = classmethod(Nepal.displayCapital)
# Nepal.displayCapital()



# # create classmethod using classmethod()
# class Food:

#     meat = "Steak"

#     def favMeat(eat):
#         print("I love", eat.meat)
    
# Food.favMeat = classmethod(Food.favMeat)
# Food.favMeat()


# Use of Class method and Static method
from datetime import *
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year-year)
    
    @staticmethod
    def isAdult(age):
        return age>18
    
p1 = Person('Ravi', 25)
p2 = Person.fromBirthYear('Ravi', 2000)

print(p1.age)
print(p2.age)
print(Person.isAdult(22))




# class SumOfNumber:
#     @classmethod
#     def addMethod(cls,)