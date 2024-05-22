from collections import ChainMap

# Simple example of chain map
d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6}
d3 = {'g':7,'h':8,'i':9}
d = ChainMap(d1, d2, d3)
print(d)

# accessing value of ChainMap
print(d['a'])

# accessing value of ChainMap using .keys()
print(d.keys())

# accessing value using .values()
print(d.values())



# Using .new_child() method to insert dictionary in Chain Map
d4 = {'j':10,'k':11,'l':12}
c = d.new_child(d4)
print(c)