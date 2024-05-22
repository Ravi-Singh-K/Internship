# fibonacci series
def fibonacci_series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
term = int(input("Enter the times to iterate fibonacci series : "))
print(f"The fibonacci series upto the term {term} is : ")
for i in range(term):
    print(fibonacci_series(i), " ", end="")

print('\n')

# Factorial of a number
def factNumber(n):
    if n == 0 or n == 1:
        return 1
    return n * factNumber(n-1)
num = int(input("Enter any number to calculate factorial : "))
result = factNumber(num)
print(f"The factorial of {num} number is {result}.")

print('\n')

