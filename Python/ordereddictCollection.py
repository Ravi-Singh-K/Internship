from collections import OrderedDict

# Simple assigning value with key in Ordered Dictionary
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)


# Differences in insertion after popping elements in OD
print("\n After POPPING 'a' element from OD")
od.pop('a')
for key, value in od.items():
    print(key, value)


# Now inserting 'a' element in OD
print("\n Inserting 'a' element in OD")
od['a'] = 1
for key, value in od.items():
    print(key, value)        
# In OrderedDict popped values are inserted at the end of the OD as it maintains the order of insertion



# Key Value Change in OrderedDict
print("\nBefore")
od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for key, value in od.items():
    print(key, value)
print("\nAfter")
od['c']=10       # Changing the value of key doesnot change the position of element
for key, value in od.items():
    print(key, value)


# Equality comparison in OrderedDict
od1 = OrderedDict([('b',2),('a',1),('c',3)])
od2 = OrderedDict([('a',1),('b',2),('c',3)])
print(od1 == od2)    # ' == ' operator is used to compare two ordered dictionary that gives ' False ' output as it checks the order of the insertion as well


# OrderedDict Reversal in OrderedDict
# od = OrderedDict([('a',2),('b',3),('c',4)])
# od1 = reversed(od)
# for key in od1():
#     print(key)
# throws type error


# OrderedDict Popitem()
od = OrderedDict([('a',1),('b',2),('c',3),('d',4),('e',5)])
last_item = od.popitem(last=True)    # Delete last element
print(last_item)
print(od)
last_item = od.popitem()    # Also delete last element
print(last_item)
print(od)
last_item = od.popitem(last=False)   # Delete First element
print(last_item)
print(od)


# Key Insertion at Arbitrary Position in OrderedDict
od = OrderedDict([('a',1),('b',2),('c',3)])
# ' a ' is moved at the end of ordered dictionary
od.move_to_end('a')
# ' c ' is moved at the beginning of the ordered dictionary
od.move_to_end('c', last=False)
for key, value in od.items():
    print(key, value)


# Using all the possible methods
od = OrderedDict([('a',1),('b',2),('c',3)])
od['d']=4
od.update([('e',5),('f',6)])
od.move_to_end('e', last=False)
print("\n All Possible methods application")
for key, value in od.items():
    print(key, value)