import json
from operationclass import *

with open("./materials.json", "r") as outfile:
        data = json.load(outfile)


coffee = data['coffee']
milk = data['milk']
water = data['water']
totalbalance = data['totalbalance']
espresso = data['Espresso']
latte = data['Latte']
americano = data['Americano']

coffeeMachine = CoffeeMachine(coffee, milk, water, totalbalance, espresso, latte, americano)

