list1 = [2,5,4,6,7,8,9,0,12,32,53,65,76,89,90,87,6,54,34,23,56,17,18,45,23,21]
temp = list1[0]
s_temp = list1[0]

for i in list1:
    if temp < i:
        temp = i
    if s_temp > i:
        s_temp = i
print("The highest Value from the list is " ,temp)
list1.remove(max(list1))
print("The second highest value from the list is ", max(list1))
print("The smallest value from the list is " ,s_temp)
