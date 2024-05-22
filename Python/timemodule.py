import time

# printing epoch (the point where the time starts and is platform - dependent)
print(time.gmtime(0))

# Prints the current time in seconds
print(time.time())

# getting time string from seconds
curr = time.ctime(109289384932.34234)
print("Current time : ", curr)

# getting current time string
print("Current time is : ", time.ctime())

# delaying execution time of program
for i in range(4):
    time.sleep(0)
    print(i, " ", end="")
print()


# localtime() method
obj = time.localtime(982324754.3242342)
print(obj)


# .strptime() method
string = "Tuesday, 03 August 2021 10:45:08"
# obj = time.strptime(string, "%a, %d %b %Y %H:%M:%S")