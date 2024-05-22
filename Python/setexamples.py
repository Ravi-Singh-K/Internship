# set1 = {1,2,3,4,5,6,7,8,9}
# set2 = {8,7,6,5,4,7,3,2}
# # print(set1)
# # print(set2)
# set3 = set1.intersection(set2)
# print(set3)




# '''
#     1
#    121
#   12321
#  1234321
# 123454321
# '''

# myset = {"apple", "banana", "cherry", "apple"}  # Does not takes duplicate elements
# # print(myset)

# print(len(myset))
# print(type(myset))

# set1 = set(("hello","world","this","is","developer"))
# # print(set1)

# for i in set1:
#     print(i)

# print("this" in set1)

# set1.add("python")
# print(set1)

# tropical = {"pineapple", "mango", "papaya"}
# set1.update(tropical)
# print(set1)

# set1.remove("mango")  #removes mango from the set but will raise error if element is not available
# set1.pop() # since set is unordered datatype it will delete random element
# set1.discard("papaya")  # will not raise error if not available
# print(set1)

# set1.clear() # clears the elements from the set
# print(set1)

# del set1 # delete the set
# print(set1)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)    # also ' | ' operator can be used. myset=set1|set2|set3|set4
# print(myset)

# set1 = {1,2,3,4}
# tuple1 = (5,6,7,8)
# myset = set1.union(tuple1)
# print(myset)

# set1 = {"a", "b", "c", 2,3}
# set2 = {1, 2, 3, "b","c"}
# myset = set1.intersection(set2)   # intersection extracts the common elements. also ' & ' can also be used like "set1 & set2"
# print(myset)

# set1 = {1, 0, False, "apple"}
# set2 = {True, 1, 0, "Ball", "Cat", "Apple"}
# myset = set1.intersection(set2) 
# print(myset)

# set1 = {1, 0, False, "apple"}
# set2 = {True, 1, 0, "Ball", "Cat", "Apple"}
# myset=set2.difference(set1)   # checks and print all the elements that are not available in set1
# print(myset)

