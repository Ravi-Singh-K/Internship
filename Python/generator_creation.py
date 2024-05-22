# # Simple generator

# def simpleGenerator():  # contains yield keyword. Same like return keyword
#     yield 1
#     yield 2
#     yield 3
# for i in simpleGenerator():
#     print(i, " ", end="")  # gives 1 2 3


# # Next() method in Generator

# def next_implement():
#     yield "Hello"
#     yield "World"
#     yield "I am Robo. Speed 1 Tera Hertz. Memory 1 zetabyte."
# x = next_implement()
# print(x)  # <generator object next_implement at 0x000001D6EE699B10>
# print(next(x))
# print(next(x))
# print(next(x))


# # Fibonacci Series using generator

# def fibSeries(limit):
#     if limit == 0:
#         yield 0
#     elif limit == 1:
#         yield 0
#         yield 1
#     else:
#         a,b = 0,1
#         while a < limit:
#             yield a
#             a,b = b, a+b
# # n = int(input("Enter nth term for fibonacci series : "))
# c = fibSeries(7)
# # a = 0
# # while a < n:
# #     print(next(c), " ", end=" ")  # Here it raises StopIteration error. Does not run upto 8th or 10th term
# #     a += 1

# # Does not throw error except it uses "pass" keyword to terminate program without throwing error
# try:
#     while True:
#         print(next(c), " ", end=" ")
# except StopIteration:
#     pass

# # Using For loop 
# print("\n")
# for i in fibSeries(5):
#     print(i, " ", end="")


# # Generator expression that multiplies the number by 5 if divisible by 2
# gen_exp = (i * 5 for i in range(10) if i % 2 == 0)
# print("\n")
# for i in gen_exp:
#     print(i, " ", end="")

# print("\n")

# Generator to calculate square of numbers till that squared number is less than 100
# def square_gen():
#     i = 1
#     while True:    # this approach is not good
#         yield i * i
#         i += 1
def square_gen():
    for i in range(10):
        yield i**2
# numbers = square_gen()
# for num in numbers:
#     if num > 100:
#         break
#     print(num, " ", end="")


y = square_gen()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))