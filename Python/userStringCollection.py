from collections import UserString

class MyString(UserString):
    def append(self, s):
        self.data += s
    def remove(self,s):
        self.data = self.data.replace(s, "")
strings = MyString("Hello World")
print("Initial String ------", strings.data)
strings.append('This is testing')
print("After appending string.-----", strings.data)
strings.remove("l")
print("After removing certain letter.-----", strings.data)