# class BankAccount:

#     account_number : str =  '32100100'

#     def __init__(self):   # here type annotation practice is good. makes code readability
#         # self.account_number = account_number
#         self.total_balance : float = 0.0
    
#     def depositBalance(self):
#         amount = int(input("Enter amount to deposit : "))
#         if amount >= 0:
#             self.total_balance += amount
#             print("The updated amount is ", amount)
#             print("The new total balance is ", self.total_balance)
#         else:
#             print("The given amount is negative. Negative balance cannot be deposited.")
        
#     def withdrawBalance(self):
#         amount = int(input("Enter amount to withdraw : "))
#         if amount <= self.total_balance:
#             self.total_balance -= amount
#             print("The withdrawn amount is ", amount)
#             print("The new total balance is ",self.total_balance)
#         else:
#             print("The provide amount exceeds the available total balance.")
#     @property
#     def displayCurrentBalance(self):
#         return self.total_balance
    


# bankacc = BankAccount()
# bankacc.depositBalance()
# bankacc.withdrawBalance()
# print(bankacc.displayCurrentBalance)




# # Hierarchy Inheritance
# class A:
#     def display(self):
#         print("From A")
# class B(A):
#     def display(self):
#         print("From B")
# class C(B):
#     def display(self):
#         print("From C")
# class D(B,C):   # Cannot create consistent MRO : TypeError
#     def display(self):
#         print("From D")
# c = C()
# c.display()