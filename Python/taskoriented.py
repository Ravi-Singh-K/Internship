# # list1 = [1,2,3,4,5]
# # empty_list = []

# # # for i in range(0,len(list1)):
# # #     if list1 > 3:
# # #         empty_list.append(list1[i])

# # # print(empty_list)

# # # for i in list1:
# # #     if list1 > 3:
# # #         empty_list.append(list1[i])
# # # print(empty_list)

# # sub_list = [i for i in list1 if i > 3]
# # print(sub_list)

# list1 = ["ram","shyam","hari"]

# for i in list1:

#     print(list1[i])

# # A = "I,am,ravee"
# # print(A.split(','))

# list1 = 1
# print(dir(list1))

""""
1
121
12321
1234321
123454321

"""

# num = int(input("Enter any number to print pyramid : "))
# n=1
# for i in range(num):
#     for j in range(i+1):
#         print(n, end="")
#         n=n+1
#     n=1
#     print()

# def print_number_triangle(rows):
#     for i in range(1, rows + 1):        # Loop for the given number of
#         for j in range(1, i + 1):       # Prints the first part 
#             print(j, end="")
#         for j in range(i - 1, 0, -1):   # Prints the second part in reverse order
#             print(j, end="")
#         print()                         # Move to the next line

# num = int(input("Enter any number : "))
# print_number_triangle(num)

# str1 = ""
# str2 = ""
# for i in range(1,6):
#     str1 += str(i)
#     print(str1 + str2[::-1])
#     str2 += str(i)

# text1 = "Rave"
# print(text1 + "s")

# list1 = [1,4,3,5,2,3,4,1,2,3,2,4,5,2,1]
# list2 = enumerate(list1)     # index as key and elements as value
# print(dict(list2))
# list2 = list1
# # my_dict = { k:list1.count(k) for k in list1}       # Dictionary comprehension that counts the number of times 'k' is repeated in list1
# # print(dict(sorted(my_dict.items(), key=lambda x:x[1], reverse=True)))    # converts generated tuple by sorted into dictionary where .items() give keys and values and x:x[1] in which x is the parameter and x[1] is index, starts from 1 index and reverse help to print in descending order
# count =0
# empty_list = []
# count_list = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             count += 1
#             empty_list.append(j)
#     count_list.append(count)
#     print(count_list)
# print(my_dict)
# print(sorted(my_dict.values()))


# for i in range(1, 5):
#     print(i, end="")


# dict1 = {'a':1, 'b':2, 'c':3}
# list1 = ['j', 'k', 'l', 'm']
# dict2 = {'a':2, 'd':4, 'c':5}

# for k,v in dict1.items():
#     dict1.setdefault(k,[].append(list1))
# print(dict1)


# dict1 = {'':2, 'b':30}
# print(dict1)

# dict1.setdefault('a',2)
# print(dict1)


# string_name = "Tarun"
# y = enumerate(string_name)
# # for i in y:
# #     print(i)
# print(next(y))
# print(next(y))


# list_ = [1,4,3,5,2,3,4,1,2,3,2,4,5,2,1]
# dict1 = {}
# for i in list_:
#     dict1[i]=dict1.get(i,0) + 1
# print(dict1)



# for i in list_:
#     if i in dict1:
#         dict1[i] = dict1[i] + 1
#     else:
#         dict1[i] = 1
# dict2 = dict(sorted(dict1.items(), key=lambda x:x[1]))
# # print(dict2)


# list2 = [k*v for k,v in dict2.items()]
# print(list2)



# nested_list = [[1,2,3],[4,5,6]]
# names = [['yeuta','duita','tinta'],['charwota','paanchwota','chhawota']]
# new_dict = {}
# for i in nested_list:
#     for j in i:
#         for k in names:
#             for l in k:
#                 new_dict[i][j]=l
#                 k.remove(l)
# print(new_dict)

# first_word = str(input("Enter first word : "))
# second_word = str(input("Enter second word : "))
# fword = list(first_word)
# sword = list(second_word)
# # for i in fword:    # Checks character wise
# #     if i in sword:
# #         print(True)
# #     else:
# #         print(False)
# flag = []
# if len(fword) == len(sword):
#     for i in fword:
#         if i in sword:
#             flag.append(True)
#         else:
#             flag.append(False)
    
#     if any(flag):
#         print(True)
#     else:
#         print(False)
# else:
#     print("The length of two words is not compatible.")



# num1 = int(input("Enter 1st number : "))
# num2 = int(input("Enter 2nd number : "))
# num3 = int(input("Enter 3rd number : "))
# if num2 < num1 > num3:
#     print(num1)
# elif num1 < num2 > num3:
#     print(num2)
# else:
#     print(num3)




# Leap year checker

def leapYearChecker(year_in_number):
    if (year_in_number % 4 == 0 and year_in_number % 100 != 0) or (year_in_number % 400 == 0):
        print("----- Year {} is a leap year. -----".format(year_in_number))
    else:
        print("----- Year {} is not a leap year. -----".format(year_in_number))

year_in_number = int(input("Enter any year to check the leap year : "))
leapYearChecker(year_in_number)


# # using isleap() function from module calender

# def leapModule(year):
#     import calendar as cl
#     return cl.isleap(year)   # if built in press ctrl + click to see implementation

# year = int(input("Enter year to verify leap year : "))
# if (leapModule(year)):
#     print("----- {} year is a leap year.".format(year))
# else:
#     print("----- {} year is not a leap year.".format(year))