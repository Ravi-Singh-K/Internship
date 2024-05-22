a = (1,2,3,3,4,4,5)
emptylist = []
for b in a:
    if b in emptylist:
        continue
    else:
        emptylist.append(b)
print(emptylist)