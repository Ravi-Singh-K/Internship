import json

class CoffeeMachine:

    def __init__(self, coffee, milk, water, balance, espresso, latte, americano):
        self.milk = milk
        self.coffee = coffee
        self.water = water
        self.balance = balance
        self.espresso = espresso
        self.latte = latte
        self.americano = americano
        self.displayMenu()

    def handlingOrder(self, order):
        if order == 1:
            if self.coffee >=10 and self.water >= 100:
                print("Your order is Confirmed.")
                print(f"You need to pay Rs. {self.espresso} for Espresso.")
                self.coffee -= 10
                self.water -= 100
                self.makePayment(order)
            else:
                print("Sorry ! Espresso is out of Stock. Please choose any other product.")
                self.displayMenu()

        elif order == 2:
            if self.coffee >= 5 and self.water >= 50 and self.milk >= 50:
                print("Your order is Confirmed.")
                print(f"You need to pay Rs. {self.latte} for Latte.")
                self.coffee -= 5
                self.water -= 50
                self.milk -= 50
                self.makePayment(order)
            else:
                print("Sorry ! Latte is out of Stock. Please choose any other product.")
                self.displayMenu()

        elif order == 3:
            if self.coffee >=5 and self.water >= 75:
                print("Your order is Confirmed.")
                print(f"You need to pay Rs. {self.americano} for Americano.")
                self.coffee -= 5
                self.water -= 75
                self.makePayment(order)
            else:
                print("Sorry ! Americano is out of Stock. Please choose any other product.")
                self.displayMenu()
        
        elif order == 4:
            self.displayBalMate()
        
        else:
            print("You choosed wrong number. Please choose again.")
            self.displayMenu()

    def makePayment(self, order):
        while True:
            try:
                pay = float(input("Please make your payment : "))
                if pay <= self.balance:
                    if order == 1:
                        if pay > self.espresso:
                            print("Here is your change : ", (pay - self.espresso))
                            self.balance += self.espresso
                            self.exitMachine()
                        elif pay < self.espresso:
                            print("Sorry ! You have paid insufficient amount. Please make payment again.")
                            self.makePayment(order)
                        else:
                            self.balance += pay
                            print("Thank you ! Your payment has been confirmed.")
                            self.exitMachine()
                    
                    elif order == 2:
                        if pay > self.latte:
                            print("Here is your change : ", (pay - self.latte))
                            self.balance += self.latte
                            self.exitMachine()
                        elif pay < self.latte:
                            print("Sorry ! You have paid insufficient amount. Please make payment again.")
                            self.makePayment(order)
                        else:
                            self.balance += pay
                            print("Thank you ! Your payment has been confirmed.")
                            self.exitMachine()

                    else:
                        if pay > self.americano:
                            print("Here is your change : ", (pay - self.americano))
                            self.balance += self.americano
                            self.exitMachine()
                        elif pay < self.americano:
                            print("Sorry ! You have paid insufficient amount. Please make payment again.")
                            self.makePayment(order)
                        else:
                            self.balance += pay
                            print("Thank you ! Your payment has been confirmed.")
                            self.exitMachine()
                
                else:
                    print("Sorry no change to give. Please provide small amount.")
                    self.makePayment(order)
                break
            except Exception:
                print("Please provide legit amount.")
                self.makePayment(order)

    def exitMachine(self):
        self.displayBalMate()
        exit()

    def displayBalMate(self):
        print("Your remaining materials are : ")
        print("Coffee : ", self.coffee)
        print("Milk : ", self.milk)
        print("Water : ", self.water)
        print("Total Balance : ", self.balance)
        self.updateData()

    def updateData(self):
        with open("./CoffeeVendingMachine/materials.json", "r") as readfile:
            data = json.load(readfile)
        
        data['coffee'] = self.coffee
        data['milk'] = self.milk
        data['water'] = self.milk
        data['totalbalance'] = self.balance

        with open("./CoffeeVendingMachine/materials.json", "w") as writefile:
            json.dump(data, writefile, indent = 4)

    
    def displayMenu(self):
        print("1. Espresso ----- Rs. ", self.espresso," \n2. Latte ----- Rs. ",self.latte," \n3. Americano ----- Rs. ", self.americano,"\n 4. Display Materials")
        while True:
            try:
                order = int(input("Please choose the number : "))
                self.handlingOrder(order)
                break
            except Exception:
                print("Please give valid input.")
                self.displayMenu()       