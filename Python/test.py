

# x = [1,2,3,4,5]

# y = list(map(lambda x:x**2, x))
# print(y)

# y = filter(lambda x : x % 2 == 0, x)
# print(list(y))


# import array as arr
# x = [1,2,3,4,'a']
# y = arr.array('i',[1,2,3,4,97])
# print(x)
# print(y)


# # Assert Keyword 
# x = 10 / 2
# assert x == 5, "x not 6"
# print(x)


# # Deepcopy example
# import copy as cp

# list1 = [1,2,3,4,5]
# list2 = cp.copy(list1)
# print("The original list : ")
# print(list1)

# list2[2] = 100
# print("The copied list : ")
# print(list2)


# Assignment
# nested_dictionary = {'a':{'b':{'c':True}}}
# print(nested_dictionary.get('a').get('b').get('c'))
# def returnValue(nested_dictionary, dict_key):
    # print(nested_dictionary)
    # print(type(nested_dictionary))
    # print(nested_dictionary['a'])
    # print(nested_dictionary['a']['b'])
    # print(nested_dictionary['a']['b']['c'])
    # print(nested_dictionary['a'].get('b'))
    # print(nested_dictionary['a'].get('b').get('c'))

    # if dict_key == nested_dictionary.keys():
    #     print(nested_dictionary.get(dict_key))
    # elif dict_key == nested_dictionary['a'].keys():
    #     print(nested_dictionary['a'][dict_key])
    # elif dict_key == nested_dictionary['a']['b'].keys():
    #     print(nested_dictionary['a']['b']['c'].keys())
    # else:
    #     print("The key is not found")

    # for k,v in nested_dictionary.items():
    #     if dict_key == k:
    #         print(k)   # prints 'a'
    #         print(v)   # prints ' {'b':{'c':True}}
    #         break
    #     else:
    #         None
    #     for i,j in v.items():
    #         if dict_key == i:
    #             print(i)   # prints 'b'
    #             print(j)   # prints '{'c':True}
    #             break
    #         else:
    #             None
    #         for a,b in j.items():
    #             if dict_key == a:
    #                 print(a)   # prints 'c'
    #                 print(b)   # prints 'True'
    #                 break
    #             else:
    #                 None
    
    # a = [v for k,v in nested_dictionary.items() if dict_key==k]
    # print(a)
    # b = [j for k,v in nested_dictionary.items() for i,j in v.items() if dict_key==i]
    # print(b)
    # c = [z for k,v in nested_dictionary.items() for i,j in v.items() for y,z in j.items() if dict_key==y]
    # print(c)
# returnValue(nested_dictionary, 'c')

# Short form to access value
# nested_dictionary = {'a':{'b':{'c':True}}}
# def returnValue(data, key):
#     for i in key:
#         data = data.get(i, {})
#     return data
# print(returnValue(nested_dictionary, 'abd'))


# # Optimised code
# # Using separator to detect keys
# nested_dictionary = {'a':{'b':{'c':True}}}
# def returnValue(data, key, split_operator=','):
#     for i in key.split(split_operator):
#         if not isinstance(data, dict):
#             return None
#         data = data.get(i, {})
#     return data
# print(returnValue(nested_dictionary, 'a.b', '.'))


# # Multiple Inheritance Example
# class Animal:
#     def __init__(self, mammal_name, mammal_type):
#         self.mammal_name = mammal_name
#         self.mammal_type = mammal_type
    
#     def displayMammals(self):
#         print("Mammal Class : ")
#         print("Mammal Name : ", self.mammal_name)
#         print("Mammal Type : ", self.mammal_type)

# class Human(Animal):
#     def __init__(self, human_age, mammal_name, mammal_type):
#         self.age = human_age
#         Animal.__init__(self,mammal_name, mammal_type)
        

#     def displayMammals(self):
#         print("Human Class : ")
#         print("Age : ", self.age)
#         return super().displayMammals()

# class Plant:
#     def __init__(self, plant_name, plant_type):
#         self.plant_name = plant_name
#         self.plant_type = plant_type
    
#     def displayPlant(self):
#         print("Plant Class : ")
#         print("Name : ", self.plant_name)
#         print("Type : ", self.plant_type)

# class Earth(Human, Plant):
#     def __init__(self, human_age, mammal_name, mammal_type, plant_name, plant_type, earth_age):
#         self.earth_age = earth_age
#         Human.__init__(self,human_age, mammal_name, mammal_type)
#         Plant.__init__(self, plant_name, plant_type)
    
#     def displayEarth(self):
#         print("From Earth View : ")
#         print("Age : ", self.earth_age)
#         return super().displayMammals()

# mars = Earth(100, "Male", "Mammal", "Hydrilla", "Submerged", "13 billions")
# print(mars.displayEarth())
# print(mars.displayPlant())
# print(mars.displayMammals())


# # Function
# def sumOfData(a, b=0):
#     return a+b

# print(sumOfData( 10)) 

# # Function
# def subData(a = "Ram", b = 0):
#     return f"{a}'s age is {b}"

# print(subData("Saurav", 50000))



# Example of property decorator
class Country:
    def __init__(self, country_name, country_language):
        self.country_name = country_name
        self.country_language = country_language

    @property
    def getCountryName(self):
        return self.country_name
    
    @getCountryName.setter  # Here getter function must be used
    def setCountryName(self, value):
        self.country_name = value
    
Nepal = Country("Nepal","Nepali")
Nepal.setCountryName = "Chinea"
print(Nepal.getCountryName)  # getCountryName is attribute so no use of ()
