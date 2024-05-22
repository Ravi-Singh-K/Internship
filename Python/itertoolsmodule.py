import operator
import time as t
import itertools

l1 = [1,2,3,4,5]
l2 = [5,4,3,2,1]

# Using time before map function
t1 = t.time()

# Result using map()
c = list(map(operator.mul, l1, l2))

# End time after map function
t2 = t.time() 

# Time taken by map function
print("Result : ", c)
print("Time taken by map function : %.6f" %(t2-t1))

# Starting time for loop function
t1 = t.time()

# Result using loop 
print("Result : ", end="")
for i in range(3):
    print(l1[i] * l2[2], end="")

# End time after loop
t2 = t.time()
print("\n The time taken by loop : %.6f" %(t2-t1))
# Conclusion ! map is faster than for loop. so iter tools is faster and memory efficient tool.


# Example of infinite iterators 
# .count(start, step)
for i in itertools.count(199, 100):
    if i == 999:
        break
    print(i ," ", end="")  # Does not print 999

print("\n")
# .cycle(iterable)
count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i," ", end="")
        count += 1

print("\n")
# next(iterator)
l = ["Hello", "World"]
iterators = itertools.cycle(l)
for i in range(6):
    print(next(iterators), " ", end="")


print("\n")
# repeat(value, number_of_times)
print("printing the numbers repeatedly : ")
print(list(itertools.repeat(45,5)))


# Combinatoric iterators
# Product()
from itertools import product

print("The cartesian product using repeat : ")
print(list(product([1,2], repeat=2)))
print()

print("The cartesian product of the containers : ")
print(list(product(["Hello", "World", "Welcome"], '3')))
print()

print("The cartesian product of the containers : ")
print(list(product("AB", [3,4])))
print()


# Permutations()
from itertools import permutations

print("All the permutations of the given list is : ")
print(list(permutations([1, 'geeks'], 2)))
print()

print("All the permutations of the given string is : ")
print(list(permutations('AB')))
print()

print("All the permutation of the given container is : ")
print(list(permutations(range(3), 2)))
print()


# Program to check the validity of permutation as single value does not repeat twice
print("Permutating (a,ravi,singh,25,b)")
x = list(permutations(["a", "ravi", "singh", 25 ,"b"], 5))  # must specify group_size not greater than the elements of iterable
flag = 1
for i in x:
    if i == "('a', 'ravi', 25, 'b', 'singh')":
        flag += 1
if flag == 1:
    print("There are no duplicate permutation")
else:
    print("Permutation does not work.")


# combinations()
from itertools import combinations

print("All the combination of list in sorted order(without replacement) is : ")
print(list(combinations(['A', 2], 2)))
print()

print("All the combination of string in sorted order(without replacement) is : ")
print(list(combinations('AB', 2)))
print()

print("All the combination of list in sorted order(without replacement) is : ")
print(list(combinations(range(2), 1)))


# Combinations_with_replacement()

from itertools import combinations_with_replacement

print("All the combination of string in sorted order(with replacement) is : ")
print(list(combinations_with_replacement("AB", 2)))
print()

print("All the combination of list in sorted order(with replacement) is : ")
print(list(combinations_with_replacement([1,2], 2)))
print()

print("All the combination of container in sortd order(with replacement) is : ")
print(list(combinations_with_replacement(range(2), 1)))
print()


# Terminating Iterators
# accumulate(iter, func)

import itertools
import operator

l1 = [1,2,3,4,5]
print(l1)
print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(l1)))

print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(l1, operator.mul)))


# Chain()
l1 = [1,4,7]
l2 = [2,5,8]
l3 = [3,6,9]
print("All values in mentioned chain are : ", end="")
print(list(itertools.chain(l1,l2,l3)))


# chain.from_iterable()
# here it works like chain but it takes list of lists as arguement
l4 = [l1,l2,l3]
print(list(itertools.chain.from_iterable(l4)))
l = [[1,2,3],[4,5,6],[7,8,9]]
print(list(itertools.chain.from_iterable(l)))


# compress(iter, selector)
print("The compressed values in sting are : ", end="")
print(list(itertools.compress('Hello World This is Ravi', [1,0,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1])))


#dropwhile(func, seq)
li = [2,3,5,6,7]
print("The values after condition returns false : ", end="")
print(list(itertools.dropwhile(lambda x : x % 2 == 0, li)))


#filterfalse(func, seq)
print("The values that return false to function are : ", end="")
print(list(itertools.filterfalse(lambda x : x % 2 == 0, li)))


# islice(iterable, start, stop, step)
li = [2,4,5,6,7,8,9,45,30]
print("The sliced list values are : ", end="")
print(list(itertools.islice(li, 1, 6, 2)))


# starmap(func, tuple list)
li = [(1,10,5),(8,4,1),(11,10,1)]
print("The value according to function are : ", end="")
print(list(itertools.starmap(min, li)))


# takewhile(func, iterable)
li = [2,4,6,8,10,12,3,45,32]
print("The list values till 1st false value are : ", end="")
print(list(itertools.takewhile(lambda x : x % 2 ==0, li)))


# tee(iterator, count)
li = [2,4,6,7,8,10,20]
iti = iter(li)
it = itertools.tee(iti, 3)
print("The iterators are : ")
for i in range(0,3):
    print(list(it[i]))


# zip_longest()
print("The combined value of iterables is : ")
print(*(itertools.zip_longest('Hellorld', 'Thisisravi', fillvalue='-')))