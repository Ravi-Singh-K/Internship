x = "This is global variable"

def localFunction():
    x = "This is local variable"
    print(x)

localFunction()
print(x)