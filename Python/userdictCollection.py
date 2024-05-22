from collections import UserDict

class MyDict(UserDict):
    def __del__(self):
        # raise RuntimeError("Deletion not allowed")
        raise NotImplementedError({'a':1,'b':2}) # We can pass dictionary as well instead of string
    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")  # we can use NotImplementedError instead of RuntimeError. Mostly used NotImplementedError
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")

d = MyDict({'a':1,'b':2,'c':3})
print(d)