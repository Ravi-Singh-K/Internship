import copy as cp

# List Example

# list1 = [[1,2,3],[4,5,6],[7,8,9]]

# list2 = list1 # does not create new object but copies the reference of old list to new list
# print(id(list1))  # prints the id of same location
# print(id(list2))

# list2 = cp.copy(list1) # it is shallow copy that creates new object but stores the reference of old list to new list
# print(id(list1))
# print(id(list2)) # after shallow copy, prints the id of different memory location

# list2[1][1] = 'a' # changes is done in new list and changes can be seen in old list too
# # print(list1)
# # print(list2)

# list2.append(['b','c','d'])  # new dimension is added to the new list but the changes is not seen in old list as new dimension is added
# print(list1)
# print(list2)

# print(id(list1))
# print(id(list2))

# list1.append([1,2,3])
# print(list1, id(list1))
# print(list2, id(list2))

# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# list2 = cp.deepcopy(list1)   # deep copy creates the new object and recursively add the elements of the original list
# print(id(list1))  # prints the address of different memory locations
# print(id(list2))

# # list1[2][1] = 'abc'   # original list is changed but changes cannot be seen in new list
# # print(list1)
# # print(list2)

# list2.append(['a','b','c'])
# print(list1)
# print(list2)


# Dictionary Example

# old_dictionary = {'a':'apple','b':'ball','c':'cat','d':'dog','e':'ear'}
# new_dictionary = old_dictionary.copy()   # copy method creates new dictionary that is filled with the copy of the references from the old dictionary
# old_dictionary.clear() # only clears the old dictionary but new dictionary remains as it is
# # print(id(old_dictionary))
# # print(id(new_dictionary))  #.copy() does not take any arguements 
# print(old_dictionary)
# print(new_dictionary)

# new_dictionary = old_dictionary  # '=' operator is used where new variable is referenced from old dictionary
# # new_dictionary.clear() # clears both list

# # # print(id(old_dictionary))
# # # print(id(new_dictionary))  # same id number
# # print(old_dictionary)
# # print(new_dictionary)


# a = [4,8,2,5,0]
# print(a , id(a))

# c = cp.deepcopy(a)
# c[2] = "RJ"
# print(c, id(c),'\n',a, id(a))

# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# list2 = cp.copy(list1)
# list2[0][1] = "AJ"
# print(list2 , '\n' , list1 )

# list3 = cp.deepcopy(list1)
# list3[1][0] = "JA"
# print(list3 , '\n', list1)



