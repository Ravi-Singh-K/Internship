# def arb_arg(*kids):    #   "*" is the arbitrary arguement that can take values like list, tuple, dictionary or set
#     for i in kids:
#         print("The name of the kid is : " + i)

# arb_arg("Ram","Shyam","Hari")

# def  kwarg_eg(**kname):  # double asterisk " ** "  enables to pass any number of value 
#     print("The name of kid is : " + kname["lname"])

# kwarg_eg(fname="Tobias", lname="Alias")

# def country_name(country="Nepal"):  # Here default parameter is given. if calling function does not has value it will use default argument
#     print("The country name is : " + country)

# country_name()
# country_name("America")
# country_name("Europe")

# def food_name(foods):
#     for i in foods:    print(i)
# eat = ["Apple","Rice","Juice"]
# food_name(eat)

# def pass_stmt():   # pass is used if we do not know about the body part and does not throw exception or any errors
#     pass
# pass_stmt()

def lambda_eg(n):
    return lambda x:x*n
eg = lambda_eg(2)
print(eg(22))