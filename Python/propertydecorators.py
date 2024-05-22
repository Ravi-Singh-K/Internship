# Properties make attributes read only attribute



class TemperatureModel:
    def __init__(self, temp):
        self._temperature = temp

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if 10 <= value <= 40:
            self._temperature = value
        else:
            print("Temperature out of range. Please set between 10 and 40")


obj = TemperatureModel(35)
print(obj.temperature)
x = obj.temperature
print(x)
# model = TemperatureModel(20)
# print(model.temperature)
# model.temperature = 35
# print(model.temperature)
# model.temperature = 5


