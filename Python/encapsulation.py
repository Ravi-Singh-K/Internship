from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def accelerator(self):
        pass

class SUV(Car):

    def accelerator(self):
        print("From SUV Class")

    def brake(self):
        print("Braking from Child class")

s = SUV()
s.accelerator()
s.brake()