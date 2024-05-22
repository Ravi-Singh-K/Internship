x = [2,3,5,7,1,0,4]
x.reverse()
print(x)
x[1]='AJ'
print(x)

y = reversed(x)
print(list(y))
y=list(y)
# y[0]=1
print(y)