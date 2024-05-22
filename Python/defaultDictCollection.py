from collections import defaultdict


def default_dict_return():   # function to return default value for non existing key
    return "Not Present"    # Default value for non-existing key
d = defaultdict(default_dict_return)    # defining defaultdict(parameter) with default_dict_return as parameter
d['a']=2
d['b']=3
print(d['a'])
print(d['b'])
print(d['c'])    # gives default value as "Not Present" 

print('\n Using Lambda to return default value')
# using lambda as default_factory to give default value
d = defaultdict(lambda : "Not Present")
d['d']=3
d['e']=5
print(d['d'])
print(d['e'])
print(d['f'])


print('\n Using list')
# List as default_factory
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print("Dictionary as value of list : ")
print(d)


