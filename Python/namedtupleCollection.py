from collections import namedtuple

a = namedtuple('Student', ['name', 'age', 'address'])
V = a('Ravi', 26, 'Swoyambhu')

# Using index of student to access age
print(V[1])

# Using key_name to access value
print(V.name)
print(V.address)