from abc import ABC, abstractmethod
import time

# class BaseClass(ABC):
#     @abstractmethod
#     def method_1(self):
#         pass

# # Implementation of Abstraction
# class Car(ABC):

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     # Abstract Method
#     @abstractmethod
#     def printDetails(self):
#         pass

#     # Concrete Method
#     def accelerate(self):
#         print("Speed Up ...")
    
#     # Concrete Method
#     def brake(self):
#         print("Slow Down and Stop")
    
#     # Concrete Method
#     def clutch(self):
#         print("Change Gear")

# class Hatchback(Car):
    
#     # Implementation of Abstract Method
#     def printDetails(self):
#         print("Brand : ", self.brand)
#         print("Model : ", self.model)
#         print("Year : ", self.year)
    
#     def sunRoof(self):
#         print("Not having this feature")

# class Suv(Car):

#     # Implementation of Abstract Method
#     def printDetails(self):
#         print("Brand : ", self.brand)
#         print("Model : ", self.model)
#         print("Year : ", self.year)

#     def sunRoof(self):
#         print("Available")

# car1 = Suv("Mahindra", "XUV 3XO", "May 26, 2024")
# car1.printDetails()
# time.sleep(1.5)
# car1.accelerate()
# time.sleep(1.5)
# car1.clutch()
# time.sleep(1.5)
# car1.brake()
# time.sleep(1.5)
# car1.sunRoof()



# # Example No. 3
# class Polygon(ABC):

#     @abstractmethod
#     def noofsides(self):
#         pass

# class Triangle(Polygon):

#     #overriding abstract method
#     def noofsides(self):
#         print("Triangle has 3 sides.")

# class Pentagon(Polygon):

#     #overriding abstract method
#     def noofsides(self):
#         print("Pentagon has 5 sides.")

# t = Triangle()
# t.noofsides()

# p = Pentagon()
# p.noofsides()



# # Example no. 4
# class Animal(ABC):

#     def move(self):
#         pass

# class Human(Animal):

#     def move(self):
#         print("Human can walk.")

# class Snake(Animal):

#     def move(self):
#         print("Snake can crawl.")

# class Dog(Animal):

#     def move(self):
#         print("Dog can run.")

# h = Human()
# h.move()

# s = Snake()
# s.move()

# d = Dog()
# d.move()



# # Accessing method of Abstract class
# class R(ABC):
#     def rk(self):
#         print("Abstract Base Class")
# class K(R):
#     def rk(self):
#         super().rk()         # Using super() to access Base Class
#         print("Sub Class")
# r = K()
# r.rk()



# Example no. 5
class Bike(ABC):

    # def __init__(self, name, model):
    #     self.__name = name
    #     self.__model = model

    @abstractmethod
    def __startBike(self):
        print("Start Bike")

    @abstractmethod
    def __stopBike(self):
        print("Stop Bike")

class DirtBike(Bike):

    # methodoverriding
    def _Bike__startBike(self):
        print("Start Dirt Bike")

    def _Bike__stopBike(self):
        print("Stop Dirt Bike")

d = DirtBike()
d._Bike__startBike()
d._Bike__stopBike()

