# # multiplys = lambda x,y : x*y 
# # print(multiplys(3,4))

# # # Using Lambda Function

# # defined_fun = lambda a: a**a
# # print(defined_fun(5))

# # lambda with map for finding square
# def square_numbers(n):
#     return n**2
# result = map(square_numbers, range(1,11))
# print(list(result))

# result = set((map(lambda x : x**2, range(1,10,2))))     #   calculate squares of the list of range 1 to 10
# print(result)

# a = [1,2,3]
# b = [4,5,6]
# result = map(lambda x,y : x+y , a, b)      # Adds lists a and b and 
# print(tuple(result))

# nums = [45,23,66,73,22,89,6,3,45,22,35,53,64]
# def odd_nums(n):    
#     if n%2 != 0:    return n

# result = filter(odd_nums, nums)    # filter odd numbers from nums list
# print(list(result))

# result = list(filter(lambda x: x % 2 != 1, nums))  # filter even numbers from the list
# print(result)


# from functools import reduce as rd

# result = rd(lambda x,y: x+y, range(1,11))    # Reduce function returns single value after cumulative running of function
# print(result)
# import copy as cp
# data = [1,2,3,4,5]
# data2 = data
# data2[2]='a'
# print(data,"\n",data2)
# result2 = list(filter(lambda x: x % 2 == 0, data))
# print(result2)

def square_calc():
    i = 1
    while True:
        yield i*i
        i += 1
x = square_calc()
print(next(x))
print(next(x))
print(next(x))