from collections import Counter

# Creating counter using Counter() method
list1 = [1,2,3,4,5,6,7,8,6,5,4,3,2,5,3,4,2,3,4,5,1,3,6,4,7,2,3,4,1,2,4,7]
print(Counter(list1))
print(Counter(['a','b','c','d','a','c','d','c','d','e','a']))
print(Counter(A=2, B=3, C=5))
print(Counter({'a':1, 'b':2, 'c':4}))


# Updating Counter using Update() method
con = Counter()
con.update([1,2,5,4,7,8,6,3,2,5,1,4,2,5,1,6,3,5])
print(con)
con.update([9,9,9])
print(con)
print(con.keys())    # Must assign to variable to extract keys like this


# Subtracting counts ( values ) of data that can be zero or negative
c1 = Counter(A=2, B=3, C=5)
c2 = Counter(A=5, B=3, C=5, D=9)
c1.subtract(c2)       # Subtract c2 from c1 and if extra data then value becomes negative
print(c1)


# Using .keys() .values() and .items() in Counter
con = Counter('abcdefshadfasdfasskfasklhgjshfjadkgjlkh')
print(con.keys())
print(con.values())
print(con.items())


# Other way of accessing elements
z = ['blue','red','blue','yellow','blue','red']
col_count = Counter(z)
print(col_count)
col = ['blue','red','yellow','green']
for color in col:
    print(color, col_count[color])


# Elements() method in counter to print all elements in Counter
coun = Counter(a=1, b=2, c=2,d=5)
print(coun)    # Prints Counter
print(list(coun.elements()))   # prints list of elements in Counter


# Most_common() method with parameter in integer prints in the form of highest descending order accourding to value or count
coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219)
for k, v in coun.most_common(4):
    print('%s : %d' %(k,v))


# Simple accessing the content
con = Counter('umbrellautensils')
print(con['l'])      