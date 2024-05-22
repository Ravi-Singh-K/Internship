







# dict1 = {'a':1, 'b':2,'c':3}
# print(dict1['b'])
# dict2 = {'d':4}
# dict1.update(dict2)  # Update the dict2 key and value in dict1 
# # print(dict1)

# # print(dict1.keys())   # Print all the available keys in dict1

# # print(dict1.values())   # print all the available values in dict1

# # print(dict1.items())    # display all the elements keys and values in tuple form with , operator

# if 'd' in dict1:    # checks if 'd' key is available in dict1 or not
#     print(dict1['d'])


# # Changing element of specific key
# dict1['b'] = "Balloon"  # Changing the value of 'b' key
# # print(dict1)

# dict1.update({'c':"Cartoon"})  #  Updating the value of key 'c'
# # print(dict1)

# dict1.pop('d')
# # print(dict1)

# dict1.popitem()
# # print(dict1)

# del dict1   # Delete the dictionary completely. also can specify name of key to delete element like del dict1["key"]
# # print(dict1) 

# new_dict = dict({"A":"Apple","B":"Ball","C":"Cat","D":"Dog","E":"Elephant"})   # constructor to create dictionary
# print(new_dict)

# for x in new_dict:   
#     print(new_dict[x])   # Prints all the values of the dictionary
#     # print(x)   # Prints all the keys of the dictionary

# for x in new_dict.values():     # .values() function also helps to print to values of dictionary
#     print(x)

# for x in new_dict.keys():     # .keys() function helps to print the keys of the dictionary
#     print(x)

# for x,y in new_dict.items():   # .items() function helps to print all the keys and values of the dictionary
#     print(x,y)

# dups_dict = new_dict
# # print(dups_dict)

# dict1 = new_dict.copy()
# # print(dict1)

# # print(id(dict1), id(dups_dict), id(new_dict))

# dict2 = dict(dict1)
# # print(dict2)

# print(id(dict1), id(dict2), id(new_dict), id(dups_dict))

# dict2.update({"F":"Fiscal"})
# # print(dict2)
# # print(dict1)


nested_dict = {
    "Child1":{
        "Name":"Ram",
        "Age" : 11
    },
    "Child2":{
        "Name":"Shyam",
        "Age" : 13
    },
    "Child3":{
        "Name":"Hari",
        "Age":12
    }
    }
print(nested_dict["Child1"]["Name"])    # Prints the name of child1
print(nested_dict["Child1"])    # Prints the elements of child1
print(nested_dict.items())   # Prints all the elements of nested_dict dictionary

for x,y in nested_dict.items():
    print(x)
    for obj in y:
        print(obj + ":", y[obj])
    print()

print(nested_dict.get("Child1"))  # Get the value of the given child