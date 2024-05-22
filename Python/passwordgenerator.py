# import random
# import string

# char = string.ascii_letters
# char += string.digits
# char += string.punctuation

# length = int(input("Enter the length for password : "))
# password = ""
# password = ''.join([random.choice(char) for i in range(length)])   # List comprehension

# # for i in range(length):
# #     next_char = random.choice(char)
# #     password += next_char

# print("Your random password is : ", password)


# import random

# chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
# length = int(input("Enter the length for password : "))
# password = ''.join(random.sample(chars, length))
# print("Your random password is ", password)
