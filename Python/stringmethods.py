# txt = "This is an example ßßß  of string  ßßß "
# sen = str("this Is Specified bY strInG conStruCtor")
# print(type(txt))
# print(type(sen))
# print(txt[0])
# print(sen[0:1])
# print(txt[:1])
# sum = "The sum of 1 + 2 is {0}" .format(1+2)
# print(sum)
# eg = "{0},{1},{2}".format('a','b','c')
# print(eg)
# eg = "{},{},{}".format('a','b','c')
# print(eg)
# eg = "{2},{0},{1}".format('a','b','c')
# print(eg)
# eg = "{2},{0},{1}".format(*'xyz')
# print(eg)
# print(sen.capitalize()) # .capitalize() makes first letter capital and other small
# print(txt.casefold())  #  .casefold() converts 'ß' to small 'ss'
# print(txt.lower())  # .lower() converts into lower case but 'ß' doesnot convert as it is already in small case

# subs = "aeiou"
# subsby = "bdjpv"
# remvalue = "straight"
# newsubs = str.maketrans(subs,subsby) # str.maketrans(x,y) this function replaces value in variable 'x' by value in variable 'y'
# print(sen.translate(newsubs)) # sen.translate(newsubs) this function translate value of sen variable
# newsen = str.maketrans(subs,subsby,remvalue) # here .maketrans(a,b,c) 'c' parameter resembles the value removed in sen variable
# print(sen.translate(newsen))

# # Example
# # a1 = "ravi"
# # a2 = "a" # length 1
# # a3 = "bcd"   # length 3
# # a4 = "iod"
# # a5 = str.maketrans(a2,a3,a4)  # the first two arguements must have equal length
# # print(a1.translate(a5))

# # name = "Ravi"
# # print(name[1:3])
# # print(name[1::2])
# # print(list(name))
# # for x in name:
# #     if x.isupper()==True:
# #         print(True)

# text = "abci\t"  
# print(text.isprintable())

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9]
# print(list1 + list2)
# list1.extend(list2) # .extend(list) adds the value of list elements
# print(list1)

# list1.remove(1) # remove(value) removes value from list
# print(list1)

# list1.sort(reverse=True)  # sort() sorts the elements  reverse() function takes boolean value
# print(list1)

# print(list1.index(2)) # index(index_value) gives the value at position index_value

# print(len(list1))
# print(list1.count(9)) # count() 

# list1.clear() # clear() clears elements from the list but saves in memory
# print(list1)

# del list1 # del removes the list from the memory
# print(id(list1)) # id() prints the id from the memory
# print(list1)

# a = "I love Football"
# b = "I doesnot love f Football"
# commons = []
# uniques = []
# for c in b.split(): # c is the elements in splitted b
#     if c in a.split(): # checks if c is available in splitted a
#         commons.append(c) # adds in commons if available in a
#     else:
#         uniques.append(c) # adds in uniques if not available in a
# print(commons)
# print(uniques)

# list1 = [1,1,2,2,2,3,4,5,6,6,7,8,9,9]
# print(list1)
# print(list(set(list1)))
# print(list(list1))

# set1 = {1,2,3,4,5,"b","c"}
# print(set1)
# set1.add(90)
# print(set1)

# tuple1=(1,2,3,4,5,6,7)
# print(tuple1)

# emptylist = []
# for elem in list1:
#     if elem not in emptylist:
#         emptylist.append(elem)
# print(emptylist)


# dict1 = {"a":5, 'b':6, 'c':6}

# id_list = [1,2,3,4,5]
# value_list = ["Ram","Shyam","Hari","Gita","Sita"]

# dict_list = { keys:values for keys,values in zip(id_list,value_list)}
# print(dict_list)

# dict_list = {}
# for a in range(0, len(id_list) ):       
#         dict_list[id_list[a]]=value_list[a]
# print(dict_list)

# dict1[2]="Ravi"
# print(dict1)
# dict1.popitem() # delete last element from the dictionary

# del dict1["a"] # delete first element from the dictionary
# print(dict1)

# name = "THisstrinG"
# print(all([True, True, False, False]))``
# for x in name:
#         print(any([x.isupper()]))

# for a in name:
#     print(a.isupper())
# listcomp = [a.isupper() for a in name]
# print(listcomp)
# # print(any[a.isupper() for a in name])

# list1 = [1,2,3,4,5,6]
# print(list1.index(5))

# list1.insert(4,9)
# print(list1)

# list1[2]=90
# print(list1)

# list1 = [4,5,6,33,6,0,999]
# list1.sort(reverse=True) # Reverses the list elements
# print(list1[0], list1[1] ) # prints the list by slicing i.e prints from index 0 to 1 (only 2 elements) ignore stop index

# print(max(list1))
# print(min(list1))

# nested_list = [ [1,2,3], [4,5,6], [7,8,9, 10] ]
# print(nested_list)

# print(nested_list[2][1])
# print(nested_list[2])
# for x in range(0, len(nested_list)):
#     print(nested_list[x])

# text = "I love fruits."
# print(text.count("love")) # Counts the number of times "love" is repeated
# print(text.count("l",2,4)) # here start and end is mentioned to search for "love"

# text = "This is an example of string."
# print(text.endswith("string")) # checks the string if it ends with "string"
# print(text.endswith("string.")) 
# print(text.endswith("string.",len(text)-8,len(text))) # here we can specify start and end to specify search part. 

# print(text.find("ring")) # both finds the position of string but it display -1 if not found
# print(text.index("ring")) # it returns exception if string is not found

# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)   # joins all the name using "#" as operator
# print(x)

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)   # joins the keys of dictionary using TEST as seperator ! does not return value but returns key and joins them
# print(x)

