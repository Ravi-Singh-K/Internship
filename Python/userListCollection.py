from collections import UserList

class MyList(UserList):
    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")
    def pop(self, s = None):
        raise RuntimeError("Deletiuon not allowed")
l = MyList([1,2,3,4,5])
print("Original List", l)
l.append(9)
print("After Insertion", l)
l.remove()
print(l)